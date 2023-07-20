lop = {0: 'boy', 1:'girl', 2:'word', 3:'ipi'}

def unshift(index, obbj):
        for i in range(index, 3):
            obbj[i] = obbj[i + 1]
        del obbj[3]
        print(obbj)

unshift(2,lop)


