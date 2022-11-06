class BinTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left, self.right = left, right

    def __iter__(self):
        yield self
        
        if self.left:
            for subtree in self.left:
                yield subtree
                
        if self.right:
            for subtree in self.right:
                yield subtree

    def get_root(self):
        return self.value
