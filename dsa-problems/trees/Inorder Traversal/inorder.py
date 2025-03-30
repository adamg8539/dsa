from binarytree import Node 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
  
# # Getting binary tree 
# print('Binary tree :', root) 
  
# # Getting list of nodes 
# print('List of nodes :', list(root)) 
  
# # Getting inorder of nodes 
# print('Inorder of nodes :', root.inorder) 
  
# # Checking tree properties 
# print('Size of tree :', root.size) 
# print('Height of tree :', root.height) 
  
# # Get all properties at once 
# print('Properties of tree : \n', root.properties) 

# def inorder_traversal(root):
#   arr = []
#   curr = root
#   while curr != None:
#     if curr.left == None:
#       arr.append(curr.val)
#       curr = curr.right
#     else:
#       pred = curr.left
#       while pred.right 


# inorder_traversal(root)
resp = []
def recursive_inorder(root):
  if not root:
    return
  recursive_inorder(root.left)
  resp.append(root.val)
  recursive_inorder(root.right)
  return resp

x = recursive_inorder(root)
print(x)
