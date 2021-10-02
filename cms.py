import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


# changes varuthiii


def createContact():
    print("\n\n\t\t CREATE CONTACT")
    file = open("contacts.txt", "at")
    name = input("\nEnter the name : ")
    phno = input("Enter the number : ")
    file.write(name)
    file.write("\n")
    file.write(phno)
    file.write("\n")
    file.close()
    return None


def viewContacts():
    print("\n\n\t\t VIEW CONTACTS")
    try:
        file = open("contacts.txt", "rt")
    except FileNotFoundError:
        input("\nNo contacts to display.")
        return None
    contacts = file.readlines()
    for i in range(len(contacts)):
        if i % 2 == 0:
            print(contacts[i], end="")
        else:
            print(contacts[i])
    input("\nPress enter to continue... ")
    file.close()
    del contacts
    return None


def updateContact():
    viewContacts()
    print("\n\n\t\t UPDATE CONTACT")
    try:
        file = open("contacts.txt", "rt")
    except FileNotFoundError:
        input("\nNo contacts to display.")
        return None
    contacts = file.readlines()
    file.close()
    name = input("\nEnter the name to search : ")
    print("\nEnter the old one if there is no change")
    new_name = input("Enter new Name : ")
    new_phno = input("Enter new Phone number : ")
    for i in range(len(contacts)):
        if i % 2 == 0:
            if contacts[i].replace("\n", "") == name:
                contacts[i] = contacts[i].replace(contacts[i], (new_name + "\n"))
                contacts[i + 1] = contacts[i + 1].replace(
                    contacts[i + 1], (new_phno + "\n")
                )
                break
    file = open("contacts.txt", "wt")
    file.writelines(contacts)
    file.close()
    del contacts
    return None


def deleteContact():
    viewContacts()
    print("\n\n\t\t DELETE THE CONTACT")
    try:
        file = open("contacts.txt", "rt")
    except FileNotFoundError:
        input("\nThere are no contacts to display.")
        return None
    contacts = file.readlines()
    file.close()
    name = input("\nEnter the name that you wish to delete : ")
    for i in range(len(contacts)):
        if i % 2 == 0:
            if contacts[i].replace("\n", "") == name:
                del contacts[i]
                del contacts[i]
                break
    file = open("contacts.txt", "wt")
    file.writelines(contacts)
    file.close()
    del contacts
    return None


def home():
    clear()
    print("\n\n\t\t C O N T A C T S")
    menu = int(
        input(
            "\n\n\n  1. Create Contact\n\n  2. View Contacts\n\n  3. Update Contact\n\n  4. Delete Conatact\n\n  5. Exit\n\n\n\t : "
        )
    )
    if menu == 1:
        clear()
        createContact()
        home()
    elif menu == 2:
        clear()
        viewContacts()
        home()
    elif menu == 3:
        clear()
        updateContact()
        home()
    elif menu == 4:
        clear()
        deleteContact()
        home()
    elif menu == 5:
        clear()
        exit(0)
    else:
        home()


if __name__ == "__main__":
    home()
