print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("*************** BINARY TREE ********************")
print("************** PART 1 AND 2 ********************")

# The entire code contains the Part 1 & 2 of the Exercise
# Part 1 - Min, Max, Sum, Pre and Post order traversal
# Part 2 - Deleting Method

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

    # Part 1 : Exercise - Min, Max, Sum, Pre and Post order traversal
    def minimum(self):
        if self.left is None:
            return self.data
        return self.left.minimum()

    def maximum(self):
        if self.right is None:
            return self.data
        return self.right.maximum()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

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

    # Part 2 : Exercise - Deleting Section
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.maximum()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


# This is the section where the if__name__ statement for main is located
if __name__ == '__main__':
    print("\n****---> Example Run Code using Countries <---****")
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)
    print("The Content for Binary Tree (Countries):", countries)
    print("\nIs UK in the list?", country_tree.search("UK"))
    print("Is Sweden in the list?", country_tree.search("Sweden"))

    # This is the section where The content of the Binary tree is the Letters of my Full Name
    print("\n****---> Letters of my Full name as the Content of the Binary Tree  <---****")
    fullname = ["N", "H", "I", "Z", "A", "L", "Y", "N",
                "P",
                "T", "O", "R", "I", "B", "I", "O"]
    fullname_tree = build_tree(fullname)

    print("The Content for Binary Tree (Full Name):", fullname)
    print("Min:", fullname_tree.minimum())
    print("Max:", fullname_tree.maximum())
    print("Is the letter N in the Content list?", fullname_tree.search("N"))
    print("Is the letter U in the Content list?", fullname_tree.search("U"))

    print("\nIn Order Traversal of the Content list", fullname_tree.in_order_traversal())
    print("Post Order Traversal of the Content list:", fullname_tree.post_order_traversal())
    print("Pre Order Traversal of the Content list:", fullname_tree.pre_order_traversal())

    # This is the output of Part 2 Code of Delete Section
    print("\n****---> Part 2 : Deleting Letters to the Content Full Name <---****")
    fullname_tree.delete("A")
    print("After deleting the letter A", fullname_tree.in_order_traversal())
    fullname_tree.delete("N")
    print("After deleting the letter N", fullname_tree.in_order_traversal())

    # This section is where the user will ask to search the letter that she/he wants to search
    def locateletter():
        search_letter = input(str("Enter the letter that you want to search in the Content of the Binary Tree: "))
        print("Is the letter "f"{search_letter} located in the Content list?", user_name_tree.search(search_letter))

    print("\n\n*---> Users Input - Enter your Full name as the Content <---*")
    user_name = input(str("Enter your full name (provide space in every letter): "))
    user_name_list = user_name.split()
    user_name_tree = build_tree(user_name_list)
    print("The Content for Binary Tree (Users Full Name):", user_name_list)
    print("Min:", user_name_tree.minimum())
    print("Max:", user_name_tree.maximum())

    locateletter()
    locateletter()

    print("\nIn Order Traversal of the Content list:", user_name_tree.in_order_traversal())
    print("Post Order Traversal of the Content list:", user_name_tree.post_order_traversal())
    print("Pre Order Traversal of the Content list:", user_name_tree.pre_order_traversal())

    # This is the output of Part 2 Code of Delete Section
    print("\n****---> Part 2 : Deleting Letters to the Content Full Name <---****")
    user_name_tree.delete("a")
    print("After deleting the letter a", user_name_tree.in_order_traversal())
    user_name_tree.delete("n")
    print("After deleting the letter n", user_name_tree.in_order_traversal())

    print("\n------------------------------------------------------------------------")

# This section is the complete Exercise Part 1 and 2 using numbers to get the Sum of all the Content
if __name__ == '__main__':

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("\nThe Content for Binary Tree (Number):", numbers)
    # This is the Part 1 : Exercise using numbers
    print("Min:", numbers_tree.minimum())
    print("Max:", numbers_tree.maximum())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal of the content list:", numbers_tree.in_order_traversal())
    print("Post order traversal of the content list:", numbers_tree.post_order_traversal())
    print("Pre order traversal of the content list:", numbers_tree.pre_order_traversal())

    print("\nIs the number 17 on the list of numbers?", numbers_tree.search(17))
    print("Is the number 26 on the list of my numbers?", numbers_tree.search(26))

    # This is the Part 2 : Exercise using numbers
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("\nAfter deleting the number 20", numbers_tree.in_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting the number 9", numbers_tree.in_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting the number 17 ", numbers_tree.in_order_traversal())
