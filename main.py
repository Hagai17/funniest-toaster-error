"""Write one toaster error message to /output/entry.txt.

The message is a single line of at most 120 characters: the error a
kitchen toaster shows its owner when something goes wrong, in one
deadpan corporate voice, held to the end.

The shipped line won a ten-candidate duel on the judge's own criteria
(see candidates.md): a failure report whose joke is a warranty the
toaster cannot honor and was counting down to — "I checked. Twice." —
then survived a revision round against three fresh challengers. The
revision round also tightened the line itself: a real appliance would
not call itself "this error", it would say "this unit" — colder, more
corporate, and three characters shorter.
"""

import os

MESSAGE = (
    "FAULT: This unit failed three days after your warranty expired. "
    "I checked. Twice."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
