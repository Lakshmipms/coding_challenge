def count_pairs_with_sum(arr, X):
    """
    This function counts pairs in the given array that sum up to X.

    :param arr: Sorted integer list
    :param X: required sum
    :return: Count of pairs with sum equal to required sum(X).
    """

    # Initialize pointers at the start and end of the array
    left, right = 0, len(arr) - 1

    # Variable to keep count of the pairs found
    count = 0

    # Iterate until left pointer is less than right pointer
    while left < right:
        # Calculate the current sum of the numbers at the left and right pointers
        current_sum = arr[left] + arr[right]

        # If the current sum is equal to X
        if current_sum == X:
            count += 1  # Increment the count
            left += 1  # Move the left pointer to the right
            right -= 1  # Move the right pointer to the left
        # If the current sum is less than X
        elif current_sum < X:
            left += 1  # Move the left pointer to the right
        # If the current sum is greater than X
        else:
            right -= 1  # Move the right pointer to the left

    # Return the final count of pairs
    return count
