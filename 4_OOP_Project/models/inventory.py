from models.medical_product import MedicalProduct


class Inventory:
    def __init__(self):
        self.products = {}
        self.suppliers = {}

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier

    def add_product(self, product):
        self.products[product.product_id] = product

        if product.supplier:
            self.add_supplier(product.supplier)
            product.supplier.add_product(product)

    def remove_product(self, product_id):
        if product_id in self.products:
            product = self.products[product_id]

            if product.supplier:
                product.supplier.remove_product(product)

            del self.products[product_id]
        else:
            raise ValueError("Product not found")

    def get_product_by_id(self, product_id):
        return self.products.get(product_id)

    def search_products(self, keyword):
        result = []

        for product in self.products.values():
            if keyword.lower() in product.name.lower():
                result.append(product)

        return result

    def get_low_stock_products(self, threshold):
        result = []

        for product in self.products.values():
            if product.quantity_in_stock < threshold:
                result.append(product)

        return result

    def get_expired_products(self):
        result = []

        for product in self.products.values():
            if isinstance(product, MedicalProduct) and product.is_expired():
                result.append(product)

        return result

    def get_total_inventory_value(self):
        total = 0

        for product in self.products.values():
            total += product.price * product.quantity_in_stock

        return total