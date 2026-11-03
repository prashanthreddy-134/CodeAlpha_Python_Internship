import argparse
import re
import shutil
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError
from html.parser import HTMLParser
IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp",
    ".bmp", ".gif", ".tiff", ".tif"
}
EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)
def move_image_files(source_dir, dest_dir):
    source = Path(source_dir).resolve()
    destination = Path(dest_dir).resolve()
    if not source.is_dir():
        raise FileNotFoundError(
            f"Source folder not found: {source}"
        )
    if source == destination or source in destination.parents:
        raise ValueError(
            "Destination cannot be the source folder or inside it."
        )
    destination.mkdir(parents=True, exist_ok=True)
    moved = 0
    skipped = 0
    files = [
        file for file in source.rglob("*")
        if file.is_file()
        and file.suffix.lower() in IMAGE_EXTENSIONS
        and destination not in file.parents
    ]
    for file in files:
        relative_path = file.relative_to(source)
        target = destination / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            counter = 1
            while True:
                new_name = (
                    f"{target.stem}_{counter}{target.suffix}"
                )
                new_target = target.with_name(new_name)
                if not new_target.exists():
                    target = new_target
                    break
                counter += 1
        try:
            shutil.move(str(file), str(target))
            print(f"Moved: {file.name} -> {target}")
            moved += 1
        except OSError as error:
            print(f"Could not move {file}: {error}")
            skipped += 1
    print("\n========== IMAGE ORGANIZER ==========")
    print(f"Images found: {len(files)}")
    print(f"Images moved: {moved}")
    print(f"Images skipped: {skipped}")
    print(f"Destination: {destination}")
    return moved
def extract_emails(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.is_file():
        raise FileNotFoundError(
            f"Input file not found: {input_path}"
        )
    text = input_path.read_text(encoding="utf-8")
    emails = sorted(
        set(EMAIL_PATTERN.findall(text)),
        key=str.lower
    )
    output_path.parent.mkdir(
        parents=True, exist_ok=True
    )
    output_path.write_text(
        "\n".join(emails) + ("\n" if emails else ""),
        encoding="utf-8"
    )
    print("\n========== EMAIL EXTRACTOR ==========")
    print(f"Unique emails found: {len(emails)}")
    for email in emails:
        print(f"Email: {email}")
    print(f"Saved to: {output_path}")
    return emails
class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside_title = False
        self.title_parts = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self.inside_title = True
    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.inside_title = False
    def handle_data(self, data):
        if self.inside_title:
            self.title_parts.append(data)
def scrape_title(url, output_file):
    if not url.startswith(("http://", "https://")):
        raise ValueError(
            "Please enter a valid HTTP or HTTPS URL."
        )
    request = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    try:
        with urlopen(request, timeout=15) as response:
            html = response.read().decode(
                "utf-8", errors="replace"
            )
    except (URLError, OSError, ValueError) as error:
        raise RuntimeError(
            f"Unable to access website: {error}"
        ) from error
    parser = TitleParser()
    parser.feed(html)
    title = " ".join(
        "".join(parser.title_parts).split()
    )
    if not title:
        title = "No title found"
    output_path = Path(output_file)
    output_path.parent.mkdir(
        parents=True, exist_ok=True
    )
    output_path.write_text(
        title + "\n",
        encoding="utf-8"
    )
    print("\n========== WEBSITE TITLE ==========")
    print(f"Website: {url}")
    print(f"Title: {title}")
    print(f"Saved to: {output_path}")
    return title
def build_parser():
    parser = argparse.ArgumentParser(
        description="CodeAlpha Python Task Automation"
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )
    jpg_parser = subparsers.add_parser(
        "jpg",
        help="Organize image files"
    )
    jpg_parser.add_argument("source_dir")
    jpg_parser.add_argument("dest_dir")
    email_parser = subparsers.add_parser(
        "emails",
        help="Extract email addresses"
    )
    email_parser.add_argument("input_file")
    email_parser.add_argument("output_file")
    title_parser = subparsers.add_parser(
        "title",
        help="Extract website title"
    )
    title_parser.add_argument("url")
    title_parser.add_argument("output_file")
    return parser
def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "jpg":
            move_image_files(
                args.source_dir,
                args.dest_dir
            )
        elif args.command == "emails":
            extract_emails(
                args.input_file,
                args.output_file
            )
        elif args.command == "title":
            scrape_title(
                args.url,
                args.output_file
            )
    except (FileNotFoundError, ValueError, RuntimeError) as error:
        print(f"\nERROR: {error}")
        raise SystemExit(1)
if __name__ == "__main__":
    main()
