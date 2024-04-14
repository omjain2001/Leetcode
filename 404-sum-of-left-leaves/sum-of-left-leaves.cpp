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
    void recur(TreeNode *root, TreeNode *parent, int &sum){
        if(root == NULL) return;
        if(root -> left == NULL && root->right == NULL && parent -> left == root){
            sum += root -> val;
        }
        recur(root->left, root, sum);
        recur(root->right, root, sum);
    }
    int sumOfLeftLeaves(TreeNode* root) {
        int sum = 0;
        recur(root, root, sum);
        return sum;
    }
};