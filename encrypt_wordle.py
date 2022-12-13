# Usage:
#  python encrypt_wordle.py slate "This is the message to encrypt!"

_yellow = "🟨"
_black = "⬛"
_green = "🟩"

def wordle_encrypt(key: str, s: str):
    words = s.lower().split(" ")
    encrypted_words = []
    for word in words:
        encrypted_word = ""
        for i, letter in enumerate(word):
            if not letter.isalpha():
                encrypted_word += letter
            elif key[i % len(key)] == letter:
                encrypted_word += _green
            elif letter in key:
                encrypted_word += _yellow
            else:
                encrypted_word += _black
        encrypted_words.append(encrypted_word)

    return " ".join(encrypted_words)


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)

    import sys

    key = sys.argv[1]
    s = sys.argv[2]

    print(wordle_encrypt(key, s))
