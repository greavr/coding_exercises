import unittest
from node import node

class TestNode(unittest.TestCase):
    
    def test_init(self):
        # Test init
        aNode = node(node_data=1)
        self.assertIsNone(aNode.get_next())
        self.assertEqual(aNode.get_data(),1)


    def test_node_get_next(self):
        # Test that return values for next node are either valid node or None
        aNode = node(node_data=1)
        self.assertIsNone(aNode.get_next())
        bNode = node(node_data=2, next_node=aNode)
        self.assertEqual(bNode.get_next(),aNode)
        self.assertNotEqual(bNode.get_next(),3)

    def test_set_next(self):
        # Test to make sure next node can be set
        # Baseline is None
        aNode = node(node_data=1)
        self.assertIsNone(aNode.get_next())
        # Check is able to set
        bNode = node(node_data=2)
        self.assertIsNone(bNode.get_next())
        bNode.set_next(next_node=aNode)
        self.assertEqual(bNode.get_next(),aNode)
        # Check that reset to None works
        bNode.set_next(next_node=None)
        self.assertIsNone(bNode.get_next())

    def test_get_data(self):
        # Test to ensure expected data comes back
        aNode = node(node_data=1)
        self.assertEqual(aNode.get_data(),1)
    
    def test_set_data(self):
        # Test ability to set data
        aNode = node(node_data=1)
        self.assertEqual(aNode.get_data(),1)
        aNode.set_data(node_data=2)
        self.assertEqual(aNode.get_data(),2)
        # Test Errors
        self.assertRaises(TypeError, aNode.set_data, "String")
        self.assertRaises(TypeError, aNode.set_data, False)
        self.assertRaises(TypeError, aNode.set_data, None)

    def test_has_next(self):
        # Test True Flase has next
        aNode = node(node_data=1)
        self.assertFalse(aNode.has_next())
        bNode = node(node_data=2,next_node=aNode)
        self.assertTrue(bNode.has_next())

    def test_str(self):
        # Test node returns as string
        aNode = node(node_data=1)
        self.assertEqual(str(aNode), "1")
        # Test Errors
        self.assertNotEqual(str(aNode), 1)
        self.assertNotEqual(str(aNode), True)




if __name__ == '__main__':
    unittest.main()
