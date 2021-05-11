import glob

breaktest=0

filmsAll = []
filmsWithPosters = []
filmsWithoutPosters = []

posterPath = ""

folderString = "/Volumes/video/Biblioteca_2019_01_17/Movies/Doc*"
posterString = "/Volumes/video/Biblioteca_2019_01_17/Movies/Doc*/poster.*"

print('Start\n')

print("filmsAll:")

for folderName in glob.glob(folderString) :
    breaktest = breaktest+1
    if breaktest>10: break
    print(folderName)
    filmsAll.append(folderName)

breaktest=0

print("\nfilmsWithPosters:")

for posterName in glob.glob(posterString) :
    breaktest = breaktest+1
    if breaktest>10: break
    posterPath = "/"
    posterPath += posterName.strip("/poster.jpg")
    print(posterPath)
    filmsWithPosters.append(posterPath)

breaktest=0

filmsWithoutPosters = list(set(filmsAll).difference(filmsWithPosters))

# print("\nfilmsAll")
# for i in filmsAll :
#     print(i)

# print("\nfilmsWithPosters")
# for i in filmsWithPosters :
#     print(i)

print("\nfilmsWithoutPosters")
for i in filmsWithoutPosters :
    print(i)

print('End')
