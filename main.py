online = "ONLINE:"


def main():
    names = splitnames(find_latest_line())
    print(names)
    




def find_latest_line():
    file = open('C:/Users/ethan/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log', 'r')
    for line in reversed(file.readlines()):
        if online in line:
            print(line)
            return line 
    else:
        print("No entries found")



def splitnames(line):

    index = line.find(online)
    line = line[index + len(online):]
    names = line.strip().split(", ")
    return names



if __name__ == "__main__":
    main()