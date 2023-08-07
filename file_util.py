import os

csv_header = "Name, \tBrand, \tPrice, \tQuantity"


def read_csv(filename):
    file = open(filename, 'r')
    data = file.readlines()
    # remove csv header
    data.pop(0)
    file.close()
    return data


def make_dictionary(data):
    product = {}
    for i in range(len(data)):
        product[i] = data[i].replace("\n", '').split(",")
        product[i][0] = product[i][0].strip()
        product[i][1] = product[i][1].strip()
        product[i][2] = float(product[i][2])
        product[i][3] = int(product[i][3])
    return product


def write_file(data, file):
    f = open(file, 'w')
    f.write(data)
    f.close()


def write_csv(data_list, file):
    data = csv_header
    for key in data_list:
        data = data + "\n{:<4},{:<50},{:<20},{:<10}".format(data_list[key][0], data_list[key][1],
                                                  data_list[key][2], data_list[key][3])
    print(data.replace(",",''))
    write_file(data, file)


def read_invoice(file_name):
    file = open(file_name)
    data = file.readlines()
    id = data[0].replace('\n', "")
    rent_date = data[1].replace("\n", "")
    customer_name = data[2].replace("\n", "")
    items = data[3:]
    products = {}
    for i in range(len(items)):
        products[i] = items[i].replace("\n", '').split(",")
        products[i][0] = products[i][0].strip()
        products[i][1] = int(products[i][1])
        products[i][2] = float(products[i][2])
    #     return as tuple
    return id, rent_date, customer_name, products


def remove_file(file_name):
    os.remove(file_name)
