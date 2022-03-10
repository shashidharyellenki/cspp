import os
def recusrion(path1, flag):
    print("testing",path1)
    files = os.listdir(path1)
    print("***",files)
    for file in files:
        if os.path.isfile(file):
            flag=True
        else:
            flag=False
    if flag:
        print(files)
        return
    else:
        for file in files:
            if os.path.isfile(file):
                print(file)
            else:
                path=os.path.join(path1, file)

                # print("+-+-+-", path)
                recusrion(path, False)
root1="E:\msit\computer systems\project1B\www"
path = os.getcwd()
files = os.listdir(path)
for file in files:
    if os.path.isfile(file):
        print("This is file ",file)
        pass
    else:
        # print("This is a folder ", file)
        recpath = os.path.join(os.getcwd(), file)
        recusrion(recpath, False)

# f = os.listdir(root1)
# print(f)
# for file in f:
#     print("fileswww", os.path.isfile(file))
