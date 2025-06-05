#class calleed tracker  consist and a class called product
class Product:
    def __init__(self , name:str , price:float , category:str , stock:int ) -> None:
        self.name = name
        self.category  = category
        self.stock = stock
        self.price = price
        
    @classmethod   
    def __repr__(self):
        return f"Product: Name->  {self.name} Category -> {self.category} stock -> {self.stock} "
    

        
        








