import math
import random

class ComplexNumber:
    def __init__(self, real_in, complex_in):
        self.real = real_in
        self.complex = complex_in

    def __add__(self, other):
        self.real_new = self.real + other.real
        self.complex_new = self.complex + other.complex
        return ComplexNumber(self.real_new, self.complex_new)

    def __mul__(self, other):
        self.real_new = self.real * other.real - (self.complex * other.complex)
        self.complex_new = self.real * other.complex + self.complex * other.real
        return ComplexNumber(self.real_new, self.complex_new)
    
    def __sub__(self, other):
        self.real_new = self.real - other.real
        self.complex_new = self.complex - other.complex
        return ComplexNumber(self.real_new, self.complex_new)
    
    def __div__(self, other):
        if (other.real != 0 and other.complex !=0):
            self.real_new = self.real / other.real
            self.complex_new = self.complex / other.complex
        return ComplexNumber(self.real_new, self.complex_new)
    
    def __str__(self):
        return str(self.real) + " + " + str(self.complex) + "i"
    
    def __abs__(self):
        self.abs_i = math.sqrt(math.pow(self.real,2) + math.pow(self.complex,2))
        return self.abs_i

def find_max(in_list):
    max = 0
    array_idx = []
    array = in_list
    total = 0

    for x in range(len(array)):
        if (max < array[x]):
            array_idx = [x]
            max = array[x]
        elif (max == array[x]):
            array_idx.append(x)
    total = len(array_idx)
    return max, array_idx[0:x], total

def Generate_List(len):
    Atribute_list = []
    for x in range(len):
        Atribute_list.append(random.randint(1,100))
    return Atribute_list[0:len]

if __name__ == "__main__":
    lenght = 100
    atributes = Generate_List(lenght)
    max_val, positions, total = find_max(atributes)
    print(max_val, positions, total)
    i1 = ComplexNumber(5,-1)
    i2 = ComplexNumber(1,2)
    print(i1, abs(i1))
    i3 = i1 * i2
    print(i3)
    i3 = i1 - i2
    print(i3)