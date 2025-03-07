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
    int maxDepth(TreeNode* root) {
        if(root == NULL) return 0;
        queue<pair<TreeNode*,int>> q;
        q.push({root,1});
        int maxi = INT_MIN;
        while(!q.empty()){
            auto [temp, count] = q.front();
            q.pop();
            maxi = max(maxi, count);
            if(temp->left) q.push({temp->left, count+1});
            if(temp->right) q.push({temp->right, count+1});
        }

        return maxi;
    }
};