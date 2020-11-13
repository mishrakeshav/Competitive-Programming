/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */
int solve(Tree* root, vector<string>& moves) {
    vector<Tree *> stack;
    for(int i = 0; i < moves.size(); i++){
        if(moves[i] == "RIGHT"){
            stack.push_back(root);
            root = root->right;
        }else if(moves[i] == "LEFT"){
            stack.push_back(root);
            root = root->left;
        }else{
            root = stack[stack.size()-1];
            stack.pop_back();
        }
    }
    return root->val;
}