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
    int recur(TreeNode *root, TreeNode *parent){
        if(!root) return 0;
        int moves = recur(root->left, root) + recur(root -> right, root);
        int x = root->val - 1;
        if(parent) parent->val += x;
        moves += abs(x);
        return moves;
    }
    int distributeCoins(TreeNode* root) {
        return recur(root, NULL);
    }
};