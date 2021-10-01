# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 03:34:00 2021

@author: Manish Kumar Goswami
"""

def num_in_row(i, line, start, end):
    arr = [start]
    switch = False
    while True:
        if line != i or line != 0:
            if switch:
                new_arr= arr[-1] + 2*(i)
            else:
                new_arr = arr[-1] + 2*(line-i-1)
            switch = not switch
        else:
            new_arr = arr[-1] + 2*(line-1)

        if new_arr >= end:
            break
        else:
            arr.append(new_arr)
    return sorted(list(set(arr)))

def space_between(a, b):
    print(' '*(b-a), end="")

def main(line, end):
    for i in range(line):
        space_between(0, i)
        elements = num_in_row(i,line,i,end+1)
        for j in range(len(elements)):
            if len(str(elements[j])) > 1:
                inend = ""
            else :
                inend = " "
            print(elements[j]+1, end=inend)
            try:
                space_between(elements[j], elements[j+1])
            except:
                pass
        print()

if __name__ == "__main__":
    main(7,16)