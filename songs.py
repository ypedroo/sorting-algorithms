
if __name__ == "__main__":
    songs = [9, 5, 4, 3, 2, 5, 2, 3 , 1]

    index = songs.index(5)

    print(index)

    songs.sort()
    songs.reverse()

    print(songs)
    max = 10
    cds = []

    while (len(songs) > 0):
        cd = []

        index = 0
        while (index < len(songs)):
            song = songs[index]
            print(index, song)
            if (sum(cd) + song <= max):
                cd.append(song)
                del songs[index]
                index = index - 1
            
            index = index + 1
        
        print("novo cd:", cd)
        cds.append(cd)

    
    print(cds) 