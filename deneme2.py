

def deneme():
    serialDL_f = open("serialDL.txt","r")
    serialWL_f = open("serialWL.txt","r")
    serialDL = serialDL_f.read()
    serialWL = serialWL_f.read()

    if(serialDL == "1" and serialWL == "1"):
        return "ok"

    
print(deneme())
