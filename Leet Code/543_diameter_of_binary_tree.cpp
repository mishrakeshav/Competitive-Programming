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
    pair<int,int> helper(TreeNode* root){
        if(root == NULL) return {0,0};
        if(root->left == NULL && root->right == NULL) return {1,1};
        pair<int,int> a1 = helper(root->left);
        pair<int,int> a2 = helper(root->right);
        int  l = max(a1.first, a2.first);
        int m = max(a1.second,a2.second);
        m = max(m,a1.first + a2.first + 1);
        return {l + 1,m};
        
    }
    int diameterOfBinaryTree(TreeNode* root) {
        pair<int,int> ans = helper(root);
        if(ans.second == 0) return ans.second;
        return ans.second - 1;
    }
};