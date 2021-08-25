import unittest
from list import LinkedList
from node import node

class TestList(unittest.TestCase):

    def test_init(self):
        # Test init
        aList = LinkedList()
        self.assertEqual(aList.size, 0)
        self.assertIsNone(aList.root_node)
        # Test case with node
        aNode = node(node_data=1)
        bList = LinkedList(root_node=aNode)
        self.assertEqual(bList.size, 1)
        self.assertIsNotNone(bList.root_node)
    
    def test_get_size(self):
        # Test sizing return
        aList = LinkedList()
        self.assertEqual(aList.get_size(), 0)
        aList.add(node_data_to_add = 1)
        self.assertEqual(aList.get_size(), 1)
        aList.remove(node_data_to_remove=1)
        self.assertEqual(aList.get_size(), 0)

    def test_find(self):
        # Test finding data
        aList = LinkedList()
        aList.add(node_data_to_add = 1)
        aList.add(node_data_to_add = 2)
        aList.add(node_data_to_add = 3)
        #self.assertEqual(aList.find(node_data_to_find=2), 2)
        self.assertFalse(aList.find(4))
        # Test Error
        self.assertRaises(TypeError, aList.find, "Tree")
        self.assertRaises(TypeError, aList.find, "1")
        self.assertRaises(TypeError, aList.find, False)
        self.assertRaises(TypeError, aList.find, None)

    def test_add(self):
        # Test ability to add
        aList = LinkedList()
        self.assertEqual(aList.get_size(), 0)
        aList.add(node_data_to_add=1)
        self.assertEqual(aList.get_size(), 1)

        # Test Errors
        self.assertRaises(TypeError, aList.add, "Tree")
        self.assertRaises(TypeError, aList.add, "1")
        self.assertRaises(TypeError, aList.add, False)
        self.assertRaises(TypeError, aList.add, None)

    def test_remove(self):
        # Test ability to remove
        aList = LinkedList()
        aList.add(node_data_to_add=1)
        self.assertTrue(aList.remove(node_data_to_remove=1))
        self.assertEqual(aList.get_size(), 0)

        # Test Errors
        self.assertFalse(aList.remove(node_data_to_remove=1))
        self.assertRaises(TypeError, aList.remove, "Tree")
        self.assertRaises(TypeError, aList.remove, "1")
        self.assertRaises(TypeError, aList.remove, False)
        self.assertRaises(TypeError, aList.remove, None)

    def test_validate_size(self):
        # Test sizing return
        aList = LinkedList()
        self.assertEqual(aList.validate_size(), 0)
        aList.add(node_data_to_add = 1)
        self.assertEqual(aList.validate_size(), 1)
        aList.remove(node_data_to_remove=1)
        self.assertEqual(aList.validate_size(), 0)   

if __name__ == '__main__':
    unittest.main()