/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */
bool solve(Tree* root) {
    if(root==NULL) return true;
    if(!root->left && !root->right) return true;
    int s = 0;
    bool left = solve(root->left);
    bool right = solve(root->right);
    if(root->left) s += root->left->val;
    if(root->right) s += root->right->val;
    return (root->val == s) && left && right;
}