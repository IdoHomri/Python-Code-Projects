# this exercises are taken from https://www.w3resource.com/python-exercises/python-basic-exercises.php

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

def ex29():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    print(color_list_1.difference(color_list_2))
    print(color_list_2.difference(color_list_1))

