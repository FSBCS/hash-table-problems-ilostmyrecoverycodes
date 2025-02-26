def k_most_frequent(lst, k):
    #Steps: Make dictionary {this symbol}
    cool_dictionary = {}
    #2. Iterate through the list, and every time you come across a NEW character, add it to the dictionary with a value of 1 
    for i in k:
        if i not in cool_dictionary:
            pass
            
    
    #3. Every time you come across a character youve already seen, add 1 in the dictionary of that character

    #4. In dictionary.items, sort list from highest value to lowest value.
    #5. While loop: while k is greater than 0, add an item from the sorted list to another list, then decrease k by 1 if frequency value of that character is lower 
    #6. return list
    pass