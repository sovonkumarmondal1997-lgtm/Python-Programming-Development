from models.person import Person


class Supplier(Person):
    def __init__(self, name, email, phone, address, supplier_id, company_name):
        super().__init__(name, email, phone, address)
        self.supplier_id = supplier_id
        self.company_name = company_name
        self.products_supplied = []

    def add_product(self, product):
        self.products_supplied.append(product)

    def remove_product(self, product):
        if product in self.products_supplied:
            self.products_supplied.remove(product)

    def get_catalogue(self):
        return self.products_supplied

    def __str__(self):
        return f"Supplier ID: {self.supplier_id}, Company: {self.company_name}, Name: {self.name}"