import os.path
import uuid
from datetime import datetime

from file_util import csv_header, write_csv, write_file


def rent_costume(data):
    cart = []
    while True:
        print_costume(data)
        selected_costume = input("Please input costume sn. amd press q to back ")
        if selected_costume == 'q':
            break
        try:
            selected_costume = int(selected_costume)
            if selected_costume not in data:
                print("Costume not exists please add valid costume")
                continue
            quantity = add_rent(data, selected_costume)
            data = new_product(data, selected_costume, quantity)
            cart.append({
                "quantity": quantity,
                "productId": selected_costume,
            })
            question = input("Want to rent more costume(y/n): ")
            if question == 'n':
                break
        except (RuntimeError, TypeError, NameError):
            print("Please press correct input")

    name = input("Please insert name of customer")
    date = datetime.now().strftime('%m/%d/%Y')
    id = str(uuid.uuid4())
    file_content = id + "\n" + date + '\n' + name
    for i in cart:
        product_name = data[i['productId']][0]
        product_price = data[i['productId']][2]
        total_price = product_price * quantity
        file_content += "\n" + product_name + ",\t" + str(quantity) + ',\t' + str(total_price)
        write_file(file_content, os.path.join( "rent",id + '.txt'))
    print("*" * 30)
    print(" " * 10 + "Bill of " + name)
    print(file_content)
    print("*" * 30)

def add_rent(data, index):
    while True:
        try:
            quantity = int(input("Please add quantity for product: "))
            if data[index][3] < quantity:
                continue
            return quantity
        except:
            print("Please add valid quantity")


def print_costume(data):
    print("*" * 70)
    print(" "*20+"List of Product\t")
    print("*" * 70)

    head = csv_header.split(',')
    print("{:<4}{:<50}{:<20}{:<10}{:<10}".format("sn", head[0], head[1],"price", "quantity"))
    for key in data:
        print("{:<4}{:<50}{:<20}{:<10}{:<10}".format(key, data[key][0], data[key][1], data[key][2], data[key][3]))
    print("-" * 40)


def new_product(data, product_id, quantity):
    data[product_id][3] = data[product_id][3] - quantity
    write_csv(data, 'customes.csv')
    return data
