'''
@author: Yiz56865
'''

def readSpecLine(fileName, specString):
    if not isinstance(fileName, str):
        raise TypeError('bad file name')
    if not isinstance(specString, str):
        raise TypeError('bad file name')    
    f = open(fileName)
    line = f.readline()
    while line:
        if line.find(specString) != -1:
            f.close()
            return line
        line = f.readline()
    f.close()
    raise TypeError('bad file') 
    
def getValue(roughString):
    if not isinstance(roughString, str):
        raise TypeError('bad rough string')
    idx0 = roughString.find(">")
    if idx0 == -1:
        raise ValueError('bad rough string')
    tmpStr0 = roughString[idx0+1:]
    idx1 = tmpStr0.find("<")
    if idx1 == -1:
        raise ValueError('bad rough string')
    tmpStr1 = tmpStr0[0:idx1]
    return tmpStr1  
    
if __name__ == "__main__":
    print("I am in");
    roughValue = readSpecLine("C:\\Disk-D\\Dev-works\\30Days\\day-3\\com\\jack\\abc.xml", "Total_W")
    print("result: " + roughValue)
    specValue = getValue(roughValue)
    print("spec: " + specValue)
    print(float("1.01E7"))