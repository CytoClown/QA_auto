# data1 = ['Veu', 'Downloads', 'Word File.doc', 'Excel File.doc']
# data2 = ['veu', 'downloads', 'wordFile', 'excelFile']
# data3 = []
# data4 = []
# # for i in data1:
# #    a = i.replace(' ', '')
# #    a = a.replace('.doc', '')
# #    data3.append(a.lower())
# # print(data3)
# #
# # for i in data2:
# #    data4.append(i.lower())
# # print(data4)
# #
# # print(data3 == data4)
#
# for i in data1:
#    i.replace(' ', '')
#    print(i.lower())
# print(data1)
#
# #Вариант
# data1 = str(data1).replace(' ', '').replace('.doc', '').lower()
# data2 = str(data2).replace(' ', '').lower()

data = ['Cierra\nVega\n39\ncierra@example.com\n10000\nInsurance', 'Alden\nCantrell\n45\nalden@example.com\n12000\nCompliance', 'Kierra\nGentry\n29\nkierra@example.com\n2000\nLegal', '       ', '       ', '       ', '       ', '       ', '       ', '       ']
new_list = [i.split('\n') for i in data]
print(new_list)