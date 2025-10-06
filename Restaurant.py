
def order():
    food_menu = {
        "KFC": 120,
        "BUTTER CHICKEN": 150,
        "TANDOORI": 130,
        "PANEER": 100,
        "SPRITE": 40,
        "MILK TEA": 20
    }

    print("\n--- MENU ---")
    for item, price in food_menu.items():
        print(f"{item} - ₹{price}")

    with open("menu.txt", "w") as f:
        while True:
            choice = input("\nEnter your order (or type 'done' to finish): ").strip().upper()
            if choice == "DONE":
                break
            elif choice in food_menu:
                f.write(choice + "\n")
                print(f"{choice} added to your order.")
            else:
                print("Item not found in menu. Please try again.")

def bill():
    food_menu = {
        "KFC": 600,
        "BUTTER CHICKEN": 150,
        "TANDOORI": 130,
        "PANEER": 100,
        "SPRITE": 40,
        "MILK TEA": 20
    }

    total = 0
    try:
        with open("menu.txt", "r") as f:
            items = f.readlines()
            print(items)
            if not items:
                print("No items ordered yet.")
                return
            print("\n--- YOUR BILL ---")
            for item in items:
                item = item.strip().upper()
                if item in food_menu:
                    price = food_menu[item]
                    total += price
                    print(f"\n{item} - ₹{price}")
                if total>500:
                    total-=100

            print(f"\nTotal Bill: ₹{total}")
    except FileNotFoundError:
        print("No orders found.")

def main():
    while True:
        print("\n======================= WELCOME TO ACE LOUNGE =======================")
        print(" ----- MENU ------- ")
        print("1) Order")
        print("2) Bill")
        print("3) Exit")
        print("4)OREDER AGAIN")

        try:
            choice = int(input("ENTER YOUR CHOICE: "))
        except ValueError:
            print("Please enter a valid number (1-3).")
            continue

        if choice == 1:
            order()
        elif choice == 2:
            bill()
        elif choice == 3:
            print("Thank you for visiting ACE Lounge!")
            break
        elif choice==4:
            order()           
        else:
            print("Please select right option")
            continue
main()