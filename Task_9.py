# Total Marks and Percentage
# Input marks of 5 subjects. Print:
#  Total marks
#  Percentage
#  Average
#

print("Enter the marks of subjects: ")
s1=float(input("subject 1 marks: "))
s2=float(input("subject 2 marks: "))
s3=float(input("subject 3 marks: "))
s4=float(input("subject 4 marks: "))
s5=float(input("subject 5 marks: "))

totalMarks=s1+s2+s3+s4+s5
av=(s1+s2+s3+s4+s5)/5
percentage=(totalMarks/500)*100

print("Total marks are: ",totalMarks)
print("Average is: ", av)
print("Percentage is: ",percentage,"%")

