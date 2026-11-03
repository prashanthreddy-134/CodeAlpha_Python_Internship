# Task 3: Task Automation with Python Scripts

Automates repetitive file and web tasks. All three ideas from the brief are included as subcommands.

## Commands

| Command | What it does |
|---------|--------------|
| `jpg <source> <dest>` | Moves all `.jpg` files from one folder to another |
| `emails <input.txt> <output.txt>` | Extracts unique email addresses into a new file |
| `title <url> <output.txt>` | Scrapes the page `<title>` and saves it |

## Run
```bash
python automation.py --help
python automation.py jpg ./photos ./sorted_photos
python automation.py emails contacts.txt emails_found.txt
python automation.py title https://www.codealpha.tech title.txt
```

The `title` command needs `requests`: `pip install requests`

## Concepts Used
`os`, `shutil`, `re`, `requests`, file handling, `argparse`
