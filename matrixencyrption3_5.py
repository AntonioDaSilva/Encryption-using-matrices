#FOR USE THIS PROGRAM USE MUST CREATE A FILE CALLED ""encrypt.txt"
#WHICH MUST CONTAIN THE NUMLIST WHICH WILL BE ENCRYPTED AFTER THE PROGRAM 
#EXECUTED! AFTER THEN EXECUTE THE PROGRAM AND THATS ALL..

#DO NOT FORGET THAT IT CAN ONLY ENCRYPT TWO NINE
#DIGIT NUMBERS SUCH AS "678235410 82385012"
#IF YOUR DATA HAS LOWER DIGITS ; LET THE OTHER DIGITS ZERO , THEY WONT CHANGE
#IF YOUR DATA HAS HIGHER DIGITS ; ENCRYPT THEM SEPERATELY 

from numpy import matrix
from numpy import linalg

#import the libraries for maths stuff

def readthefile():
    a=input("Enter a file name: ")
    try:
        f=open(a)
        for c in f:
            c=c.rstrip()
            return c
    except:
        return 0

#function to read the text in the file

def splitthedata():
    n=readthefile().split(" ")
    return n

#function that splits the digits

def returnmatrices_1_1():
    q=splitthedata()
    str1=q[0]
    n=0
    list1=[]
    for i in str1:
        list1.append(str1[n])
        n+=1
    return list1

def returnmatrices_2_1():
    q=splitthedata()
    str2=q[2]
    n=0
    list2=[]
    for i in str2:
        list1.append(str2[n])
        n+=1
    return list2

def returnmatrices_1_2():
    a=returnmatrices_1_1()
    n=0
    first_matrix=matrix( [ [a[n],a[n+1],a[n+2]] , [a[n+3],a[n+4],a[n+5]] , [a[n+6],a[n+7],a[n+8]] ] )
    return first_matrix

def returnmatrices_2_2():
    a=returnmatrices_2_1()
    n=0
    second_matrix=matrix( [ [a[n],a[n+1],a[n+2]] , [a[n+3],a[n+4],a[n+5]] , [a[n+6],a[n+7],a[n+8]] ] )
    return second_matrix

#functions that creates new matrices one by one

def take_transpoze_1():
    x=returnmatrices_1_2()
    transpoze1=x.T
    return transpoze1

def take_transpoze_2():
    x=returnmatrices_2_2()
    transpoze2=x.T
    return transpoze2

#functions that starts the encyrpting by taking transpoze.

def encyrpt_1():
    q=take_transpoze_1()
    a=[]
    n=0
    for i in range(9):
        a.append(q.item(n))
        n+=1
    encyrptedfile1_1=""
    for i in a:
        encyrptedfile1_1=encyrptedfile1_1+str(i)
    return encyrptedfile1_1


def encyrpt_2():
    q=take_transpoze_1()
    a=[]
    n=0
    for i in range(9):
        a.append(q.item(n))
        n+=1
    encyrptedfile2_2=""
    for i in a:
        encyrptedfile2_2=encyrptedfile2_2+str(i)
    return encyrptedfile2_2

#two functions returns strings (encypted ones)

def sumencyrptedsup():
    a=((encyrpt_2())+(encyrpt_1()))
    return a

def filecreate_write():
    encyrptedfile = open("secret.txt", "w")
    encyrptedfile.write(sumencyrptedsup())
    encyrptedfile.close()

#function that creates a new file and writes the encrypted string on it

def main():
    filecreate_write()


if __name__ == "__main__":
    main()

        
    





