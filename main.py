# TODO  create a simple Python program that manages a small product inventory system
from product import Product

available_stock = [] # stock to keep track of available items
def add_new_product(name , cater , price , quant):
    new_product = Product(name , price , cater , quant )
    
    if new_product.name in available_stock and new_product.stock == quant:
        choice =   input(f"{new_product.name} already exist do you want to add more ? (Y/N)").lower()
    
        match choice:
            case "y":
               available_stock.append(new_product)
            case "n":
                print("Product already exists ")

#looping on the products list and format to  tabels  data
def list_products(products:list):pass

def serach_by_name():
    pass

def  update_stock():
    pass
    
    
#looping on the stcoks for each product / check quantitty if its zero then out 
def marking_product_as_out(products):
    pass      

def main()-> None:
 
    product_name = input("Enter prduct Name")
    category = input("Category : ")
    price =  float(input("Price: "))
    quantity  = int(input("Enter quantity"))





if __name__=="__main__":
    main()

