while True:
    dpm=[31,28,31,30,31,30,31,31,30,31,30,31]
    year=int(input("Input the year: "))
    Leapyear = False
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print ("The year you inputed is leap year(366 days)! ")
        leapyear = True
        dpm[1]=29
    else:
        print ("The year you inputed is common year(365 days)! ")
    mode=1
    mode=int(input("Do you want to change DOY to date(1) or change date to DOY(2)? : "))
    if mode==1:
        doy=int(input("Input the day of year: "))
        for month in range(12):
            for day in range(dpm[month]):
                doy-=1
                if doy==0:
                    break
            if doy==0:
                break
        print ("Month: ",month+1)
        print ("Day: ", day+1)
    else:
        doy=0
        month=int(input("Input the month: "))
        day=int(input("Input the day: "))
        for months in range(month):
            for days in range(dpm[months]):
                doy+=1
                if (days==day-1) and (months==month-1):
                    break
        print ("The day of year is: ",doy)
    again=input("Do you want another loop? yes or no: ")
    if again=="no":
        break
