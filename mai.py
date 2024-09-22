products = ["cat", "banana", "obama", "batman", "car", "cow", "alibaba"]

inp = input("Nhap tu khoa can tim: ")
output = []

for i in range(len(products)):
    if products[i].startswith(inp):
        output.append(i)

for i in output:
    print(i, end=" ")