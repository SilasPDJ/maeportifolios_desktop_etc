import os
import pdf2image


class EverythingForms:
    def __init__(self, pdf_path, img_path):
        self.pdf_path = pdf_path
        self.img_path = img_path
        pass

    def list_dir(self, dire, fullname=False, endswith='.pdf', sort=True):
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
                file_fim = f'{dire}\\{file}'
                if not fullname:
                    final.append(file)
                else:
                    final.append(file_fim)

                os.renames(file_fim, f'{dire}\\{self.just_rename2upper(file)}')
                # input(f'test {file_fim}')

        if sort:
            import re
            final.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
            # nice, sort by names
            return final
        else:
            return final

    def complete_name(self, name, pre, materia=None):
        if not materia:
            final = f'{pre}\\{name}'
            # aqui o caminho já vem com a matéria
        else:
            final = f'{pre}\\{materia}\\{name}'
            # aqui ainda não vem...
        return final

    def transforma_pdf_em_img_por_materia(self, materia):
        searched = materia
        pdf_path = self.pdf_path

        if pdf_path:
            list_files = self.list_dir(self.complete_name(searched, pre=pdf_path), True)
        else:
            from tkinter import filedialog
            dale = filedialog.askdirectory(initialdir=os.path.realpath(''.join((__file__.split('\\')[:-1]))))
            list_files = self.list_dir(self.complete_name(searched, pre=dale), True)
            # C:\Users\Silas\Desktop\projeto-mae\Atividades_outubro
        volta = os.getcwd()
        for file in list_files:

            pages = pdf2image.convert_from_path(file)
            print(file)
            os.chdir(volta)
            for e, page in enumerate(pages):

                e_cont = e + 1
                # dir_name = '../MATERIAS_CRIA_FILES'
                dir_name = self.img_path

                dir_name += '\\' + searched + '\\'
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

    @classmethod
    def just_rename2upper(cls, name=None):
        if name is None:
            name = 'Laura matos da Silva Carvalho'

        name = name.upper()
        if ' ' in name:
            name = '_'.join(name.split())

        return name


rout = EverythingForms(r'C:\Users\Silas\Desktop\projeto-mae\Atividades_outubro',
                       'MATERIAS_CRIA_FILES-09112020')

# rout.transforma_pdf_em_img_por_materia('Português')
#rout.transforma_pdf_em_img_por_materia('História')
# rout.transforma_pdf_em_img_por_materia('Geografia e Ciências')
rout.transforma_pdf_em_img_por_materia('Matemática')



