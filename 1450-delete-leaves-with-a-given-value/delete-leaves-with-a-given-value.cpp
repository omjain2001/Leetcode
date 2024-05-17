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
    TreeNode* recur(TreeNode *root, int target){
        if(root == NULL) return NULL;
        TreeNode *left = recur(root->left, target);
        TreeNode *right = recur(root->right, target);
        if(left && left -> left == NULL && left -> right == NULL && left -> val == target){
            delete left;
            root -> left = NULL;
        }
        if(right && right -> left == NULL && right -> right == NULL && right -> val == target){
            delete right;
            root -> right = NULL;
        }
        return root;
    }
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        root = recur(root, target);
        if(root -> left == NULL && root -> right == NULL && root -> val == target){
            return NULL;
        } else {
            return root;
        }
    }
};