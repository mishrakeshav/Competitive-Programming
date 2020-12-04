/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */
int solve(Tree* root, int a, int b) {
    if(root==NULL) return -1;
    int left = solve(root->left,a,b);
    int right = solve(root->right,a,b);
    if(left!=-1 && right!=-1) return root->val;
    if(root->val==a || root->val==b) return root->val;
    return left!=-1?left:right;   
}