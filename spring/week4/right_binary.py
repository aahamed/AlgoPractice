"""
Author: Aadil Ahamed
right_binary.py: Right Side View of Binary Tree - Leetcode
"""

class Solution(object):

    def rightSideView(self, root):
        output = []
        self.traverse_right(root, -1, 0, output)
        return output

    def traverse_right(self, node, max_ht, curr_ht, queue):
        if node is None:
            return 0
        else:
            if curr_ht > max_ht:
                queue.append(node.val)
                max_ht = curr_ht
            rmax = traverse_right(node.right, max_ht, curr_ht+1, queue)
            if rmax > max_ht:
                max_ht = rmax
            lmax = traverse_right(node.left, max_ht, curr_ht+1, queue)
            if lmax > max_ht:
                max_ht = lmax
            return max_ht



def main():
    pass

if __name__ == "__main__":
    main()
