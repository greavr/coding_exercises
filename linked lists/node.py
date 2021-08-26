class node(object):
    def __init__(self, node_data: int, next_node: 'node' = None):
        if type(node_data) != int:
            raise TypeError("Node value must be int")
        if type(next_node) != node and next_node != None:
            raise TypeError("Next node must be node or None class")

        self.node_data = node_data
        self.next_node = next_node
    
    def get_next(self):
        return self.next_node

    def set_next(self, next_node: 'node'):
        if type(next_node) != node and next_node != None:
            raise TypeError("Next node must be node or None class")
        self.next_node = next_node
    
    def get_data(self):
        return self.node_data
    
    def set_data(self, node_data: int):
        if type(node_data) != int:
            raise TypeError("Node value must be int")
        self.node_data = node_data
    
    def has_next(self):
        if self.next_node:
            return True
        else:
            return False

    def __str__(self):
        return str(self.node_data)