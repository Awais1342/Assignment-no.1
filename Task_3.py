# Question 3:
# Calculate Compound Interest
# Use the formula:
# CI = P * (1 + R/100)**T - P
# Where P = principal, R = rate, T = time


print("Please Enter principal, rate and time")
p=float(input("Please Enter principal: "))
r=float(input("Please Enter rate: "))
t=float(input("Please Enter time: "))

ci=p*(1+r/100)**t -p
print("Ci is : ",ci)
