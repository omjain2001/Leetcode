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
    vector<TreeNode*> possibleBSTs(int st, int e){
        if(st > e) return {NULL};
        if(st == e) return {new TreeNode(st)};
        vector<TreeNode*> ans;
        for(int i=st; i<=e; i++){
            vector<TreeNode*> possibleLeft = possibleBSTs(st, i-1);
            vector<TreeNode*> possibleRight = possibleBSTs(i+1,e);

            for(int j=0; j<possibleLeft.size(); j++){
                for(int k=0; k<possibleRight.size(); k++){
                    TreeNode *root = new TreeNode(i);
                    root->left = possibleLeft[j];
                    root->right = possibleRight[k];
                    ans.push_back(root);
                }
            }
        }
        return ans;
    }
    vector<TreeNode*> generateTrees(int n) {
        return possibleBSTs(1,n);
    }
};