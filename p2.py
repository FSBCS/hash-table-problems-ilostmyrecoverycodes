def k_most_frequent(lst, k):
    #Steps: Make dictionary {this symbol}
    if len(lst) == 0:
        return []
    
    cool_dictionary = {}
    #2. Iterate through the list, and every time you come across a NEW character, add it to the dictionary with a value of 1 
    #3. Every time you come across a character youve already seen, add 1 in the dictionary of that character
    for i in lst:
        if i not in cool_dictionary:
            cool_dictionary[i] = 1
        else:
            cool_dictionary[i] += 1
    #4. sort list from highest value to lowest value.
    leaderboard = sorted(cool_dictionary.keys(), key=lambda x: cool_dictionary[x], reverse=True)

    
    best_list = []
    p = k
    counter = 0
    #if there is a tie for the kth most frequent, return all of the tied elements
    while p > 0:
        best_list.append(leaderboard[counter])
        p -= 1
        counter += 1
    while counter < len(leaderboard) and cool_dictionary[leaderboard[counter]] == cool_dictionary[leaderboard[counter - 1]]:
        best_list.append(leaderboard[counter])
        counter += 1
    return best_list

    #5. While loop: while k is greater than 0, add an item from the sorted list to another list, then decrease k by 1 if frequency value of that character is lower 
    #6. return list

print(k_most_frequent([1], 1))
print(k_most_frequent([1, 1, 1, 2, 2, 3], 3))