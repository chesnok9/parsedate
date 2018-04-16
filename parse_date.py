import sys
import datetime


# Check string is valid year
def check_year(year_str):
    year=int(year_str)
    result=False

    if year >= 0:
        result=True

    return result

# Check string is valid month
def check_month(month_str):
    month = int(month_str)
    result = False

    if month > 0 and month <= 12:
        result = True

    return result

# Check string is valid day
def check_day(day_str):
    day = int(day_str)
    result = False

    if day > 0 and day <= 31:
        result = True

    return result

# Parse date from string
def parse_date(input_str):
    arr=input_str.split('/')

    years=[]
    months=[]
    days=[]

    # All valid values for year, month and days
    for item in arr:
        years.append(check_year(item))
        months.append(check_month(item))
        days.append(check_day(item))

    # Default result
    output_str = input_str + " is illegal"

    # loop for all valid combinations
    for index, value in enumerate(years):
        if years[index]:
            for index2, value2 in enumerate(months):
                if months[index2] and index2 != index:
                    for index3, value3 in enumerate(days):
                        if days[index3] and index3 != index and index3 != index2:
                            fail=False

                            try:
                                year=int(arr[index])
                                year = year + 2000 if year < 2000 else year
                                month=int(arr[index2])
                                day=int(arr[index3])

                                # Get date for valid combination with validation for illegal date
                                output_str=datetime.datetime(year, month, day, 0, 0).strftime("%Y-%m-%d")
                            except:
                                fail=True

                            # return first valid result
                            if not fail:
                                return output_str

    return output_str


in_filename='input.txt'

if len(sys.argv) > 1:
    in_filename=sys.argv[1]

try:
    with open(in_filename, 'r') as input_file:
        print("Input file:", in_filename)

        input_date=input_file.read()
        print("Input string:", input_date)
        output_date=parse_date(input_date)
        print("Parsed date:", output_date)

        out_filename="output.txt"
        print("Output file:", out_filename)

        try:
            with open(out_filename, "w") as output_file:
                output_file.write(output_date)
        except:
            print("Error writing file.")
except:
    print("Input file not found.")
