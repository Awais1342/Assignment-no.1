# Convert Minutes to Hours and Minutes
# Input number of minutes and convert to hours and remaining minutes.
# Example: 130 minutes → 2 hours 10 minutes

print("Enter time")
time=int(input())
hours=time//60
min=time%60
print("time in hours is:",hours,"hours",min,"mintues")
