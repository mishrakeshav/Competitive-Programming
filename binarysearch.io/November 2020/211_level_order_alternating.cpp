/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */
void add_to_list(int s,vector<int>  & order, vector<Tree *>  newl){
    if(s){
        for(int i = newl.size()-1; i >=0; i--){
            order.push_back(newl[i]->val);
        }
    }else{
        for(int i = 0; i < newl.size(); i++){
            order.push_back(newl[i]->val);
        }
    }
}
vector<int> solve(Tree* root) {
    vector<Tree *> stack;
    stack.push_back(root);
    int s = 1;
    vector<int> order;
    order.push_back(root->val);
    while(stack.size()){
        vector<Tree *> newl;
        for(auto &node : stack){
            if(node->left) newl.push_back(node->left);
            if(node->right) newl.push_back(node->right);
        }
        add_to_list(s,order,newl);
        stack = newl;
        s ^= 1;
    }
    return order;
}