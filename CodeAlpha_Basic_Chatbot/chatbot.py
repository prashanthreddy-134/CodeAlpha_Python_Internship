
import random
import re
BOT_NAME = "CodeAlpha Bot"
INTENTS = {
    "greeting": {
        "patterns": [r"\b(hi|hello|hey|hai|good morning|good evening|good afternoon)\b"],
        "responses": [
            "Hello! How can I help you today?",
            "Hey there! Nice to meet you!",
            "Hi! What's going on?",
            "Hello! Ready to chat?"
        ]
    },
    "feeling": {
        "patterns": [r"\bhow are you\b", r"\bhow r u\b", r"\bhow r you\b"],
        "responses": [
            "I'm doing great! How about you?",
            "I'm fine, thanks for asking!",
            "Doing awesome! What about you?"
        ]
    },
    "name": {
        "patterns": [r"\bwhat is your name\b", r"\bwho are you\b", r"\byour name\b"],
        "responses": [
            "I'm CodeAlpha Bot, your Python chatbot assistant!",
            "My name is CodeAlpha Bot. Nice to meet you!"
        ]
    },
    "creator": {
        "patterns": [r"\bwho created you\b", r"\bwho made you\b", r"\bdeveloper\b"],
        "responses": [
            "I was created using Python as a CodeAlpha internship project!",
            "A Python developer built me using rule-based chatbot logic."
        ]
    },
    "thanks": {
        "patterns": [r"\bthank you\b", r"\bthanks\b", r"\bthx\b"],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "Anytime! Keep learning."
        ]
    },
    "goodbye": {
        "patterns": [r"\bbye\b", r"\bgoodbye\b", r"\bsee you\b", r"\bexit\b", r"\bquit\b"],
        "responses": [
            "Goodbye! Have a wonderful day!",
            "See you again. Keep coding!",
            "Bye! Thanks for chatting with me!"
        ]
    },
    "python": {
        "patterns": [r"\bpython\b", r"\blearn python\b"],
        "responses": [
            "Python is a beginner-friendly programming language.",
            "Python is widely used in AI, machine learning and automation!",
            "Keep practising Python. Build projects to improve your skills."
        ]
    },
    "programming": {
        "patterns": [r"\bprogramming\b", r"\bcoding\b", r"\bcode\b"],
        "responses": [
            "Coding is all about solving problems logically.",
            "Practice coding every day to improve your programming skills!",
            "Which programming language are you learning?"
        ]
    },
    "internship": {
        "patterns": [r"\binternship\b", r"\bcodealpha\b"],
        "responses": [
            "Internships help you gain practical development experience!",
            "Keep completing your internship tasks and documenting your work.",
            "Building real projects is a great way to improve your skills."
        ]
    },
    "joke": {
        "patterns": [r"\btell me a joke\b", r"\bjoke\b", r"\bmake me laugh\b"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the computer cold? It left its Windows open!",
            "A programmer's favourite place? The Foo Bar!"
        ]
    },
    "help": {
        "patterns": [r"\bhelp\b", r"\bwhat can you do\b", r"\bfeatures\b"],
        "responses": [
            "I can chat about Python, programming, internships, jokes and more!",
            "Try asking about my name, Python, coding or tell me a joke."
        ]
    },
    "motivation": {
        "patterns": [r"\bsad\b", r"\bsuccess\b", r"\bmotivate me\b", r"\bmotivation\b"],
        "responses": [
            "Don't give up. Every expert was once a beginner!",
            "Small progress every day leads to big results.",
            "Your mistakes are part of your learning journey."
        ]
    }
}
def normalize(message):
    return re.sub(r"[^a-z0-9\s]", "", message.lower()).strip()
def get_reply(message):
    cleaned = normalize(message)
    if not cleaned:
        return "Please type something.", False
    for intent, data in INTENTS.items():
        for pattern in data["patterns"]:
            if re.search(pattern, cleaned):
                reply = random.choice(data["responses"])
                return reply, intent == "goodbye"
    return (
        "I'm still learning! Try asking about Python, programming, "
        "internships, jokes or type 'help'.",
        False
    )
def main():
    print("=" * 45)
    print("       WELCOME TO CODEALPHA CHATBOT")
    print("=" * 45)
    print(f"{BOT_NAME}: Hello! I'm your chatbot assistant.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit.")
    print("-" * 45)
    while True:
        user_input = input("You: ")
        reply, should_exit = get_reply(user_input)
        print(f"{BOT_NAME}: {reply}")
        if should_exit:
            print("Chat session ended.")
            break
if __name__ == "__main__":
    main()
