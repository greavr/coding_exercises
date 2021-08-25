from node import node
import random

class LinkedList(object):
    def __init__(self, root_node = None):
        self.root_node = root_node
        if self.root_node:
            self.size = 1
        else:
            self.size = 0
    
    def get_size(self):
        return self.size

    def find(self, node_data_to_find):
        if type(node_data_to_find) not in [int, float]:
            raise TypeError("Node value to find must be int or float")

        current_node = self.root_node

        while current_node is not None:
            if current_node.get_data() == node_data_to_find:
                return current_node
            elif current_node.get_next() == None:
                return False
            else:
                current_node = current_node.get_next()

    def add(self, node_data_to_add):
        if type(node_data_to_add) not in [int, float]:
            raise TypeError("Node value to add must be int or float")
            
        new_node = node (node_data=node_data_to_add, next_node=self.root_node)
        self.root_node = new_node
        self.size += 1

    def remove(self, node_data_to_remove):
        if type(node_data_to_remove) not in [int, float]:
            raise TypeError("Node value to remove must be int or float")
          
        current_node = self.root_node
        previous_node = None

        while current_node is not None:
            if  current_node.get_data() == node_data_to_remove:
                if previous_node is not None:
                    previous_node.set_next(current_node.get_next())
                else:
                    self.root_node = current_node.get_next()
                self.size -= 1
                return True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
        return False

    def validate_size(self):
        count = 0
        current_node = self.root_node

        while current_node is not None:
            count += 1
            current_node = current_node.get_next()

        return count


def main():
    myList = LinkedList()
    added_numbers = []
    
    i = random.randint(2,30)
    while i > 0:
        random_int = random.randint(1,100)
        myList.add(random_int)
        added_numbers.append(random_int)
        i -= 1

    print (f"Node values: {added_numbers} ")

    print(f"List Size: {myList.get_size()}")

    print(f"Validated List Size: {myList.validate_size()}")

    print(f"Removing value {added_numbers[1]} from List : {myList.remove(added_numbers[1])}")
    print(f"New List Size: {myList.get_size()}")
    print(f"New Validated List Size: {myList.validate_size()}")

    find_value = random.choice(added_numbers)
    print(f"Finding value: {find_value}: {myList.find(find_value)}")

main()