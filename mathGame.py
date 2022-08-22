import myPythonFunctions as mPF

user_name = input('''Please enter your user name or create one if you're a new user: ''')
user_score = mPF.get_user_score(user_name)
if user_score == -1:
    new_user = True
    user_score = 0
else:
    new_user = False

user_choice = 0

while user_choice != '-1':
    user_score += mPF.generate_question()
    user_choice = input('Press Enter to Continue or -1 to Exit: ')

mPF.update_user_score(new_user=True, user_name='', score=str(user_score))

