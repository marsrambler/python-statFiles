'''
Created on Jun 15, 2018

@author: yiz
'''


all_rands = [9943,7885]

if __name__ == "__main__":
#     val = 5
#     b_val = bin(val)
#     b_val_trim = b_val[2:]
#     print(b_val_trim)
#     print(len(b_val_trim))
    
    total = 0;
    for num in all_rands:
       #print(num)
       b_val = bin(num)
       b_val_trim = b_val[2:]
       #print(b_val_trim)
       #print(len(b_val_trim))
       total += len(b_val_trim)
    
    print("total: " + str(total))