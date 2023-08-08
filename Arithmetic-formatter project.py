import re

def arithmetic_arranger(problems, solve = False):

    if(len(problems) > 5):
        return "Error: Too many problems."

    firstNum = ""
    secNum = ""
    lines = ""
    sumX = ""
    string = ""

    for problem in problems:
        if(re.search("[^\s0-9.+-]", problem)):
            if(re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        
        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
            return "Error: numbers cannot be more than four digits."
        
        sum = ""
        if(operator == "+"):
            sum = str(int(firstNumber) + int(secondNumber))
        elif(operator == "-"):
            sum = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)
        line = ""
        res = str(sum).rjust(length)
        for s in range(length):
            line += "-"


        if problem != problems[-1]:
            firstNum += top + '    '
            secNum += bottom + '    '
            lines += line + '    '
            sumX += res + '    '
        else:
            firstNum += top
            secNum += bottom
            lines += line
            sumX += res

    if solve:
        string = firstNum + "\n" + secNum + "\n" + lines + "\n" + sumX
    else:
        string = firstNum + "\n" + secNum + "\n" + lines
    
    return string


