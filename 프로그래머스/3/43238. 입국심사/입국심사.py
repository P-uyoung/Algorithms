def solution(n, times):
    left, right = 1, max(times) * (n//len(times))

    def count(time):
        nums = 0
        for a in times:
            nums += time // a
        return nums

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        
        counted = count(mid)
        if n == counted:
            answer = mid  # Save the result if the count matches
            right = mid - 1  # Still try to find a smaller value
        elif n < counted:
            right = mid - 1
        else:
            left = mid + 1

    # If no exact match is found, return the saved result or the left value
    return answer if answer else left