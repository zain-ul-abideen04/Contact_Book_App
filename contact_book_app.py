def show_data():
    print("--Wellcome Contact App Book--")
    print("press 1 to add contact")
    print("press 2 to view contact")
    print("press 3 to delete contact")
    print("press 4 to exit")
def add_contact(contact_list):
    name = input("Enter a name :")
    contact = input("Enter a Contact :")
    contact_list.append({'name':name,'contact':contact})
    print("Contact added")
def view_history(contact_list):
    print("All history contact")
    for idx,entry in enumerate(contact_list,start=1):
        print(f"{idx}. Name : {entry['name']}, Contact : {entry['contact']}")
        # print("Contact added")
def delete_contact(contact_list):
    try:
        index = int(input("Enter a index that deleted"))
        if 1 <= index <= len(contact_list):
            deleted = contact_list.pop(index - 1)
            print(f"Deleted contact : {deleted['name']}")
        else:
            print("Invalid")
    except ValueError:
        print("Value Error")

contacts = []
while True:
    show_data()
    try:
        choice = int(input("Enter a choice :"))
    except ValueError:
        print("invalid choice")
        continue
    if choice == 1:
        add_contact(contacts)
    elif choice == 2:
        view_history(contacts)
    elif choice == 3:
        delete_contact(contacts)
    elif choice == 4:
        print("Good by")
        break
    else:
        print("Invalid Input.")
