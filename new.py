__author__ = 'student'

while True:
    s_id = input('Choose what you would like to do from the following options: \n1.)Scan student id?,\n2.)View Report, \n3.)Quit? \nType the option number here: ')
    if s_id in ['1']:
        pass# the scan id group write your code here:
    elif s_id in ['2']:
        report_menu = input('Choose to see either the student reports or class reports.\nC)Class Report\nS)Student Menu.')
        if report_menu in ['c','C']:
            print('You are now in the class reports section.')
            class_report = input('Enter period number:')
            if class_report in ['p1,p2,p3,p4,p5,p6,p7,p8,p9,p10']:

                break
        elif report_menu in ['s','S']:
            print('You are now in the student report menu.')
        # the view report group write your code here:
    else:
