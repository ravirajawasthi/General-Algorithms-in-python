def permutation(n, f, r, dictinct_characters):
    '''
    N -> Level of recursion
    f -> frequency dict of string
    r -> recursion starter
    '''
    result[n] = r
    f[r] -= 1
    zero_flag = True
    for i in dictinct_characters:
        if f[i] != 0:
            zero_flag = False

    if not zero_flag:
        for i in dictinct_characters:
            if f[i] != 0:
                permutation(n+1, f.copy(), i, dictinct_characters)
    else:
        all_permutations.append(result[:])
        return


recursion_level = 0
all_permutations = []
string = input()
result = [0]*len(string)
length = len(string)
frequency_dictionary = {}
for i in string:
    frequency_dictionary[i] = string.count(i)
dictinct_characters = sorted(list(frequency_dictionary.keys()))
for i in dictinct_characters:
    permutation(recursion_level, frequency_dictionary.copy(),
                i, dictinct_characters)
print(all_permutations)