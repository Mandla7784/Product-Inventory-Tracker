#class calleed tracker  consist and a class called product
class Product:
    def __init__(self , name:str=None , price:float =None , category:str =None , stock:int =None ) -> None:
        self.name = name
        self.category  = category
        self.stock = stock
        self.price = price
        self.outOfStock = False
        

    def __repr__(self ):
        return f"Product: Name->  {self.name} Category -> {self.category} stock -> {self.stock} "
   
   
    def update_quanity(self , q):
        self.stock += q
   
   
    @classmethod
    def master(self)-> None:
        pass

        
if __name__=="__main__":
    Product().master()    








