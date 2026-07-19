# Distribute Items Equally - You have n candies and k students.
# Write a program to find:
# how many candies each student gets
# how many are left

print("Enter candies: ")
n=int(input("Enter candies:" ))
k=int(input("Enter students: "))

total=n//k
left=n%k

print("Each student will get: ", total)
print("Left: ",left)