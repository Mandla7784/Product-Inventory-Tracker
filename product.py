#class calleed tracker  consist and a class called product
class Product:
    def __init__(self , name:str=None , price:float =None , category:str =None , stock:int =None ) -> None:
        self.name = name
        self.category  = category
        self.stock = stock
        self.price = price
        
    @classmethod   
    def __repr__(self):
        return f"Product: Name->  {self.name} Category -> {self.category} stock -> {self.stock} "
   
    @classmethod
    def main(self)-> None:
        pass

        
if __name__=="__main__":
    Product().main()    








