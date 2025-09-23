
from product import Product
from prettytable import PrettyTable
from pathlib import Path

import json


available_stock = [] # stock to keep track of available items
def add_new_product(name , cater , price , quant)-> None:
    new_product = Product(name , price , cater , quant )
    available_stock.append(new_product)
    print("Product :{} successfully added ".format(name))

#looping on the products list and format to  tabels  data
def list_products(products:list) -> None:
    table = PrettyTable()
    table.field_names = ["ProductName" , "Price","category","stock" , "OutOfStock"]
 
    for product in products:
        table.add_row([product.name , product.price , product.category , product.stock , product.outOfStock]) 
    print(table)

def search_by_name(products:list)-> Product:
    choice = input("Please enter the product  you would like to see: ").lower()
    for i in  products:
        if choice == i.name:
  
            print(i.__repr__())
            return i
    
    print("Product not found")
    return None
        
              

def  update_stock(product:Product)-> None:
    """_summary_
    #takes the product and update ist quantity

    Args:
        product (Product): _description_
    """
    update_stock_num  = int(input(f"How many stcoks want to add for {product.name} ? "))
    product.update_quanity(update_stock_num)
    

def save_to_json(products:list)->None:
    
    file_path = Path("data.json")
    if file_path.exists():
        file_path.unlink()
         
        with open(file_path, "w+") as f:
            product_list  =[]
            for i in products:
                product_list.append( {
                    "isInstock":f"{i.outOfStock}",
                "name":f"{i.name}",
                "category":f"{i.category}",
                "stock":f"{i.stock}",
                "Representation":f"{i.__repr__()}"
                     })
       
                json.dump(product_list, f, indent=4)
            f.close()
    else:
        print("Not found")
            
   
#looping on the stcoks for each product / check quantitty if its zero then out 
def marking_product_as_out(products:list) -> None:
    
    for eachItem in products:
        if eachItem.stock == 0:
            eachItem.outOfStock = True
        else:
            eachItem.outOfStock = False
            
        
def main()-> None:
    print("Buy more with lowest price")
    products = {
        "Apple": "🍎",
        "Sneakers": "👟",
        "Smartphone": "📱",
        "Toy": "🧸",
        "Watch": "⌚",
        "Headphones": "🎧",
        "Laptop": "💻"
    }

    print("🛒 Products for Sale:")
    for name, emoji in products.items():
        print(f"{emoji} {name}")
        
        
        
  
        

    while True:
        try:
            option  = input("Do you want to add new product ? (yes/no): ").lower()
            if option != "yes":
                print("Exiting the program.Good by ")
                return
            else:
                print("You can add new products to the inventory.")
        
                product_name = input("Enter product name: ")
                category = input("Category: ")

                # Handle price input
                try:
                    price = float(input("Price: "))
                except ValueError:
                    print("Invalid price. Please enter a numeric value.")
                    price = 0.0

                # Handle quantity input
                try:
                    quantity = int(input("Enter quantity: "))
                except ValueError:
                    print("Invalid quantity. Please enter an integer.")
                    quantity = 0

                add_new_product(product_name, category, price, quantity)

                print("\nAvailable Stock:")
                print(available_stock)
                list_products(available_stock)

                # Search
                try:
                    result = search_by_name(available_stock)
                    print(result)
                except Exception as e:
                    print(f"Error while searching: {e}")

                # Update stock
                choice = input("Which item do you want to update? ").lower()

                found = False
                for item in available_stock:
                    if choice == item.name.lower():
                        try:
                            update_stock(item)
                            print(f"{item.name} Updated [🧦]  new_stock => {item.stock}")
                            list_products(available_stock)
                            found = True
                            break
                        except Exception as e:
                            print(f"Error updating stock: {e}")

                if not found:
                    print(f"{choice} not found.")

                # Save to JSON
                try:
                    save_to_json(available_stock)
                except Exception as e:
                    print(f"Error saving data: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__=="__main__":
    main()



