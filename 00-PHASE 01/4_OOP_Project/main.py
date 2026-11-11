from datetime import date, timedelta

from models import order
from models import customer
from models.supplier import Supplier
from models.customer import Customer
from models.medical_product import MedicalProduct
from models.general_product import GeneralProduct
from models.inventory import Inventory
from models.order import Order
from reports.report import Report


def create_sample_data():
    supplier1 = Supplier(
        "Amit Das",
        "amit@supplier.com",
        "9000000001",
        "Howrah, West Bengal, 711101",
        "SUP001",
        "MediLife Distributors"
    )

    customer1 = Customer(
        "Priya Sen",
        "priya@email.com",
        "9000000002",
        "Salt Lake, Kolkata, 700091",
        "CUS001"
    )

    paracetamol = MedicalProduct(
        "M001",
        "Paracetamol 500mg",
        25,
        100,
        supplier1,
        date.today() + timedelta(days=20),
        False,
        "Take 1 tablet after food"
    )

    cough_syrup = MedicalProduct(
        "M002",
        "Cough Syrup",
        90,
        30,
        supplier1,
        date.today() + timedelta(days=120),
        False,
        "10ml twice daily"
    )

    sanitizer = GeneralProduct(
        "G001",
        "Hand Sanitizer",
        80,
        200,
        supplier1,
        "Hygiene",
        "CleanSafe"
    )

    inventory = Inventory()
    inventory.add_product(paracetamol)
    inventory.add_product(cough_syrup)
    inventory.add_product(sanitizer)

    return inventory, supplier1, customer1


def show_menu():
    print()
    print("INVENTORY MANAGEMENT SYSTEM")
    print("-" * 40)
    print("1. View Inventory")
    print("2. Search Product")
    print("3. View Inventory Summary Report")
    print("4. View Expiry Alert Report")
    print("5. Place Order")
    print("6. Exit")


def view_inventory(inventory):
    print()
    print("PRODUCT LIST")
    print("-" * 40)

    for product in inventory.products.values():
        print(product)


def search_product(inventory):
    keyword = input("Enter product name to search: ")

    results = inventory.search_products(keyword)

    print()
    print("SEARCH RESULTS")
    print("-" * 40)

    if len(results) == 0:
        print("No product found")
    else:
        for product in results:
            print(product)

def place_order(inventory, customer):
    order_id = input("Enter order ID: ")
    order = Order(order_id, customer)

    while True:
        product_id = input("Enter product ID to order or type 'done' to finish: ")

        if product_id.lower() == "done":
            break    

        if product_id not in inventory.products:    
            print("Product not found")
            continue    
        product = inventory.get_product_by_id(product_id)

        if product is None:
            print("Product not found")
            continue

        quantity = int(input("Enter quantity: "))

        try:
            order.add_item(product, quantity)
            print("Product added to order")
        except ValueError as error:
            print(error)

        more = input("Add more products? (yes/no): ")

        if more.lower() != "yes":
            break

        if len(order.items) == 0:
            print("No products added. Order cancelled.")
            return

        order.update_status("confirmed")
        customer.place_order(order)

        print()
        print("ORDER PLACED SUCCESSFULLY")
        print("-" * 40)
        print(order.generate_invoice())



def main():
    inventory, supplier1, customer1 = create_sample_data()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            view_inventory(inventory)

        elif choice == "2":
            search_product(inventory)

        elif choice == "3":
            Report.inventory_summary(inventory)

        elif choice == "4":
            Report.expiry_alert(inventory)

        elif choice == "5":
            place_order(inventory, customer1)

        elif choice == "6":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()