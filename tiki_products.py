tiki_products = [
    {
        "id": 1,
        "name": "Laptop A",
        "price": 1000,
        "desc": "This is a laptop A",
        "img": f"https://fastly.picsum.photos/id/1/200/300"
    },
    {
        "id": 2,
        "name": "Laptop B",
        "price": 2000,
        "desc": "This is a laptop B",
        "img": f"https://fastly.picsum.photos/id/1/200/300"
    },
    {
        "id": 3,
        "name": "Laptop C",
        "price": 4000,
        "desc": "This is a laptop C",
        "img": f"https://fastly.picsum.photos/id/1/200/300"
    }
]

def get_products():
    global tiki_products
    for product in tiki_products:
        print(product)

def add_new_product():
    name = input("Ten: ")
    price = float(input("Gia tien: "))
    desc = input("Mieu ta: ")
    global tiki_products
    new_product = {
        "id": len(tiki_products) + 1,
        "name": name,
        "price": price,
        "desc": desc,
        "img": f"https://fastly.picsum.photos/id/1/200/300"
    }
    tiki_products.append(new_product)

def search_product():
    search_name = input("Nhap ten san pham ban muon tim kiem: ")
    global tiki_products
    for product in tiki_products:
        if search_name.lower() in product["name"].lower():
            print(
                f"Da tim thay: {product["id"]}, {product['name']}, {product['price']}, {product['desc']}")
            return product
    print(
        "Khong tim thay")
    return None

def delete_product():
    product_founded = search_product()
    global tiki_products
    if product_founded:
         tiki_products = [product for product in tiki_products if product["id"] != product_founded["id"]]
         print("Xoa thanh cong")
    else:
        print("Xoa that bai")

def edit_product():
    product_founded = search_product()
    if product_founded:
        for product in tiki_products:
            if product["id"] == product_founded["id"]:
                product["name"] = input("Ten can sua: ")
                product["price"] = int(input("Gia can sua: "))
                product["desc"] = input("Mo ta: ")
                print("Mang sau khi xoa phan tu vua nhap:   ")
                for i in tiki_products:
                    print(f"{i['id']}, {i['name']}, {i['price']}, {i['desc']}")



def main():
    while True:
        print("\n Quan ly san pham: ")
        print("1. Hien thi danh sach san pham")
        print("2. Them san pham")
        print("3. Xoa san pham")
        print("4. Sua san pham")
        print("5. Tim kiem san pham")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
               get_products()
            elif choice == 2:
                add_new_product()
            elif choice == 3:
                delete_product()
            elif choice == 4:
                edit_product()
            elif choice == 5:
                search_product()
            elif choice == 6:
                print("Thoat...")
                break
            else:
                print("Lua chon khong hop le!")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
