f = open('links2022.txt', 'r')
flist = f.readlines()
farr = []
for i in range(len(flist)-1):
    if 'gist.github' in flist[i]:
        farr.append(flist[i][:-1])
# last item when using readlines does not have newline character
farr.append(flist[len(flist) - 1])
