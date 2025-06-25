#current = date.today()
#input_i = input("please input your date of birth in the format "0000-00-00" for "year-month-day"")
# for testing purposes the proper ways to get the current date and the users date of birth are above with placeholders below.

try:
    input_i = ("2025-01-01")
    year_i = int(input_i[0:3])
    month_i = int(input_i[5:7])
    day_i = int(input_i[9:11])

except:
    print("wrong_input.error")
    sys.exit()


#current year
current = ("2025-01-01")
year_c = int(current[0:3])
month_c = int(current[5:7])
day_c = int(current[9:11])


# getting the specific numbers
conv_year = year_i - year_c
conv_mon = month_i - month_c
conv_day = day_i - day_c


#Final output
minutes = (round(conv_year + conv_mon + conv_day))
print("You are " + minutes + " minutes old")