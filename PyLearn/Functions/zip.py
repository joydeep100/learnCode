first_zip = zip([1,2,3], [4,5,6])

lz = list(first_zip)
print(lz) #[(1, 4), (2, 5), (3, 6)]

for l,r in lz:
    print(l, r)

'''
1 4
2 5
3 6
'''