__author__ = 'student'

import time
import pickle
with open("student_info.p","rb") as f:
    student_info = pickle.load(f)
while True:
    s_id = input('Choose what you would like to do from the following options: \n1.)Scan student id?,\n2.)View Report, \n3.)Quit? \nType the option number here: ')
    if s_id in ['1']:
        try:
            scan = input('Scan your ID here or type L to start marking students late: ')

            if scan in ['l', 'L']:
                input('Scan late student ID: ')
                print('%s signed in late at - %s' % (student_info[scan], time.strftime("%I:%M %p")))
            else:
                print('%s signed in at - %s' % (student_info[scan], time.strftime("%I:%M %p")))


        except KeyError:
                print('This is an invalid ID. Please try again.')
        else:
            print('ERROR. PLEASE TRY AGAIN')
    elif s_id in ['2']:
        report_menu = input('Choose to see either the student reports or class reports.\nC)Class Report\nS)Student Menu.')
        if report_menu in ['c','C']:
            print('You are now in the class reports section.')
            class_report = input('Enter period number:')
            if class_report in ['p1,p2,p3,p4,p5,p6,p7,p8,p9,p10']:

                break
        elif report_menu in ['s','S']:
            print('You are now in the student report menu.')
        pass
    elif s_id in ['3']:
        exit = input('Mark rest absent?\n (y/[n]')
        if exit in ['N','n']:
            exit2 = input('Still Quit?(y/[n]')
        elif exit in ['y','Y']:
            exit1 = input('Mark all missing absent? (y/[n]')
            if exit in ['y','Y','N', 'n']:
                exit2 = input('Still Quit?(y/[n]')
                break

