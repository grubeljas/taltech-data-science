import xlrd
book = xlrd.open_workbook("tshekid.xls")
sh = book.sheet_by_index(0)

prev_index = 1.0
with open('input2.txt', 'w') as writer:
    for rx in range(1, sh.nrows):
        row = sh.row(rx)[:2]
        index = row[0].value
        product = row[1].value
        if prev_index != index:
            writer.write('\n')
            prev_index = index

        product = product.replace(" ", "")
        writer.write(product.lower() + " ")
