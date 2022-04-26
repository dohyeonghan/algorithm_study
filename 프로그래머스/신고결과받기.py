from collections import defaultdict

report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]

id_list = ["muzi", "frodo", "apeach", "neo"]

k = 2

answer = [0] * len(id_list)
print(answer)
report = set(report)
report = list(report)
print(report)
report_dict = defaultdict(set)
report_count = defaultdict(int)
stop = []
for item in report:
    a, b = item.split()
    report_count[b] += 1
    report_dict[a].add(b)

    if report_count[b] >= k:
        stop.append(b)
    print(report_dict)
    # a, b = item.split()
    # report_dict[a] = b
for i in stop:
    for j in range(len(id_list)):
        if i in report_dict[id_list[j]]:
            answer[j] += 1


print(report_dict)

print(report_count)

print(stop)

print(answer)