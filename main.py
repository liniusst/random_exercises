# Create a dataclass named "Product" that has the following attributes:
#     product_id: int
#     name: str
#     price: float
#     quantity: int

# The class should also have a method named "total_cost" that calculates and returns the total cost
# of the product, which is the price multiplied by the quantity.

# Create a list of Product objects and write a function that takes this list as input
# and returns the product with the highest total cost.

# Write a program that creates a list of 5 Product objects, prints out their attributes,
# and then calls the function to find the product with the highest total cost.
# pylint: disable= missing-docstring
from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int
    products_list = []

    def total_cost(self) -> float:
        if self.quantity == 0:
            return 0.00
        else:
            return self.quantity * self.price


@dataclass
class Restaurant:
    products_list = []
    price_list = []

    def add_products(self, products_db: List[Product]) -> List:
        for product_element in products_db:
            self.products_list.append(product_element)
        return self.products_list

    def get_products(self) -> List:
        return self.products_list

    def get_price_list(self) -> List:
        for product_element in self.products_list:
            suma = round(Product.total_cost(product_element), 2)
            self.price_list.append(suma)
        return self.price_list

    def get_product_info(self):
        bigest_price = max(self.get_price_list())
        for product_element in self.products_list:
            product_total = round(Product.total_cost(product_element), 2)
            if product_total == bigest_price:
                return product


product_list = [
    Product(product_id=1, name="Grill kepsnys", price=12.99, quantity=5),
    Product(product_id=2, name="Šaltibarščiai", price=2.99, quantity=40),
    Product(product_id=3, name="Čili sriuba", price=1.99, quantity=9),
    Product(product_id=4, name="Kepta duona", price=0.99, quantity=22),
    Product(product_id=5, name="Bokalas aliuko", price=3.99, quantity=50),
]
restaurant = Restaurant()
restaurant.add_products(products_db=product_list)
for product in restaurant.get_products():
    print(
        f"ID: {product.product_id}, {product.name} cost {product.price} and {product.quantity} qty"
    )
expensive_product = restaurant.get_product_info()
print(f"Most expensive product is: {expensive_product.name}")
