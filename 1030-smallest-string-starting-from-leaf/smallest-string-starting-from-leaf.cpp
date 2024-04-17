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
    void recur(TreeNode *root, set<string> &s, string temp){
        if(root == NULL) return;
        char chr = 'a' + root->val;
        temp = temp + chr;
        if(root -> left == NULL && root -> right == NULL){
            reverse(temp.begin(), temp.end());
            s.insert(temp);
            return;
        }
        recur(root->left,s,temp);
        recur(root->right,s,temp);

    }
    string smallestFromLeaf(TreeNode* root) {
        set<string> s;
        recur(root, s, "");
        return *s.begin();
    }
};