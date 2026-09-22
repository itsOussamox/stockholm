import argparse

VERSION = "1.0"


def get_args():
    """
    Parse and return the command-line arguments.
    Kept in its own file to stay organized.
    """

    parser = argparse.ArgumentParser(
        prog="stockholm",
        description="A small educational ransomware simulation. For learning only.",
        add_help=False  # We define -h manually to keep full control
    )

    parser.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show this help message and exit."
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"stockholm v{VERSION}",
        help="Show the program version and exit."
    )

    parser.add_argument(
        "-r", "--reverse",
        metavar="KEY",
        type=str,
        help="Reverse the infection using the provided decryption key."
    )

    parser.add_argument(
        "-s", "--silent",
        action="store_true",
        help="Run without printing anything to the terminal."
    )

    return parser.parse_args()