'''

@author: Yiz56865
'''

#import FileProcessor
from FileProcessor import readSpecLine, getValue

def getSpecValuesFromFile(filename):
    gameCount = readSpecLine(filename, "Total_M")
    gameCount = getValue(gameCount);
    
    wagerCount = readSpecLine(filename, "Wager")
    wagerCount = getValue(wagerCount);
    
    basePay = readSpecLine(filename, "Pay_Lines")
    basePay = getValue(basePay)
    
    bonusPay = readSpecLine(filename, "Wheel_Slice_pay_W")
    bonusPay = getValue(bonusPay)
    
    payM = readSpecLine(filename, "Pay_M")
    payM = getValue(payM)
    
    payW = readSpecLine(filename, "Pay_W")
    payW = getValue(payW)
    
    sum0 = int(float(basePay)) + int(float(bonusPay))
    sum1 = int(float(payM)) + int(float(payW))
    if sum0 != sum1:
        raise ValueError('error value files')
    
    rtp = float(sum0) / float(wagerCount)
    rtp1 = format(rtp, '.3%')
    
    values = [int(float(gameCount)), int(float(wagerCount)), int(float(basePay)), int(float(bonusPay)), int(float(payM)), int(float(payW)), sum0, rtp, rtp1]
    maps = {"Total_M":      int(float(gameCount)),
            "Wager":        int(float(wagerCount)),
            "Pay_Lines":    int(float(basePay)),
            "Wheel_Slice_pay_W": int(float(bonusPay))}
    
    return values, maps
    
    
    
if __name__ == "__main__":
    values, maps = getSpecValuesFromFile("C:\\Disk-D\\Dev-works\\30Days\\day-3\\com\\jack\\abc.xml")
    print(maps)
    print(values)