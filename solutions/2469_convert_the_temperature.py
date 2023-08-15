"""
LeetCode Problem: 
2469. Convert the Temperature

You are given a non-negative floating point number rounded to two decimal places celsius, 
that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. 
Answers within 10-5 of the actual answer will be accepted.

Note that:
- Kelvin = Celsius + 273.15
- Fahrenheit = Celsius * 1.80 + 32.00
"""

from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32]