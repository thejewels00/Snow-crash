#!/usr/bin/env python3

def decode(encoded_output):
    chift = ""
    for i, c in enumerate(encoded_output):
        chift += chr(ord(c) - i)
    return chift

def main():
    # Read first non-empty line from file
    with open("token", "r") as f:
        for line in f:
            encod = line.strip()
            if encod:
                break

    print(decode(encod))

if __name__ == "__main__":
    main()
