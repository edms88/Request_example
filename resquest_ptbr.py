import requests
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
from pathlib import Path
from datetime import datetime as dt

# Desativar os avisos de plataforma insegura
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

# Obtém o diretório do script
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# Nome do arquivo dia
today = dt.now()
folder_today = str(today.day)

# Nome arquivo mes
mes_atual = dt.now()
folder_name = str(mes_atual.month)

# Cria os caminhos completos para as pastas
folder_name = current_dir / "Folder_name" / "folder_name_year" / folder_name
folder_today = folder_name / folder_today

# Verifica se a pasta do mês não existe antes de criar
if not folder_name.exists():
    folder_name.mkdir(parents=True)
    print(f'Pasta do mês criada em: {folder_name}')
else:
    print(f'A pasta do mês {folder_name} já existe.')

# Verifica se a pasta do dia não existe antes de criar
if not folder_today.exists():
    folder_today.mkdir()
    print(f'Pasta do dia criada em: {folder_today}')
else:
    print(f'A pasta do dia {folder_today} já existe.')

# Login & Senha
usuario = 'usuario'
senha = 'senha!@#'

url_csv = 'URL_PARA_DOWNLOAD'

dados_login = {
    'usuario': usuario,
    'senha': senha,
}

# Sessão de requisição
with requests.Session() as session:
    # Desativar a verificação do certificado SSL
    session.verify = False

    # Realizar o login usando autenticação básica no cabeçalho
    #session.post(url_csv, auth=(usuario, senha))

    # Fazer o download do arquivo CSV após o login
    resposta = session.get(url_csv, auth=(usuario,'senha!@#'))

    # Verificar se a requisição foi bem-sucedida (código 200)
    if resposta.status_code == 200:
        print(f'Conexão 100%')
        # Especificar o caminho onde você deseja salvar o arquivo
        caminho_destino = str(folder_today / 'arquivo.csv')

        # Salvar o conteúdo do arquivo
        with open(caminho_destino, 'wb') as arquivo:
            arquivo.write(resposta.content)

        print(f"Download concluído. Arquivo salvo em: {caminho_destino}")
    else:
        print(f"Erro no download. Código de status: {resposta.status_code}")