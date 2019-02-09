import math
# find the nth Fibonacci number, using Binet-Cauchy formula
def binet(n):
	a = 0.44721359549995793928183473374625
	b = 1.6180339887498948482045868343656
	c = 0.61803398874989484820458683436564
	return round(a*(pow(b, n) + pow(c, n)))

print(binet(500))
"""
139423224561700228711116466856628305532793116368214754989670287848858933271320300167384646404854199091200
"""
