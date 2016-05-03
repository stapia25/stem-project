i__author__ = 'student'
import time
import pickle
with open("student_info.p","rb") as f:
         student_info = pickle.load(f)
while True:
    s_id = input('Choose what you would like to do from the following options: \n1.)Scan student id?,\n2.)View Report, \n3.)Quit? \nType the option number here: ')
    if s_id in ['1']:
        try:
            s_id = input('Scan your ID here: ')
            print('%s signed in at - %s' % (student_info[s_id], time.strftime("%I:%M %p")))
        except KeyError:
            print('This is an invalid ID. Please try again.')

    elif s_id in ['2']:
        pass# the view report group write your code here:
    else:
        pass# the quit group write your code here:
