# way 1

questions = ['Who founded python?', 'What is the shortened version of "boolean" in Python?', 'what is 23+71?',
             'when was Python created?', 'To assign a variable, do we use = or ==?']

answers = ['Guido van Rossum', 'bool', '94', '1991', '=']


def quizGame1(questions, answers):
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        ans = input('Please answer \n')
        if ans == answers[i]:
            print('CORRECT!!!!')
            score += 1
        else:
            print('incorrect, you FOOOOOL!!!')

    print(f'Final score: {score}')


# better way

QUESTIONS_AND_ANSWERS = [{'question': 'Who founded python?', 'answer': 'Guido van Rossum'},
                         {'question': 'What is the shortened version of "boolean', 'answer': 'bool'},
                         {'question': 'what is 23+71?', 'answer': '94'},
                         {'question': 'To assign a variable, do we use = or ==?', 'answer': '=='}]


def quizGame2(qna):
    score = 0
    for q in qna:
        print(q['question'])
        answer = input('Your answer? \n')
        if answer.lower() == q['answer'].lower():
            print('CORRECT!!!!')
            score += 1
        else:
            print('incorrect, you FOOOOOL!!!')
    print(f'Final score: {score}')


# quizGame1(questions, answers)

quizGame2(QUESTIONS_AND_ANSWERS)
