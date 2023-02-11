
myseq = [1, 1, 0] #initial seed
coeff = [1,1,1]
start=0
lfsr_len = len(coeff)
#print(myseq)
seq_length = 10   #change this to the value for how many sequence values you want after seed

for i in range(seq_length):
    nextbit=0
    for j in range(start, start+lfsr_len):
        nextbit^=(coeff[j-start]*myseq[j])
    start+=1
    myseq.append(nextbit)

print(myseq)
