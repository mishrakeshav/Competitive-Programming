from sys import stdin,stdout
path = [
    (2,2),(1,3),(2,4),(1,5),(2,6),(1,7),(2,8),
    (3,7),(4,8),(5,7),(6,8),(7,7),(8,8),(7,7),
    (8,6),(7,5),(8,4),(7,3),(8,2),(7,1),(6,2),
    (5,1),(4,2),(3,1),(4,2),(3,3),(4,4),(3,5),
    (4,6),(5,5),(6,6),(7,5),(6,4),(5,3)
]

for t in range(int(stdin.readline())):
    r,c = map(int, stdin.readline().split())
    if r == 1 and c == 1:
        stdout.write(str(len(path)) + "\n")
        for bis in path:
            stdout.write(str(bis[0]) + " " + str(bis[1]) + "\n")
    else:
        stdout.write(str(len(path) + 2) + "\n")
        stdout.write(str((r+c)//2) + " " + str((r+c)//2) + "\n")
        stdout.write("1 1\n")
        for bis in path:
            stdout.write(str(bis[0]) + " " + str(bis[1]) + "\n")

    
