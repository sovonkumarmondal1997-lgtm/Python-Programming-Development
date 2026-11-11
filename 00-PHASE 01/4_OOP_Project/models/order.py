from datetime import datetime
from models.order_item import OrderItem


class Order:
    VALID_STATUSES = ["pending", "confirmed", "shipped", "delivered", "cancelled"]

    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.status = "pending"
        self.created_at = datetime.now()

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if not product.is_available():
            raise ValueError("Product is not available")

        if quantity > product.quantity_in_stock:
            raise ValueError("Not enough stock available")

        order_item = OrderItem(product, quantity)
        self.items.append(order_item)
        product.sell(quantity)

    def remove_item(self, product_id):
        for item in self.items:
            if item.product.product_id == product_id:
                self.items.remove(item)
                item.product.restock(item.quantity)
                return

        raise ValueError("Product not found in order")

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_line_total()
        return total

    def update_status(self, new_status):
        if new_status not in Order.VALID_STATUSES:
            raise ValueError("Invalid order status")

        self.status = new_status

    def generate_invoice(self):
        invoice = f"Invoice for Order ID: {self.order_id}\n"
        invoice += f"Customer: {self.customer.name}\n"
        invoice += f"Status: {self.status}\n"
        invoice += f"Created At: {self.created_at}\n"
        invoice += "-" * 40 + "\n"

        for item in self.items:
            invoice += str(item) + "\n"

        invoice += "-" * 40 + "\n"
        invoice += f"Total Amount: {self.get_total()}"

        return invoice

    def __str__(self):
        return (
            f"Order ID: {self.order_id}, "
            f"Customer: {self.customer.name}, "
            f"Status: {self.status}, "
            f"Total: {self.get_total()}"
        )