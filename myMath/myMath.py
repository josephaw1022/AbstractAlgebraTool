from typing import AbstractSet


class myMath:
    def add(a,b): 
        return a+b 

    def subtract(a,b): 
        return a-b 

    def multiply(a,b):
        return a*b

    def divide(a,b): 
        return a/b

    def divideInt(a,b):
        return a//b 

    def mod(a,b):
        return a%b 

    def exponent(a,b): 
        return a__b 

    ## More specific stuff
    def GCD(a,b):
        bigVal , smallVal = max([a,b]) , min([a,b])
        # start euclid's alogirthm 

        done = False 
        while not done:

            tempVal = bigVal 
            bigVal = smallVal    
            potentialGCD = smallVal 
            smallVal = tempVal % smallVal
            if smallVal ==0: 
                return potentialGCD

    def gcdSteps(a,b):
        def equationFormat(valOne, valTwo, valThree, valFour):
            return "{} = {}*{} + {}".format(valOne, valTwo, valThree, valFour)

        def endingsFormat(valOne, valTwo, valThree, valFour): 
            return "{} = {} - {}*{}".format(valFour, valOne, valTwo, valThree)
        
        def popEndValue(list):
            return list[0:len(list)-1]

        endingVals = []    
        allEquations=[]
        bigVal , smallVal = max([a,b]) , min([a,b])
        # start euclid's alogirthm  
        # FORMAT =>  A = M*X + B  
        aValues =[]
        mValues =[]
        xValues =[]
        bValues =[]

        done = False 
        while not done:
            
            tempVal = bigVal 
            bigVal = smallVal    
            smallVal = tempVal % smallVal
            endingVals.append(endingsFormat(tempVal,bigVal,tempVal//bigVal,smallVal))
            allEquations.append(equationFormat(tempVal,bigVal,tempVal//bigVal,smallVal))

            aValues.append(tempVal)
            mValues.append(bigVal)
            xValues.append(tempVal//bigVal)
            bValues.append(smallVal)

            if smallVal ==0: 
                break 
        aValues = popEndValue(aValues)
        mValues = popEndValue(mValues)
        xValues = popEndValue(xValues)
        bValues = popEndValue(bValues)
        endingVals = popEndValue(endingVals)

        # "\n",aValues,"\n",mValues,"\n", xValues,"\n" , bValues, "\n")
        
        return allEquations, endingVals


    def simplifyCongruence(initVal1, initVal2, iterVal): 
        returnVals = []
        while initVal1<=0: 
            initVal1+=iterVal 
            if initVal1>0: 
                returnVals.append(initVal1)
                break 

        while initVal1-iterVal>= 0: 
            initVal1 -= iterVal
            if initVal1-iterVal < 0:
                returnVals.append(initVal1)
                break 

        while initVal2 <=0: 
            initVal2+=iterVal 
            if initVal2>0: 
                returnVals.append(initVal2)
                break 

        while initVal2-iterVal>= 0: 
            initVal2 -= iterVal
            if initVal2-iterVal < 0:
                returnVals.append(initVal2)
                break 
        
        topline = "{}a ≡ {}b (mod {}) is equivalent to\n\n".format(initVal1, initVal2, iterVal)
        templateFormat = topline+ "{}a ≡ {}b (mod {})\n\n".format(initVal1, initVal2, iterVal)
        return templateFormat


    # This is still in the works at the moment 
    def linearCombination(valueOne, valueTwo): 
        s = 0
        old_s = 1
        t = 1
        old_t = 0
        r = valueOne
        old_r = valueTwo

        while r != 0:
            quotient = old_r//r 
            old_r, r = r, old_r - quotient*r
            old_s, s = s, old_s - quotient*s
            old_t, t = t, old_t - quotient*t
        
        return "{}({})+ {}({}) = {}".format(old_t, valueOne, old_s,  valueTwo, old_r )
    



    def zTable(zOne, zTwo, operation=""): 
        if zOne > 3 or zTwo > 3: 
            indent = ""
            for i in range(2): 
                indent+=" "
        else: 
            indent = "\t"

        if operation=="" or operation=="None": 
            return  "\n\nATTENTION!\n\nMust give a string of a operation ['+', '*'] argument. Cannot be anything else.\n\nExample of correct method use:\n\n{}\n\n{}\n\n{}\n\n".format("ZTable(3,4,'+')","ZTable(3,2,'*')","ZTable(9,4,'+')")

        def doOperation(valueOne, valueTwo, operation): 
            if operation=="+": 
                return Abstract.add(valueOne,valueTwo)
            elif operation=="*": 
                return multiply(valueOne,valueTwo)

        def makeArray(lengthDesired):
            anyArray = []
            for i in range(lengthDesired): 
                anyArray.append(i)
            return anyArray

        def line(num=35):
            string = ""
            for i in range(num): 
                string+="-"
            return string  
            


        outpieces = []

        for zOneElement in makeArray(zOne): 
            for zTwoElement in makeArray(zTwo): 
                outpieces.append([zOneElement, zTwoElement])

        

        finalTable = []

        for chunk1 in outpieces: 
            tempRow = []
            for chunk2 in outpieces: 
                tempRow.append([Abstract.mod(doOperation(chunk1[0],chunk2[0],operation),zOne), Abstract.mod(doOperation(chunk1[-1],chunk2[-1],operation),zTwo)])
            finalTable.append(tempRow)
            
        def formatTableValue(pieceOne,pieceTwo): 
            return "({} , {})".format(pieceOne, pieceTwo)

        def formattedTable(givenTable, key=None):
            string = []
            
            newTable = [] 
            
            iterCount = 0 
            for row in givenTable: 
                
                innerIterCount =0 
                
                row = sorted(row)
                for pair in row:
                    tempArray =  row[iterCount-1] 
                    string.append( str("{} {} {} => {}\n\n".format( formatTableValue(pair[0],pair[1]) , operation , formatTableValue(tempArray[0], tempArray[1]) , formatTableValue( (doOperation(pair[0], tempArray[0], operation)) % zOne , (doOperation(pair[1], tempArray[1],operation))%zTwo ) ))) 
                    innerIterCount+=1 
                string+="\n"
                iterCount+=1 
            
            return string


        def formatTitleRow(row): 
            finalString=""
            for value in row: 
                finalString += formatTableValue(value[0],value[1])
            print(finalString)
            return finalString


    
        return formattedTable(finalTable)

