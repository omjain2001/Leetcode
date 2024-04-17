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
    void recur(TreeNode *root, vector<string> &ans, string temp){
        if(root == NULL) return;
        if(temp != "") temp += "->";
        temp += to_string(root->val);
        if(root->left == NULL && root->right == NULL){
            ans.push_back(temp);
            return;
        }
        recur(root->left,ans,temp);
        recur(root->right,ans,temp);
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        recur(root,ans,"");
        return ans;
    }
};