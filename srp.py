class Invoice(): 
    def __init__(self, items):
        self.items = items  
        
    def calculate_total(self):
        return sum(
            item["price"] * item["quantity"]
            for item in self.items
        )
    def save_to_db(self):
        #db logic 
        print("Saving inoice to db")   
     
    def print_invoice(self):
        #Formatting logic
        print("Printing invoice")       
        
        
# Improved design

class Invoice:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(
            item["price"] * item["quantity"]
            for item in self.items
        )


class InvoiceRepository:
    def save(self, invoice):
        # Database persistence belongs here.
        print("Saving invoice to database")


class InvoicePrinter:
    def print_invoice(self, invoice):
        # Presentation logic belongs here.
        print(f"Invoice total: {invoice.calculate_total()}")      
        
# Usage 
items = [
    {"price": 100, "quantity": 2},
    {"price": 50, "quantity": 3},
]

invoice = Invoice(items)

print(invoice.calculate_total())  # 350

repository = InvoiceRepository()
repository.save(invoice)

printer = InvoicePrinter()
printer.print_invoice(invoice)  