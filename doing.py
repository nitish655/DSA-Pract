def pair_with_given_sum(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return True
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return False

# Example usage:
arr = [1, 2, 3, 4, 5]
target = 7
result = pair_with_given_sum(arr, target)
print(result) # Output: True