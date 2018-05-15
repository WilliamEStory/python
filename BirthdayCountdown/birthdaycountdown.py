import datetime

print('Birthday App')

def get_birthday_from_user():
    print('when were you born? ')
    year = input('Year [YYYY]: ')
    month = input('Month [MM]: ')
    day = input('Day [DD]: ')

    bday = datetime.date(int(year), int(month), int(day))

    return bday

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(number_of_days):
    if number_of_days < 0:
        print('Your birthday was {0} days ago!'.format(number_of_days * -1))
    elif number_of_days > 0:
        print('Your birthday is in {0} days!'.format(number_of_days))
    else:
        print('Happy birthday!')


def main():
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)

main()


