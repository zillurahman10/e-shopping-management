class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.products = {} 

class Customer:
    def create_account(self, email, password):
        self.email = email
        self.password = password
        print("Account created successfully !!")

    def view_products(self):
        global EmaJohn
        print("Available products:")
        for product_name, details in EmaJohn.products.items():
            print(f"Name: {product_name}, Price: ${details['Price']}, Quantity: {details['Quantity']}")

    def place_order(self, product_name, quantity):
        global EmaJohn
        if product_name not in EmaJohn.products:
            print(f"Sorry, '{product_name}' is not available for sale.")
            return
        
        available_quantity = EmaJohn.products[product_name]['Quantity']
        if quantity > available_quantity:
            print(f"Sorry, only {available_quantity} units of '{product_name}' are available.")
            return
        
        price_per_unit = EmaJohn.products[product_name]['Price']
        total_price = price_per_unit * quantity
        
        print(f"Order placed successfully: '{product_name}' ({quantity} units) - Total Price: ${total_price}")

class Seller:
    def __init__(self) -> None:
        self.products = {} 

    def create_account(self, email, password):
        self.email = email
        self.password = password
        print("Account created successfully !!")

    def publish_product(self, product_name, price, quantity):
        product = {'Price': price, 'Quantity': quantity}
        self.products[product_name] = product
        print(f"Product '{product_name}' published successfully with price ${price} and quantity {quantity}.")

class Main:
    @staticmethod
    def run():
        global EmaJohn
        EmaJohn = Shop('Ema-John')
        
        flag = False
        while True:
            if flag == False:
                print("Welcome!!")
                print("1. Customer")
                print("2. Seller")
                print("3. Exit")
                choice = int(input("Enter your choice : "))
            if choice == 1:
                customer = Customer() 
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                customer.create_account(email, password)

                print("What do you want ?")
                print("1. View Products")
                print("2. Place Products")
                print("3. Exit")

                ans = int(input("Enter your choice: "))
                if ans == 1:
                    customer.view_products()
                elif ans == 2:
                    product_name = input("Enter your product name: ")
                    product_quantity = int(input("Enter your product quantity: "))
                    customer.place_order(product_name, product_quantity)
                elif ans == 3:
                    break
                else:
                    print("Invalid input !!")
                    
            elif choice == 2 or flag == True:
                if flag == False:
                    seller = Seller() 
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    seller.create_account(email, password)

                print("What do you want ?")
                print("1. Publish Product")
                print("2. Exit")

                ans = int(input("Enter your choice: "))
                if ans == 1:
                    product_name = input("Enter your product name: ")
                    product_price = float(input("Enter your product price: ")) 
                    product_quantity = int(input("Enter your product quantity: "))
                    seller.publish_product(product_name, product_price, product_quantity)
                    flag = True
                elif ans == 2:
                    flag = False
                    break
                else:
                    print("Invalid input !!")
            elif choice == 3:
                break
            else:
                print("Invalid Input!!")

Main.run()
