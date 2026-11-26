import os

ENTRY = (
    "I'm out of the office until Monday, and honestly I'm not checking email "
    "because I need this break \u2014 but your message matters to me, and I'll "
    "answer it properly as soon as I'm back."
)

def main():
    # Gate self-check: entry must be 1-200 chars, a single sentence.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside gate"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
