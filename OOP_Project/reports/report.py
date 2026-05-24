from models.medical_product import MedicalProduct


class Report:
    @staticmethod
    def inventory_summary(inventory):
        print("INVENTORY SUMMARY")
        print("-" * 40)

        for product in inventory.products.values():
            print(
                f"{product.product_id} | "
                f"{product.name} | "
                f"Stock: {product.quantity_in_stock} | "
                f"Price: {product.price}"
            )

        print("-" * 40)
        print(f"Total Inventory Value: {inventory.get_total_inventory_value()}")

    @staticmethod
    def sales_summary(orders):
        total_revenue = 0
        product_sales = {}

        for order in orders:
            total_revenue += order.get_total()

            for item in order.items:
                product_name = item.product.name

                if product_name not in product_sales:
                    product_sales[product_name] = 0

                product_sales[product_name] += item.quantity

        print("SALES SUMMARY")
        print("-" * 40)
        print(f"Total Revenue: {total_revenue}")

        print("Top Products:")
        for product_name, quantity in product_sales.items():
            print(f"{product_name}: {quantity} units sold")

    @staticmethod
    def expiry_alert(inventory):
        print("EXPIRY ALERT")
        print("-" * 40)

        for product in inventory.products.values():
            if isinstance(product, MedicalProduct):
                days_left = product.days_until_expiry()

                if 0 <= days_left <= 30:
                    print(
                        f"{product.name} expires in "
                        f"{days_left} days"
                    )