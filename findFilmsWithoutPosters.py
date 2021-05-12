import glob

breaktest=0

filmsAll = []
filmsWithPosters = []
filmsWithoutPosters = []
filmsWithLongNamePosters = []

posterPath = ""

folderString = "/Volumes/video/Biblioteca_2019_01_17/Movies/Doc*"
posterString = folderString + "/poster.*"
posterLongNameString = folderString + "/*-poster.*"

print('Start\n')

print("filmsAll:")

for filmName in glob.glob(folderString) :
    breaktest = breaktest+1
    if breaktest>50: break
    print(filmName)
    filmsAll.append(filmName)

breaktest=0

print("\nfilmsWithPosters:")

for filmName in glob.glob(posterString) :
    breaktest = breaktest+1
    if breaktest>50: break
    if filmName.endswith("/poster.jpg") :
        posterPath = filmName[:-11]
    print(posterPath)
    # print(filmName)
    filmsWithPosters.append(posterPath)

breaktest=0

print("\nfilmsWithLongNamePosters:")

for filmName in glob.glob(posterLongNameString) :
    breaktest = breaktest+1
    if breaktest>50: break
    if filmName.endswith("-poster.jpg"):
        # print("Yep!") 
        posterPath = filmName.rpartition('/') [0]
    # print(filmName)
    print(posterPath)
    filmsWithLongNamePosters.append(posterPath)

breaktest=0

filmsWithoutPosters = list(set(filmsAll).difference(filmsWithPosters).difference(filmsWithLongNamePosters))

#print("\nfilmsAll LIST")
#for i in filmsAll :
#    print(i)

#print("\nfilmsWithPosters LIST")
#for i in filmsWithPosters :
#    print(i)

#print("\nfilmsWithLongNamePosters LIST")
#for i in filmsWithLongNamePosters :
#    print(i)

print("\nfilmsWithoutPosters LIST")
for i in filmsWithoutPosters :
    print(i)

print('End')
