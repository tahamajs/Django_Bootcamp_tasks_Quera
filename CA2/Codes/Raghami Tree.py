"""
Python program to print all path from root to
leaf in a binary tree
"""

all_ints = 0


class Node:
    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data) + " " + str(self.left) + " " + str(self.right)


# function to print all path from root
# to leaf in binary tree
def printPaths(root):
	# list to store path
	path = []
	printPathsRec(root, path, 0)

# Helper function to print path from root
# to leaf in binary tree
def printPathsRec(root, path, pathLen):
	
	# Base condition - if binary tree is
	# empty return
	if root is None:
		return

	# add current root's data into
	# path_ar list
	
	# if length of list is gre
	if(len(path) > pathLen):
		path[pathLen] = root.data
	else:
		path.append(root.data)

	# increment pathLen by 1
	pathLen = pathLen + 1

	if root.left is None and root.right is None:
		
		# leaf node then print the list
		printArray(path, pathLen)
	else:
		# try for left and right subtree
		printPathsRec(root.left, path, pathLen)
		printPathsRec(root.right, path, pathLen)

# Helper function to print list in which
# root-to-leaf path is stored
def printArray(ints, length): 
    global all_ints

    digit = ""
    for i in ints[0 : length]:
        digit = digit + str(i)
    #     print(i, " ", end="")
    # print(digit)
    all_ints += int(digit)
    

# # Driver program to test above function
# """
# Constructed binary tree is
# 			10
# 		/ \
# 		8	 2
# 	/ \ /
# 	3 5 2
# """
# root = Node(10)
# root.left = Node(8)
# root.right = Node(2)
# root.left.left = Node(3)
# root.left.right = Node(33)
# root.right.left = Node(2)
# printPaths(root)
# print(all_ints)
# This code has been contributed by Shweta Singh.


# Main function
def main():
    n = int(input())  # Number of nodes

    nodes = [Node(0) for i in range(n + 1)]


    for _ in range(n - 1):
        v, u = map(int, input().split())
        if nodes[u].left is None:
            nodes[u].left = nodes[v]
        else:
            nodes[u].right = nodes[v]

    root = nodes[1]  # Root of the tree

    for i in range(1, n + 1):
        nodes[i].data = (int(input()))
        
        
    # print(nodes)
    printPaths(root)
    print(all_ints)
    


    
    
    
if __name__ == "__main__":
    main()