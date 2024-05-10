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
    int recur(TreeNode *root, map<TreeNode*,int> &m){
        if(root == NULL) return 0;
        if(m.find(root) != m.end()) return m[root];
        // Either rob root and move to its grandchildren OR don't rob root and move to its children
        // Rob root
        int sum1 = root->val;
        if(root -> left != NULL) sum1 += recur(root->left->left, m) + recur(root->left->right, m);
        if(root -> right != NULL) sum1 += recur(root->right->left, m) + recur(root->right->right, m);

        return m[root] = max(sum1, recur(root->left, m) + recur(root->right, m));
    }
    int rob(TreeNode* root) {
        map<TreeNode*,int> m;
        return recur(root,m);
    }
};