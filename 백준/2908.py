a, b = map(list, input().split())
a.reverse()
b.reverse()
print(max((''.join(a)), (''.join(b))))