# COMMENTS.md

## Escolha das Ferramentas

- **Docker**: Para garantir um ambiente consistente e isolado.
- **Docker Compose**: Para orquestração local de serviços.
- **Prometheus e Grafana**: Para monitoramento local da aplicação.

## Decisões de Arquitetura

- Utilização de contêineres para facilitar o setup e deploy local.
- Orquestração de serviços com Docker Compose para simplificar a gestão.
- Monitoramento com Prometheus e Grafana para visibilidade.

## Testes e Melhorias

- Testes básicos com pytest para validar a API.
- Sugestões futuras incluem integração contínua com GitHub Actions para garantir a qualidade do código.
- Implementação de logs para melhorar a depuração e monitoramento.

project_root/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── app.py
│   ├── tests/
│   │   └── test_api.py
│   ├── Dockerfile
│   └── requirements.txt
├── infrastructure/
│   ├── docker-compose.yml
│   └── prometheus.yml
├── generate_comments.py
├── Makefile
└── .github/
    └── workflows/
        └── ci.yml

## Passos para Executar o Script de Geração de Comentários
1. Criar o Ambiente Virtual:
Navegue até o diretório raiz do projeto e crie um ambiente virtual:
$ python3 -m venv venv

2. Ativar o Ambiente Virtual:
Ative o ambiente virtual. O comando pode variar dependendo do sistema operacional que você está usando:

No Windows:
$ venv\Scripts\activate

No Linux ou MacOS:
$ source venv/bin/activate

3. Instalar o Pacote requests:
Com o ambiente virtual ativado, instale o pacote requests:
$ pip install requests

4. Executar o Script:
No diretório raiz do projeto, execute o script para gerar comentários:
$ python generate_comments.py

5. Verificar os Comentários:
Após executar o script, você pode listar os comentários para verificar se foram inseridos corretamente:

curl -sv localhost:8000/api/comment/list/1
curl -sv localhost:8000/api/comment/list/2
curl -sv localhost:8000/api/comment/list/3
curl -sv localhost:8000/api/comment/list/4
curl -sv localhost:8000/api/comment/list/5

6. Monitorar os Logs:
Continue monitorando os logs do contêiner da aplicação para verificar se as requisições estão sendo processadas corretamente:

docker-compose -f infrastructure/docker-compose.yml logs app

## Sugestões Adicionais:

Validação de Dados: Implementar validação de dados nos endpoints para garantir que os comentários recebidos estão no formato correto.
Autenticação e Autorização: Adicionar autenticação e autorização para controlar quem pode enviar e visualizar comentários.
Testes de Integração: Adicionar testes de integração para garantir que todos os componentes do sistema funcionam bem juntos.
Deploy em Produção: Configurar pipelines de deploy para ambientes de staging e produção usando ferramentas como AWS, Azure ou GCP.
