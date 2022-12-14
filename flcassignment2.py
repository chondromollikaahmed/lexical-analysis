# with open ("input.c","r") as file:
#     for line in file:
#         print(line)



def printString(nstr):
    for word in nstr.split():
        print(word)





import re
delimator={";",",","'","+","-","*","/","%","(",")","{","}","[","]","=","<",">"}
keywords={
    "auto", 
    "break", 
    "case", 
    "char", 
    "continue", 
    "do", 
    "default", 
    "const", 
    "double", 
    "else", 
    "enum", 
    "extern", 
    "for", 
    "if", 
    "goto", 
    "float", 
    "int", 
    "long", 
    "register", 
    "return", 
    "signed", 
    "static", 
    "sizeof", 
    "short", 
    "struct", 
    "switch", 
    "typedef", 
    "union", 
    "void", 
    "while", 
    "volatile", 
    "unsigned"
}
symbol={'<  =','>  =','+  =','-  =','*  =','/  =','=  ='}
separetor ={".",";","'","(",")","{","}","[","]",","}
operator={"+","-","*","/","%","=","<=",">="}

newString = open ("input.c","r").read()

for symbols in symbol:
    if symbols in newString:
           newString=newString.replace(symbols, symbols.replace(" ","") ) 
        




for delim in delimator:
    if delim in newString:
        newString=newString.replace(delim," "+delim+" ") 

print(newString)


for symbols in symbol:
    if symbols in newString:
            newString=newString.replace(symbols, symbols.replace(" ","") ) 




printString(newString)



for word in newString.split():
    if word in keywords:
      print("[kw "+ word +"]"+"\n")
    elif re.match("[_a-zA-Z][_a-zA-Z0-9]*",word):
         print("[id "+ word +"]"+"\n")
    elif re.match("^(?=.)(([0-9]*)(\.([0-9]+))?)$",word):
         print("[num "+ word +"]"+"\n")
    elif word in separetor:
        print("[sep "+word+" ]"+"\n")
    elif word in operator:
        print("[ope "+word+" ]"+"\n")
 

    else:
        print("[unkn "+ word +"]"+"\n")

