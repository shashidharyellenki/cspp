# import os

# f = open('./www/one.png', 'rb')
# newfile = open('testing.png','wb')
# for line in f:
#     newfile.write(line)

nums=[1,1,2]
i=1
while (i<len(nums)):
    if nums[i-1]==nums[i]:
        del nums[i]
        i-=1
    i+=1
print(nums)

# print(len(list(set(nums))))