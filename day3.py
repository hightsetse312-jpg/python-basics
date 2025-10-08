def show_list(items):
    print("\nYour Shopping List:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

items = []
while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    choice = input("Choose: ")
 
    if choice == "1":
        item = input("Enter Item: ")
        items.append(item)
    elif choice == "2":
        item= input("Enter Item To Remove: ")
        if item in items: 
            items.remove(item)
        else:
            print("Item Not FOund.")
    elif choice == "3":
        show_list(items)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")



        