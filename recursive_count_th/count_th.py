'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
_______________
UPER:
convert the word to a list array.
whats the base case?

word => count of # of "th" that occur
'''
def split_word(word):
    return [c for c in word]

def count_th_iterative(word):
    th_count = 0
    for i,c in enumerate(word):
        if c == 't' and word[i+1] == 'h':
            th_count = th_count + 1
    
    print(th_count)
    return th_count


count_th_iterative('thalth')

