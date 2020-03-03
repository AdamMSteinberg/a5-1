from bitstring import BitArray,Bits
if __name__=="__main__":
    x=BitArray('0b1010101010101010101')
    y=BitArray('0b1100110011001100110011')
    z=BitArray('0b11100001111000011110000')

    ctr=0
    key=""
    while(ctr<8):
        ctr+=1
        
        if((x[8] and y[10]) or (x[8] and z[10]) or (y[10] and z[10])):
            if(x[8]):
                newbit=x[18]^x[17]^x[16]^x[13]
                x=x[0:-1]
                x.prepend(Bits(bool=newbit))
            if(y[10]):
                newbit=y[20]^y[21]
                y=y[0:-1]
                y.prepend(Bits(bool=newbit))
            if(z[10]):
                newbit=z[22]^z[21]^z[20]^z[7]
                z=z[0:-1]
                z.prepend(Bits(bool=newbit))
        else:
            if(not x[8]):
                newbit=x[18]^x[17]^x[16]^x[13]
                x=x[0:-1]
                x.prepend(Bits(bool=newbit))
            if(not y[10]):
                newbit=y[20]^y[21]
                y=y[0:-1]
                y.prepend(Bits(bool=newbit))
            if(not z[10]):
                newbit=z[22]^z[21]^z[20]^z[7]
                z=z[0:-1]
                z.prepend(Bits(bool=newbit))

        if(x[-1]^y[-1]^z[-1]):
            key+="1"
        else:
            key+="0"

    print(key)