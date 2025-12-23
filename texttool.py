#!/usr/bin/env python3



def process_line(line):
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()
    if cmd == "lowercase":
        return text.lower()
    if cmd == "prefix":
        return text[:10]
    if cmd == "counter-words":
        return str(len(text.split()))
    if cmd == "length":
        return str(len(text))

    return "Unknown command " + cmd


def main():

"""Boucle principale récupérant les entrées utilisateur."""

    while True:
        try:
            line = input("commade> ")
        except EOFError:
            break

        print(process_line(line))



if __name__ == "__main__":
    main()
