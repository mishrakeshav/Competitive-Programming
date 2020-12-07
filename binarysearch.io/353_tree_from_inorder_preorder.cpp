/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */
Tree* helper(int &pi, int i, int j, vector<int>& preorder, vector<int>& inorder){
    if(i > j) return NULL;
    Tree* node = new Tree();
    node->val = preorder[pi];
    pi+= 1;
    for(int k = i ; k <=j; k++){
        if(inorder[k]==node->val){
            node->left = helper(pi,i,k-1,preorder,inorder);
            node->right = helper(pi,k+1,j,preorder,inorder);
            break;
        }
    }
    return node;
}
Tree* solve(vector<int>& preorder, vector<int>& inorder) {
    int pi = 0;
    return helper(pi,0,preorder.size()-1,preorder,inorder);
}