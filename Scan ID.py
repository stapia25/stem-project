i__author__ = 'student'
import time
import pickle
with open("student_info.p","rb") as f:
         student_info = pickle.load(f)
while True:
     if s_id in ['1']:
        try:
                scan = input('Scan your ID here: ')
                print('%s signed in at - %s' % (student_info[scan], time.strftime("%I:%M %p")))
        except KeyError:
                print('This is an invalid ID. Please try again.')
        if scan in ['l', 'L']:
                 print('%s checked in late - %s' % (student_info[s_id], time.strftime("%I:%M %p")))

    elif s_id in ['2']:
        pass# the view report group write your code here:
    else:
        pass# the quit group write your code here:
