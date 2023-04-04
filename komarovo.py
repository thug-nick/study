#For a week until the 2nd I'm going to Komarovo ... by a train on Sunday
#Show dates that match: day of week is Sunday and date +7 days will be 2nd of any month for next 3 years
import datetime
start_date = datetime.datetime.now()
for single_date in (start_date + datetime.timedelta(n) for n in range(1095)):
    d = (single_date - datetime.timedelta(days=7))
    #print(str(single_date.strftime('%d')) + " " + str(d.strftime('%w')) )
    if  (str(single_date.strftime('%d')) == "02"):
        if str(d.strftime('%w')) == "0":
            print(d.strftime('%Y-%m-%d'))
