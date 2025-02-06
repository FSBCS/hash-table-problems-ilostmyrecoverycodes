


def group_anagrams(words):
    #2. Create lists
    hash_Value_word_list = {}
    #3. Create hash values for all of the words
    for i in words:
        totally_sorted_word = totally_sorted_word.sort
        hash_Value_word_list.append(hash(i))
    #4. Group words by same hash value
        if totally_sorted_word in hash_Value_word_list:
            hash_Value_word_list[totally_sorted_word].append(i)
        else:
            hash_Value_word_list[totally_sorted_word] = i
    # some sort of .sort function
    return list(hash_Value_word_list)
    #5. Output