import re
def solution(s):
    ans = ''
    convert = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    for num in re.split('(\d+)', s):
        if num.isalpha():
            if num not in convert:
                num_split = ''
                i = 0
                while i < len(num):
                    num_split += num[i]
                    if num_split in convert:
                        ans += convert[num_split]
                        num_split = ''
                    i += 1
                    
            else: ans += convert[num]
        else:
            ans += num
    return int(ans)