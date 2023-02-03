class BitVector:
    def __init__(self, size: int):
        self.table = [0] * (size // 32 + 1)

    def set_bit(self, where):
        index = where // 32 
        position = where % 32
        self.table[index] |= (1 << position)
        return self.table[::-1]

    def reset_bit(self, where):
        index = where // 32 
        position = where % 32 
        self.table[index] &= (0)
        return self.table[::-1]

bv = BitVector(200)
print(bv.table)
bv.set_bit(56)
print(bv.table)
bv.set_bit(99)
print(bv.table)
bv.reset_bit(56)
print(bv.table)

