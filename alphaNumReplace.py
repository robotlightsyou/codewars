#! /usr/bin/env python3

test = "The narwhal bacons at midnight."


def alphabet_position(text):
    nums = []
    for i in range(1, 27):
        nums.append(i)
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
#    alpha = "abcdefghijklmnopqrstuvwxyz"
    master = dict(zip(alpha.split(), nums))
 #   print(master)
    newText = []
    for letter in text:
        if letter.lower() in master.keys():
            newText.append(master[letter.lower()])
    newText = " ".join(map(str, newText))
    return newText


answer = alphabet_position(test)
#answer = ' '.join(answer)
#answer = " ".join(map(str, answer))
print('The answer is \n' + answer)
# return answer


'''
Final

def alphabet_position(text):
    nums = []
    for i in range(1, 27):
        nums.append(i)
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    master = dict(zip(alpha.split(), nums))
    newText = []
    for letter in text:
        if letter.lower() in master.keys():
            newText.append(master[letter.lower()])
    newText = " ".join(map(str, newText))
    return newText

'''
