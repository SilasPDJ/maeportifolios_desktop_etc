def list_dir(dire, fullname=False, endswith='.pdf', sort=True):
    """
    :param dire: path...
    :param fullname: True -> returns with fullpath, False -> only images names...
    :param endswith: ...
    :param sort: order...
    :return:
    """
    import os
    final = []
    for file in os.listdir(dire):
        if file.endswith(endswith.upper()) or file.endswith(endswith.lower()):

            if not fullname:
                final.append(file)
            else:
                file_fim = f'{dire}\\{file}'
                final.append(file_fim)
    if sort:
        import re
        final.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
        # nice, sort by names
        return final
    else:
        return final


def complete_name(name, materia=None, pre=r'C:\Users\Silas\Desktop\projeto-mae\Atividades_outubro'):
    if not materia:
        final = f'{pre}\\{name}'
    else:
        final = f'{pre}\\{materia}\\{name}'

    return final
