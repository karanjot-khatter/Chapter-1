#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     03/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("Hello, World!")
    print(2+3)
    print("2+3 = ", 2+3)

main()

#Parameters used in function to define something specifically.
#E.g. greet(“John”) – shows customized greeting
def greet(person):
    print("Hello", person)
    print("How are you?")

greet("karanjot")