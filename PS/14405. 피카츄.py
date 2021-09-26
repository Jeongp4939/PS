# https://www.acmicpc.net/problem/14405

# 조건이 a 하나만 있을 시에 chkpiau NO를 출력해야 하나 YES로 출력
# 조건을 더 추가해줌

s = input().strip()
a = s.replace('pi','').replace('ka','').replace('chu','')
b = s.replace('ka','').replace('chu','').replace('pi','')
c = s.replace('chu','').replace('pi','').replace('ka','')
if (a+b+c).strip()=='':
    print('YES')
else:
    print('NO')
