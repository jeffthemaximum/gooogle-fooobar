import pudb

def lift(string, start, length):
    """
    Returns a string with a specified index range removed
    """
    a = start
    b = start + length
    return string[:a] + string[b:]


def rclean(subject, search, offset):
    """
    Repeatedly removes all occurrences of search starting at offset
    """

    # find the first index of the word, starting at offset
    index = subject.find(search, offset)

    length = len(search)

    # keep relacing until search can not be found in subject
    while index != -1 and offset < length:
        subject = lift(subject, index, length)
        index = subject.find(search)

    return subject


def answer(chunk, word):
    """
    Returns the shortest, lexicographically earliest string that can be formed
    by removing occurrences of word from chunk.
    This method does all replacements for each subsequent section of the string.
    """
    results = []
    
    pu.db

    for offset in range(len(chunk) - len(word)):

        # repeatedly removes all occurrences of word in chunk starting at offset
        result = rclean(chunk, word, offset)

        # check if there were any replacements
        if result != chunk:
            results.append(result)

    return sorted(results)[0]

chunk = "goodgooogoogfogoood"
word = "goo"
print answer(chunk, word)

'''
def trim_word(chunk, word):
    length_chunk = len(chunk)
    length_word = len(word)
    i = length_chunk
    
    while i > 0:
        substring = chunk[(i - length_word):i]
        if substring == word:
            end_of_first_half = (i - length_word)
            start_of_second_half = i
            first_half = chunk[:end_of_first_half]
            second_half = chunk[start_of_second_half:]
            chunk = first_half + second_half
            return chunk
        i -= 1
    
def other_trim_word(chunk, word):
    while word in chunk:
        chunk = chunk.replace(word, '')
    return chunk

def answer(chunk, word):
    # pu.db

    length_chunk = len(chunk)
    length_word = len(word)
    # array_of_indices = []
    # i = 0

    # while i < length_chunk:
    #     substring = chunk[i:(i + length_word)]
    #     if substring == word:
    #         array_of_indices.append(i)
    #     i += 1

    # return array_of_indices

    other_chunk = chunk[:]

    while word in chunk:
        chunk = trim_word(chunk, word)

    other_chunk = other_trim_word(other_chunk, word)


    return_chunk = min(chunk, other_chunk)

    return return_chunk
'''

'''
def trim_word(chunk, word, idx):
    length_chunk = len(chunk)
    length_word = len(word)
    i = idx
    
    while i > 0:
        substring = chunk[(i - length_word):i]
        if substring == word:
            end_of_first_half = (i - length_word)
            start_of_second_half = i
            first_half = chunk[:end_of_first_half]
            second_half = chunk[start_of_second_half:]
            chunk = first_half + second_half
        i -= 1

    j = length_word
    while j >= i:
        substring = chunk[(j - length_word):i]
        if substring == word:
            end_of_first_half = (j - length_word)
            start_of_second_half = j
            first_half = chunk[:end_of_first_half]
            second_half = chunk[start_of_second_half:]
            chunk = first_half + second_half
        j -= 1

def iterate_and_remove(chunk, word, idx):
    while word in chunk:
        chunk = trim_word(chunk, word, idx)
    return chunk

def other_trim_word(chunk, word):
    while word in chunk:
        chunk = chunk.replace(word, '')
    return chunk

def answer(chunk, word):
    # pu.db

    length_chunk = len(chunk)
    length_word = len(word)
    results = []
    # array_of_indices = []
    # i = 0

    # while i < length_chunk:
    #     substring = chunk[i:(i + length_word)]
    #     if substring == word:
    #         array_of_indices.append(i)
    #     i += 1

    # return array_of_indices

    other_chunk = chunk[:]
    pu.db 
    for i in range(length_chunk - 1, 0, -1):
        chunk = iterate_and_remove(chunk, word, i)

        results.append(chunk)

    return sorted(results)





chunk = "goodgooogoogfogoood"
word = "goo"


print answer(chunk, word)
'''

'''
removes last goo always
def trim_word(chunk, word):
    length_chunk = len(chunk)
    length_word = len(word)
    i = length_chunk
    
    while i > 0:
        substring = chunk[(i - length_word):i]
        if substring == word:
            end_of_first_half = (i - length_word)
            start_of_second_half = i
            first_half = chunk[:end_of_first_half]
            second_half = chunk[start_of_second_half:]
            chunk = first_half + second_half
            return chunk
        i -= 1

    
def other_trim_word(chunk, word):
    while word in chunk:
        chunk = chunk.replace(word, '')
    return chunk

def get_array_of_indices(chunk, word):
    array_of_indices = []
    i = 0
    length_chunk = len(chunk)
    length_word = len(word)
    while i < length_chunk:
        substring = chunk[i:(i + length_word)]
        if substring == word:
            array_of_indices.append(i)
        i += 1
    return array_of_indices

def answer(chunk, word):
    # pu.db

    length_chunk = len(chunk)
    length_word = len(word)






    other_chunk = chunk[:]
    pu.db
    while word in chunk:
        chunk = trim_word(chunk, word)

    other_chunk = other_trim_word(other_chunk, word)


    return_chunk = min(chunk, other_chunk)

    return return_chunk





chunk = "goodgooogoogfogogoood"
word = "goo"


print answer(chunk, word)
'''


'''
removes all goos right to left in one swipe, then does that again till all goos gone

def trim_words(chunk, word, indices):
    length_chunk = len(chunk)
    length_word = len(word)
    i = length_chunk
    indices = reversed(indices)

    for index in indices:
        substring = chunk[index:(index + length_word)]
        if substring == word:
            end_of_first_half = index
            start_of_second_half = index + length_word
            first_half = chunk[:end_of_first_half]
            second_half = chunk[start_of_second_half:]
            chunk = first_half + second_half
    return chunk


    
# def other_trim_word(chunk, word):
#     while word in chunk:
#         chunk = chunk.replace(word, '')
#     return chunk

def get_array_of_indices(chunk, word):
    array_of_indices = []
    i = 0
    length_chunk = len(chunk)
    length_word = len(word)
    while i < length_chunk:
        substring = chunk[i:(i + length_word)]
        if substring == word:
            array_of_indices.append(i)
        i += 1
    return array_of_indices

def answer(chunk, word):
    # pu.db

    length_chunk = len(chunk)
    length_word = len(word)






    other_chunk = chunk[:]

    while word in chunk:
        indices = get_array_of_indices(chunk, word)
        chunk = trim_words(chunk, word, indices)

    return chunk





chunk = "goodgooogoogfogogoood"
word = "goo"



print answer(chunk, word)
'''