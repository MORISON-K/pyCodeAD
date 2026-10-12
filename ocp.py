# code violating ocp
def calculate_discount(price, customer_type):
    if customer_type == "regular":
        return price * 0.05

    elif customer_type == "premium":
        return price * 0.10

    elif customer_type == "vip":
        return price * 0.20

    return 0

# That works but if a new discount is intoduced the function has to be modified
'''elif customer_type == "student":
    return price * 0.15'''
    
# Improved design using polymorphism
from typing import Protocol


class DiscountPolicy(Protocol):
    def calculate_discount(self, price: float) -> float:
        ...


class RegularDiscount:
    def calculate_discount(self, price: float) -> float:
        return price * 0.05


class PremiumDiscount:
    def calculate_discount(self, price: float) -> float:
        return price * 0.10


class StudentDiscount:
    def calculate_discount(self, price: float) -> float:
        return price * 0.15     
            