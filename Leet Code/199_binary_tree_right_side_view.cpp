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
    int max_level = 0;
public:
    void rightView(TreeNode* root, vector<int> &result, int level){
        if(root==NULL) return;
        if(level > max_level){
            max_level++;
            result.push_back(root->val);
        }
        rightView(root->right, result, level + 1);
        rightView(root->left,result,level + 1);
        
    }
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result = {};
        rightView(root,result,1);
        return result;
    }
};