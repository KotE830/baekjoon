import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_preorder(postorder: list, inorder: list):
    result = []
    def preorder(postorder: list, inorder: list):
        if inorder:
            index = inorder.index(postorder.pop())
            
            preorder(postorder, inorder[index+1:])
            preorder(postorder, inorder[:index])
            result.append(inorder[index])
            

    
    preorder(postorder, inorder)
    print(*result[::-1])
    
'''
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

print_preorder(postorder, inorder)
'''
#print_preorder(['A','C','B','F','E','D','H','J','L','K','I','G'],['A','B','C','D','E','F','G','H','I','J','K','L'])

print_preorder([1, 2, 3, 4], [4, 3,2, 1])