def differentiate(func):

    # print function
    print(func)

    # split expression into separate words using spaces
    split_func = func.split()

    # get the function name (everything before opening bracket of first expression)
    func_name = split_func[0][: split_func[0].find("(")]

    # get function variable (everything between the brackets of first expression
    func_var = split_func[0][split_func[0].find("(")+1 : split_func[0].find(")")]

    # array with function declaration {f(x) = } removed leaving the body monomials
    func_body = split_func[2:]

    # generate a copy of the function body to store results
    result = func_body

    #
    # FLAG ALL RELEVANT INFORMATION ABOUT THE FUNCTION
    #

    # for each monomial in the function body
    for i in range(len(func_body)):

        #set defaults
        mult = 1 
        exponent = 1 
        is_operator = False

        # if an operator, print as is
        if func_body[i] == "+" or func_body[i] == "-":
            is_operator = True
        
        # check if the monomial has an exponent ^ symbol 
        elif str(func_body[i]).find("^") != -1:
            # capture exponent
            exponent = func_body[i][func_body[i].find("^")+1:]

        # check if there is a number in front of the variable
        var_position = func_body[i].find(func_var)

        if var_position != 0:
            # capture numbers in front of var
            mult = func_body[i][:var_position]
        
        # SECTION TO START CONVERTING MONOMIALS TO THEIR DERIVATIVES
        if is_operator:
            continue

        #if a constant and the only expression, the derivative is 0
        elif func_body[i].isnumeric():
            result[i] = 0

        else:
            result[i] = str(int(mult) * int(exponent)) + func_var + "^" + str(int(exponent) - 1)

    #
    # START POPULATING RESULT STRING
    #
 
    result_string = func_name + "'(" + func_var + ") = "

    # make a single string for results
    for i in range(len(func_body)):
        result_string += str(result[i]) + " "

    # remove powers of 1
    result_string = result_string.replace("^1", "")

    #remove powers of 0
    result_string = result_string.replace(str(func_var + "^0"), "")

    #remove + 0s
    result_string = result_string.replace("+ 0", "")

    #remove - 0s
    result_string = result_string.replace("- 0", "")

    # print resulting string
    print(result_string)
    print()
        
differentiate("b(r) = 5")
differentiate("f(x) = x")
differentiate("g(z) = 6z")
differentiate("f(x) = 17x^4 + 12x^3 + 34x - 21")
differentiate("g(a) = 6a^3 + a^2 + 4")
