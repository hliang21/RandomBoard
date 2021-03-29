# RandomBoard Exercise
import random


def main():
    arr = []
    num_row = 10
    num_col = 10

    for i in range(num_row):
        row = []
        for j in range(num_col):
            row.append(random.randint(0, 9))
        arr.append(row)

    print_2d_array(arr)
    find_sum(arr)


def print_2d_array(arr):
    for x in arr:
        for y in x:
            print(y, end=' ')
        print()


def find_sum(arr):
    sum = 0
    for x in arr:
        for y in x:
            sum += y

    print('The sum is ' + str(sum))


if __name__ == '__main__':
    main()
