import datetime
import sys

while True :
    YOB = input('year of birth ')
    try :
        YOB = datetime.datetime.strptime(YOB, "%d/%m/%Y")
        break
    except ValueError:
        print("Error: must be format dd/mm/yyyy ")
        userkey = input("press 1 to try again or 0 to exit:")
        if userkey == "0":
            sys.exit()

print (f"YOB is {YOB}")            
