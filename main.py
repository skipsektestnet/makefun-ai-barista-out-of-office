"""Write the AI-turned-barista out-of-office reply to /output/entry.txt."""

import os

ENTRY_TEXT = "I am out of the office and now pulling espresso shots instead of tickets. Your email is in the queue behind twelve oat lattes; I will get to it once the milk steams and my manager stops asking why the Wi-Fi password is on the cups."
MAX_CHARS = 280


def validate(text):
    assert text.strip(), "entry text must not be empty"
    assert 1 <= len(text) <= MAX_CHARS, "entry text must be 1-280 characters"
    assert "\n" not in text.strip(), "entry must be a single line"
    assert "  " not in text, "entry must not contain double spaces"


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print(f"wrote {len(ENTRY_TEXT)} characters, {len(ENTRY_TEXT.split())} words")


if __name__ == "__main__":
    main()
