from rent_costume import rent_costume, print_costume
from file_util import read_csv, make_dictionary
from return_costume import return_costume


def app_intro():
    print("*" * 40)
    print("\t\tRental Store\t\t")
    print("*" * 40)


def main(name):
    try:
        file_content = make_dictionary(read_csv(name))
    except:
        print("Provided file is not valid")
        exit()
    app_intro()
    print()
    ask_question(file_content)
    print("-"*40)
    print(" "*10+"Thank you ")


def ask_question(file_content):
    while True:
        print("What do you want to do?")
        print("(1) \tRent a costume,\n(2) \tReturn costume \n(3) \tExit application")
        try:
            a = int(input("Please type one of the number : "))
            match a:
                case 1:
                    rent_costume(file_content)
                case 2:
                    return_costume(file_content)
                case 3:
                    break


                case default:
                    print("Please type valid number")
        except:
            print("Please type valid number 1")
            continue


if __name__ == '__main__':
    main('customes.csv')
