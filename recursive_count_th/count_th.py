'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
_______________
UPER:
try to solve it iteratively first
convert the word to a list array.
whats the base case?
what is the subproblem?
start with an easy input:  "health" 

word => count of # of "th" that occur
'''
def split_word(word):
    return [c for c in word]

def join_word(word_arr):
    blank_string = ''
    return blank_string.join(word_arr)

def remove_th(word_arr):
    word = join_word(word_arr)
    print('word in remove_th', word, 'char length:', len(word))
    print('word index of th', word.index('th'))
    th_i = word.index('th')
    word = word[:th_i] + word[th_i + 2:]
    print('after slicing word', word, 'char length:', len(word))  ##BUG after slicing, another th appeared in sequence, so counted extra
    return word

def count_th(word):

    print('word to count th of: ', word)

    if len(word) == 0:
        return 0
    
    if 'th' in word:
        word_arr = split_word(word)
        print('word array of th_word', word_arr)

        cleared_th = remove_th(word_arr)
        return 1 + count_th(cleared_th)
        
        # clear_th = list(filter(lambda w: w != 't' and w != 'h', word_arr))  #pblm: this removes ALL the th's in the word
        # print('cleared th word: ', cleared_th)
        # print('filtered', clear_th)
        # print('new word', new_word)
    else:
        return 0

word = 'thhtthht'
print('word length', len(word))

print(count_th(word))



    # th_count = 0
    # print(word, 'th' in word, 'th_count', th_count)
    # if (len(word) <= 2):
    #     if 'th' in word: return th_count + 1
    #     else: return 0
    # return count_th(word[2:])




# def count_th_iterative(word):
#     th_count = 0
#     for i,c in enumerate(word):
#         if c == 't' and word[i+1] == 'h':
#             th_count = th_count + 1
    
#     print(th_count)
#     return th_count


count_th_iterative('thalth')

