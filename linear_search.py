lstNum = [7,2,1,9,20,66,44,84, 100, 264,333, 631, 10, 55]
# nhap 1 so => tim so do trong mang
# co tra ve so do
# khong tra ve -1

def linear_search(lstNum, num):
    for i in range(len(lstNum)):
        if lstNum[i] == num:
            return i
    return -1

def main():
    num = int(input("Nhap so can tim: "))
    result = linear_search(lstNum, num)
    if result == -1:
        print("Khong tim thay so")
    else:
        print(f"Tim thay so {num} tai vi tri {result}")

if __name__ == "__main__":
    main()

