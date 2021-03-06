
offset = 10

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
original_message = "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"
#original_message = "We are in lockdown!"
message="vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

def decoder(message, offset):
    #declare variables
    alphabet =  [] 
    #alphabet_number = list(range(26))
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
    #alphabet_number = list(range(26))
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

def vigenere_coder(message,keyword):
    # generate the keyword phrase
    alphabet =  [] 
    alphabet =  [chr(x) for x in range(ord('a'), ord('z') + 1)] 
    keyword_phrase=""
    coded_message=""
    ctr=0
    for word in message:
        for xar in word:
            if xar not in alphabet:
                keyword_phrase+=xar
            else:
                keyword_phrase+=keyword[ctr%len(keyword)]
                ctr+=1
    #print(keyword_phrase)
    ctr=0
    while ctr < len(message):
        if message[ctr] not in alphabet:
            coded_message+=message[ctr]
        else:
            place_value = alphabet.index(message[ctr]) + alphabet.index(keyword_phrase[ctr])
            if place_value < 26:
                coded_message+=alphabet[place_value]
            else:
                coded_message+=alphabet[place_value-len(alphabet)]

        ctr+=1
    return coded_message

def vigenere_decoder(message,keyword):
    # generate the keyword phrase
    alphabet =  [] 
    alphabet =  [chr(x) for x in range(ord('a'), ord('z') + 1)] 
    keyword_phrase=""
    coded_message=""
    ctr=0
    for word in message:
        for xar in word:
            if xar not in alphabet:
                keyword_phrase+=xar
            else:
                keyword_phrase+=keyword[ctr%len(keyword)]
                ctr+=1
    #print(keyword_phrase)
    ctr=0
    while ctr < len(message):
        if message[ctr] not in alphabet:
            coded_message+=message[ctr]
        else:
            place_value = alphabet.index(message[ctr]) - alphabet.index(keyword_phrase[ctr])
            if place_value < 0:
                coded_message+=alphabet[place_value+len(alphabet)]
            else:
                coded_message+=alphabet[place_value]

        ctr+=1
    return coded_message

                



# Test area
# for i in range(0,26):
    #print("Offset: {}".format(i)+decoder(message,i))
#print(decoder(message,offset))
#print(coder(original_message,offset))
message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message,keyword))
print(vigenere_coder(vigenere_decoder(message,keyword),keyword))



        

