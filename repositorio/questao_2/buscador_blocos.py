import pandas as pd

dados_Blocos = pd.read_csv("Carnaval 2018.csv", sep=';')
dados_Blocos.columns = dados_Blocos.columns.str.strip() #Tratar espaços em nomes de colunas

#Organização de Data/Hora
concentracao_Horario = dados_Blocos['Data'] + ' ' + dados_Blocos['Concentração']
desfile_Horario = dados_Blocos['Data'] + ' ' + dados_Blocos['Desfile']
final_Horario = dados_Blocos['Data'] + ' ' + dados_Blocos['Final']

format_string = '%d/%m/%Y %H:%M:%S'

dados_Blocos['horario_Concentracao'] = pd.to_datetime(concentracao_Horario, format=format_string, errors='coerce')
dados_Blocos['horario_Desfile'] = pd.to_datetime(desfile_Horario, format=format_string, errors='coerce')
dados_Blocos['horario_Final'] = pd.to_datetime(final_Horario, format=format_string, errors='coerce')

print("Digite o nome do bairro para a busca: ")
bairro_Usuario = input()
blocos_No_Bairro = dados_Blocos[dados_Blocos['Bairro'].str.contains(bairro_Usuario, case=False, na=False)] #Mais específico para buscar até variações

if blocos_No_Bairro.empty:
    print("Nenhum bloco encontrado para o bairro: ", bairro_Usuario)
else:
    print("Blocos encontrados em ", bairro_Usuario, ": ")
    dias_Unicos = blocos_No_Bairro['Data'].unique()
    for dia in dias_Unicos:
        print("\nDia:", dia)
        blocos_Do_Dia = blocos_No_Bairro[blocos_No_Bairro['Data'] == dia]
        for index, linha in blocos_Do_Dia.iterrows():
            print("Nome do bloco: ", linha['Bloco'], "| Horário: ", linha['horario_Concentracao'])

print("\nDeseja exportar esse resultado para um arquivo CSV? (S/N)")
resposta_Usuario = input().upper()

if resposta_Usuario == 'S':
    colunas_para_exportar = [
        'Bloco', 
        'Bairro', 
        'Data', 
        'Concentração', 
        'Desfile', 
        'Final',
        'Local da Concentraçao',
        'Público Estimado'
    ]
    blocos_Para_Exportar = blocos_No_Bairro[colunas_para_exportar]
    nome_Arquivo = "Blocos_em_" + bairro_Usuario.replace(' ', '_') + ".csv"
    blocos_Para_Exportar.to_csv(nome_Arquivo, index=False, sep=';', encoding='utf-8-sig')
    print("Arquivo", nome_Arquivo, "salvo com sucesso!")