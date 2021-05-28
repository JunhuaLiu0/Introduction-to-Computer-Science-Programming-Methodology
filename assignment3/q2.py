class derivative:
    def __init__(self, polynomial):
        self.polynomial = polynomial

    # Generate a list with operator as element
    def getOperatorList(self):
        operatorList = [""]
        polynomial_list = list(self.polynomial)
        for i in range(len(polynomial_list)):
            if polynomial_list[i] == "+":
                operatorList.append(polynomial_list[i])
            if polynomial_list[i] == "-":
                operatorList.append(polynomial_list[i])
        polynomial_list.append("")
        return operatorList

    # Split the polynomial
    def replaceOperator(self):
        replace_polynomial = self.polynomial
        replace_polynomial = replace_polynomial.replace("-", "+")
        # Changes all operators to positive to make polynomial easier to split
        replace_polynomial = replace_polynomial.split("+")
        return replace_polynomial

    # Formatting each sequence in the polynomial
    def getSplitSequence(self):
        sequence_list = []
        coefficient = 0
        split_list = self.replaceOperator()
        for sequence in split_list:
            if "*" in sequence:
                coefficient = sequence.split("*")[0]
                if "^" in sequence:
                    variable = sequence.split("*")[1]
                else:
                    variable = sequence.split("*")[1] + "^1"
                sequence_list.append((coefficient, variable))
            elif "^" in sequence:
                coefficient = 1
                sequence_list.append((coefficient, sequence))
            elif sequence.isdigit() == False:
                coefficient = 1
                sequence_list.append((coefficient, "^1"))
            else:
                coefficient = 1
                sequence_list.append((coefficient, "^0"))
        return sequence_list

    # Derivate each sequence in the polynomial
    def derivation(self):
        i = 0
        operator = self.getOperatorList()
        for (coefficient, variable) in self.getSplitSequence():
            unknown = str(variable.split("^")[0])
            exponent = int(variable.split("^")[1])
            newCoefficient = str(exponent * int(coefficient))
            newExponent = str(exponent - 1)
            if int(newExponent) > 1 and int(newCoefficient) == 1:
                derivation = "".join([unknown, "^", newExponent])
            elif int(newExponent) > 1 and int(newCoefficient) > 1:
                derivation = "".join([newCoefficient, "*", unknown, "^", newExponent])
            elif int(newExponent) == 0 and int(newCoefficient) > 0:
                derivation = "".join([newCoefficient])
            elif int(newExponent) == 1 and int(newCoefficient) > 1:
                derivation = "".join([newCoefficient, "*", unknown])
            elif int(newExponent) == 1 and int(newCoefficient) == 1:
                derivation = "".join([unknown])
            elif int(newExponent) == -1:
                derivation = ""
            if derivation != "":
                print(operator[i], end="")
            print(derivation, end="")
            i = i + 1


polynomial = input(
    "Input a proper polynomial."
)
equation = derivative(polynomial)
equation.derivation()
