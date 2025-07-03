# saved-file
Download de Arquivo do SharePoint e Salvar na Pasta de Rede
O que é esse projeto?
Esse script em Python faz o seguinte:

Acessa um arquivo do SharePoint Online usando autenticação via Azure AD (Client ID e Secret).

Baixa o arquivo Excel que tá no SharePoint.

Salva esse arquivo numa pasta de rede (compartilhada na empresa).

Requisitos
Python 3.7 ou superior

Acesso ao SharePoint Online com permissões para o arquivo

Registro de um aplicativo no Azure AD com Client ID e Client Secret configurados

Permissão para gravar na pasta de rede onde o arquivo será salvo

Setup
Clone ou baixe esse projeto.

Instale a biblioteca necessária:

bash
Copiar
Editar
pip install Office365-REST-Python-Client
Como configurar
No arquivo script.py (ou onde estiver o código), preencha as variáveis:

Variável	O que colocar	Onde achar/obter
site_url	URL do site SharePoint, ex: https://empresa.sharepoint.com/sites/Financeiro	URL do SharePoint da sua empresa
client_id	Client ID do app registrado no Azure	Azure Portal > App registrations > Seu app
client_secret	Client Secret do app (senha gerada no Azure)	Azure Portal > Certificates & secrets do app
tenant	Tenant ID do seu diretório Azure	Azure Portal > App registrations > Seu app
relative_url	Caminho relativo do arquivo no SharePoint	SharePoint > Clique no arquivo > Copiar link
pasta_rede	Caminho da pasta compartilhada onde salvar o arquivo	Exemplo: \\servidor\pasta

Como rodar
Basta executar o script Python:

bash
Copiar
Editar
python script.py
Se tudo estiver certo, ele vai baixar o arquivo do SharePoint e salvar na pasta de rede.

Observações
O script usa autenticação via Azure AD com ClientCredential.

Para o app funcionar, o administrador do Azure deve conceder as permissões necessárias (ex: Sites.Read.All).

A pasta de rede deve estar acessível e você precisa ter permissão para gravar nela.

Em empresas, pode ser necessário rodar o script em uma máquina que tenha acesso à rede interna.

