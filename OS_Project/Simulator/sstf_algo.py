
def sstf(disk_seq,head):
    current = head
    no_of_cylinders=0
    output_seq = [head]
    for i in range(len(disk_seq)):
        seek = [abs(j-current) for j in disk_seq]
        minimum = min(seek)
        index = seek.index(minimum)
        current = disk_seq[index]
        output_seq.append(disk_seq.pop(index))
        no_of_cylinders+=minimum
    
    output = [output_seq,no_of_cylinders]
    return output

# print(sstf([176, 79, 34, 60, 92, 11, 41, 114],50))