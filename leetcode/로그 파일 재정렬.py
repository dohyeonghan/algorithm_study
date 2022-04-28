class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = []
        strs = []
        for log in logs:
            if log.split()[1].isdigit():
                nums.append(log)
            else:
                strs.append(log)

        # 문자 로그를 두가지 조건으로 정렬 1. 로그 내용 2. 로그 내용이 같으면(else) 로그 식별자
        strs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return (strs + nums)