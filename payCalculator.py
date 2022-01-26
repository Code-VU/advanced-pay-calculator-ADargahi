def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    rate = input("Enter Rate: ")
    overtimeHrs = 0
    overtimeRate = float(rate) * 1.5
    gross_pay = 0
    
    if float(hrs) > 40:
        overtimeHrs = float(hrs)-40
        hrs = 40
        gross_pay = (float(hrs) * float(rate)) + (float(overtimeHrs) * float(overtimeRate))
    else:
        gross_pay = float(hrs) * float(rate)

    print(gross_pay)
    
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()