#!/usr/bin/python3
import fileinput

# 1.py < input.txt
data = [int(line) for line in fileinput.input()]

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if i !=j and data[i] + data[j]  == 2020:
            # part 1
            print(data[i]* data[j])
        for k in range(j+2, len(data)):
            if j != k  and data[i] + data[j] +data[k] == 2020:
                # part 2
                print(data[i]*data[j]*data[k])
