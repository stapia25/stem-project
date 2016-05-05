__author__ = 'student'

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

