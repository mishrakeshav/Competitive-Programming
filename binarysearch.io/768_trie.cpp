struct Node{
    Node * children[26];
    bool isEndOfTheWord;
};
class Trie {
    public:
    const int ALPHABET_SIZE = 26;
    struct Node * root = getNode();
    Trie() {
    }

    void add(string s) {
        Node * node = root;
        for(int i = 0; i < s.length(); i++){
            int index = s[i] - 'a';
            if(!node->children[index]){
                node->children[index] = getNode();

            }
            node = node->children[index];
        }
        node->isEndOfTheWord = true;
    }

    bool exists(string word) {
        Node * node = root;
        int n = word.length();
        for(int i = 0; i < n; i++){
            int index = word[i] - 'a';
            if(!node->children[index]) return false;
            node = node->children[index];
        }
        if(!node->isEndOfTheWord) return false;
        return true;
    }

    bool startswith(string p) {
        Node * node = root;
        int n = p.length();
        for(int i = 0; i < n; i++){
            int index = p[i] - 'a';
            if(!node->children[index]) return false;
            node = node->children[index];
        }
        return true;
    }

    Node * getNode(){
        struct Node * node = new Node;
        node->isEndOfTheWord = false;
        for(int i = 0; i < ALPHABET_SIZE; i++){
            node->children[i] = NULL;
        }
        return node;
    }
};