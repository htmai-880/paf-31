"""
This function makes the multiplication between the vector X, and the Hadamard matrix with the right size.

     Parameter
     ---------
     X : vector
    
     Return
     ------
     X : vector
         X became X*H
"""
def FHL(X):
    
    h = 1
    longX = len(X) #We calculate the size of X to know the right  size of the Hadamard matrix
    
    while h < longX:
        
        for i in range(0, longX, h * 2):
            
            for j in range(i, i + h):
                
                Y = X[j]
                Z = X[j + h]
                X[j] = Y + Z       #This addition is the definition of the Hadamard matrix     H2=[1  1]
                X[j + h] = Y - Z   #This difference is the definition of the Hadamard matrix      [1 -1]
                
        h *= 2 #We multiply by 2 the size of the Hadamard matrix
        
    return X



"""
This function calculate the hash vector using FHL function.

    Parameters
    ----------
    symbPerm : list
        list of values that the elements of the hash vector can take
    nbSymb : int
        size of symbPerm
    vectDep : vector
        vector we want to hash
    longDep : int
        size of vectDep
        
    Return
    ------
    vectSortie : vector
        hash vector
"""
def outVect(symbPerm, nbSymb, vectDep, longDep):
    
    nouvVect = [] # We create a new vector nouvVect
    
    for i in range(longDep):
        
        # nouvVect takes random values in the list of values symbPerm
        j = (2*i+3)*vectDep[i] + i+1
        nouvVect.append(symbPerm[j%nbSymb])
    
    # We calculate nouvVector*H, and the hash vector vectSortie will take its value
    vectSortie = [elem%nbSymb for elem in FHL(nouvVect)]
    
    return vectSortie

