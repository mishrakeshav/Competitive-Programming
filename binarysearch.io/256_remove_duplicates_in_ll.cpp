#include "solution.hpp"
using namespace std;

/**
 * class LLNode {
 *     public:
 *         int val;
 *         LLNode *next;
 * };
 */
class Solution {
    public:
    LLNode* solve(LLNode* node){
        unordered_map<int,int> hashmap;
        LLNode * head = node;
        LLNode * prev;
        while(node){
            if(hashmap.find(node->val) != hashmap.end()){
                prev->next = node->next;
            }else{
                prev = node;
            }
            hashmap[node->val] = 1;
            node = node->next;
        }
        return head;
    }
};
