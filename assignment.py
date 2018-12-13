def grade(grade_list):
    for x in grade_list:
        if 100 >= x >= 90:
            print('Excellent')
        elif 89 >= x >= 70:
            print('Very good')
        elif 69 >= x >= 60:
            print('Good')
        elif 59 >= x >= 40:
            print('Poor')
        elif 39 >= x >= 20:
            print('Very poor')
        else:
            print('Repeat')
    print('-' * 20, '\n')


def question_zero():
    grades = [23, 4, 5, 6, 64, 90, 67, 98, 45, 23, 67, 78, 89]
    list1, list2 = [], []

    for mark in grades:
        if mark > 50:
            list1.append(mark)
        else:
            list2.append(mark)

    print(' Grading list one', '\n', '-' * 17)
    grade(list1)

    print(' Grading list two', '\n', '-' * 17)
    grade(list2)


def question_one():
    valid_nums = []
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 == 0:
            valid_nums.append(num)
    return valid_nums


def question_two():
    num_of_lines = int(input('Enter number of lines of sequence: '))
    sequence = [input().upper() for l in range(num_of_lines)]

    print('\n')
    for line in sequence:
        print(line)


def question_three(nums):
    # converting binary numbers to decimal
    decimal_equiv = [int(bi_str, 2) for bi_str in nums.replace(',', ' ').split()]
    for n in decimal_equiv:
        if n % 5 == 0:
            return bin(n)[2:]


def question_four():
    transaction_num = int(input('Enter number of transactions: '))
    total_in_bank = 0
    for trans in range(transaction_num):
        trans = input().split()
        if trans[0] == 'D':
            total_in_bank += int(trans[1])
        else:
            total_in_bank -= int(trans[1])

    return total_in_bank


def printList():
    squares = [x ** 2 for x in range(1, 21)]
    for num in squares[:5]:
        print(num)


if __name__ == '__main__':
    """
        Please uncomment each function to see how it works, thanks.
        By -Kyeza Arnold M
    """
    # question_zero()
    # print(question_one())
    # question_two()
    # print(question_three(input()))
    # print(question_four())
    # printList()
