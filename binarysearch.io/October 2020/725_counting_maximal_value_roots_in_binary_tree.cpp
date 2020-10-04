#include "solution.hpp"
using namespace std;

/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */
class Solution {
    public:
    int val = 0;
    int solve(Tree* root) {
        helper(root);
        return val;
    }
    int helper(Tree* root){
        if(root == NULL){
            return 0;
        }
        if(root->left == NULL && root->right == NULL){
            val += 1;
            return root->val;
        }
        int v1 = helper(root->left);
        int v2 = helper(root->right);
        int m = max(v1,v2);
        m = max(root->val,m);
        if (m == root->val){
            val += 1;
        }
        return m;
    }
};
