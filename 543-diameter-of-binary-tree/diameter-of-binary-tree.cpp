/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxi = INT_MIN;
    int recur(TreeNode *root){
        if(root == NULL) return 0;
        int left = 0, right = 0;
        if(root->left) left = 1 + recur(root->left);
        if(root->right) right = 1 + recur(root->right);
        maxi = max(maxi, left+right);
        return max(left,right);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        recur(root);
        return maxi;
    }
};