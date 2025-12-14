from collections import Counter

def clean_word(word: str) -> str:
    cleaned = "".join(ch for ch in word.lower() if ch.isalpha() or ch == "'")
    return cleaned

def main():
    path = "week1/project/sample/input.txt"

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()
    raw_words = text.split()

    words = []
    for w in raw_words:
        cw = clean_word(w)
        if len(cw) >= 3:
            words.append(cw)

    counts = Counter(words)

    print("=== Text Report ===")
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print("\nTop 10 words:")
    for word, count in counts.most_common(10):
        print(f"- {word}: {count}")

if __name__ == "__main__":
    main()
