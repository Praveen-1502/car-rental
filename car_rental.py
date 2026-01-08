# ---------- ADD VEHICLE ----------
def add_vehicle():
    vid = input("Enter Vehicle ID: ")
    name = input("Enter Vehicle Name: ")
    price = input("Enter Price per Day: ")

    f = open("vehicles.txt", "a")
    f.write(vid + "," + name + "," + price + "\n")
    f.close()

    print("Vehicle added successfully!")


# ---------- VIEW VEHICLES ----------
def view_vehicles():
    print("\n--- VEHICLE LIST ---")
    f = open("vehicles.txt", "r")

    for line in f:
        vid, name, price = line.strip().split(",")
        print("ID:", vid, "| Name:", name, "| Price/day:", price)

    f.close()


# ---------- ADD CUSTOMER ----------
def add_customer():
    cid = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")

    f = open("customers.txt", "a")
    f.write(cid + "," + name + "," + phone + "\n")
    f.close()

    print("Customer added successfully!")


# ---------- VIEW CUSTOMERS ----------
def view_customers():
    print("\n--- CUSTOMER LIST ---")
    f = open("customers.txt", "r")

    for line in f:
        cid, name, phone = line.strip().split(",")
        print("ID:", cid, "| Name:", name, "| Phone:", phone)

    f.close()


# ---------- RENT VEHICLE ----------
def rent_vehicle():
    cid = input("Enter Customer ID: ")
    vid = input("Enter Vehicle ID: ")
    days = int(input("Enter Number of Days: "))

    price = 0
    f = open("vehicles.txt", "r")
    for line in f:
        v_id, name, p = line.strip().split(",")
        if v_id == vid:
            price = int(p)
    f.close()

    if price == 0:
        print("Vehicle not found!")
        return

    total = price * days

    f = open("rentals.txt", "a")
    f.write(cid + "," + vid + "," + str(days) + "," + str(total) + "\n")
    f.close()

    print("Vehicle rented successfully!")
    print("Total Amount: ₹", total)


# ---------- VIEW RENTALS ----------
def view_rentals():
    print("\n--- RENTAL RECORDS ---")
    f = open("rentals.txt", "r")

    for line in f:
        cid, vid, days, total = line.strip().split(",")
        print("Customer ID:", cid,
              "| Vehicle ID:", vid,
              "| Days:", days,
              "| Amount:", total)

    f.close()

while True:
    print("\n===== CAR RENTAL SYSTEM =====")
    print("1. Add Vehicle")
    print("2. View Vehicles")
    print("3. Add Customer")
    print("4. View Customers")
    print("5. Rent Vehicle")
    print("6. View Rentals")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_vehicle()
    elif choice == "2":
        view_vehicles()
    elif choice == "3":
        add_customer()
    elif choice == "4":
        view_customers()
    elif choice == "5":
        rent_vehicle()
    elif choice == "6":
        view_rentals()
    elif choice == "7":
        print("Thank you for using Car Rental System!")
        break
    else:
        print("Invalid choice! Try again.")
