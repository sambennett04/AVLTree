import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Test(unittest.TestCase):

    def setUp(self):
        self.__BST = Binary_Search_Tree()

    def test_empty_BST_height(self):
       self.assertEqual(0, self.__BST.get_height())
    
    def test_empty_BST_string(self):
       self.assertEqual('[ ]', str(self.__BST))

    def test_empty_BST_inorder(self):
       self.assertEqual('[ ]', self.__BST.in_order())
    
    def test_empty_BST_preorder(self):
       self.assertEqual('[ ]', self.__BST.pre_order())

    def test_empty_BST_postorder(self):
       self.assertEqual('[ ]', self.__BST.post_order())

    def test_insert_50_height(self):
       self.__BST.insert_element(50)
       self.assertEqual(1 , self.__BST.get_height())
    
    def test_insert_50_str(self):
       self.__BST.insert_element(50)
       self.assertEqual('[ 50 ]', str(self.__BST))

    def test_insert_50_inorder(self):
       self.__BST.insert_element(50)
       self.assertEqual('[ 50 ]', self.__BST.in_order())
    
    def test_insert_50_preorder(self):
       self.__BST.insert_element(50)
       self.assertEqual('[ 50 ]', self.__BST.pre_order())

    def test_insert_50_postorder(self):
       self.__BST.insert_element(50)
       self.assertEqual('[ 50 ]', self.__BST.post_order())

    def test_insert_50_then_remove_50_height(self):
        self.__BST.insert_element(50)
        self.__BST.remove_element(50)
        self.assertEqual(0 , self.__BST.get_height())

    def test_insert_50_then_remove_50_str(self):
        self.__BST.insert_element(50)
        self.__BST.remove_element(50)
        self.assertEqual('[ ]' , str(self.__BST))

    def test_insert_50_then_remove_50_inorder(self):
       self.__BST.insert_element(50)
       self.__BST.remove_element(50)
       self.assertEqual('[ ]', self.__BST.in_order())
    
    def test_insert_50_then_remove_50_preorder(self):
       self.__BST.insert_element(50)
       self.__BST.remove_element(50)
       self.assertEqual('[ ]', self.__BST.pre_order())

    def test_insert_50_then_remove_50_postorder(self):
       self.__BST.insert_element(50)
       self.__BST.remove_element(50)
       self.assertEqual('[ ]', self.__BST.post_order())

    def test_insert_50_then_30_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_50_then_30_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.assertEqual('[ 30, 50 ]' , str(self.__BST))

    def test_insert_50_then_30_inorder(self):
       self.__BST.insert_element(50)
       self.__BST.insert_element(30)
       self.assertEqual('[ 30, 50 ]', self.__BST.in_order())
    
    def test_insert_50_then_30_preorder(self):
       self.__BST.insert_element(50)
       self.__BST.insert_element(30)
       self.assertEqual('[ 50, 30 ]', self.__BST.pre_order())

    def test_insert_50_then_30_postorder(self):
       self.__BST.insert_element(50)
       self.__BST.insert_element(30)
       self.assertEqual('[ 30, 50 ]', self.__BST.post_order())

    def test_insert_30_then_50_height(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.assertEqual(2 , self.__BST.get_height()) 
    
    def test_insert_30_then_50_str(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.assertEqual('[ 30, 50 ]' , str(self.__BST)) 

    def test_insert_30_then_50_inorder(self):
       self.__BST.insert_element(30)
       self.__BST.insert_element(50)
       self.assertEqual('[ 30, 50 ]', self.__BST.in_order())
    
    def test_insert_30_then_50_preorder(self):
       self.__BST.insert_element(30)
       self.__BST.insert_element(50)
       self.assertEqual('[ 30, 50 ]', self.__BST.pre_order())

    def test_insert_30_then_50_postorder(self):
       self.__BST.insert_element(30)
       self.__BST.insert_element(50)
       self.assertEqual('[ 50, 30 ]', self.__BST.post_order())

    def test_insert_50_then_70_then_remove_50_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(50)
        self.assertEqual(1 , self.__BST.get_height()) 

    def test_insert_50_then_70_then_remove_50_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(50)
        self.assertEqual('[ 70 ]' , str(self.__BST)) 

    def test_insert_50_then_70_then_remove_50_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(50)
        self.assertEqual('[ 70 ]', self.__BST.in_order())
    
    def test_insert_30_then_50_then_remove_50_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(50)
        self.assertEqual('[ 70 ]', self.__BST.pre_order())

    def test_insert_30_then_50_then_remove_50_postorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(50)
        self.assertEqual('[ 70 ]', self.__BST.post_order())

    def test_insert_50_then_70_then_remove_70_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(70)
        self.assertEqual(1 , self.__BST.get_height())  

    def test_insert_50_then_70_then_remove_70_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(70)
        self.assertEqual('[ 50 ]' , str(self.__BST))      

    def test_insert_50_then_70_then_remove_70_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(70)
        self.assertEqual('[ 50 ]', self.__BST.in_order())
    
    def test_insert_50_then_70_then_remove_70_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(70)
        self.assertEqual('[ 50 ]', self.__BST.pre_order())

    def test_insert_50_then_70_then_remove_70_postorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.remove_element(70)
        self.assertEqual('[ 50 ]', self.__BST.post_order())

    def test_insert_50_then_30_then_remove_30_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.remove_element(30)
        self.assertEqual(1 , self.__BST.get_height())  
 
    def test_insert_50_then_30_then_remove_30_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50 ]' , str(self.__BST))  

    def test_insert_50_then_30_then_remove_30_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50 ]', self.__BST.in_order())
    
    def test_insert_50_then_30_then_remove_30_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50 ]', self.__BST.pre_order())

    def test_insert_50_then_30_then_remove_30_postorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50 ]', self.__BST.post_order())

    def test_insert_70_then_50_then_30_height(self):
        self.__BST.insert_element(70)
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_70_then_50_then_30_str(self):
        self.__BST.insert_element(70)
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.assertEqual('[ 30, 50, 70 ]' , str(self.__BST))

    def test_insert_70_then_50_then_30_inorder(self):
       self.__BST.insert_element(70)
       self.__BST.insert_element(50)
       self.__BST.insert_element(30)
       self.assertEqual('[ 30, 50, 70 ]', self.__BST.in_order())
    
    def test_insert_70_then_50_then_30_preorder(self):
       self.__BST.insert_element(70)
       self.__BST.insert_element(50)
       self.__BST.insert_element(30)
       self.assertEqual('[ 50, 30, 70 ]', self.__BST.pre_order())

    def test_insert_70_then_50_then_30_postorder(self):
       self.__BST.insert_element(70)
       self.__BST.insert_element(50)
       self.__BST.insert_element(30)
       self.assertEqual('[ 30, 70, 50 ]', self.__BST.post_order())
    
    def test_insert_30_then_50_then_70_height(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_30_then_50_then_70_str(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.assertEqual('[ 30, 50, 70 ]' , str(self.__BST))

    def test_insert_30_then_50_then_70_inorder(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.assertEqual('[ 30, 50, 70 ]', self.__BST.in_order())
    
    def test_insert_30_then_50_then_70_preorder(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.assertEqual('[ 50, 30, 70 ]', self.__BST.pre_order())

    def test_insert_30_then_50_then_70_postorder(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.assertEqual('[ 30, 70, 50 ]', self.__BST.post_order())
    
    def test_insert_50_then_70_then_30_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_50_then_70_then_30_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.assertEqual('[ 30, 50, 70 ]' , str(self.__BST))

    def test_insert_50_then_70_then_30_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.assertEqual('[ 30, 50, 70 ]', self.__BST.in_order())
    
    def test_insert_50_then_70_then_30_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.assertEqual('[ 50, 30, 70 ]', self.__BST.pre_order())

    def test_insert_50_then_70_then_30_postorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.assertEqual('[ 30, 70, 50 ]', self.__BST.post_order())
    
    def test_insert_70_then_30_then_50_height(self):
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_70_then_30_then_50_str(self):
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.assertEqual('[ 30, 50, 70 ]' , str(self.__BST))

    def test_insert_70_then_30_then_50_inorder(self):
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.assertEqual('[ 30, 50, 70 ]', self.__BST.in_order())
    
    def test_insert_70_then_30_then_50_preorder(self):
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.assertEqual('[ 50, 30, 70 ]', self.__BST.pre_order())

    def test_insert_70_then_30_then_50_postorder(self):
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(50)
        self.assertEqual('[ 30, 70, 50 ]', self.__BST.post_order())
    
    def test_insert_30_then_70_then_50_height(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(50)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_30_then_70_then_50_str(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(50)
        self.assertEqual('[ 30, 50, 70 ]' , str(self.__BST))

    def test_insert_30_then_70_then_50_inorder(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(50)
        self.assertEqual('[ 30, 50, 70 ]', self.__BST.in_order())
    
    def test_insert_30_then_70_then_50_preorder(self):
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(50)
        self.assertEqual('[ 50, 30, 70 ]', self.__BST.pre_order())

    def test_insert_30_then_70_then_50_postorder(self):    
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(50)
        self.assertEqual('[ 30, 70, 50 ]', self.__BST.post_order())

    def test_insert_50_30_70_20_10_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_50_30_70_20_10__str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.assertEqual('[ 10, 20, 30, 50, 70 ]' , str(self.__BST))

    def test_insert_50_30_70_20_10_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.assertEqual('[ 10, 20, 30, 50, 70 ]' , self.__BST.in_order())
    
    def test_insert_50_30_70_20_10_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.assertEqual('[ 50, 20, 10, 30, 70 ]', self.__BST.pre_order())

    def test_insert_50_30_70_20_10_postorder(self):    
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.assertEqual('[ 10, 30, 20, 70, 50 ]', self.__BST.post_order())

    def test_insert_50_30_70_80_90_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_50_30_70_80_90_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual('[ 30, 50, 70, 80, 90 ]' , str(self.__BST))

    def test_insert_50_30_70_80_90_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual('[ 30, 50, 70, 80, 90 ]' , self.__BST.in_order())
    
    def test_insert_50_30_70_80_90_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual('[ 50, 30, 80, 70, 90 ]', self.__BST.pre_order())

    def test_insert_50_30_70_80_90_postorder(self):    
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual('[ 30, 70, 90, 80, 50 ]', self.__BST.post_order())

    def test_insert_50_30_70_10_20_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_50_30_70_10_20_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.assertEqual('[ 10, 20, 30, 50, 70 ]' , str(self.__BST))

    def test_insert_50_30_70_10_20_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.assertEqual('[ 10, 20, 30, 50, 70 ]' , self.__BST.in_order())
    
    def test_insert_50_30_70_10_20_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.assertEqual('[ 50, 20, 10, 30, 70 ]', self.__BST.pre_order())

    def test_insert_50_30_70_10_20_postorder(self):    
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(10)
        self.__BST.insert_element(20)
        self.assertEqual('[ 10, 30, 20, 70, 50 ]', self.__BST.post_order())

    def test_insert_50_30_70_90_80_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(90)
        self.__BST.insert_element(80)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_50_30_70_90_80_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(90)
        self.__BST.insert_element(80)
        self.assertEqual('[ 30, 50, 70, 80, 90 ]' , str(self.__BST))

    def test_insert_50_30_70_90_80_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(90)
        self.__BST.insert_element(80)
        self.assertEqual('[ 30, 50, 70, 80, 90 ]' , self.__BST.in_order())
    
    def test_insert_50_30_70_90_80_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(90)
        self.__BST.insert_element(80)
        self.assertEqual('[ 50, 30, 80, 70, 90 ]', self.__BST.pre_order())

    def test_insert_50_30_70_90_80_postorder(self):    
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(90)
        self.__BST.insert_element(80)
        self.assertEqual('[ 30, 70, 90, 80, 50 ]', self.__BST.post_order())

    def test_insert_50_30_70_20_40_10_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_50_30_70_20_40_10_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.assertEqual('[ 10, 20, 30, 40, 50, 70 ]' , str(self.__BST))

    def test_insert_50_30_70_20_40_10_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.assertEqual('[ 10, 20, 30, 40, 50, 70 ]' , self.__BST.in_order())
    
    def test_insert_50_30_70_20_40_10_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.assertEqual('[ 30, 20, 10, 50, 40, 70 ]', self.__BST.pre_order())

    def test_insert_50_30_70_20_40_10_postorder(self):    
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(10)
        self.assertEqual('[ 10, 20, 40, 70, 50, 30 ]', self.__BST.post_order())

    def test_insert_50_30_70_60_80_90_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_50_30_70_60_80_90_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual('[ 30, 50, 60, 70, 80, 90 ]' , str(self.__BST))

    def test_insert_50_30_70_60_80_90_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual('[ 30, 50, 60, 70, 80, 90 ]' , self.__BST.in_order())
    
    def test_insert_50_30_70_60_80_90_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual('[ 70, 50, 30, 60, 80, 90 ]', self.__BST.pre_order())

    def test_insert_50_30_70_60_80_90_postorder(self):    
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(90)
        self.assertEqual('[ 30, 60, 50, 90, 80, 70 ]', self.__BST.post_order())

    def test_insert_50_30_70_20_40_35_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(35)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_50_30_70_20_40_35_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(35)
        self.assertEqual('[ 20, 30, 35, 40, 50, 70 ]' , str(self.__BST))

    def test_insert_50_30_70_20_40_35_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(35)
        self.assertEqual('[ 20, 30, 35, 40, 50, 70 ]' , self.__BST.in_order())
    
    def test_insert_50_30_70_20_40_35_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(35)
        self.assertEqual('[ 40, 30, 20, 35, 50, 70 ]', self.__BST.pre_order())

    def test_insert_50_30_70_20_40_35_postorder(self):    
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(20)
        self.__BST.insert_element(40)
        self.__BST.insert_element(35)
        self.assertEqual('[ 20, 35, 30, 70, 50, 40 ]', self.__BST.post_order())

    def test_insert_50_30_70_60_80_65_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(65)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_50_30_70_60_80_65_str(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(65)
        self.assertEqual('[ 30, 50, 60, 65, 70, 80 ]' , str(self.__BST))

    def test_insert_50_30_70_60_80_65_inorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(65)
        self.assertEqual('[ 30, 50, 60, 65, 70, 80 ]' , self.__BST.in_order())
    
    def test_insert_50_30_70_60_80_65_preorder(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(65)
        self.assertEqual('[ 60, 50, 30, 70, 65, 80 ]', self.__BST.pre_order())

    def test_insert_50_30_70_60_80_65_postorder(self):    
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(60)
        self.__BST.insert_element(80)
        self.__BST.insert_element(65)
        self.assertEqual('[ 30, 50, 65, 80, 70, 60 ]', self.__BST.post_order())

    def test_insert_60_50_70_30_65_80_remove_80_height(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_60_50_70_30_65_80_remove_80_str(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.assertEqual('[ 30, 50, 60, 65, 70 ]' , str(self.__BST))

    def test_insert_60_50_70_30_65_80_remove_80_inorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.assertEqual('[ 30, 50, 60, 65, 70 ]' , self.__BST.in_order())
    
    def test_insert_60_50_70_30_65_80_remove_80_preorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.assertEqual('[ 60, 50, 30, 70, 65 ]', self.__BST.pre_order())

    def test_insert_60_50_70_30_65_80_remove_80_postorder(self):    
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.assertEqual('[ 30, 50, 65, 70, 60 ]', self.__BST.post_order())

    def test_insert_60_50_70_30_65_80_remove_80_50_30_height(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_60_50_70_30_65_80_remove_80_50_30_str(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual('[ 60, 65, 70 ]' , str(self.__BST))

    def test_insert_60_50_70_30_65_80_remove_80_50_30_inorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual('[ 60, 65, 70 ]' , self.__BST.in_order())
    
    def test_insert_60_50_70_30_65_80_remove_80_50_30_preorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual('[ 65, 60, 70 ]', self.__BST.pre_order())

    def test_insert_60_50_70_30_65_80_remove_80_50_30_postorder(self):    
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(80)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual('[ 60, 70, 65 ]', self.__BST.post_order())

    def test_insert_60_50_70_30_55_80_remove_30_70_80_height(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(30)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_60_50_70_30_55_80_remove_30_70_80_str(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(30)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual('[ 50, 55, 60 ]' , str(self.__BST))

    def test_insert_60_50_70_30_55_80_remove_30_70_80_inorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(30)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual('[ 50, 55, 60 ]' , self.__BST.in_order())
    
    def test_insert_60_50_70_30_55_80_remove_30_70_80_preorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(30)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual('[ 55, 50, 60 ]', self.__BST.pre_order())

    def test_insert_60_50_70_30_55_80_remove_30_70_80_postorder(self):    
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(30)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual('[ 50, 60, 55 ]', self.__BST.post_order())

    def test_insert_60_50_70_30_65_80_remove_65_50_30_height(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(65)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_60_50_70_30_65_80_remove_65_50_30_str(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(65)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual('[ 60, 70, 80 ]' , str(self.__BST))

    def test_insert_60_50_70_30_65_80_remove_65_50_30_inorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(65)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual('[ 60, 70, 80 ]' , self.__BST.in_order())
    
    def test_insert_60_50_70_30_65_80_remove_65_50_30_preorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(65)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual('[ 70, 60, 80 ]', self.__BST.pre_order())

    def test_insert_60_50_70_30_65_80_remove_65_50_30_postorder(self):    
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(65)
        self.__BST.insert_element(80)
        self.__BST.remove_element(65)
        self.__BST.remove_element(50)
        self.__BST.remove_element(30)
        self.assertEqual('[ 60, 80, 70 ]', self.__BST.post_order())

    def test_insert_60_50_70_30_55_80_remove_55_70_80_height(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(55)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual(2 , self.__BST.get_height())

    def test_insert_60_50_70_30_55_80_remove_55_70_80_str(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(55)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual('[ 30, 50, 60 ]' , str(self.__BST))

    def test_insert_60_50_70_30_55_80_remove_55_70_80_inorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(55)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual('[ 30, 50, 60 ]' , self.__BST.in_order())
    
    def test_insert_60_50_70_30_55_80_remove_55_70_80_preorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(55)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual('[ 50, 30, 60 ]', self.__BST.pre_order())

    def test_insert_60_50_70_30_55_80_remove_55_70_80_postorder(self):    
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(55)
        self.__BST.remove_element(70)
        self.__BST.remove_element(80)
        self.assertEqual('[ 30, 60, 50 ]', self.__BST.post_order())

    def test_insert_60_50_70_30_55_80_remove_60_height(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_60_50_70_30_55_80_remove_60_str(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.assertEqual('[ 30, 50, 55, 70, 80 ]' , str(self.__BST))

    def test_insert_60_50_70_30_55_80_remove_60_inorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.assertEqual('[ 30, 50, 55, 70, 80 ]' , self.__BST.in_order())
    
    def test_insert_60_50_70_30_55_80_remove_60_preorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.assertEqual('[ 70, 50, 30, 55, 80 ]', self.__BST.pre_order())

    def test_insert_60_50_70_30_55_80_remove_60_postorder(self):    
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.assertEqual('[ 30, 55, 50, 80, 70 ]', self.__BST.post_order())

    def test_insert_60_50_70_30_55_80_remove_60_70_height(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.__BST.remove_element(70)
        self.assertEqual(3 , self.__BST.get_height())

    def test_insert_60_50_70_30_55_80_remove_60_70_str(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.__BST.remove_element(70)
        self.assertEqual('[ 30, 50, 55, 80 ]' , str(self.__BST))

    def test_insert_60_50_70_30_55_80_remove_60_70_inorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.__BST.remove_element(70)
        self.assertEqual('[ 30, 50, 55, 80 ]' , self.__BST.in_order())
    
    def test_insert_60_50_70_30_55_80_remove_60_70_preorder(self):
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.__BST.remove_element(70)
        self.assertEqual('[ 50, 30, 80, 55 ]', self.__BST.pre_order())

    def test_insert_60_50_70_30_55_80_remove_60_70_postorder(self):    
        self.__BST.insert_element(60)
        self.__BST.insert_element(50)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(55)
        self.__BST.insert_element(80)
        self.__BST.remove_element(60)
        self.__BST.remove_element(70)
        self.assertEqual('[ 30, 55, 80, 50 ]', self.__BST.post_order())

if __name__ == '__main__':
  unittest.main()

    