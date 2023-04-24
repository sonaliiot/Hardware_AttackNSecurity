## Considering the size of the coefficient (omitting the 0 at postion 0) is same as the size of seed 
## Code mentioned below produces correct sequences for seed size = coeff size = 3. Verified for seed size 3
## First of all, run seedn.py to generate required sized seed or coefficient sequences

def seedread(file_path,seed_size):
    with open(file_path, 'r') as f1:
        l2 = []
        l3 = []
      
        l1 = f1.readline()
        i=0
        j=0
        var = 1
        for s in range(seed_size*len(l1)):
            if j < pow(2,seed_size)-1:
                
                if i <seed_size*var:
                    l2.append(int(l1[i]))
                    i=i+1
                else:
                    l3.append(l2)
                    j=j+1
                    var = var+1
                    l2 = []

    return l3    
   

def seqtrace(file_path,tracefilepath,seq_length,seed_size,coeff1):
    l3 = seedread(file_path,seed_size)
    for li in range(len(l3)):
        #myseq = [1, 1, 0] #initial seed
        myseq = l3[li]
        #coeff = [1,1,1]
        coeff = coeff1
        start=0
        lfsr_len = len(coeff)-1
        #print(myseq)
        #seq_length = 10   #change this to the value for how many sequence values you want after seed

        for i in range(seq_length):
            nextbit=0
            for j in range(0, lfsr_len):
                nextbit^=(coeff[j+1]*myseq[start+lfsr_len-j-1])
            start+=1
            myseq.append(nextbit)
        with open(tracefilepath, 'a') as f2:
            seq = ''
            seq1=''    
            for count in range(len(myseq)):
                
                seq = seq + str(myseq[count])
            
            seq1 = seq + '\n'
            f2.write(seq1)
        f2.close()
    

def tracegen(file_path,seed_size,seq_length,tracefilepath):
    c = seedread(file_path,seed_size)

    for ci in range(len(c)):
        coeff1 = c[ci]
        coeff1.insert(0,0)
        #print(coeff1)
    
        seqtrace(file_path,tracefilepath,seq_length,seed_size,coeff1)


tracegen('/home/sonali/Downloads/Papers/Power Analysis Attacks/BK_Algo_py_scripts/seed3.txt',3,10,'/home/sonali/Downloads/Papers/Power Analysis Attacks/BK_Algo_py_scripts/seqseed3.txt')
