try:
    month = int(input("Enter the month in numeric form: "))
except ValueError:
    print("Error: Invalid Month Input")
else:
    try:
        day = int(input("Enter the day in numeric form: "))
    except ValueError:
        print("Error: Invalid Day Input")
    else:
        try:
            year = int(input("Enter the year as two numerical digits (for example: 98, 20, 21): "))
            if year < 0 or year > 99:
                raise ValueError
        except ValueError:
            print("Error: Invalid Year Input")
        else:
            print("Success: Congratulations! you entered the correct date.")
            print("{}/{}/{}".format(month, day, year))
    
    # Command to exit program if day input is invalid
    if day < 1 or day > 31:
        print("Error: Invalid Day Input")
        exit()
        
# Command to exit program if month input is invalid
if month < 1 or month > 12:
    print("Error: Invalid Month Input")
    exit()
