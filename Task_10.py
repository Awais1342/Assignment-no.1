# Salary Calculator
# Input basic salary. Calculate:
#  HRA = 20% of basic
#  DA = 15% of basic
#  Total Salary = Basic + HRA + DA


basicsalary=float(input("Basic salary: "))
hra=(basicsalary*20)/100
da=(basicsalary*15)/100
totalsalary=basicsalary+hra+da


print("HRA is: ",hra)
print("Da is: ",da)
print("Total salary is: ",totalsalary)