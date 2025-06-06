# TODO  create a simple Python program that manages a small product inventory system
from product import Product
from prettytable import PrettyTable
from pathlib import Path

import json



available_stock = [] # stock to keep track of available items
def add_new_product(name , cater , price , quant)-> None:
    new_product = Product(name , price , cater , quant )
    available_stock.append(new_product)
    print("Product :{} successfully added ✅".format(name))

#looping on the products list and format to  tabels  data
def list_products(products:list) -> None:
    table = PrettyTable()
    table.field_names = ["ProductName" , "Price","category","stock" , "OutOfStock"]
 
    for product in products:
        table.add_row([product.name , product.price , product.category , product.stock , product.outOfStock]) 
    print(table)



def search_by_name(products:list)-> Product:
    choice = input("Please enter the name you would like to see: ").lower()
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
                # f.writelines(f"{productDict}")
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
  
    
 while True:
    product_name = input("Enter prduct Name: ")
    category = input("Category : ")
    price =  float(input("Price: "))
    quantity  = int(input("Enter quantity: "))
    add_new_product(product_name , category , price , quantity)
       
    print(available_stock)
    list_products(available_stock)
    print(search_by_name(available_stock))
        
    choice = input("Wich item want to update").lower()
        
    for item in available_stock:
        if choice == item.name:
            update_stock(item)
            print(f"{item.name} Updated [🧦]  new_stock=> {item.stock} ")
            list_products(available_stock)
        else:
            print(f"{choice}not found")


                
    save_to_json(available_stock)

if __name__=="__main__":
    main()








    # if new_product.name in available_stock and new_product.stock == quant:
    #     choice =   input(f"{new_product.name} already exist do you want to add more ? (Y/N)").lower()
    
    #     match choice:
    #         case "y":
    #            available_stock.append(new_product)
    #         case "n":
    #             print("Product already exists ")