# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:08:24 2026

@author: wiley
"""

#Favorite animal is cat
#length of arms 9inch
#length of legs 10inch
#number of eyes (2)
#Tail?(yes)
#is it furry (yes)

length_arm = int()
length_leg = int()
number_eyes = int()
tail = bool()
fur = bool()

print(length_arm)
print(length_leg)
print(number_eyes)
print(tail)
print(fur)

def main():
    length_arm = 9
    length_leg = 10
    number_eyes = 2
    tail = True
    fur = True
    print(f"The arm length is {length_arm}")
    print(f"The leg length is {length_leg}")
    print(f"It has {number_eyes} eyes")
    if tail == True:
        print("It has a tail")
    if fur == True:
        print("It has fur")
        
    if tail == False:
        print("It doesn't have a tail")
    if fur == False:
        print("It has no fur")
        
    if (length_arm == 9, length_leg == 10, number_eyes == 2, tail == True, fur == True):
        print("It is a cat")

if __name__ =='__main__':
    main()
