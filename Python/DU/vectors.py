class MyVector:
    def __init__(self, array):
        self.Vector = array
        pass

    def get_vector(self):
        return self.Vector
    
    def __mul__(self, other):
        self.total = 0
        self.List = []
        for x in range(len(self.Vector)):
            self.List.append(self.Vector[x]*other.Vector[x])
        for x in range(len(self.List)):
            self.total += self.List[x] 
        return self.total
    
    def __add__(self, other):
        self.new_vector = []
        for x in range(len(self.Vector)):
            self.new_vector.append(self.Vector[x] + other.Vector[x])
        return MyVector(self.new_vector)
    
    def norm(self):
        self.size = 0
        for x in range(len(self.Vector)):
            self.size += self.Vector[x] ** 2
        self.si = self.size ** 0.5
        return self.si

if __name__ == "__main__":
    vec1 = MyVector([1,2,3,10,12])
    vec2 = MyVector([3,2,1,5,20])
    vec3 = MyVector([4,3])
    print(vec1.get_vector())
    dot_product = vec1 * vec2
    print(dot_product)
    add = vec1 + vec2
    print(add.get_vector())
    print(vec3.norm())