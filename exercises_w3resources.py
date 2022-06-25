# this exercises are taken from https://www.w3resource.com/python-exercises/python-basic-exercises.php

# calendar  
import math


def ex12():
    import calendar

    suc = False

    while suc == False:
        m = int(input('Insert Month: '))
        y = int(input('Insert Year: '))


        print('\n')
        try:
            calendar.prmonth(y,m)
            suc = True
        except:
            print('Month or Year are in incorrect format, try again..')
        print('\n')

# check if n exists in group_n
def ex25(group_n, n):
    for x in group_n:
        if(x == n):
            return True 
    return False

# even and braker
def ex28():
    numbers = [    
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
        958,743, 527
        ]

    braker = 237

    for n in numbers:
        if n%2==0:
            print(n)
        if(n==braker):
            print(str(n) + " - the braker")
            break

# array comperation
def ex29():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    print(color_list_1.difference(color_list_2))
    print(color_list_2.difference(color_list_1))

# triangle area
def ex30(h, w):
    return float((h * w) / 2)

# check if file exsists
def ex42(file):
    import os.path as p
    return p.exists(file)

# get os info (copied, was not written by me)
def ex43():
        import os, sys, platform, sysconfig
        print("os.name                     ", os.name)
        print("sys.platform                ", sys.platform)
        print("platform.system()           ", platform.system())
        print("sysconfig.get_platform()    ", sysconfig.get_platform())
        print("platform.machine()          ", platform.machine())
        print("platform.architecture()     ", platform.architecture())

# count the number occurrence of a specific character in a string
def ex84(str, ch):
    return str.count(ch)


print(ex84("ido homri",'i'))