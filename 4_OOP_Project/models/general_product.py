from models.product import Product


class GeneralProduct(Product):
    def __init__(
        self,
        product_id,
        name,
        price,
        quantity_in_stock,
        supplier,
        category,
        brand
    ):
        super().__init__(product_id, name, price, quantity_in_stock, supplier)
        self.category = category
        self.brand = brand

    def __str__(self):
        return (
            f"General Product ID: {self.product_id}, "
            f"Name: {self.name}, "
            f"Price: {self.price}, "
            f"Stock: {self.quantity_in_stock}, "
            f"Category: {self.category}, "
            f"Brand: {self.brand}"
        )