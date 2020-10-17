#! /usr/bin/python3
a,t,c,g = 0,0,0,0
cnt = 0

with open('sam_seq.txt') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith('>'):
            continue
        a += line.count('A')
        t += line.count('T')
        c += line.count('C')
        g += line.count('G')
    
print("A :",a)
print("C :",c)
print("T :",t)
print("G :",g)



