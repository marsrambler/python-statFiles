'''
@author: Yiz56865
'''

import os
from RtpReader import getSpecValuesFromFile

def listFiles(dirname):
    if os.path.isdir(dirname) == False:
        raise TypeError('invalid dir name')
    files = []
    for x in os.listdir(dirname):
        if (os.path.splitext(x)[1] == ".xml"):
            files.append(x)
    return files


if __name__ == "__main__":
        
    wfile = open("Z:\\shared\\result-200-1448-003.csv", "w")
    
    files = listFiles("Z:\\shared\\histo_result.001");
    for x in files:
        #values, maps = RtpReader.getSpecValuesFromFile("Z:\\shared\\histo_result.001\\" + x)
        values, maps = getSpecValuesFromFile("Z:\\shared\\histo_result.001\\" + x)
        line = str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[6]) + "," + str(values[8]) + "\n"
        wfile.write(line)
    wfile.close()