# calc_tool/operations.py
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """返回 a + b"""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """返回 a - b"""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """返回 a * b"""
    return a * b

def divide(a: Number, b: Number) -> Number:
    """返回 a / b；遇到除以零则抛出 ZeroDivisionError"""
    if b == 0:
        raise ZeroDivisionError("error： can not divided by 0。")
    return a / b
