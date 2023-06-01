vowels = ['a', 'e', 'i', 'o', 'u']
vowel_dict = {}
for vowel in vowels:
    vowel_dict[vowel + 'p' + vowel] = vowel

coded = input()
for x in vowel_dict:
    coded = coded.replace(x, vowel_dict[x])

print(coded)