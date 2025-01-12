class Book:
    def __init__(self,title,author,isbn,quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.active = True

    def show_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}"

    def update_quantity(self,quantity):
        self.quantity += quantity
        print(f"Quantity of {self.title} changed to {self.quantity}")

    def borrow(self,quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            print(f"Quantity of {self.title} changed to {self.quantity}")
        else:
            raise ValueError(f"amount of {self.title} is less than your request")

    def is_active(self):
        if self.quantity != 0:
            self.active = True
            print(f"{self.title} is activated.")
        else:
            print(f"{self.title} is deactivated.")




