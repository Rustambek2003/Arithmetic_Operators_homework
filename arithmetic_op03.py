#Create a variable called 'number' and assign it the two-digit number

#Find the reverse of the number and assign it to a variable called 'answer'.

#Print the answer variable
number = 28
answer = (number % 10) * 10 + (number -(number % 10))//10
print(answer)