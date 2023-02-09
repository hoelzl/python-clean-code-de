from simple_packaging.greeting import say_hi
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="simple-packaging",
        description="A simple packaging example.",
        epilog="Have fun!",
    )
    parser.add_argument(
        "-n", "--name", default="world", help="the name of the person to greet"
    )
    args = parser.parse_args()
    say_hi(args.name)


if __name__ == "__main__":
    main()
