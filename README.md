# Abstract Algebra tool kit 
---
###### This is a toolkit to help speed up the process of doing tedious tasks and to see values really fast. This is not meant to replace your understanding of certain topics, but, instead is designed to help when speed up the process when the goal is to solve problems that are higher in abstractions. 
---
## Online Editor 


### Instructions 
Click this [link](https://alpha.iodide.io/notebooks/7057/) after reading the entire instructions
- You will need to make a Github account. If you don't understand what Github is, don't worry. It's only needed to access the editor 
- Just in case you're not familiar with coding, you can use your own examples simply by modifying the numbers after typing or copying and pasting an example given 

	    If in code is in grey box like this.
	    Just copy line with the example in it,
	    and paste it in your code chunk. 
	    Then hit the double arrow or single arrow. 
	    And the results will be on the left  

## Local
### Instructions 
- simply download the github repository and run the commands locally
-  If you would like to have a pull-request to the repo, send me a note as it is common curtosy to do so and we'll go from there 
-



## Abstract's class methods example
    

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
        
        ###### You want to see the table for

                Zsubscript(2) + Zsubscript(3)
            
         ###### with addition or multiplication 
        ---

        ###### We can simplify this by typing out the following by copying the line below
        ###### and clicking single arrow in the top left of the screen
       
        ---
            Abstract.zTable(2,3,"+")
        
        
         or 
         
            Abstract.zTable(2,3,"*")
        ---
        
       ###### This should return one of these (not actual result) 
        
            a long table of (Zsubscript(2) x Zsubscript(3), +)
        
	   or 

            a long table of (Zsubscript(2) x Zsubscript(3), *)
             
---

## __More Basic Methods__ (Nothing special) 

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
        
