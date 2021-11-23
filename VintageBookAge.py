book_age = int(input('What year was the book was published? '))


def the_century(book_age):
    if book_age < 1900 and book_age >= 1800:
        century = 'Nineteenth Century'
    elif book_age < 1951 and book_age >= 1900:
        century = 'Twentieth Century'
    else:
        century = 'Error'
    return century


def the_decade(book_age):
    if book_age in range(1800, 1809) or book_age in range(1900, 1909):
        decade = 'Hundreds'
    elif book_age in range(1810, 1819) or book_age in range(1910, 1919):
        decade = 'Tens'
    elif book_age in range(1820, 1829) or book_age in range(1920, 1929):
        decade = 'Twenties'
    elif book_age in range(1830, 1839) or book_age in range(1930, 1939):
        decade = 'Thirties'
    elif book_age in range(1840, 1849) or book_age in range(1940, 1949):
        decade = 'Fourties'
    elif book_age in range(1850, 1859) or book_age == 1950:
        decade = 'Fifties'
    elif book_age in range(1860, 1869):
        decade = 'Sixties'
    elif book_age in range(1870, 1879):
        decade = 'Seventies'
    elif book_age in range(1880, 1889):
        decade = 'Eighties'
    elif book_age in range(1890, 1899):
        decade = 'Nineties'
    else:
        decade = 'this book is out of range.'
    return decade


final_century = the_century(book_age)
final_decade = the_decade(book_age)

print(f"{final_century}, {final_decade}")
