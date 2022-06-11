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
