#INVENTORY MANAGEMENT SYSTEM PROJECT
class product:
    def __init__(self,company, price, quantity,name):
        self.company = company
        self.price = price
        self.quantity = quantity
        self.name = name

    def info(self):
        print("The company is:",self.company)                            #method to display the product information 
        print("The price is:", self.price)
        print("The quantity is:", self.quantity)
        print("The name is:",self.name)

    def recevied(self, quantity):            #method to receive the product
        self.quantity += quantity
        print("The quantity is:",self.quantity)
    def sold(self,quantity):          
     if  quantity > self.quantity:
            print("Not enough stock available")
     else:
            self.quantity -= quantity
            print("The quantity after sell is:",self.quantity)
laptop = product("dell", 2000, 5,"laptop",)            # OBJECT CREATION 1
keyboard = product ("apple", 1500, 10,"keyboard")        # OBJECT CREATION 2
mouse = product("hp",1000,20,"mouse")     #OBJECT CREATION 3   

class inventory:             #another class to manage the inventory of products
    def __init__(self):
        self.products = {}
    def view_product(self):
       for item in self.products.values():    
           item.info()
    def add_products(self, item):
        self.products[item.name] = item
    def sold_product(self):
        sold = input("Enter name of product you want to sell :")
        if sold in self.products:
          quantity = int(input("Enter quantity please :"))
          self.products[sold].sold(quantity)
        else:
            print("Not Found") 
    def recevied_product(self):
        recevied = input("Enter the name of product you want to increase :")
        if recevied in self.products:
            quantity = int(input("Enter quantity  please :"))
            self.products[recevied].recevied(quantity)
        else:
            print('Not Found')

    def search_product(self):
            name= input("Enter the name of product:")
            if name in self.products:
               self.products[name].info()
            else:
               print("product not found")

tablet= product("samsung", 3000, 15,"tablet")             #OBJECT CREATION 4   
inventroy1 = inventory()
inventroy1.add_products(tablet)
inventroy1.add_products(laptop)
inventroy1.add_products(keyboard)
inventroy1.add_products(mouse)
                            #MENU FOR STORE===
while True:
     print("=====MENU=====")
     print("1. View Products")
     print("2. Search Product")
     print("3. Sell Product")
     print("4. Receive Stock")
     print("5. Exit") 
     choice= int(input("Enter Your Choice (1-5) :"))
     if choice == 1:
         inventroy1.view_product()
     elif choice == 2:
         inventroy1.search_product()
     elif choice == 3:
         inventroy1.sold_product()
     elif choice == 4:
         inventroy1.recevied_product()
     elif choice == 5:
         print("See You Soon,EXIT!")
         break
         

         