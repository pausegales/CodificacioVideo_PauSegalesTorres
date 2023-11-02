
#Function definition
def encode(message):
    #Initiating the storing string
    encoded_message = ""
    i = 0
 
    #Iterate over the given message
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        #Adding the count of the character and the character itself
        encoded_message=encoded_message+str(count)+ch
        i = j+1
    return encoded_message


# ---- 5 ----
#Provide different values for message and test your program
encoded_message1 = encode("··$$%%&&&&//%%&&&&$$$")
encoded_message2 = encode("abbggbbbbah33e")
encoded_message3 = encode("00010011110010100100010001000000011101101")
encoded_message4 = encode("aaabbbcccddd···^^^***")
print(encoded_message1)
print(encoded_message2)
print(encoded_message3)
print(encoded_message4)