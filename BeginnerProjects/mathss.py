
import random


#create a list of dictionary to store questions and answers
questions = {"What is 5% of D75000":"D3750",
	         "what is the sum of 2 exp 4":"20000",
			 "Calculate the sum of 23 and 5": "28",
			 "Evaluate log of 10":"1"}
#create a new list to store the random selected question
ques = []	
for x in questions:
	ques.append(x)

i = 0
while i != len(questions):
	#selecting a random question and displaying it to the user
	randx = random.choice(ques)
	user_ans = input(f"{randx}: ")
	#check if randomly selected question is in our original dictionary
	#and if the users answert corresponds to the answer of the question
	if randx in questions.keys() and questions[randx] == user_ans:
		print("Correct answer", end="\n\n")
	else:
		print("Wrong answer", end="\n\n")
	#removing any question that was once selected to avoid repeatition
	ques.remove(randx)

	if i == len(questions):
		break
			
	i+=1 