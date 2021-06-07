def solution(dartResult):
  answer = []
  for num, i in enumerate(dartResult, 1):
    #if i in '0123456789':
    if i == 'S':
      answer[-1] **= 1
    elif i == 'D':
      answer[-1] **= 2
    elif i == 'T':
      answer[-1] **= 3
    elif i == '*':
      answer[-1] *= 2
      if len(answer) == 2:
        answer[-2] *= 2
    elif i == '#':
      answer[-1] *= -1
    else:
      if dartResult[num-1:num+1] == '10':
        answer.append(10)
      elif dartResult[num-2:num] != '10':
        answer.append(int(i))
  return sum(answer)
print(solution('1S2D*3T'))


## 정규표현식
import re
testcase = ['1S2D*3T', '1D2S#10S']
패턴 = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
r = 패턴.findall(testcase[1])
print('정규표현식 사용 솔루션')
print(r)

def solution_re(dartResult):
  패턴 = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
  answer = []
  계산식 = {
    'S':lambda 값: 값,
    'D':lambda 값: 값**2,
    'T':lambda 값: 값**3
  }
  for 숫자, 승수, 상 in 패턴.findall(dartResult):
    #print(숫자, 승수, 상)
    if 승수 == 'S':
      점수 = 계산식['S'](int(숫자))
    elif 승수 == 'D':
      점수 = 계산식['D'](int(숫자))
    elif 승수 == 'T':
      점수 = 계산식['T'](int(숫자))
    if 상 == '*':
      점수 *= 2
      if answer:
        answer[-1] *= 2
    elif 상 == '#':
      점수 *= -1
    answer.append(점수)
  return sum(answer)
print(solution_re('1S2D*3T'))

