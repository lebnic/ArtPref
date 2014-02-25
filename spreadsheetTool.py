# ===============================
# nicolas.leblanc3@mail.mcgill.ca
# ===============================

import openpyxl


def getOrderedInput(filename = 'Dummy Data.xlsx'):
    workbook = openpyxl.load_workbook(filename = filename, use_iterators = True)
    worksheet = workbook.get_sheet_by_name("Input")
    
    lInput0 = [row for row in worksheet.iter_rows()]
    lInput1 = ["%s_%s"%(lCell[0][3],int(lCell[1][3])) for lCell in lInput0]
    lInput2 = [[],[],[],[]]
    for lInput in lInput1:
        if int(lInput.split("_")[1]) == 0:
            lInput2[0].append(lInput)
        elif int(lInput.split("_")[1]) == 1:
            lInput2[1].append(lInput)
        elif int(lInput.split("_")[1]) == 2:
            lInput2[2].append(lInput)
        elif int(lInput.split("_")[1]) == 3:
            lInput2[3].append(lInput)
        
    return lInput2

