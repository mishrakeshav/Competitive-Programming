
class Trie:
    def __init__(self, name, isendofword = False ):
        self.name = name
        self.isendofword = isendofword
        self.elements = dict()
    
    def __repr__(self):
        return str(
            {
                'name' : self.name,
                'isendiftheword' : self.isendofword,
                'elements' : self.elements.keys()
            }
        )

def search(trie,name):
    new = trie
    for i in name:
        if i in new.elements:
            new = new.elements[i]
        else:
            return False 
    return True 
def printTrie(trie):
    if  trie:
        print(trie.name)
        print(trie.elements)
        for node in trie.elements:
            printTrie(trie.elements.get(node))
def insert(trie,name):
    new = trie 
    for i in range(len(name)):
        if name[i] in new.elements:
            new = new.elements[name[i]]
            if i == len(name)  - 1: 
                new.isendofword = True
        else:
            node = Trie(name[i])
            new.elements[name[i]] = node 
            new = node
    new.isendofword = True
    return trie

def sol(trie,name,flag=False,start=0,word = []):
    root = trie
    for i in range(start, len(name)):
            if name[i] in root.elements:
                root = root.elements[name[i]]
                word.append(name[i])
            
            if flag:
                return False
            k = word[:]
            for j in root.elements:
                k = word[:]
                k.append(j)
                l = checkdictionary(root.elements[j],name, flag = 1,start = i,word =  k)
                if l:
                    return l 
    if trie.isendofword:
        return word 
    else:
        for node in root.elements:
            if root.elements[node]:
                word.append(node)
                break

    return word
    
            

def checkdictionary(trie,name,flag = False, start = None, word = []):
    root = trie 
    if flag ==1:
        for i in range(start,len(name)):
            if name[i] in root.elements:
                root = root.elements[name[i]]
                word.append(name[i])
            else:
                # if abs(len(name) - len(word)) == 1:
                #     return word
                return False 
        return word
    else:
        for i in range(len(name)):
            if name[i] in root.elements:
                root = root.elements[name[i]]
                word.append(name[i])
            else:
                k = word[:]
                for j in root.elements:
                    k = word[:]
                    k.append(j)
                    l = checkdictionary(root.elements[j],name, flag = 1,start = i,word =  k)
                    if l:
                        return l 
        return word
        




def solve():
    n, q = map(int, input().split())
    dictionary = []
    trie = Trie(None)
    for i in range(n):
        name = input()
        trie = insert(trie,name)
    for i in range(q):
        name = input()
        print("".join(sol(trie,name, word = [])))
    # printTrie(trie)


if __name__ == '__main__':
    for t in range(int(input())):
        solve()