
import unittest

from main import add_new_product , available_stock ,search_by_name ,update_stock 
from product import Product


class TestMain(unittest.TestCase):
    
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        
    def setUp(self):
        available_stock.clear()
        self.new_item = Product("mock_banana",20 , "fruit" , 12)
     
    def test_add_new_product(self):
        available_stock.append(self.new_item)
        self.assertEqual(len(available_stock) , 1)
        self.assertEqual(available_stock[0].name , "mock_banana")
        
       

    
    
    
if __name__=="__main__":
    unittest.main()
        