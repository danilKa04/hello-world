lines = ["Неисправное", "Повреждение", "Ямы", "Открытый","Реклама", "Неисправность","Мусор","Нескошенная","Некачественный","Неубранный",
"Снег","Проблемы","Ненадлежащее","Содержание","Несанкционированное"]
with open(r"E:\slov.txt", "w") as file:
    for  line in lines:
        file.write(line + '\n')
