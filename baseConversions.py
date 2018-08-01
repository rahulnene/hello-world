from time import clock as time

def numberValidInBase(input,base):
    input_string = str(input)
    digitRep = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8 9:9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":33, "G":33, "H":33, "I":33, "J":33, "K":33, "L":33, "M":33, "N":33, "O":33, "P":33, "Q":26, "R":27, "S":28, "T":29, "U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35, }
    for digit in input_string:
        if int(digit) >= base:
            print(input," cannot exist in this base (" ,base, "), try agian.")
            return False
    return True

def baseChangefromDecimal(input,base):
    outputArray = []
    remainder = input
    iterator = 0
    digitRep = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6: 6, 7:7, 8:8, 9:9, 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", 16:"G", 17:"H", 18:"I", 19:"J", 20:"K", 21:"L", 22:"M", 23:"N", 24:"O", 25:"P", 26:"Q", 27:"R", 28:"S", 29:"T", 30:"U", 31:"V", 32:"W", 33:"X", 34:"Y", 35:"Z"}
    outString = ""
    while input >= 1:
        remainder = input%base
        outputArray.append(digitRep[remainder])
        input //= base
    outputArray.reverse()
    for digit in outputArray:
        outString += str(digit)
    return outString

def baseChangetoDecimal(input,base):
    input_string = str(input)
    if (numberValidInBase(input, base)):
        iterator = 0
        sum = 0
        input_string = input_string[::-1]
        for digit in input_string:
            sum += int(digit) * (base**iterator)
            iterator += 1
        return sum

def convertBase(num, oldBase, newBase):
    return baseChangefromDecimal(baseChangetoDecimal(num,oldBase),newBase)

startTime = time()
print(convertBase(1122847592384756978246268,10,26))
print((time()-startTime) * 1000000, "microseconds taken to process")