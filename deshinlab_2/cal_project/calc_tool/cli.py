# calc_tool/cli.py
import argparse
from typing import Tuple

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calc_tool",
        description="命令行计算器：支持 add, subtract, multiply, divide"
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="要执行的运算"
    )
    parser.add_argument("a", help="第一个操作数")
    parser.add_argument("b", help="第二个操作数")
    parser.add_argument("--precision", "-p", type=int, default=None,
                        help="可选：结果保留的小数位数（例如 -p 3）")
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
                raise argparse.ArgumentTypeError(f"不是合法数字: {s!r}")

    a = to_number(args.a)
    b = to_number(args.b)
    return args.operation, a, b, args.precision
# calc_tool/cli.py
import argparse
from typing import Tuple

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calc_tool",
        description="命令行计算器：支持 add, subtract, multiply, divide"
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="要执行的运算"
    )
    parser.add_argument("a", help="第一个操作数")
    parser.add_argument("b", help="第二个操作数")
    parser.add_argument("--precision", "-p", type=int, default=None,
                        help="可选：结果保留的小数位数（例如 -p 3）")
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
                raise argparse.ArgumentTypeError(f"不是合法数字: {s!r}")

    a = to_number(args.a)
    b = to_number(args.b)
    return args.operation, a, b, args.precision
