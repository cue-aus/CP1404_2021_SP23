"""
Testing for functions
"""
import csv


def is_leap(year):
    """return true if year is an Olympic year"""
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False


def tax_return(income):
    if income <= 16000:
        return 0
    else:
        return (income - 16000) * 0.2


def size_compare(L1, L2):
    if len(L1) == len(L2):
        return 0
    elif len(L1) > len(L2):
        return 1
    else:
        return -1


def main():
    print("Start the main function")
    for year in range(1900, 2022):
        if is_leap(year):
            print(year, end=' ')
    print()
    print(tax_return(16000))
    print(tax_return(15000))
    print(tax_return(20000))
    print(size_compare([], [1]))
    print(size_compare([], []))
    print(size_compare([1, 2], [1]))

    my_list = [['a', 'b', 'cdf'], [1, 2, '123']]
    with open('test.csv', 'w') as f:
        write = csv.writer(f)
        # write.writerow(header)
        write.writerows(my_list)

    a_list = ["a", "b", "c"]
    joined_string = ",".join(a_list)
    print(joined_string)

    a_list = [1, '2', 3]
    converted_list = [str(element) for element in a_list]
    joined_string = ",".join(converted_list)
    print(joined_string)


if __name__ == '__main__':
    main()
