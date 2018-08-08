from time import clock as time

def printTime():
    print("This process took",(time()-startTime) * 1000000, "microseconds to process.")

def numberValidInBase(input,base):
    input_string = str(input)
    digitRep = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20, "L":21, "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29, "U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35, }
    for digit in input_string:
        if int(digitRep[digit]) >= base:
            print(input,"cannot exist in given base (", base, "), try agian.")
            return False
    return True
    # return True

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
    digitRep = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20, "L":21, "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29, "U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35, }
    if (numberValidInBase(input, base)):
        iterator = 0
        sum = 0
        input_string = input_string[::-1]
        for digit in input_string:
            sum += digitRep[digit] * (base**iterator)
            iterator += 1
        return sum
    else:
        printTime()
        exit()

def convertBase(num, oldBase, newBase):
    return baseChangefromDecimal(baseChangetoDecimal(num,oldBase),newBase)

startTime = time()
print(convertBase("ABCDEF",25,10))
printTime()