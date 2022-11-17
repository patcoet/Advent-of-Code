from collections import deque
from functools import reduce
import operator

class mdeque(deque):
    def poplefts(self, num):
        res = mdeque()
        for _ in range(num):
            res.append(self.popleft())
        return res
    
    def __int__(self):
        tot = 0
        mul = 1
        for i, d in enumerate(reversed(self)):
            tot += d * mul
            mul *= 2
        return tot

binary = mdeque()

with open('input') as file:
    for char in file.readline().strip():
        if char.isdigit():
            binary.extend([int(x) for x in f'{bin(int(char))[2:]:0>4}'])
        else:
            binary.extend([int(x) for x in bin(ord(char) - 55)[2:]])

def read_packet(packet):
    p_ver = int(packet.poplefts(3))
    p_type = int(packet.poplefts(3))
    subs = []

    if p_type == 4:
        subs.append((p_type, read_literal(packet)))
    else:
        subs.append((p_type, read_other(packet)))

    return subs

def read_literal(packet):
    val = mdeque()

    for _ in range(0, len(packet), 5):
        prefix = int(packet.poplefts(1))
        val += packet.poplefts(4)
        if prefix == 0:
            break

    return int(val)

def read_other(packet):
    len_type = int(packet.poplefts(1))
    subs = []
    
    if len_type == 0:
        subs_len = int(packet.poplefts(15))
        subs = packet.poplefts(subs_len)
        while len(subs) > 4:
            subs.append(read_packet(subs))
    else:
        subs_num = int(packet.poplefts(11))
        for _ in range(subs_num):
            subs.append(read_packet(packet))

    return subs

intermediate = read_packet(binary)

def tf(tup):
    code, subs = tup[0]
    match code:
        case 0:
            return sum(map(tf, subs))
        case 1:
            return reduce(operator.mul, map(tf, subs))
        case 2:
            return min(map(tf, subs))
        case 3:
            return max(map(tf, subs))
        case 4:
            return subs
        case 5:
            return (tf(subs[0]) > tf(subs[1])) * 1
        case 6:
            return (tf(subs[0]) < tf(subs[1])) * 1
        case 7:
            return (tf(subs[0]) == tf(subs[1])) * 1

print(tf(intermediate))
