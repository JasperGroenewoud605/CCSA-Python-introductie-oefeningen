aantalStuks = int(input())
kostPrijs = float(input())
barcodesPerCoupon = int(input())
mijlenPerCoupon = int(input())

uitgegeven = aantalStuks*kostPrijs
coupons = aantalStuks // barcodesPerCoupon
mijlen = coupons*mijlenPerCoupon

print(f"Phillips spendeerde ${uitgegeven} voor {mijlen} frequent flyer mijlen.")