def cafe_management_system():
    # List of menus:
    menu = {
        "Coffee" : 10.00,
        "Tea" : 5.00,
        "Sandwich" : 20.00,
        "Cake" : 15.00,
        "Ice-Cream" : 10.00
    }

    while True:
        print("\nCafe Management System: ")
        print("1. View Menu")
        print("2. Add menu item")
        print("3. Remove sold-out item")
        print("4. Place order")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            if menu:
                print("\nMenu:")
                for item, price in menu.items():
                    print(f"{item} : ${price}")
            else:
                print("The cafe menu is currently empty.")

        elif choice == '2':
            item = input("Enter the item: ")
            if item in menu:
                print(f"{item} is already present in the menu.")
            else:
                try:
                    price = float(input("Enter the price of the item: "))
                    menu[item] = price
                    print(f"The item {item} has been added to the menu with price ${price}")
                except ValueError:
                    print("Invalid price entered.")
        
        elif choice == '3':
            item = input("Enter the item: ")
            if item in menu:
                del menu[item]
                print(f"{item} has been removed from the menu.")
            else:
                print(f"{item} is not present on the menu.")
        
        elif choice == '4':
            order_items = set()
            total_bill = 0.0
            while True:
                item = input("Enter the item to order (or 'done' to finish): ")
                if item.lower() == 'done':
                    break

                if item in menu:
                    order_items.add(item)
                    total_bill += menu[item]
                    print(f"{item} added to your order. Current Bill: ${total_bill}")
                else:
                    print(f"{item} is not present on the menu.")
            
            # Display Bill:
            if order_items:
                print("\nYour menu summary:")
                for item in order_items:
                    print(f"{item} : ${menu[item]}")
                print(f"Total bill : ${total_bill}")
            else:
                print("No items ordered.")

        elif choice == '5':
            print("Thank you for visiting our cafe.")
            break

        else:
            print("Invalid choice.")

cafe_management_system()