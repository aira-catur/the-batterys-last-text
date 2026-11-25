import os

TEXT = "I spent all day at 1% saving my last words for you, and you show up at midnight plugged into the iPad \u2014 so I'm dying, and I'm taking the alarm clock with me."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
