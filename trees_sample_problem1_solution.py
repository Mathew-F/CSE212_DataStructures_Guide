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
        if value < node.value:
            if node.left == None:
                node.left = BST.Node(value)
            elif node.left == value:
                return
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right == None:
                node.right = BST.Node(value)
            elif node.right == value:
                return
            else:
                self._insert(value, node.right)
        
    def contains(self, value):
        return self._contains(value, self.root)

    def _contains(self, value, node):
        if value <= node.value:
            if node.value == value:
                print('True')
            elif node.left == None:
                print('False')
            else:
                self._contains(value, node.left)
        elif value > node.value:
            if node.value == value:
                print('True')
            elif node.right == None:
                print('False')
            else:
                self._contains(value, node.right)
        else:
            print('False')

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
        if count == None:
            count = 0
        if node != None:
            count += 1
            count = self._length(node.left, count)
            count = self._length(node.right, count)
        return count

    def height(self):
        if self.root == None:
            return 0
        else:
            return self._height(self.root)

    def _height(self, node, count_left = None, count_right = None):
        '''
        Returns the height of the tallest branch in the bst
        '''
        count_left = 0
        count_right = 0
        if node.right == None and node.left == None:
            return 1
        else:
            if node.left != None:
                count_left += self._height(node.left)
                count_left += 1
            if node.right != None:
                count_right += self._height(node.right)
                count_right += 1
        if count_left > count_right:
            return count_left
        else:
            return count_right

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
