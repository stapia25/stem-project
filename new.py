__author__ = 'student'

while True:
    s_id = input('Choose what you would like to do from the following options: \n1.)Scan student id?,\n2.)View Report, \n3.)Quit? \nType the option number here: ')
    if s_id in ['1']:
        pass# the scan id group write your code here:
    elif s_id in ['2']:
        pass# the view report group write your code here:
    elif s_id in ['3']:
        exit = input('Mark rest absent?\n (y/[n]')
        if exit in ['N','n']:
            exit2 = input('Still Quit?(y/[n]')
        elif exit in ['y','Y']:
            exit1 = input('Mark all missing absent? (y/[n]')
            if exit in ['y','Y','N', 'n']:
                exit2 = input('Still Quit?(y/[n]')
                break
