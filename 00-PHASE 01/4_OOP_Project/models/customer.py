from models.person import Person


class Customer(Person):
    def __init__(self, name, email, phone, address, customer_id):
        super().__init__(name, email, phone, address)
        self.customer_id = customer_id
        self.order_history = []

    def place_order(self, order):
        self.order_history.append(order)

    def get_order_history(self):
        return self.order_history

    def get_total_spent(self):
        total = 0
        for order in self.order_history:
            total += order.get_total()
        return total

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}"