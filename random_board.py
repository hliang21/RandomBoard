# RandomBoard Exercise
import random


def main():
    # initialize a 10 x 10 array/list
    arr = [[0 for y in range(10)] for x in range(10)]

    # assign a random number to each element in arr
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = random.randint(0, 9)

    print_2d_array(arr)
    find_sum(arr)


def print_2d_array(arr):
    for x in arr:
        for y in x:
            print(y, end=' ')
        print()


def find_sum(arr):
    sum_of_arr = 0
    for x in arr:
        for y in x:
            sum_of_arr += y

    print('The sum is ' + str(sum_of_arr))


if __name__ == '__main__':
    main()
