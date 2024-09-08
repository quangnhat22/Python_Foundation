# 1 Tính giai thừa của số nguyên
def calc_factorial(value):
    if value == 0 or value == 1:
        return 1
    return value * calc_factorial(value - 1)


# 2 Tính tổng các chữ số của một số nguyên
def count_number(value):
    number = 1
    if value % 10 == value:
        return 1
    number += count_number(value // 10)
    return number


def count_total_number(value):
    if value // 10 == 0:
        return value
    return value % 10 + count_total_number(value // 10)


# 3 Đảo ngược chuỗi
def reverse_string(string):
    if len(string) == 1:
        return string
    return string[len(string) - 1] + reverse_string(string[:len(string) - 1])


# 4 Tìm số lớn nhất trong mảng
def find_max_in_array(array, max, index):
    if index >= len(array):
        return max
    if array[index] > max:
        return find_max_in_array(array, array[index], index + 1)
    return find_max_in_array(array, max, index + 1)


def main():
    input = '123 456    '
    print(reverse_string(input))


if __name__ == '__main__':
    main()
