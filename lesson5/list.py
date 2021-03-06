#!/usr/local/bin/python3

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']
print(endings)
year = input('year: ')
month = input('month(1-12): ')
day   = input('day(1-31): ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print(month_name + ' ' + ordinal + ' ' + year)