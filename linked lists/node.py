class node(object):
    def __init__(self, node_data, next_node = None):
        if type(node_data) not in [int, float]:
            raise TypeError("Node value must be int or float")

        self.node_data = node_data
        self.next_node = next_node
    
    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node
    
    def get_data(self):
        return self.node_data
    
    def set_data(self, node_data):
        if type(node_data) not in [int, float]:
            raise TypeError("Node value must be int or float")

        self.node_data = node_data
    
    def has_next(self):
        if self.next_node:
            return True
        else:
            return False

    def __str__(self):
        return str(self.node_data)