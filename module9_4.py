
def all_variants(text):
    l = len(text)
    for i in range(1,l+1):
        for start in range(0,l+1-i):
            for end in range(start + i,  start + 1 + i):
#                print('i = ',i,'start = ',start,'end = ',end)
                yield text[start:end]


a = all_variants("abcdef")
for i in a:
    print(i)





































