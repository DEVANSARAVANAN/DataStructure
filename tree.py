class Node:
    def __init__(self,root):
        self.val=root
        self.left=None
        self.right=None
    
def PrintInOrderTraversel(root):
    if root:
        PrintInOrderTraversel(root.left)
        print(root.val)
        PrintInOrderTraversel(root.right)

def PrintPreOrderTraversel(root):
    if root:
        print(root.val)
        PrintInOrderTraversel(root.left)
        PrintInOrderTraversel(root.right)

def PrintPostOrderTraversel(root):
    if root:
        PrintInOrderTraversel(root.left)
        PrintInOrderTraversel(root.right)
        print(root.val)
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)

print("Inorder")
PrintInOrderTraversel(root)
print('preorder')
PrintPreOrderTraversel(root)
print('postorder')
PrintPostOrderTraversel(root)