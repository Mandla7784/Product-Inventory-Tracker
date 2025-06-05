# TODO  create a simple Python program that manages a small product inventory system
from product import Product

stock = [] # stock to keep track of available items
def add_new_product(name , cater , price , quant):
    new_product = Product(name , price , cater , quant )
    
    if new_product.name in stock and new_product.stock == quant:
      choice =   print(f"{new_product.name} already exist do you want to add more ? (Y/N)")
    
    
    
    


def main()-> None:
 
    product_name = input("Enter prduct Name")
    category = input("Category : ")
    price =  float(input("Price: "))
    quantity  = int(input("Enter quantity"))





if __name__=="__main__":
    main()
