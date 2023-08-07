from distutils.file_util import write_file
import os.path
from datetime import datetime

from file_util import read_invoice, write_csv, remove_file


def return_costume(file_content):
    while True:
        c_id = input("Please enter your bill no or press 'q' for back: ")
        if c_id == 'q':
            break
        elif os.path.exists(os.path.join('rent', c_id + ".txt")):
            (customer_id, rent_date, customer_name, products) = get_invoice(c_id)
            current_date = datetime.now()
            rent_date_date = datetime.strptime(rent_date, "%m/%d/%Y")
            date_difference = current_date - rent_date_date
            date_difference_day = date_difference.total_seconds() / (60 * 60 * 24)
            # file 10 added for each day if returned after 5 days
            fine = 0.0
            if date_difference_day > 5:
                fine_day = date_difference_day - 5
                fine = 10 * fine_day
            total = 0
            for i in products:
                total += products[i][2] * products[i][1]
                for j in file_content:
                    if (products[i][0] == file_content[j][0]):
                        file_content[j][3] += products[i][1]
            write_csv(file_content, 'customes.csv')
            new_content = ""
            new_content += customer_id + "\n"
            new_content += customer_name + "\n"
            new_content += rent_date + "\n"

            for i in products:
                quantity = products[i][1]
                product_name = products[i][0]
                product_price = products[i][2]
                total_price = product_price * quantity
                new_content += "\n" + product_name + ",\t" + str(quantity) + ',\t' + str(total_price)
                write_file(new_content, os.path.join( "return",customer_id + '.txt'))
            print("*" * 30)
            print(new_content)
            print("*" * 30)
            print("-"*30)
            print(" "*10+"Instrument returned")
            print("-" * 30)
            net_total = total+fine
            print("total price is "+ str(net_total) + " with fine of "+str(fine))
            remove_file(os.path.join('rent', customer_id + ".txt"))
            break
        else:
            print("Please enter valid customer Id")
            continue


def get_invoice(customer_id):
    return read_invoice(os.path.join('rent', customer_id + ".txt"))
