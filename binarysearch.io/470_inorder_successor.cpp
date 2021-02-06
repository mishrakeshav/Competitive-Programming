/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */

int solve(Tree* root, int t) {
    int ans = INT_MAX;
    while(root){
        if(root->val > t){
            ans = min(root->val,ans);
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return ans;
}