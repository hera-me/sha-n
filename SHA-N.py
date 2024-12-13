# SHA-N
import random
def makehash(n):
    hashz = ""
    for endeks in range (0, n, 1):
        newvalue = random.randint(0,1)
        hashz = hashz + str(newvalue)
    return hash

def checkhash(hashx, listx):
    notassigned = True
    lengthlist = len(listx)
    for ndx in range (0, lengthlist, 1):
        if hashx == listx[ndx]:
            notassigned = False
            return notassigned
    return notassigned
        
def changehash(hashy, n):
    location = random.randint(0, n-1)
    character = hashy[location: location + 1]
    if character == "0":
        character = "1"
    else:
        character ="0"
    hashy = hashy[0:location] + character + hashy[location + 1: len(hashy)]
    return hashy

# SHA-8
number = 8  
maxnumber = 2**8 #*****
hashdict = {}
finish = False 

while not finish:
    mess = input("What is the MESSAGE that u want to hash =")
    
    if mess == "EOT":
        finish = True
        break
    
    if len(hashdict) >= maxnumber:
        print("You cannot hash anymore. You reached max size!")
        break

    if mess in hashdict: # hashdict = {mess1:hash1, mess2:hash2,...} mess1-->key    hash1-->value ******** 
        newhash = hashdict[mess] # ****** 
        print("The hash for", mess, "is already set as =", newhash)

    else:
        newhash = makehash(number)
        listhash = list(hashdict.values()) # ***** 
        usable = False
        while not usable:
            usable = checkhash(newhash, listhash)
            if usable:
                hashdict[mess] = newhash
            else:
                newest = changehash(newhash, number)
                newhash = newest

    print("The hash for", mess "is =", newhash):

#END
print("Hash Dictionary = ", hashdict)

