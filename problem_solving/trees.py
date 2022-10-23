import collections

def printBinaryTree(root, space, height):
 
    # Base case
    if root is None:
        return
 
    # increase distance between levels
    space += height
 
    # print right child first
    printBinaryTree(root.right, space, height)
    print()
 
    # print the current node after padding with spaces
    for i in range(height, space):
        print(' ', end='')
 
    print(root.val, end='')
 
    # print left child
    print()
    printBinaryTree(root.left, space, height)
class TreeNode : 
  def __init__(self, val=None):
    self.val=val
    self.right=None
    self.left=None

  
################################### Q1 #########################################
    """
    rightSideView
    return all node from right side-view
    - use queue to store root at first.
    - loop over level ,loop each level over level depends on length of queue, 
    - store the poped node in variable.
    """
  def rightSideView(self, root):
    res=[]
    q= collections.deque([root])

    while q :
      q_len=len(q)
      right_side=None

      for i in range(q_len):
        node=q.popleft()
        if node:
          right_side=node 
          q.append(node.left)
          q.append(node.right)
      if right_side:   
        res.append(right_side.val)
    return res


###################################Q2#########################################

  """
  https://leetcode.com/problems/binary-tree-level-order-traversal/
  Given the root of a binary tree, return the level order
  traversal of its nodes' values. (i.e., from left to right, level by level).
  """
  def levelOrder(self, root) :
    d={}
    def bdf(root,level):
        nonlocal d
        if root:
            v= d.get(level,-1)
            if v ==-1 :
                d[level]=[root.val]
            else:
                d[level].append(root.val)
            bdf(root.left,level+1)
            bdf(root.right,level+1)
  
    bdf(root,0)
    res=[v for v in d.values()]
    return res
                
###################################Q3#########################################

  """
  105. Construct Binary Tree from Preorder and Inorder Traversal

  Given two integer arrays preorder and inorder where preorder is the preorder traversal 
  of a binary tree and inorder is the inorder traversal of the same tree, 
  construct and return the binary tree.
  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
  """

  def buildTree(self, preorder, inorder):
    
      if not  preorder or not inorder : return 
      root=TreeNode(preorder[0])
      mid=inorder.index(preorder[0])
      root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
      root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
      return root



if __name__ == '__main__':


  tree=TreeNode()
  # tree.left=TreeNode(9)
  # tree.right=TreeNode(20)
  # tree.right.left=TreeNode(15)
  # tree.right.right=TreeNode(7)
  # #print(tree.rightSideView(tree))
  

  preorder = [3,9,5,1,20,15,7]
  inorder = [9,5,1,3,15,20,7]
  buildTree=tree.buildTree(preorder,inorder)
  print(buildTree)
  space = 4
  height = 7
  printBinaryTree(buildTree, space, height)