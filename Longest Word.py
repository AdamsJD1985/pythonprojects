"""Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome"""

txt = input()


def long(words):
    words = words.split(" ")
    return (words)


# print(long(txt))
def anal(lIST):
    y = ""
    x = ""
    for i in lIST:
        if len(i) > len(x):
            x = i
            y = i
        # print(i + " " + x)
        else:
            continue
        # print(y + " y changed")
    return (y)


print(anal(long(txt)))