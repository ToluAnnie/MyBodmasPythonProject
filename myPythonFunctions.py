def get_user_score(user_name):
    try:
        user_details = open('user_scores.txt', 'r')
        for line in user_details:
            content = line.split(', ')
            if content[0] == user_name:
                return content[1]
            else:
                user_details.close()
                return -1
    except IOError:
        print('File not found. A new file will be created.')
        # I think I could still improve upon this code to ensure the user doesn't have to run it twice
        user_details = open('user_scores.txt', 'w')
        user_details.close()
        return '-1'


def update_user_score(new_user, user_name, score):
    from os import remove, rename

    if new_user is True:
        user_details = open('user_scores.txt', 'a')
        user_details.write(f'{user_name}, {score}')
        user_details.close()
    else:
        user_details = open('user_scores.txt', 'r')
        for line in user_details:
            content = line.split(',')
            if content[0] == user_name:
                temp_file = open('userScores.tmp', 'w')
                temp_file.write(f'{user_name}, {score}')
            else:
                temp_file.write(line)
        user_details.close()
        temp_file.close()

        remove('user_scores.txt')
        rename('userScores.tmp', 'user_scores.txt')


def generate_question():
    from random import randint

    operand_list = [0, 0, 0, 0, 0]
    operator_list = ['', '', '', '']
    operator_dict = {1: '+', 2: '-', 3: '*', 4: '**'}

    for index in range(0, 4):
        operand_list[index] = randint(1, 9)

    for index in range(0, 4):
        if index > 0 and operator_list[index - 1] != '**':
            operator = operator_dict[randint(1, 4)]
        else:
            operator = operator_dict[randint(1, 3)]
        operator_list[index] = operator

    question_string = str(operand_list[0])

    for index in range(1, 5):
        question_string = f'{question_string} {operator_list[index - 1]} {str(operand_list[index])}'

    result = eval(question_string)
    question_string = question_string.replace('**', '^')
    print(question_string)

    answer = input('Answer: ')
    while True:
        try:
            if int(answer) == result:
                print('Excellent')
                return '1'
            else:
                print(f'Sorry, wrong answer. The correct answer is {result}')
                return '0'
        except ValueError:
            print('You did not enter a number. Please try again.')
            answer = input('Answer: ')








