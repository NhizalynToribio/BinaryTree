print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("*************** BINARY TREE ********************")


# This is the Class Section of the Binary Tree Search Node
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


# This is the section where the if__name__ statement for main is located
if __name__ == '__main__':
    print("\n****---> Example Run Code using countries <---****")
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)
    print("The Content for Binary Tree:", countries)
    print("\nIs UK in the list?", country_tree.search("UK"))
    print("Is Sweden in the list?", country_tree.search("Sweden"))

    # This is the section where The content of the Binary tree is the Letters of my Full Name
    print("\n****---> Letters of my Full name as the Content of the Binary Tree  <---****")
    fullname = ["N", "H", "I", "Z", "A", "L", "Y", "N", "P", "T", "O", "R", "I", "B", "I", "O"]
    fullname_tree = build_tree(fullname)
    print("The Content for Binary Tree:", fullname)
    print("Is the letter N in the Content?", fullname_tree.search("N"))
    print("Is the letter U in the Content?", fullname_tree.search("U"))

    print("\nIn Order Traversal of the Content", fullname_tree.in_order_traversal())
    print("Post Order Traversal of the Content:", fullname_tree.post_order_traversal())
    print("Pre Order Traversal of the Content:", fullname_tree.pre_order_traversal())

    # This section is where the user will ask to search the letter that she/he wants to search
    def locateletter():

        search_letter = input(str("Enter the letter that you want to search in the Content of the Binary Tree: "))
        print("Is the letter "f"{search_letter} located in the list Content?", user_name_tree.search(search_letter))
    print("\n*---> Users Input - Enter your Full name as the Content <---*")
    user_name = input(str("\nEnter your full name (provide space in every letter): "))
    user_name_list = user_name.split()
    user_name_tree = build_tree(user_name_list)
    print("The Content for Binary Tree:", user_name_list)

    locateletter()
    locateletter()

    print("\nIn Order Traversal of the Content:", user_name_tree.in_order_traversal())
    print("Post Order Traversal of the Content:", user_name_tree.post_order_traversal())
    print("Pre Order Traversal of the Content:", user_name_tree.pre_order_traversal())
