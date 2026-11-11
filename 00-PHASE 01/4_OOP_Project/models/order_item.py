class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.unit_price = product.price

    def get_line_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return (
            f"Product: {self.product.name}, "
            f"Quantity: {self.quantity}, "
            f"Unit Price: {self.unit_price}, "
            f"Line Total: {self.get_line_total()}"
        )