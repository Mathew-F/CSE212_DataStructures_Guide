'''
This sample problem will test your basic understanding of recursion. 

__iter__ and traverse_forward functions borrowed from the week_9 prove assignment.
'''
class BST:
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = BST.Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, node):
        '''
        Paired with the insert function. Allows us to use recursion to check each 
        Node for the given value.
        '''
        pass #CODE GOES HERE
        
    def contains(self, value):
        return self._contains(value, self.root)

    def _contains(self, value, node):
        pass #CODE GOES HERE

    def length(self):
        if self.root == None:
            return 0
        else:
           return self._length(self.root)

    def _length(self, node, count = None):
        '''
        Returns the number total number of nodes in the BST.
        This may be done with the use of len() or for loop, but try and use reursion instead.
        '''
        pass #CODE GOES HERE

    def height(self):
        if self.root == None:
            return 0
        else:
            return self._height(self.root)

    def _height(self, node, count_left = None, count_right = None):
        '''
        Returns the height of the tallest branch in the bst
        '''
        pass #CODE GOES HERE

    def __iter__(self):
        '''
        Allows us to iterate through the bst using the for function
        '''
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        '''
        prints the values in the bst in ascending order. 
        '''
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.value
            yield from self._traverse_forward(node.right)

print('\n----------Test Case #1-------------')
bst = BST()
bst.insert(5)
bst.insert(8)
bst.insert(6)
bst.insert(3)
bst.insert(4)
for x in bst:
    print(x) #3 4 5 6 8
print('----------Test Case #2-------------')
bst.contains(5) #True
bst.contains(6) #True
bst.contains(2) #False
print('----------Test Case #3-------------')
print(bst.length()) #5
bst.insert(2)
print(bst.length()) #6
print('----------Test Case #4-------------')
print(bst.height()) #3
bst.insert(9)
print(bst.height()) #3
bst.insert(1)
print(bst.height()) #4
