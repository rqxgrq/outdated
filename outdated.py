# Expected inputs in month, day and year:
# 9/8/1636
# September 8, 1636

def main():
    print_iso8601_formatted_date()


def print_iso8601_formatted_date():
    while True:
        # The try block deals with input like 1/2.2022 or 1.13.1990
        try:
            month, day, year = get_month_day_year()
        except ValueError:
            continue
        except TypeError:
            continue

        # Deal with inputted day or month that is not in the form of
        # decimal. If day and month is in the form of decimal,
        # the loop won't restarted.
        if not day.isdecimal() or not year.isdecimal():
            continue

        day = format_day(day)
        if day == None:
            continue

        year = format_year(year)
        if year == None:
            continue

        month = format_month(month)
        # Deal with inputted month which not fullname or not a month
        # at all like 'jan' or 'wakaka'.
        if month == None:
            continue

        print(f'{year}-{month}-{day}')
        break


def format_year(year):
    if int(year) >= 1:
        return year


def format_day(day):
    if 1 <= int(day) <= 31:
        if int(day) < 10:
            return f'0{day}'
        else:
            return day


def format_month(month):
    months = {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12,
    }

    if month == None:
        return None
    elif month.isdecimal():
        if 1 <= int(month) <= 12:
            if int(month) < 10:
                return f'0{month}'
            else:
                return month
    else:
        if month.title() in months:
            if months[month.title()] < 10:
                return f'0{months[month.title()]}'
            else:
                return months[month.title()]


def get_month_day_year():
    date = input('Date: ').strip()
    try:
        # Deal with month in number
        month, day, year = date.split('/')
        # If it's a alphabet month, change month to None
        if month.isalpha():
            month = None
    except ValueError:
        if ',' in date:
            month, day, year = date.replace(',', '').split(' ')
        else:
            return

    return month, day, year


main()
