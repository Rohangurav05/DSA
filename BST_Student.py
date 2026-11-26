# Student Record Management System using BST
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert student roll number
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # Search the student roll number
    def search(self, key):
        temp = self.root

        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    # Inorder function for traversal
    def inorder(self, temp):
        if temp is None:
            return
        self.inorder(temp.left)
        print(temp.data, end=" ")
        self.inorder(temp.right)

    # Preorder function for traversal
    def preorder(self, temp):
        if temp is None:
            return
        print(temp.data, end=" ")
        self.preorder(temp.left)
        self.preorder(temp.right)

    # Postorder function for traversal
    def postorder(self, temp):
        if temp is None:
            return
        self.postorder(temp.left)
        self.postorder(temp.right)
        print(temp.data, end=" ")

    # Find inorder successor
    def get_successor(self, temp):
        temp = temp.right
        while temp.left:
            temp = temp.left
        return temp

    # Delete the student roll number
    def delete(self, temp, value):
        if temp is None:
            return temp

        if value < temp.data:
            temp.left = self.delete(temp.left, value)

        elif value > temp.data:
            temp.right = self.delete(temp.right, value)

        else:
            if temp.left is None:
                return temp.right

            elif temp.right is None:
                return temp.left

            succ = self.get_successor(temp)
            temp.data = succ.data
            temp.right = self.delete(temp.right, succ.data)

        return temp

    # Find minimum and maximum roll number
    def find_min_max(self):
        if self.root is None:
            print("No student records found")
            return

        temp = self.root
        while temp.left:
            temp = temp.left
        print("Minimum Roll Number:", temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right
        print("Maximum Roll Number:", temp.data)


# Main program

b1 = BST()
# Insert student roll numbers
b1.insert(Node(50))
b1.insert(Node(30))
b1.insert(Node(70))
b1.insert(Node(20))
b1.insert(Node(40))
b1.insert(Node(60))
b1.insert(Node(80))
b1.insert(Node(10))
b1.insert(Node(35))

# Display the students roll numbers in ascending order
print("Student Roll Numbers:")
b1.inorder(b1.root)

# Search student
print("Searching Roll Number 60:")

if b1.search(60):
    print("Student Found")
else:
    print("Student Not Found")

# Delete student
b1.root = b1.delete(b1.root, 30)

print("After Deleting Roll Number 30:")

# Display all roll numbers
print("\nInorder:")
b1.inorder(b1.root)

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

# Find minimum roll number and maximum roll number
print()
b1.find_min_max()
