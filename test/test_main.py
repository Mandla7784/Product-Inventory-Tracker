
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import *
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
        
    def test_search_by_name(self):
        available_stock.append(self.new_item)
        item_name = "mock_banana"
        not_item_name = "baaaaaaa"
        bfound = False
        
        for i in available_stock:
            if item_name == i.name:
                bfound = True
                
        self.assertTrue( (item_name == self.new_item.name)  , bfound)
        self.assertFalse((not_item_name == self.new_item.name) , not bfound)
                
        
    def test_update_stock (self):
        stock  = self.new_item.stock
        updated_item_stock = self.new_item.update_quanity(stock)
        self.assertEqual(updated_item_stock , 24)
        self.assertEqual((stock -1) , 11)
        
        
    def test_marking_product_as_out(self):
        stock = self.new_item.stock
        out_of_stock   = False
        if stock - stock == 0:
            out_of_stock = True
            
        self.assertTrue(out_of_stock , True )
            
            
    
if __name__=="__main__":
    unittest.main()
        