#

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
import os

# Config
site_url = "https://SEU_DOMINIO.sharepoint.com/sites/SEU_SITE"
client_id = "SEU_CLIENT_ID" #ID do aplicativo registrado no Azure.
client_secret = "SEU_CLIENT_SECRET"  #pega no "Certificates & secrets" dentro do app no Azure.
tenant = "SEU_TENANT_ID" #Tenant ID, que representa teu diretório no Azure.

#  Caminho do arquivo no SharePoint
relative_url = "/sites/SEU_SITE/Shared Documents/SEU_ARQUIVO.xlsx"

#  Pasta de rede
pasta_rede = r"\\servidor\pasta"
caminho_salvar = os.path.join(pasta_rede, "SEU_ARQUIVO.xlsx")

#  Auth
ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))

#  Baixar
response = ctx.web.get_file_by_server_relative_url(relative_url).download(caminho_salvar).execute_query()

print("Arquivo salvo com sucesso na rede! 🚀")

