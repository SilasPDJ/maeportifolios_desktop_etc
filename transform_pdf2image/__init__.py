from defs_utils import *
import pdf2image
import os


def transforma_pdf_em_img_por_materia(materia, pdf_path=None):
    searched = materia
    if pdf_path:
        list_files = list_dir(complete_name(searched, pre=pdf_path), True)
    else:
        list_files = list_dir(complete_name(searched), True)
    volta = os.getcwd()
    for file in list_files:

        pages = pdf2image.convert_from_path(file)
        print(file)
        os.chdir(volta)
        for e, page in enumerate(pages):

            e_cont = e+1
            dir_name = '../MATERIAS_CRIA_FILES'
            dir_name += '\\'+searched+'\\'
            dir_name += file.split('\\')[-1].split('-')[0]

            for folder in dir_name.split('\\'):
                try:
                    os.chdir(folder)
                except (FileNotFoundError):
                    os.mkdir(folder)
                    os.chdir(folder)
            os.chdir(volta)

            real = '\\'.join(os.path.realpath(__file__).split('\\')[:-1])
            page.save(f'{real}\\{dir_name}\\out-{e_cont}.jpg', 'JPEG')
            print(dir_name)
