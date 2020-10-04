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
    vector<int> solve(Tree* root) {
        vector<int> level;
        queue<Tree *> nodes;
        if(!root) return level;
        nodes.push(root);
        while(!nodes.empty()){
            int size = nodes.size();
            while(size--){
                Tree * node = nodes.front();
                nodes.pop();
                level.push_back(node->val);
                if(node->left) nodes.push(node->left);
                if(node->right) nodes.push(node->right);
                
            }
        }
        return level;
    
    }
};
