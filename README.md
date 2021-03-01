# AbstractAlgebraTool
Functions in Abstract Class with example
==========================================
Just copy and paste the line with print in it and see the example for yourself
----------------------

---
**Basic operations** 
-----------
---

- ##### add  
    
    ---
        Abstract.add(8,3)
    ---
    ###### Result
    ---
        11
    ---
- ##### subtract 
    
    ---
        Abstract.subtract(8,3) 
    ---
    ###### Result
    ---
        5
    ---
- ##### multiply
    
    ---
        Abstract.multiply(8,3) 
    ---
    ###### Result
    ---
        24
    ---
- ##### divide
    
    ---
        Abstract.divide(4,3) 
    ---
    ###### Result
    ---
        1.3333
    ---
- ##### divideInt 
    
    ---
        Abstract.divideInt(8,3) 
    ---
    ###### Result
    ---
        2
    ---
- ##### mod
    ---
        Abstract.mod(9,2)
    ---
     ###### Result
    
    ---
        1
    ---
- ##### exponent  
    
    ---
        Abstract.exponent(2,3) 
    ---
     ###### Result
        ----
            8 
        ----
        

---

**Tools more applicable to class**
--------

---
- ### GCD
    - ###### example 
        ---
            Abstract.GCD(3,2) 
        ---
    - should return 
        ---
            1
        ---

- ##### gcdSteps
    - Example 
        ---
            Abstract.gcdSteps(3,2)
        ---
    - Should return steps of the problem using Euclid's alogirthm

        ---
            (['3 = 2*1 + 1', '2 = 1*2 + 0'], ['1 = 3 - 2*1'])
        ---

- ##### simplifyCongruence
    - How to use method 
        - Let's say 176y ≡ 57x (mod 14)

        ###### We can simplify this by typing out the following 
       
        ---
            Abstract.simplifyCongruence(176,57,14)
        ---
        
       ###### This should return 
        ---
            8 ≡ 1 (mod 14)
        ---

        ###### This basically means that 
        ---
            8y ≡ x (mod 14)
        ---

    
