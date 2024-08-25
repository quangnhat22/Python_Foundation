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
    for product in tiki_products:
        print(product)

def add_new_product():
    name = input("Name: ")
    price = float(input("Price: "))
    desc = input("Description: ")

    new_product = {
        "id": len(tiki_products) + 1,
        "name": name,
        "price": price,
        "desc": desc,
    }

    tiki_products.append(new_product)

def search_product():
    search_name = input("Nhap ten san pham ban muon tim kiem: ")
    for product in tiki_products:
        if search_name.lower() in product["name"].lower():
            print(
                f"Found: {product["id"]}, {product['name']}, {product['price']}, {product['desc']}")
            return product
        else:
            print(
                "Khong tim thay")
            return None

def delete_product():
    product_founded = search_product()
    if product_founded:
         products = [product for product in tiki_products if product["id"] != product_founded["id"]]
         print("Mang sau khi xoa phan tu vua nhap:   ")
         for i in products:
            print(f"{i['id']}, {i['name']}, {i['price']}, {i['desc']}")



def edit_product():
    product_founded = search_product()
    if product_founded:
        for product in tiki_products:
            if product["id"] == product_founded["id"]:
                product["name"] = input("Name edit: ")
                product["price"] = int(input("Price edit: "))
                product["desc"] = input("Description edit: ")
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
                print("Existing...")
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
