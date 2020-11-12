def parse_sh_name(name='ALUNOS.xlsx', data_required=True):
    """
    :param tup: compt and excel_file_name from self._atual_compt_and_file
    :param data_required: data_Required
    :return:
    """
    import pandas as pd
    excel_file_name = name
    xls = pd.ExcelFile(excel_file_name)
    sheet_names = iter(xls.sheet_names)
    for e, sh in enumerate(sheet_names):
        # if e > 0:
        if data_required == 0:
            yield xls.parse(sh, dtype=str), sh
        elif data_required:
            yield xls.parse(sh, dtype=str)
        else:
            yield sh


def final():
    for df in parse_sh_name():
        dff = df.to_dict()
        return dff
    return None
