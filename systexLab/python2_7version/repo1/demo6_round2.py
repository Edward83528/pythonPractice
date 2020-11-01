from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

currentVale = Decimal(2.5)
result = Decimal(currentVale.quantize(Decimal(1), rounding=ROUND_HALF_UP))
print(result)
result2 = Decimal(currentVale.quantize(Decimal(1), rounding=ROUND_HALF_EVEN))
print(result2)
