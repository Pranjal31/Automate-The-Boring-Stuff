#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

from pathlib import Path
import random

# The quiz data. Keys are states and values are their capitals.
CAPITAL_TABLE = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

NUM_STUDENTS = 35
NUM_OPTIONS = 4
OPTIONS = ['A', 'B', 'C', 'D']

# create directory for quiz and answer key
data_path = Path.cwd() / Path('data')
data_path.mkdir()

# Generate quiz files
for quizNum in range(NUM_STUDENTS):
    # Create the quiz and answer key files.
    quizFile = open(data_path / f"capitalsquiz{quizNum + 1}.txt", 'w')
    answerFile = open(data_path / f"capitalsquiz_answers{quizNum + 1}.txt", 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')
   
    # Shuffle the order of the states.
    states = list(CAPITAL_TABLE.keys())
    random.shuffle(states)
    capitals = list(CAPITAL_TABLE.values())

    # Loop through all 50 states, making a question for each.
    for quesNum in range(len(states)):
        # write question to quiz file
        state = states[quesNum]
        quizFile.write(f"Q{quesNum + 1} : What's the capital for the state of {state}?\n")
        ans_options = []
        # correct option
        answer = CAPITAL_TABLE.get(state)
        ans_options.append(answer)
        # incorrect options
        for opt_idx in range(NUM_OPTIONS - 1):
            idx = random.randint(0, len(capitals) - 1)
            incorrect_answer = capitals[idx]
            # find a new option if this one is a) correct answer OR b) already picked incorrect answer
            while incorrect_answer == answer or incorrect_answer in ans_options:
                idx = random.randint(0, len(capitals) - 1)
                incorrect_answer = capitals[idx]

            ans_options.append(incorrect_answer)
        
        random.shuffle(ans_options)

        for opt_idx in range(NUM_OPTIONS):            
            quizFile.write(f"{OPTIONS[opt_idx]}. {ans_options[opt_idx]}\n")
            # answer in ABCD format
            if ans_options[opt_idx] == answer:
                file_answer = OPTIONS[opt_idx]
        quizFile.write("\n")

        # write answer to answer file (A, B, C, or D)
        answerFile.write(f"{quesNum + 1}. {file_answer}\n")

quizFile.close()
answerFile.close()


            


  
