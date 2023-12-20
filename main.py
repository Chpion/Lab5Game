import re

# Определение групп логический элементов

keywords = ["while", "do", "begin", "end", "var", "writeln", "integer", "and"]
singleOperator = ['<', '>', '+', '/', '-', '*', ';', '=', ".", ":", ",", '(', ')']
compoundOperator = [":=", "<=", ">=", "<>"]

resLab1 = [] # хранение результата лабораторной работы 1
resLab2 = [] # хранение результата лабораторной работы 2

def Main():
    with open('input.txt', 'r') as file:
        source_code = file.read()
    res = re.findall(r'\b\w+\b|[():=+\-*/<>.;,]', source_code)

# Обработка составных операторов
    for i in range(len(res)):
        if (i + 1) < len(res):
            if ((res[i] == ":" or res[i] == "<" or res[i] == ">") and res[i + 1] == "=") or (res[i] == "<" and res[i+1]
== ">"):
                a = str(res[i]) + res[i+1]
                res.insert(i, a)
                res.pop(i + 1)
                res.pop(i + 1)
    if not ErrorProcessing(res):
        LexicalAnalys(res)
    else:
        # Вывод ошибки в консоль и запись в файл
        with open('output.txt', 'w') as file:
            file.write("ERROR")
        with open('output2.txt', 'w') as file:
            file.write("ERROR")
        with open('output3.txt', 'w') as file:
            file.write("ERROR")
        with open('RESULT.txt', 'w') as file:
            file.write("ERROR")

        print("ERROR")
        return


    if SyntacticAnalys():
        # Вывод ошибки в консоль и запись в файл
        with open('output2.txt', 'w') as file:
            file.write("ERROR")
            print("ERROR")
        with open('output3.txt', 'w') as file:
            file.write("ERROR")
        with open('RESULT.txt', 'w') as file:
            file.write("ERROR")
        return

    else:
        with open('output2.txt', 'r') as file:
            file_contents = file.read()
            print(file_contents, end="\n\n")

    resSemantic = SemanticAnalys()
    # Вывод ошибки в консоль и запись в файл
    if resSemantic[0] == 0:
        with open('output3.txt', 'w') as file:
            file.write("OK")
        print("OK")

    elif resSemantic[0] == 1:
        with open('output3.txt', 'w') as file:
            file.write("Повторное объявление переменной: " + resSemantic[1])
        print("Повторное объявление переменной: " + resSemantic[1])
        with open('RESULT.txt', 'w') as file:
            file.write("ERROR")
        return

    elif resSemantic[0] == 2:
        with open('output3.txt', 'w') as file:
            file.write("Определение необъявленной переменной: " + resSemantic[1])
        print("Определение необъявленной переменной: " + resSemantic[1])
        with open('RESULT.txt', 'w') as file:
            file.write("ERROR")
        return

    elif resSemantic[0] == 3:
        with open('output3.txt', 'w') as file:
            file.write("Определение необъявленной переменной: " + resSemantic[1])
        print("Определение необъявленной переменной: " + resSemantic[1])
        with open('RESULT.txt', 'w') as file:
            file.write("ERROR")
        return

    elif resSemantic[0] == 4:
        with open('output3.txt', 'w') as file:
            file.write("Используется не определенная переменная: " + resSemantic[1])
        print("Используется не определенная переменная: " + resSemantic[1])
        with open('RESULT.txt', 'w') as file:
            file.write("ERROR")
        return


    Synthesis()


# Лексический анализ
def LexicalAnalys(result):
     file = open('output.txt', 'w')
     l = 0
     for i in range(len(result)):
        if result[i] in keywords:
            file.write("keywords: " + result[i] + "\n")
            print("keywords: " + result[i])
            resLab1.append(["keywords:", result[i]])
            if result[i] == "var" or result[i] == "begin":
                 file.write("specialSymbol: " + "\\n\n")
                 print("specialSymbol: " + "\\n")
                 resLab1.append(["specialSymbol:", "\\n"])
                 l += 2

            else:
                 l += 1
        elif result[i] in compoundOperator:
             file.write("compoundOperator: " + result[i] + "\n")
             print("compoundOperator: " + result[i])
             resLab1.append(["keywords:", result[i]])
             l += 1
        elif result[i] in singleOperator:
             file.write("singleOperator: " + result[i] + "\n")
             print("singleOperator: " + result[i])
             resLab1.append(["singleOperator:", result[i]])
             if result[i] == ";":
                 file.write("specialSymbol: " + "\\n\n")
                 print("specialSymbol: " + "\\n")
                 resLab1.append(["specialSymbol:", "\\n"])
                 l += 2
             else:
                 l += 1
        elif result[i].isnumeric():
             file.write("number: " + result[i] + "\n")
             print("number: " + result[i])
             resLab1.append(["number:", result[i]])
             l += 1
        else:
             file.write("value: " + result[i] + "\n")
             print("value: " + result[i])
             resLab1.append(["value:", result[i]])
             l += 1
     file.close()
     print("\n\n")


# Синтаксический анализ

def SyntacticAnalys():
    with open('output2.txt', 'w') as file:
         file.write("Start\n" + "|\n")

         # Ветвь объявления переменных
         file.write("|____" + "defining variables\n" + "|    |\n")
         resLab2.append(["defining variables"])
         if resLab1[0][1] != "var":
            return True
         i = 2
         while i < len(resLab1):
             if resLab1[i][1] == "begin": # проверка на окончание блока определение переменных
                 i += 2
                 break

             file.write("|    |____")
             strRes = [] # создание массива для хранения строки объявления переменной
             while resLab1[i][1] != ";":
                 strRes.append(resLab1[i][0])
                 strRes.append(resLab1[i][1])
                 i += 1
             i -= 3
             file.write(resLab1[i + 1][0] + " " + resLab1[i + 1][1] + "\n")
             file.write("|    |    |____")
             file.write(resLab1[i + 2][0] + " " + resLab1[i + 2][1] + "\n")
             file.write("|    |    |____")
             file.write(resLab1[i][0] + " " + resLab1[i][1] + "\n")
             i += 3;


             if resLab1[i-1][1] != "integer": # проверка на наличие оператора определение переменной
                return True

             strRes.append(resLab1[i][0])
             strRes.append(resLab1[i][1])
             resLab2.append(strRes)

             file.write("|    |\n")
             i += 2
         else:
            return True

         # Ветвь присвоения значений переменным
         file.write("|____" + "assigning values\n" + "|    |\n")
         resLab2.append(["assigning values"])
         while i < len(resLab1):
            if resLab1[i][1] == "while": # проверка на на ветку начала цикла
                i += 1
                break

            file.write("|    |____")
            strRes = []
            rn = 0
            while resLab1[i][1] != ";":
                 if resLab1[i][1] == ":=":
                     rn += 1

                 strRes.append(resLab1[i][0])
                 strRes.append(resLab1[i][1])
                 i += 1
            i -= 3
            file.write(resLab1[i + 1][0] + " " + resLab1[i + 1][1] + "\n")
            file.write("|    |    |____")
            file.write(resLab1[i][0] + " " + resLab1[i][1] + "\n")
            file.write("|    |    |____")
            file.write(resLab1[i + 2][0] + " " + resLab1[i + 2][1] + "\n")

            i += 3;

            if rn > 1 or rn == 0:
                 return True
            strRes.append(resLab1[i][0])
            strRes.append(resLab1[i][1])
            resLab2.append(strRes)

            file.write("|    |\n")
            i += 2
         else:
            return True


         key = 0
         j = i
         stop = 0
         # проверка на двойное условие
         while resLab1[j][1] != "do":
            if resLab1[j][1] == "and":
                 key = 1
                 break
            j += 1

         # Ветвь условия цикла
         file.write("|____" + "while\n" + "     |\n")
         file.write("     |____")
         resLab2.append(["while"])
         while i < len(resLab1):
            if resLab1[i][1] == "do" or resLab1[i][1] == "begin": # проверка на конец ветки условия цикла
                 i += 2
                 break

            if key == 1:
                 if stop == 0:
                     file.write("and\n")
                     resLab2.append(["and"])
                 stop = 1
                 file.write("     |    |____")
                 strRes = []
                 while resLab1[i][1] != "and" and resLab1[i][1] != "do":
                     #file.write(resLab1[i][0] + " " + resLab1[i][1] + ", ")
                     strRes.append(resLab1[i][0])
                     strRes.append(resLab1[i][1])
                     i += 1
                 resLab2.append(strRes)
                 i -= 3
                 file.write(resLab1[i + 1][0] + " " + resLab1[i + 1][1] + "\n")
                 file.write("     |    |    |____")
                 file.write(resLab1[i][0] + " " + resLab1[i][1] + "\n")
                 file.write("     |    |    |____")
                 file.write(resLab1[i + 2][0] + " " + resLab1[i + 2][1] + "\n")
                 file.write("     |    |\n")
                 i += 3
                 file.write("     |    | \n")
            else:
                 strRes = []
                 while resLab1[i][1] != "do":
                     #file.write(resLab1[i][0] + " " + resLab1[i][1] + ", ")
                     strRes.append(resLab1[i][0])
                     strRes.append(resLab1[i][1])
                     i += 1
                 resLab2.append(strRes)
                 i -= 3
                 file.write(resLab1[i + 1][0] + " " + resLab1[i + 1][1] + "\n")
                 file.write("     |    |____")
                 file.write(resLab1[i][0] + " " + resLab1[i][1] + "\n")
                 file.write("     |    |____")
                 file.write(resLab1[i + 2][0] + " " + resLab1[i + 2][1] + "\n")
                 file.write("     |    |\n")
                 i += 3
                 file.write("     | \n")
            i += 1
         else:
            return True

         # Ветвь тела цикла
         file.write("     |____" + "cycle body\n")
         resLab2.append(["cycle body"])
         while i < len(resLab1):
            if resLab1[i][1] == "end": # проверка на конец ветки цикла
                break
            else:
                file.write("         |____")
                strRes = []
                rn = 0
                while resLab1[i][1] != ";":

                    if resLab1[i][1] == ":=" or resLab1[i][1] == "(":
                        rn += 1
                    strRes.append(resLab1[i][0])
                    strRes.append(resLab1[i][1])
                    i += 1
                i -= 4
                if resLab1[i][1] != "writeln":
                    file.write(resLab1[i][0] + " " + resLab1[i][1] + ", ")
                    file.write("\n         |    |____")
                    file.write(resLab1[i - 1][0] + " " + resLab1[i - 1][1] + ", ")
                    file.write("\n         |    |____")
                    file.write(resLab1[i + 2][0] + " " + resLab1[i + 2][1] + ", ")
                    file.write("\n         |    |    |____")
                    file.write(resLab1[i + 1][0] + " " + resLab1[i + 1][1] + ", ")
                    file.write("\n         |    |    |____")
                    file.write(resLab1[i + 3][0] + " " + resLab1[i + 3][1] + ", ")
                    file.write("\n         |\n")
                else:
                    file.write(resLab1[i][0] + " " + resLab1[i][1] + ", ")
                    file.write("\n              |____")
                    file.write(resLab1[i + 2][0] + " " + resLab1[i + 2][1] + ", ")

                i +=4
                if rn > 1 or rn == 0:
                    return True
                strRes.append(resLab1[i][0])
                strRes.append(resLab1[i][1])
                resLab2.append(strRes)



                i += 2

         else:
            return True
         resLab2.append(["END"])
         return False


def SemanticAnalys():
    res = [0, "OK"]
    announcement = [] # объявленные переменные

    definition = [] # определенные переменные
    usage = [] # используемые переменные
    i = 0
    while i < len(resLab2):
        if resLab2[i][0] == "defining variables": # запись в массив объявлненных переменных
            i += 1
            while resLab2[i][0] != "assigning values":
                j = 0
                while j < len(resLab2[i]):
                    if resLab2[i][j] == "value:":
                        announcement.append(resLab2[i][j+1])
                        j += 2
                    j += 1
                i += 1

            for x in range(len(announcement) - 1): # проверка на повторное объявление
                 y = x + 1
                 while y < len(announcement):
                    if announcement[x] == announcement[y]:
                         res = [1, announcement[x]]
                         return res
                    # повторное объявление переменной
                    y += 1
        if resLab2[i][0] == "assigning values":
            i += 1
            while resLab2[i][0] != "while":
                 j = 2
                 while j < len(resLab2[i]):
                    if resLab2[i][j] == "value:":
                        usage.append(resLab2[i][j+1])
                        if resLab2[i][j + 1] not in announcement:
                            res = [3, resLab2[i][j + 1]] # используется не объявленная переменная
                            return res


                        if resLab2[i][j+1] not in definition:
                            res = [4, resLab2[i][j+1]] # используется не определенная переменная

                            return res
                    j += 1

                 definition.append(resLab2[i][1])
                 if resLab2[i][1] not in announcement:
                     res = [2, resLab2[i][1]] # определеная не объявленная переменная
                     return res
                 i += 1


        if resLab2[i][0] == "while":
            if resLab2[i+1][0] == "and":
                i += 2

            else:
                i += 1


            while resLab2[i][0] != "cycle body":
                if resLab2[i][0] == "value:":
                    usage.append(resLab2[i][1])
                    if resLab2[i][1] not in announcement:
                        res = [3, resLab2[i][1]]  # используется не объявленная переменная
                        return res
                    if resLab2[i][1] not in definition:
                        res = [4, resLab2[i][1]] # используется не определенная переменная
                        return res


                if resLab2[i][4] == "value:":
                    usage.append(resLab2[i][5])
                    if resLab2[i][5] not in announcement:
                        res = [3, resLab2[i][5]]  # используется не объявленная переменная
                        return res
                    if resLab2[i][5] not in definition:
                        res = [4, resLab2[i][5]]  # используется не определенная переменная
                        return res
                i += 1

        if resLab2[i][0] == "cycle body":
            i += 1


            while resLab2[i][0] != "END":
                j = 2
                while j < len(resLab2[i]):
                    if resLab2[i][j] == "value:":
                        usage.append(resLab2[i][j + 1])

                        if resLab2[i][j + 1] not in announcement:
                            res = [3, resLab2[i][j + 1]]  # используется не объявленная переменная
                            return res
                        if resLab2[i][j + 1] not in definition:
                            res = [4, resLab2[i][j + 1]]  # используется не определенная переменная
                            return res
                    j += 1
                if resLab2[i][1] != "writeln":
                    definition.append(resLab2[i][1])
                    if resLab2[i][1] not in announcement:
                        res = [2, resLab2[i][1]]  # определеная не объявленная переменная
                        return res
                i += 1
        i += 1
    return res


def Synthesis():
    file = open('RESULT.txt', 'w')
    file.write("#include <iostream>\nusing namespace std;\n\nint main(){\n\n")
    i = 1
    while resLab2[i][0] != "assigning values":
        j = 1
        file.write("int ")
        while j < len(resLab2[i]) and resLab2[i][j] != ";":
            if resLab2[i][j] == "integer" or resLab2[i][j] == ":":
                j += 2
                continue
            file.write(resLab2[i][j] + " ")
            j += 2
        file.write(resLab2[i][j] + "\n")
        i += 1
    i += 1
    file.write("\n")
    while resLab2[i][0] != "while":
        j = 1
        while j < len(resLab2[i]) and resLab2[i][j] != ";":
            if resLab2[i][j] == "integer" or resLab2[i][j] == ":":
                j += 2
                continue
            if resLab2[i][j] == ":=":
                file.write("= ")
            else:
                file.write(resLab2[i][j] + " ")
            j += 2
        file.write(resLab2[i][j] + "\n")
        i += 1
    i += 1
    file.write("\n")
    if resLab2[i][0] == "and":
        key = 1
        i += 1
    else:
        key = 0

    file.write("while( ")
    while resLab2[i][0] != "cycle body":
        j = 1

        if key == 1:

            while j < len(resLab2[i]):
                file.write(resLab2[i][j] + " ")
                j += 2
            file.write("&& ")
            key = 0
        else:
            while j < len(resLab2[i]):
                file.write(resLab2[i][j] + " ")
                j += 2
        i += 1
    file.write("){\n")

    i += 1
    while resLab2[i][0] != "END":
        j = 1
        file.write("\t")
        while j < len(resLab2[i]) and resLab2[i][j] != ";":
            if resLab2[i][j] == ":=":
                file.write("= ")
            elif resLab2[i][j] == "writeln":
                file.write("cout ")
            elif resLab2[i][j] == "(":
                file.write("<< ")
            elif resLab2[i][j] == ")":
                j += 2
                continue

            else:
                file.write(resLab2[i][j] + " ")
            j += 2
        file.write(resLab2[i][j] + "\n")
        i += 1
    file.write("}\nreturn 0;\n}")
    file.close()

# Обработка ошибок
def ErrorProcessing(res):
    begEnd = 0
    whiDo = 0
    for i in range(len(res)):
        # Подсчет парности элементов
        if res[i] == "begin":
            begEnd += 1
        elif res[i] == "end":
            begEnd -= 1
        elif res[i] == "while":
            whiDo += 1
        elif res[i] == "do":
            whiDo -= 1

    # Проверка корректности создания переменной
        if res[i] == "integer" and res[i + 1] != ";":
            return True
        if res[i] == "integer" and res[i - 1] != ":":
            return True

        # Проверка корретности вывода
        if res[i] == "writeln" and res[i + 1] != "(":
            return True

        # Проверка корретности цикла while
        if res[i] == "while":
            so = 0
            scL = 0
            scR = 0
            aNd = 0
            j = i + 1
            index = res.index("do")

            while j < index and j < len(res) - 1:
                if res[j] == "<" or res[j] == ">" or res[j] == "<>" or res[j] == "<=" or res[j] == ">=":
                    so += 1
                elif res[j] == "and":
                    aNd += 1

                elif res[j] == "(":
                    scL += 1
                elif res[j] == ")":
                    scR += 1
                j += 1
            if scR != scL:
                return True
            if so - 1 != aNd:
                return True
# Проверка корреткности определения переменной
        if res[i] == ":=":
            if res[i - 1].isnumeric() or res[i - 1] in keywords or res[i - 1] in compoundOperator or res[i - 1] == singleOperator:
                return True
            if res[i + 1] in keywords or res[i + 1] in compoundOperator:
                return True

        # Вывод ошибки в случае непарности элементов
    if whiDo != 0 or begEnd != 0:
        return True

    # Вывод ошибки в случае отсутсвии точки в конце файла
    if res[len(res) - 1] != ".":
        return True
    return False
Main()
