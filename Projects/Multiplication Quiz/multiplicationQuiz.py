#! python3
# Miltiplication Quiz

import pyinputplus as pyip
import random, time

numQuestions = 10
numCorrect = 0
for questionNum in range(numQuestions):
    # pick two numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    text = 'Question%s : %s x %s = ' % (questionNum, num1, num2)
    #text = f'Question{questionNum} : {num1} x {num2} = ' # this also works
    try:
        response = pyip.inputStr(prompt=text, timeout=8, limit=3, allowRegexes=['^%s$' % (num1*num2)], blockRegexes=[('.*', 'Incorrect!')])
        # note: ultimately, incorrect comes down to 'out of time' or 'out of tries', since multiple attempts are provided to provide a correct response
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        numCorrect += 1

time.sleep(1)
print(f'Score : {numCorrect}/{numQuestions}')