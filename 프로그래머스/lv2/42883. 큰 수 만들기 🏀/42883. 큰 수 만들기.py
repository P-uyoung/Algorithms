def solution(number, k):
  stack = []
  for num in number:
      while len(stack) > 0 and stack[-1] < num and k > 0:
          k -= 1
          stack.pop()
      stack.append(num)
    
  # 제거 횟수 다 사용하지 않았을 때, 남은 횟수만큼 리스트 뒷자리 잘라내기
  if k != 0:          
      stack = stack[:-k]

  return ''.join(stack)