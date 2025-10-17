# calc_tool/__main__.py
import sys
"""
Support two ways of running this file:

- As a package: python -m calc_tool add 1 2
- Directly from inside the package dir: python __main__.py add 1 2

When run directly, relative imports (from .cli) raise "attempted relative import with no known
parent package", so we try a relative import first and fall back to absolute imports.
"""

try:
    # Preferred: running as a package (python -m calc_tool)
    from .cli import parse_args
    from . import operations
except Exception:
    # Fallback: running as a script inside the package directory (python __main__.py)
    # Use absolute imports when relative imports aren't available.
    from cli import parse_args  # type: ignore
    import operations  # type: ignore


def main(argv=None):
    try:
        operation, a, b, precision = parse_args(argv)
    except Exception as e:
        # argparse 会自动打印帮助信息并 exit，若自定义错误则在此捕获
        print(f"参数解析错误: {e}", file=sys.stderr)
        return 2

    try:
        if operation == "add":
            result = operations.add(a, b)
        elif operation == "subtract":
            result = operations.subtract(a, b)
        elif operation == "multiply":
            result = operations.multiply(a, b)
        elif operation == "divide":
            result = operations.divide(a, b)
        else:
            print(f"未知操作: {operation}", file=sys.stderr)
            return 3

    except ZeroDivisionError as e:
        print(f"错误: {e}", file=sys.stderr)
        return 4
    except Exception as e:
        print(f"运行时错误: {e}", file=sys.stderr)
        return 5

    # 格式化输出（可选保留小数位）
    if precision is not None:
        try:
            fmt = f"{{:.{precision}f}}"
            output = fmt.format(result)
        except Exception:
            output = str(result)
    else:
        output = str(result)

    print(output)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
