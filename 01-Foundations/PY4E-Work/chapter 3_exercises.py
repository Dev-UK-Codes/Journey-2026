# My Overtime Calculator

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

h = float(hrs)
r = float(rate)

if h <= 40:
    # Standard pay logic
    pay = h * r
else:
    # Overtime logic (40 hours at regular rate + extra at 1.5x)
    regular_pay = 40 * r
    overtime_hrs = h - 40
    overtime_pay = overtime_hrs * (r * 1.5)
    pay = regular_pay + overtime_pay

print("Total Pay is:")
print(pay)

