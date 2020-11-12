import os


def list_dir(dire, endswith='.pdf', sort=True):
    final = []
    for file in os.listdir(dire):
        if file.endswith(endswith):
            final.append(file)
    if sort:
        return sorted(final)
    else:
        return final


def complete_name(name, pre=r'C:\Users\Silas\Desktop\projeto-mae\Atividades_outubro', materia=None):
    if not materia:
        final = f'{pre}\\{name}' if '\\' not in name else f'{pre}{name}'
    else:
        final = f'{pre}\\{materia}\\{name}' if '\\' not in name else f'{pre}\\{materia}{name}'

    return final


def final_rename(list_files, materia):
    for file in list_files:
        rename = os.renames
        new_file = '_'.join(file.split())
        materia = materia.upper()
        new_file = new_file.upper()

        new_file = new_file.split('.')
        new_file = f'{new_file[0]}-{materia}.{new_file[1]}'

        old_file = complete_name(file, materia=materia)
        new_file = complete_name(new_file, materia=materia)
        rename(old_file, new_file)


# geo_cie_fold = list_dir(complete_name(r"\Geografia e Ciências"))
# final_rename(list_dir(complete_name(r"\Matemática")), 'Matemática')


final_rename(list_dir(complete_name(r"\Geografia e Ciências")), 'Geografia e Ciências')


# gc = list_dir(geo_cie_fold)






