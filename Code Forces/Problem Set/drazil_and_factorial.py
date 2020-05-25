mappings = {

    '0': '',
    '1': '',
    '2': '2',
    '3': '3',
    '4': '322',
    '5': '5',
    '6': '53',
    '7': '7',
    '8': '7222',
    '9': '7332'
}
n = int(input())
a = list(input())


x = ""
for i in a:
    x += mappings[i]
x = list(x)
x.sort(reverse=True)
print("".join(x))
