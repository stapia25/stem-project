__author__ = 'student'
#eliel and abe and wayne
import pickle
with open('student_info.p','rb') as f:
    student_info = pickle.load(f)
while True:
    s_id = input('Choose what you would like to do from the following options: \n1.)Scan student id?,\n2.)View Report, \n3.)Quit? \nType the option number here: ')
    if s_id in ['1']:
        pass# the scan id group write your code here:
    elif s_id in ['2']:
        report_menu = input('C)Class Report \nS)Student Report \nType Here:')
        if report_menu in ['C','c']:
            print('Class Report')
        elif report_menu in ['S','s']:
            pickle.dump( student_info, open("student_info.p", "wb"))
            student_ID = {"ID#":"name"}
            student_info = input('Enter the ID number of the student or go bck to menu?')
            if student_info in ['']:
                student_ID = pickle.load(open)


            pickle.close()
            main_student = input('Back to Main Menu?\n[Y or N]')
            if main_student in ['Y','N']:

