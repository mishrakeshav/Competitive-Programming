/**
 * class LLNode {
 *     public:
 *         int val;
 *         LLNode *next;
 * };
 */
LLNode* solve(LLNode* node) {
    vector<LLNode *> stack;
    LLNode * fast;
    LLNode * slow;
    slow = node;
    fast = node;
    while(fast && fast->next){
        stack.push_back(slow);
        slow = slow->next;
        fast = fast->next->next;
    }
    LLNode * foldedNode = new LLNode();
    LLNode * newNode = foldedNode;
    if(fast){
        newNode->val = slow->val; 
        slow = slow->next;
    }
    while(slow){
        newNode->next = new LLNode();
        newNode = newNode->next;
        newNode->val = slow->val + stack.back()->val;
        stack.pop_back();
        slow = slow->next;
    }
    if(fast){return foldedNode;}
    return foldedNode->next;
    return node;
}