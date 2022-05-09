# Functions


def computepay(h, r):
    pay=h*r
    return pay


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
