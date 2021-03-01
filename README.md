%% md
# Abstract Algebra tool kit 
---
###### This is a toolkit to help speed up the process of doing tedious tasks and to see values really fast. This is not meant to replace your understanding of certain topics, but, instead is designed to help when speed up the process when the goal is to solve problems that are higher in abstractions. 
---
---
## Examples and functions are shown on the read me in the github repo 

#### [Github Link](https://github.com/josephaw1022/AbstractAlgebraTool) 
---

## Functions in Abstract Class with example
    If in code is in grey box like this. Just copy line with the example in it, 
    and paste it in your code chunk to see example work 

--- 

# __Helpful Tools__



- ### GCD
    ---
    ###### copy line below and click single arrow in the top left of the screen
        
            Abstract.GCD(17,19) 
        
    ###### should return 
        
            1
    ---

- ### gcdSteps
    ---
    ###### copy line below and click single arrow in the top left of the screen
        
            Abstract.gcdSteps(3,2)
        
    ###### Should return steps of the problem using Euclid's alogirthm

        
            (['3 = 2*1 + 1', '2 = 1*2 + 0'], ['1 = 3 - 2*1'])
        
    ---

- ### simplifyCongruence
    - Example  
        
            You want to simplify 176y ≡ 57x (mod 14)

        ###### We can simplify this by typing out the following by copying the line below
        ###### and clicking single arrow in the top left of the screen
       
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
- ### zTable 
    - Example  
        
            You want to see the table for Z <sub> 2 </sub> x Z <sub> 3 </sub> with addition
 
        ###### We can simplify this by typing out the following by copying the line below
        ###### and clicking single arrow in the top left of the screen
       
        ---
            Abstract.zTable(2,3,"+")
        ---
        
       ###### This should return 
        ---
            a table of (Z <sub> 2 </sub> x Z <sub> 3 </sub>, +) 
        ---

       

---

## __More Basic Tools__
-----------



- ### add  
    ---
    ###### copy line below and click single arrow in the top left of the screen
    
        Abstract.add(8,3)
    
    
    ###### Result 
    
        11
    ---
- ### subtract 
    ---
    ###### copy line below and click single arrow in the top left of the screen
    
        Abstract.subtract(8,3) 
    
    ###### Result
    
        5
    ---

- ### multiply
    ---
    ###### copy line below and click single arrow in the top left of the screen
    
        Abstract.multiply(8,3) 
    
    ###### Result
    
        24
    ---

- ### divide
    ---
    ###### copy line below and click single arrow in the top left of the screen
    
        Abstract.divide(4,3) 
    
    ###### Result
    
        1.3333
    ---
    
- ### divideInt 
    ---
    ###### copy line below and click single arrow in the top left of the screen
    
        Abstract.divideInt(8,3) 
    
    ###### Result
    
        2
    ---
    
- ### mod
    ---
    ###### copy line below and click single arrow in the top left of the screen
    
        Abstract.mod(9,2)
    
     ###### Result
    
    
        1
    ---
    
- ### exponent
    ---
    ###### copy line below and click single arrow in the top left of the screen
    
        Abstract.exponent(2,3) 
    
     ###### Result
        
            8 
    ---
        

