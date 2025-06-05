#class calleed tracker  consist and a class called product


class Product:
    def __init__(self , name:str , category:str , stock:int ) -> None:
        self.name = name
        self.category  = category
        self.stock = stock
        
        
    def __repr__(self):
        return f"Product: Name->  {self.name} {self.category} {self.stock} "
        








