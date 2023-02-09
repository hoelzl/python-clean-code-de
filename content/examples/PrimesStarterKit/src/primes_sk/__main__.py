import argparse
import sys


def main(args):
    parser = argparse.ArgumentParser(
        prog="primes",
        description="Factor prime numbers.",
        epilog="Have fun!",
    )
    parser.add_argument("number", default="42", help="the number to factor")
    args = parser.parse_args(args)
    print("Hello, world!")


if __name__ == "__main__":
    main(sys.argv[1:])
