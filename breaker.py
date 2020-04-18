#!/bin/python3
#
# This program output in a file all possibilities for the text message
#

import sys

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

i = 0
def break_this(message):
    "Breaking..."
    broken = []
    for dec in range(0,26):
        one_text = ''
        for letter in message:
            try:
                if letter in big:
                    pos = big.index(letter)
                    i =  (pos - dec) % 26
                    one_text += big[i]
                elif letter in small:
                    pos = small.index(letter)
                    i =  (pos - dec) % 26
                    one_text += small[i]   
                else:
                    one_text += letter 
            except ValueError:
                one_text += l
        broken.append(one_text)
    return broken

def save_in_file(filename, broken):
    print("Saving...")
    f = open(filename, "w")
    num = 0
    for i in broken:
        f.write('KEY = ' + str(num) + '\n')
        f.write(i)
        f.write('\n-----\n')
        num += 1

def print_help():
    print("./breaker <string_to_bruteforce> <filename_to_store>")

def main():
    to_break = sys.argv[1]
    filename = sys.argv[2]
    if to_break and filename:
        broken = break_this(to_break)
        save_in_file(filename, broken)
        print("Results saved in : " + filename)
    else:
        print_help()


if __name__ == "__main__":
    main()
