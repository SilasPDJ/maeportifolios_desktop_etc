from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import requests



def names():
    req = requests.get('https://eunenem.com/blog/nomes-de-bebe-ideias-para-meninos-e-meninas/')
    req.encoding = 'utf-8'

    req = req.text
    init = soup(req)
    tbds = init.select('tbody')

    names = tbds[2].getText('-', 'True')
    names = names.split('-')

    for nm in names:
        yield nm


def soup(me):
    """
    :param me: element
    :return:
    """
    me = str(me)
    btf = BeautifulSoup(me, 'html.parser')
    return btf


driver = Chrome('Chromedriver/chromedriver.exe')
driver.get('file:///H:/MY_PROJECTS/JAVASCRIPT-de-uma-vez-por-todas/PROJETO_LISTA_DE_CONVIDADOS/index_p9.html')
cad = driver.find_element_by_id('cadastro')

cad_inputs = cad.find_elements_by_tag_name('input')
cad_selects = cad.find_elements_by_tag_name('select')

# selects
for e, name in enumerate(names()):
    if e == 6:
        break
    [(inpt.clear(), inpt.send_keys(name)) for inpt in cad_inputs if inpt.get_property('id') == 'convidado']

    telefone = str(randint(1*(10**9), 9*(10**9)))

    celular = telefone[:2]+'9'+telefone[2:]

    # telefone fixo, celular, = **10
    [(inpt.clear(), inpt.send_keys(telefone if e % 2 == 0 else celular)) for inpt in cad_inputs if inpt.get_property('id') == 'telefone']

    [sel.send_keys(f'{randint(1, 12):02d}' if cad_selects.index(sel) < 2 else randint(1990, 2000)) for sel in cad_selects]

    driver.find_element_by_id('adiciona-bt').click()
    driver.implicitly_wait(5)


# [sel.send_keys()]



