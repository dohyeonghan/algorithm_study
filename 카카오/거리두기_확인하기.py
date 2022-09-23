'''
p 확인했을때

4방향 체크
빈곳이면 -> 넘어가고 dist + 1
true false 리턴
p 중에 하나라도 false면 x 넣기

같은 거리만큼 체크해야되니까 bfs

'''
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
for i in places:
    print(i)