myseq = [0, 1, 0,0] #initial seed
coeff = [0,0,0,1,1] # extra element at index 0. Take from c1; c0=0 is dummy to take coeff indices from c1; coeff = [0,0,0,1,1] represents (x^4 + x + 1) why?
start=0
lfsr_len = len(coeff)-1
#print(myseq)
seq_length = 10   #change this to the value for how many sequence values you want after seed

for i in range(seq_length):
    nextbit=0
    for j in range(0, lfsr_len):
        nextbit^=(coeff[j+1]*myseq[start+lfsr_len-j-1])
    start+=1
    myseq.append(nextbit)

print(myseq)
