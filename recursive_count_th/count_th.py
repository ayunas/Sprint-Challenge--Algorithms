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
    print('word in remove_th', word)
    print('word index of th', word.index('th'))
    th_i = word.index('th')
    word = word[:th_i] + word[th_i + 2:]
    # print('after slicing word', word)
    return word

def count_th(word):

    print('word to count th of: ', word)

    if len(word) == 0:
        return 0
    
    if 'th' in word:
        word_arr = split_word(word)
        print('word array', word_arr)
        # word_arr = filter(word_arr,lambda w : w == 't')
        # for w in word_arr:
        # clear_th = list(filter(lambda w: w != 't' and w != 'h', word_arr))  #pblm: this removes ALL the th's in the word
        # cleared_th = remove_th(word_arr)
        cleared_th = remove_th(word_arr)
        # print('cleared th word: ', cleared_th)
        # print('filtered', clear_th)
        # new_word = join_word(cleared_th)
        # print('new word', new_word)
        return 1 + count_th(cleared_th)
    else:
        return 0

print(count_th('health'))



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


# count_th_iterative('thalth')

