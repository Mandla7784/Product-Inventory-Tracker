
import unittest

from main import add_new_product , available_stock ,search_by_name ,update_stock 
from product import Product


class TestMain(unittest.TestCase):
    
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        
    def setUp(self):
        available_stock.clear()
        new_item  = Product()
        
            
        
    def test_add_new_product(self):
        

        pass
    
    
    
if __name__=="__main__":
    unittest.main()
        