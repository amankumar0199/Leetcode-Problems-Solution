def mergetwotree(self,t1,t2):
    if t1 and t2:
        t3 = TreeNode(t1.val + t2.val) 
        t3.left = self.mergeTrees(t1.left, t2.left)
        t3.right = self.mergeTrees(t1.right, t2.right)
        return t3
    elif t1:
        return t1
    elif t2:
        return t2