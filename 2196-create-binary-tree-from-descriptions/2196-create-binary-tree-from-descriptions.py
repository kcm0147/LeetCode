class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        global parent
        node_dic = {}

        for i in descriptions:
            node_dic[i[0]] = node_dic.get(i[0], TreeNode(i[0]))
            node_dic[i[1]] = node_dic.get(i[1], TreeNode(i[1]))
            if i[2] == 1:
                node_dic[i[0]].left = node_dic[i[1]]
            elif i[2] == 0:
                node_dic[i[0]].right = node_dic[i[1]]
            node_dic[i[1]].parent = node_dic[i[0]]

        for i in node_dic.values():
            if i.parent is None:
                parent = i
                break
        return parent