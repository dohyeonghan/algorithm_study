T = int(input())
for _ in range(T):
  stk = []
  isVPS = True
  for ch in input():
    if ch == '(':
      stk.append(ch)
    #스택 상단의 여는 괄호와 지금 닫는 괄호를 쌍을 맺어서 pop
    else:
      if len(stk) > 0:
        stk.pop()
      else:
        isVPS = False
        break
  if len(stk) > 0:
    isVPS = False
  print('YES' if isVPS else 'NO')