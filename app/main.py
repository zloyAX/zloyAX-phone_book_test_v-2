import os
from sty import fg, rs
from PIL import Image
from colorit import background, init_colorit
from art import text2art
import json


init_colorit()


def clear_scrin_logo_menu():
    os.system("cls" if os.name == "nt" else "clear")
    logo_menu()


def logo_menu():
    show_logo()
    show_menu()


def show_logo():
    text = text2art("Phone Book")
    logo = f"{fg(22, 46, 174) +text+rs.all}"

    print(logo)


def show_menu():
    print("1. Show contact")
    print("2. Add a contact")
    print("3. Edit contact")
    print(fg(248, 0, 18) + "4. Delete contact")
    print(fg(248, 0, 18) + "5. Clear contacts" + rs.all)
    print("6. Save the list to a text file")
    print("7. Generate test data")
    print(fg(192, 244, 0) + "8. Exit" + rs.all)


def show_contacts():
    with open("data.json", "r") as file:
        telephone_book = json.load(file)

    sorted_book = dict(sorted(telephone_book.items()))

    for key, value in sorted_book.items():

        text = text2art(key.upper())
        char = f"{fg(22, 46, 174) +text+rs.all}"
        print(char)

        for item in value:
            user_key = iter(item.keys())
            user_value = iter(item.values())

            img = Image.open(item["Photo"])
            img = img.resize((20, 10))

            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    print(background(" ", img.getpixel((x, y))), end="")
                try:
                    print(
                        "\t" + user_key.__next__(),
                        user_value.__next__().replace("\n", " "),
                        sep=":",
                        end="",
                    )
                except StopIteration:
                    pass
                print()
            print()


def add_contact():
    with open("data.json", "r") as file:
        telephone_book = json.load(file)

    name = input("Enter name: ").lower()
    phone = input("Phone: ")
    photo = input("Photo adress: ")

    first_char = name[0]

    if first_char in telephone_book:
        telephone_book[first_char].append(
            {"Name": name.capitalize(), "Phone": phone, "Photo": photo}
        )
    else:
        telephone_book.update(
            {first_char: [{"Name": name.capitalize(), "Phone": phone, "Photo": photo}]}
        )

    telephone_book = dict(sorted(telephone_book.items()))

    with open("data.json", "w") as file:
        json.dump(telephone_book, file)


def edit_contact():
    show_contacts()
    with open("data.json", "r") as file:
        telephone_book = json.load(file)
        try:
            name = input("Enter name: ").capitalize()
            first_char = name[0].lower()

            if first_char in telephone_book:
                for kei in telephone_book[first_char]:
                    if kei["Name"] == name:
                        del telephone_book[first_char][
                            telephone_book[first_char].index(kei)
                        ]

                        name = input("Enter name: ").lower()
                        phone = input("Phone: ")
                        photo = input("Photo adress: ")

                        new_first_char = name[0]

                        telephone_book[new_first_char] = [
                            {
                                "Name": name.capitalize(),
                                "Phone": phone,
                                "Photo": photo,
                            }
                        ]

        except KeyError:
            print("Contact not found")

    if len(telephone_book[first_char]) == 0:
        del telephone_book[first_char]
    telephone_book = dict(sorted(telephone_book.items()))

    with open("data.json", "w") as file:
        json.dump(telephone_book, file)


def del_contact():
    name = input("Delete contact\nEnter name: ").capitalize()
    first_char = name[0].lower()

    for kei in telephone_book[first_char]:
        if kei["Name"] == name:
            del telephone_book[first_char][telephone_book[first_char].index(kei)]
            if not len(telephone_book[first_char]):
                del telephone_book[first_char]
    with open("data.json", "w") as file:
        json.dump(telephone_book, file)


def save_to_file():
    with open("data.json", "r") as file:
        telephone_book = json.load(file)

    with open("contacts.txt", "w") as file:
        sorted_book = dict(sorted(telephone_book.items()))

        for key, value in sorted_book.items():
            file.write(f"{key.upper()}\n")
            for item in value:
                for key, value in item.items():
                    file.write(f"{key}: {value}\n")
                file.write("--------------\n")
            file.write("\n")


def generate_test_data():
    telephone_book.clear()

    data = {
        "i": [
            {
                "Name": "Ivan Ivanov",
                "Phone": "+79123456789",
                "Work Phone": "+74951234567",
                "Address": "Pushkina st., 10",
                "Email": "ivan.ivanov@example.com",
                "Date of Birth": "1985-03-15",
                "Notes": "Lorem Ipsum is simply dummy text.",
                "Photo": "img/boy.jpg",
            },
        ],
        "p": [
            {
                "Name": "Petr Petrov",
                "Phone": "+79876543210",
                "Work Phone": "+78129876543",
                "Address": "Lenina st., 5",
                "Email": "petr.petrov@example.net",
                "Date of Birth": "1992-11-20",
                "Notes": "Colleague, does sports.",
                "Photo": "img/boy.jpg",
            },
        ],
    }

    with open("data.json", "w") as file:
        json.dump(data, file)


with open("data.json", "r") as file:
    telephone_book = json.load(file)


logo_menu()

while True:
    action = input("Select action: ")

    if action == "1":
        os.system("cls" if os.name == "nt" else "clear")
        show_logo()
        show_contacts()
        show_menu()
    elif action == "2":
        clear_scrin_logo_menu()
        add_contact()
        clear_scrin_logo_menu()
    elif action == "3":
        clear_scrin_logo_menu()
        edit_contact()
        # clear_scrin_logo_menu()
    elif action == "4":
        clear_scrin_logo_menu()
        del_contact()
        clear_scrin_logo_menu()
    elif action == "5":
        telephone_book.clear()
        with open("data.json", "w") as file:
            json.dump(telephone_book, file)
        clear_scrin_logo_menu()
        print("Contacts have been cleared")
    elif action == "6":
        clear_scrin_logo_menu()
        save_to_file()
        print("The list has been saved to a text file")
    elif action == "7":
        clear_scrin_logo_menu()
        generate_test_data()
    elif action == "8":
        print("Exit the application")
        os.system("cls" if os.name == "nt" else "clear")
        break
