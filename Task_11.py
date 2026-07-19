# Age in Months and Days
# Input your age in years. Calculate and print age in:
#  Months
#  Days (approximate)

print("Enter your age: ")
age=float(input())
year=age*12
months=year//12
days=year%30

print("Age in months and days are: ", months,"months and",days,"days")