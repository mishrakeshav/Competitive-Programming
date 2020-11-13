/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */
bool solve(Tree* root) {
    vector<int> order;
    vector<Tree *> stack;
    Tree * curr;
    Tree * node;
    curr = root;
    while(stack.size() || curr!=NULL){
        while(curr){
            stack.push_back(curr);
            curr = curr->left;
        }
        node = stack[stack.size()-1];
        stack.pop_back();
        order.push_back(node->val);
        curr = node->right;
    }
    int n = order.size();
    for(int i = 0; i < n; i++){
        if(order[i] != order[n-i-1]) return false;
    }
    return true;
    
}