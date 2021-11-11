from random import shuffle
import copy

symbols = [chr(i) for i in range(256)]

class Rotor:
    def __init__(self):
        self.__values = symbols.copy()
        self.__countShift = 0


    def getValue(self, index):
        return self.__values[index]


    def getIndex(self, value):
        return self.__values.index(value)


    def shift(self):
        self.__values = self.__values[-1:] + self.__values[:-1]
        self.__countShift += 1


    def getCountShift(self):
        return self.__countShift


class Reflector:
    def __init__(self):
        self.__values = symbols.copy()
        shuffle(self.__values)

    def getReflectValue(self, value):
        index = self.__values.index(value)
        reflection_index = index + 1 if index % 2 == 0 else index - 1
        return self.__values[reflection_index]


class Enigma:
    def __init__(self):
        self.__rotor1 = Rotor()
        self.__rotor2 = Rotor()
        self.__rotor3 = Rotor()

        self.__reflector = Reflector()

    def __encryptSymbol(self, index):
        i1 = self.__rotor1.getValue(index)

        i2 = self.__rotor2.getIndex(i1)

        i3 = self.__rotor3.getValue(i2)

        i4 = self.__reflector.getReflectValue(i3)

        i5 = self.__rotor3.getIndex(i4)

        i6 = self.__rotor2.getValue(i5)

        i7 = self.__rotor1.getIndex(i6)

        return i7

    def encrypt(self, message):
        encryptMessage = ''
        for symbol in message:
            index = self.__encryptSymbol(ord(symbol))
            encryptMessage+=chr(index)
            self.__rotor1.shift()
            if (self.__rotor1.getCountShift() % len(symbols) == 0):
                self.__rotor2.shift()
            if (self.__rotor2.getCountShift() % len(symbols) == 0):
                self.__rotor3.shift()
        return encryptMessage


def encrypt_file(inputFileName, outputFileName, enigma):
    with open(inputFileName, 'rb') as f:
        text = f.read()
        textFormat = ""
        for byte in text:
            textFormat += chr(byte)
        textEncrypt = enigma.encrypt(textFormat)
        byteTextEncrypt = b""
        for s in textEncrypt:
            byteTextEncrypt += bytes([ord(s)])
        with open(outputFileName, 'wb') as cf:
            cf.write(byteTextEncrypt)

enigma = Enigma()
enigmaOld = copy.deepcopy(enigma)

inputFile = input('Введите полное имя файла: ')
encrypt_file(inputFile, 'crypted_' + inputFile, enigma)
encrypt_file('crypted_' + inputFile, 'decrypted_crypted_' + inputFile, enigmaOld)