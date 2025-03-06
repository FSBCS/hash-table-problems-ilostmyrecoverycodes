def count_subarrays_with_sum(arr, target_sum):
    # Dictionary to store the frequency of prefix sums
    running_dictionary = {0: 1}
    # Base case: to handle subarrays starting from index 0
    running_count_total = 0
    total_total = 0
    for i in arr:
        running_count_total += i
        if running_count_total in running_dictionary:
            running_dictionary[running_count_total] += 1
        else:
            running_dictionary[running_count_total] = 1
        if running_count_total - target_sum in running_dictionary:
            total_total += running_dictionary[running_count_total - target_sum]
    
    return total_total
    # Update the current prefix sum
    # Check if the current_sum - target_sum exists in prefix_sum_count
    # Store/update the frequency of the current prefix sum

x = [1, 1, 1, -1, 1]
print(count_subarrays_with_sum(x, 2))