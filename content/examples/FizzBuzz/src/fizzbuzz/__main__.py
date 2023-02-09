import argparse

from fizzbuzz import fizzbuzz


def main():
    parser = argparse.ArgumentParser(
        prog="fizzbuzz",
        description="Print the FizzBuzz sequence.",
    )
    parser.add_argument(
        "number", nargs="?", default="16", help="the largest number to output"
    )
    args = parser.parse_args()
    try:
        fizzbuzz(int(args.number))
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
