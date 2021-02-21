def NAND (x, y): 
  
    if x == 1 and y == 1: 
        return True
    else: 
        return False
  
if __name__=='__main__': 
    print(NAND(1, 1)) 
  
    print("+---------------+----------------+") 
    print(" | NAND Truth Table | Result |") 
    print(" x = False, y = False | x NAND y =",NAND(True,False)," | ") 
    print(" x = False, y = True | x NAND y =",NAND(False,True)," | ") 
    print(" x = True, y = False | x NAND y =",NAND(True,False)," | ") 
    print(" x = True, y = True | x NAND y =",NAND(True,True)," | ")  
