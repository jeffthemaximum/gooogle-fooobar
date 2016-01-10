'''
String cleaning
===============

Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists who are turning 
rabbits into zombies. He sends a text transmission to you, but it is intercepted by a pirate, 
who jumbles the message by repeatedly inserting the same word into the text some number of 
times. At each step, he might have inserted the word anywhere, including at the beginning or 
end, or even into a copy of the word he inserted in a previous step. By offering the pirate a 
dubloon, you get him to tell you what that word was. A few bottles of rum later, he also 
tells you that the original text was the shortest possible string formed by repeated removals 
of that word, and that the text was actually the lexicographically earliest string from all 
the possible shortest candidates. Using this information, can you work out what message your 
spy originally sent?

For example, if the final chunk of text was "lolol," and the inserted word was "lol," the 
shortest possible strings are "ol" (remove "lol" from the beginning) and "lo" (remove "lol" from the end). 
The original text therefore must have been "lo," the lexicographically earliest string.

Write a function called answer(chunk, word) that returns the shortest, lexicographically earliest 
string that can be formed by removing occurrences of word from chunk. Keep in mind that the 
occurrences may be nested, and that removing one occurrence might result in another. For example, 
removing "ab" from "aabb" results in another "ab" that was not originally present. Also keep 
in mind that your spy's original message might have been an empty string.

chunk and word will only consist of lowercase letters [a-z].
chunk will have no more than 20 characters.
word will have at least one character, and no more than the number of characters in chunk.
'''
import pudb

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

    j = length_chunk - 1
    while j >= i:
        substring = chunk[(j - length_word):i]
        if substring == word:
            end_of_first_half = (j - length_word)
            start_of_second_half = j
            first_half = chunk[:end_of_first_half]
            second_half = chunk[start_of_second_half:]
            chunk = first_half + second_half
        j -= 1
    return chunk

def iterate_and_remove(chunk, word, idx):
    while word in chunk:
        chunk = trim_word(chunk, word, idx)
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
    # pu.db 
    for i in range(length_chunk - 1, 0, -1):
        chunk = iterate_and_remove(chunk, word, i)

        results.append(chunk)

    return sorted(results)[0]





chunk = "goodgooogoogfogoood"
word = "goo"


print answer(chunk, word)