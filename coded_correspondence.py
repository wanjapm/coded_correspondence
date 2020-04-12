
offset = 10

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
original_message = "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"
#original_message = "We are in lockdown!"
#message="Wu qhu yd besatemd!"

def decoder(message, offset):
    #declare variables
    alphabet =  [] 
    alphabet_number = list(range(26))
    alphabet =  [chr(x) for x in range(ord('a'), ord('z') + 1)] 

    message_as_list = message.split()
    decoded_message=""
    start_index = 0

    def decode_xar(xar):
        if alphabet.index(xar) + offset < len(alphabet):
            return alphabet.index(xar) + offset
        else:
            return alphabet.index(xar) - (len(alphabet) - offset)

    for word in message_as_list:
        new_word = ""
        for xar in word:
            if xar not in alphabet:
                new_word+=xar
            else:
                new_word += alphabet[decode_xar(xar)]

        if start_index == 0 :
            decoded_message += message[:message.find(word)+len(word)].replace(word,new_word)
            start_index = message.find(word)+len(word)
        else:
            decoded_message += message[start_index:message.find(word,start_index)+len(word)].replace(word,new_word)
            start_index = message.find(word,start_index)+len(word)

    return decoded_message

def coder(message, offset):
     #declare variables
    alphabet =  [] 
    alphabet_number = list(range(26))
    alphabet =  [chr(x) for x in range(ord('a'), ord('z') + 1)] 

    message_as_list = message.split()
    coded_message=""
    start_index = 0

    def code_xar(xar):
        if alphabet.index(xar) - offset < 0:
            return alphabet.index(xar) + (len(alphabet) - offset)
        else:
            return alphabet.index(xar) - offset

    for word in message_as_list:
        new_word = ""
        for xar in word:
            if xar not in alphabet:
                new_word+=xar
            else:
                #new_word += alphabet[alphabet.index(xar)-(len(alphabet)-offset)]
                new_word += alphabet[code_xar(xar)]
        #print (new_word)
        if start_index == 0 :
            coded_message += message[:message.find(word)+len(word)].replace(word,new_word)
            start_index = message.find(word)+len(word)
        else:
            coded_message += message[start_index:message.find(word,start_index)+len(word)].replace(word,new_word)
            start_index = message.find(word,start_index)+len(word)

    return coded_message

print(decoder(message,10))
print(coder(original_message,10))



        

