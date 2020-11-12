# import pandas_utilities as pud
import pandas as pd


name = r'C:\Users\Silas\OneDrive\Mae_Area de Trabalho\Atividades 3ºD\OUTUBRO_AVALIAÇOES\Respostas_Ate_Agora.xlsx'
excel_file_name = name
xls = pd.ExcelFile(excel_file_name)





for sh in xls.sheet_names:

    df = xls.parse(sh)

    # perguntas = list(range(len(df.count())))
    respostas = list(range(len(tuple(df.iterrows()))))
    input(respostas)
    for headers in df.columns:
        # print(headers)

        for e, valor in enumerate(df[headers]):

            print(valor)

    # df.iloc[]

    # print(a)



