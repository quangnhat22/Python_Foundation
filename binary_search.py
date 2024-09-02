lstNum = [7,2,1,9,20,66,44,84, 100, 264,333, 631, 10, 55]
# nhap 1 so => tim so do trong mang
# co tra ve so do
# khong tra ve -1

def sort_list():
    for i in range(len(lstNum)):
        for j in range(i+1, len(lstNum)):
            if lstNum[i] > lstNum[j]:
                lstNum[i], lstNum[j] = lstNum[j], lstNum[i]

def bubble_sort():
    n = len(lstNum)
    for i in range(n):
        isSwapped = False
        for j in range(n-i-1):
            if lstNum[j] > lstNum[j+1]:
                lstNum[j], lstNum[j+1] = lstNum[j+1], lstNum[j]
                isSwapped = True
        if (isSwapped == False):
            break


def binary_search(num):
    bubble_sort()

    left = 0
    right = len(lstNum) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lstNum[mid] == num:
            return mid
        elif lstNum[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    num = int(input("Nhap so can tim: "))
    result = binary_search(num)
    if result == -1:
        print("Khong tim thay so")
    else:
        print(f"Tim thay so {num} trong mang")

if __name__ == "__main__":
    main()