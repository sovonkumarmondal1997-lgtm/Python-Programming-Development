class Product:
    def __init__(self, product_id, name, price, quantity_in_stock, supplier):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.supplier = supplier

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def restock(self, amount):
        if amount <= 0:
            raise ValueError("Restock amount must be positive")
        self.quantity_in_stock += amount

    def sell(self, amount):
        if amount <= 0:
            raise ValueError("Sell amount must be positive")

        if amount > self.quantity_in_stock:
            raise ValueError("Not enough stock available")

        self.quantity_in_stock -= amount

    def is_available(self):
        return self.quantity_in_stock > 0

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Stock: {self.quantity_in_stock}"