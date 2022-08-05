import pandas as pd
from datetime import date

aniversariantes = pd.read_excel('Planilhas/LISTA DE RG CPF CLIENTES.xlsx', engine='openpyxl')
aniversariantes['DATA DE NASCIMENTO'] = pd.to_datetime(aniversariantes['DATA DE NASCIMENTO'], errors='coerce').dt.date
nascimento = []

def Converte_Data_Nascimento():
    for i in aniversariantes['DATA DE NASCIMENTO']:
        nasc = str(i).split('-')
        del nasc[0]
        try:
            aniv = f'{nasc[1]}-{nasc[0]}'
        except:
            aniv = 'sem data'
        nascimento.append(str(aniv))

def Converte_Data_Hoje():
    hoje = str(date.today()).split('-')
    del hoje[0]
    data_atual = f'{hoje[1]}-{hoje[0]}'
    return data_atual

def Encontrar_Aniversariante():
    Converte_Data_Nascimento()
    data_hoje = Converte_Data_Hoje()
    aniv_do_dia = []
    linha = 0

    for i in nascimento:
        if str(i) == data_hoje:
            aniv_do_dia.append([aniversariantes.iloc[linha, 0]])
        linha +=1
    df = pd.DataFrame(aniv_do_dia, columns=['NOME'])

    df.to_excel('Planilhas/planilhas_do_sistema/aniversariantes do dia.xlsx', index=False, sheet_name=f'Aniversariantes do dia')






