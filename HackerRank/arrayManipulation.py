def arrayManipulation(n, queries):
    array = [0]*(n+1) 

    for i in range(len(queries)):
        a, b, k = queries[i]
        array[a-1] += k 
        array[b] += -k 
        print(array)
    for i in range((len(array)-1)):
        array[i+1] = array[i] + array[i+1]

    return max(array[:-1])

if __name__ == '__main__':

    n, q = map(int, input().split())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split()))) 
    
    print(arrayManipulation(n, queries))