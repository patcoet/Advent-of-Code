from collections import deque

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
    versions.append(p_ver)

    if p_type == 4:
        read_literal(packet)
    else:
        read_other(packet)

def read_literal(packet):
    for _ in range(0, len(packet), 5):
        prefix = int(packet.poplefts(1))
        packet.poplefts(4)
        if prefix == 0:
            break

def read_other(packet):
    len_type = int(packet.poplefts(1))
    if len_type == 0:
        subs_len = int(packet.poplefts(15))
        subs = packet.poplefts(subs_len)
        while len(subs) > 0:
            read_packet(subs)
    else:
        subs_num = int(packet.poplefts(11))
        for _ in range(subs_num):
            read_packet(packet)

versions = []
read_packet(binary)
print(sum(versions))
