months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']


def print_months(months):
    for month in months:
        print(month)


def get_short_names(months):
    for month in months:
        print(month[0:3])


def first_letter_months(months, letter):
    for month in months:
      for letter in month:
           print(month[:1])
    return letter


def main():
    print_months(months)
    get_short_names(months)


main()
