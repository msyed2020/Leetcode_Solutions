# Serialize and Deserialize Binary Tree

"""
This problem involves converting a binary tree to a string list, and a string list to a binary search tree.

Serialization: This works by capitalizing on the recursive stack of the depth first search technique, which first
recursively calls its children, then adds the childrens' values after all children have first been printed out. If a
child is null, it is replaced by 'N' rather than a specific node value. Ultimately, the string list in which the nodes
are added is modified and formatted into a final, complete string.

Deserialization: This works by reconverting the string into a list, and creating an increment, as a recursive depth
first search will be done, but an iteration combination will have to be done alongside the recursive stack, as we
are traversing through a list rather than an actual tree.
If a value is None or null, we simply increment onwards and return a None for that part of the tree, signifying that
that position in the tree belongs to a null value. Otherwise, assuming we have a node, we traverse downwards, creating
the node for that position, incrementing the i to focus on the next node, then call the dfs on the children to
solidify their position in the tree, and then returning the node for the current call stack position to be the node
that we had established. We still call dfs so that the binary tree is organized by its call stack.

Commentary will be put on code to emphasize action

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = [] # Initialize result variable

        def dfs(root, res): # create a dfs call, root is a required parameter but I put res as a parameter via my style
            if not root: # if not root, append an N (or string to signify null) and break out of this call stack
                res.append("N")
                return # break out of call stack here, since null does not have children and we have better things to do
            res.append(str(root.val)) # convert the value to string and add to the result list
            dfs(root.left, res) # now that we have the root covered, go to children
            dfs(root.right, res)

        dfs(root, res) # call dfs function
        return ",".join(res) # format list into string as desired by the result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",") # reconvert the string into a list
        self.i = 0 # initialize incrementer

        def dfs(): # create dfs call, this requires no special parameters as it's creating a new BT
            if vals[self.i] == "N": # If we find a null value, we can add a null value to the tree and just keep going
                self.i += 1
                return None # this return call is important because it signifies to the call stack that this position is null
            node = TreeNode(int(vals[self.i])) # create the TreeNode value for the BT at this position
            self.i += 1 # increment to the next value as necessary
            node.left = dfs() # cover child recursive call (this is important bc it signifies to the call stack to insert the child here in the tree)
            node.right = dfs() # cover next child recursive call
            return node # finally, return the node at this position so that its position at this area in the stack is solidified

        return dfs() # call dfs to work the binary tree through the whole stack