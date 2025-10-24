# calc_tool/operations.py
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """return a + b"""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """return a - b"""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """return a * b"""
    return a * b

def divide(a: Number, b: Number) -> Number:
    """return a / b；Raise an exception when division by zero occurs: ZeroDivisionError"""
    if b == 0:
        raise ZeroDivisionError("error： can not divided by 0。")
    return a / b
