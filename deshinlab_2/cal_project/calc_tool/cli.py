# calc_tool/cli.py
import argparse
from typing import Tuple

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calc_tool",
        description="command calc：functions: add, subtract, multiply, divide"
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="command to execute"
    )
    parser.add_argument("a", help="first operand")
    parser.add_argument("b", help="second operand")
    parser.add_argument("--precision", "-p", type=int, default=None,
                        help="optional：reserved dit number（example: -p 3）")
    return parser



def parse_args(argv=None) -> Tuple[str, float, float, int]:
    parser = create_parser()
    args = parser.parse_args(argv)

    def to_number(s: str):
        try:
            return int(s)
        except ValueError:
            try:
                return float(s)
            except ValueError:
                raise argparse.ArgumentTypeError(f"illigal number: {s!r}")

    a = to_number(args.a)
    b = to_number(args.b)
    return args.operation, a, b, args.precision
# calc_tool/cli.py
import argparse
from typing import Tuple
