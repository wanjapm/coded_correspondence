
offset = 10

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
original_message = "nke znkxk! znoy oy gt kdgsvrk ul g igkygx iovnkx. ckxk eua ghrk zu jkiujk oz? o nuvk yu! yktj sk g skyygmk hgiq cozn znk ygsk ullykz!"
original_message = "We are in lockdown!"

def decoder(message, offset):
    #declare variables
    alphabet =  [] 
    alphabet_number = list(range(26))
    alphabet =  [chr(x) for x in range(ord('a'), ord('z') + 1)] 

    message_as_list = message.split()
    decoded_message=""
    start_index = 0

    for word in message_as_list:
        new_word = ""
        for xar in word:
            if xar not in alphabet:
                new_word+=xar
            else:
                new_word += alphabet[alphabet.index(xar)-offset]
        #print (new_word)
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

    for word in message_as_list:
        new_word = ""
        for xar in word:
            if xar not in alphabet:
                new_word+=xar
            else:
                new_word += alphabet[alphabet.index(xar)-(len(alphabet)-offset)]
        #print (new_word)
        if start_index == 0 :
            coded_message += message[:message.find(word)+len(word)].replace(word,new_word)
            start_index = message.find(word)+len(word)
        else:
            coded_message += message[start_index:message.find(word,start_index)+len(word)].replace(word,new_word)
            start_index = message.find(word,start_index)+len(word)

    return coded_message

print(decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",9))
#print(coder(original_message,10))



        

