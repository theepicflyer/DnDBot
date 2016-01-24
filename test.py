sdasd= "A B C D E"

def parseInput(words, no):
    words = words.split()
    a = len(words) - no
    print(words)
    print(str(a))

    oup = words[1]
    for i in range(2, 2 + a):
        #oup += " "
        oup += words[i]
    outt = []
    outt.append(words[0])
    outt[0] = words[0]
    outt[1] = oup
    for i in range(0, no):
        outt[i] = words[a+2]
    print(oup)

parseInput(sdasd, 2)

parseInput(sdasd, 5)