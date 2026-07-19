# Percentage of Correct Answers
# Input total questions and correct answers, and calculate the percentage score.

print("Enter total questions")
totalquestions=int(input())
print("Enter correct answers")
correctasnwers=int(input())

percentage=(correctasnwers/totalquestions)*100
print("Percentage is: ", percentage,"%")