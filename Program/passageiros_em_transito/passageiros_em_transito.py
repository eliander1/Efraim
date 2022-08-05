import pandas as pd
from datetime import date

passageiros_em_transito = pd.read_excel('Program/Planilhas/Efraimtur_Passageiros em  trânsito.xlsx')
pd.set_option('display.max_columns', 100)


def Check_in_Aberto():
    passageiros = []

    for i, data in enumerate(passageiros_em_transito['DATA IDA']):
        str_data_ida = str(data).replace(' 00:00:00', '')
        date_data_ida = date(day=int(str_data_ida.split('-')[2]), month=int(str_data_ida.split('-')[1]), year=int(str_data_ida.split('-')[0]))
        data_checkin = date_data_ida - date.today()

        if 0 <= data_checkin.days < 3:
            passageiro = (str_data_ida, passageiros_em_transito['CIA / LOCALIZADOR'].iloc[i], passageiros_em_transito['PASSAGEIRO'].iloc[i])
            passageiros.append(passageiro)

    df = pd.DataFrame(passageiros, columns=['DATA DE EMBARQUE', 'CIA / LOCALIZADOR', 'PASSAGEIRO'])
    df.to_excel('Program/Planilhas/planilhas_do_sistema/checkin_aberto.xlsx', index=False, sheet_name='Checkin Aberto2')




