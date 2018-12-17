#!/usr/bin/python

# Created by Wampu$Ka+
# 
# Script created to generate a wordlist to use to brute force "Matrix: 1" on Vulnhub by Ajay Verma:
# https://www.vulnhub.com/entry/matrix-1,259/
#
# No real PoC for this just make it executable and run it:
#
#$ chmod +x k1ll0rwl.py
#$ ./k1ll0rwl.py
#
# Final output file should be called "k1ll0r_wordlist.txt", you can then use this with a bruteforce
# tool such as ncrack, medusa or hydra


# output numbers 01-99 into a number.txt file
def num1_99():

    number = [0,0]


    def num_list_to_string(num_list):
      return str(num_list[0]) + str(num_list[1])


    outfile = open("number.txt", "w")
    outfile.write(num_list_to_string(number) + "\n")

    while not number[0] == 10:
        while not number[1] == 9:
            number[1] = number[1] + 1
            outfile.write(num_list_to_string(number) + "\n")
        number[0] = number[0] + 1
        number[1] = 0
        outfile.write(num_list_to_string(number) + "\n")

# appends a combination of letters and numbers such as aa, b2, cC etc to number.txt
def combo():
    
    import itertools

    lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    all = []
    all = lower_a + upper_a + num

    outfile = open("number.txt", "w")
    
    for r in range(1, 3):
        for s in itertools.product(all, repeat=r):
             #print ''.join(s)
             outfile.write(''.join(s) + "\n")
             
             
# appends all hex combinations to number.txt
def hex_nums():
    outfile = open("number.txt", "w")
    for i in xrange(99):
        #print hex(i)[2:].zfill(2)
        outfile.write(hex(i)[2:].zfill(2) + "\n")

# removes all single letter characters lines 1-63 to only keep 2 digit combo
# in other words, this removed things such as "l, c, d, e" and kept "ll, cc, dd, ee"
def remove_extra_lines():
    import os
    lines = open('number.txt').readlines()
    open('numbers.txt', 'w').writelines(lines[62:])
    os.remove("number.txt")

# adds the first part of the password "k11l0r" and puts it in front of the 2 digit combinations from 
# previous functions
def add_k1ll0r():
    import os
    appendname='k1ll0r'
    names=open("numbers.txt", 'r')
    updatedLetters=open("k1ll0r_wordlist.txt", 'a')
    for name in names:
      updatedLetters.write(appendname + name.rstrip() + '\n')
    updatedLetters.close()
    os.remove("numbers.txt")

# main() of the program: calls all functions
hex_nums()
num1_99()
combo()
remove_extra_lines()
add_k1ll0r()

# EOF
