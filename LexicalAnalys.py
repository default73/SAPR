def lexical_analys():
    alllexemList = []

    keywords = ["while"]
    single_operators = [">", "<", "=",  "+", ':']
    sost_operators = ["<=", ">=", "!=", "==", "+=", "-=", "*=", "/=", "%="]

    with open("input2", "r") as file:
        for line in file:
            len_line = len(line)
            i = 0
            var = ""
            while i < len_line:
                if line[i] not in single_operators and line[i] != " " and line[i] != "\n":
                    var += line[i]
                elif var != "":
                    if var in keywords:
                        alllexemList.append([0, var])
                    elif not var[0].isdigit():
                        alllexemList.append([1, var])
                    elif var.isdigit():
                        alllexemList.append([2, var])
                    else:
                        print("Лексический анализ - ошибка", "\nСтрока:", line, "\nСимвол: ", var)
                        exit()
                    var = ""
                if i < len(line) - 1:
                    if line[i:i+2] in sost_operators:
                        alllexemList.append([3, line[i:i+2]])
                        i += 1
                    elif line[i] in single_operators:
                        alllexemList.append([3, line[i]])
                elif line[i] in single_operators:
                        alllexemList.append([3, line[i]])
                i += 1

    with open("lexem.txt", "w") as f:
        for item in alllexemList:
            f.write("%s\n" % item)
    return alllexemList

lexical_analys()

