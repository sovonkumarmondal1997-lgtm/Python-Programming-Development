from datetime import date
from models.product import Product


class MedicalProduct(Product):
    def __init__(
        self,
        product_id,
        name,
        price,
        quantity_in_stock,
        supplier,
        expiry_date,
        requires_prescription,
        dosage_info
    ):
        super().__init__(product_id, name, price, quantity_in_stock, supplier)
        self.expiry_date = expiry_date
        self.requires_prescription = requires_prescription
        self.dosage_info = dosage_info

    def is_expired(self):
        return date.today() > self.expiry_date

    def days_until_expiry(self):
        return (self.expiry_date - date.today()).days

    def __str__(self):
        return (
            f"Medical Product ID: {self.product_id}, "
            f"Name: {self.name}, "
            f"Price: {self.price}, "
            f"Stock: {self.quantity_in_stock}, "
            f"Expiry Date: {self.expiry_date}, "
            f"Prescription Required: {self.requires_prescription}, "
            f"Dosage: {self.dosage_info}"
        )