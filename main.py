import os

while True:
    directory = input("Please enter a directory to save your file in: ")
    if os.path.isdir(directory):
        print()
        filename = input("Please enter the name of the your file you want to save (be sure to add '.txt'): ")
        filename_directory = os.path.join(directory, filename)

        print()

        name = input("Please enter your name: ").title()
        address = input("Please enter your address: ")
        phone_number = input("Please enter your phone number: ")

        with open(filename_directory, 'w') as file_object:
            file_object.write(name + ', ' + address + ', ' + phone_number)
        
        print("\nFile saved! Does this:")
        with open(filename_directory) as file_object:
            for line in file_object:
                print(line)
        valid = input("look correct?\nY/N: ")

        if valid.upper() == "Y":
            print("\nAwesome! Thanks for using this program.\n")
            break
        else:
            print("\nLet's retry this.\n")
    else:
        print("\nSorry, that directory does not exist.\n")