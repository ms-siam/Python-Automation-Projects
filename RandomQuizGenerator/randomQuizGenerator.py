#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire':
            'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
            'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for NumOfQuiz in range(35):
    #Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{NumOfQuiz + 1}.txt', 'w')
    answerFile = open(f'capitalsquiz_ans{NumOfQuiz + 1}.txt', 'w')
    
    #Header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{NumOfQuiz + 1})')
    quizFile.write('\n\n')
    
    #Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    
    #Loop through all 50 states, making a question for each.
    
    for NumOfQues in range(50):
        #Get Right and Wrong answers
        trueAnswer = capitals[states[NumOfQues]]
        falseAnswers = list(capitals.values())
        del falseAnswers[falseAnswers.index(trueAnswer)]
        falseAnswers = random.sample(falseAnswers, 3)
        answerChoices = falseAnswers + [trueAnswer]
        random.shuffle(answerChoices)
        
        #Write the question and the answer choices to the quiz file.
        quizFile.write(f'{NumOfQues + 1}. What is the Capital of {states[NumOfQues]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {answerChoices[i]}\n")
        quizFile.write('\n')
        
        #Write the answer key to a file.
        answerFile.write(f"{NumOfQues + 1}. {'ABCD'[answerChoices.index(trueAnswer)]}")
        
    quizFile.close()
    answerFile.close()