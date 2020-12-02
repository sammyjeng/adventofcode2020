#!/usr/bin/python3
import fileinput

data = [ x.strip().split(':')  for x in  fileinput.input() ]

#print(data)
#data = [[1,3,'a','abcde'],
#[1,3,'b','cdefg'],
#[2,9,'c', 'ccccccccc']]
fd = {}
def part1():
    valid= 0
    invalid = 0
    for lis in data:
        fd['min'] = int(lis[0])
        fd['max'] = int(lis[1])
        fd['char'] = lis[-2]
        fd['pass'] = lis[-1]
        cnt = int(fd['pass'].count(fd['char']))
        if fd['char'] in fd['pass'] and  cnt <= int(fd['max']) and cnt >= int(fd['min']):
            valid +=1
        else:
            invalid +=1
    return valid
    
def part2(): 
    valid= 0
    invalid = 0
    for lis in data:
        pos1 = int(lis[0])
        pos2 = int(lis[1])
        char = fd['char'] = lis[-2]
        pas = lis[-1]
        # Be careful; Toboggan Corporate Policies have no concept of "index zero"!
        if char == pas[pos1-1] and char != pas[pos2-1] or char != pas[pos1-1] and char == pas[pos2-1]:
            valid +=1
        else:
            invalid +=1
        #print(char,pos1,pos2,pas)
    return valid

print('part1:',part1())
print('part2:',part2())

