class Solution:
    
    def pathSum(self, root, net):
        self.result = []
        if root is None:
            return self.result
        self.paths(root, net, [])
        return self.result
        
    def paths(self, root, net, p):
        if root.left is None and root.right is None and root.val == net:
            self.result.append(p + [root.val])
            return
        if root.left:
            self.paths(root.left, net - root.val, p + [root.val])
        if root.right:
            self.paths(root.right, net - root.val, p + [root.val])