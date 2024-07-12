# API Escola

API Restful para gerenciar informações de uma escola, utilizando Django Rest Framework.

## Funcionalidades

- **Gerenciamento de Alunos**: Criação, leitura, atualização e exclusão de alunos.
- **Gerenciamento de Cursos**: Criação, leitura, atualização e exclusão de cursos.
- **Autenticação de Usuários**: Implementação de autenticação baseada em token.

## Arquivos Principais

- **config.py**: Contém as configurações da aplicação, como a chave secreta e a configuração do banco de dados.
- **models.py**: Define os modelos de dados para alunos e cursos.
- **serializers.py**: Contém os serializers para converter instâncias de modelo para JSON.
- **views.py**: Define as views para a API, incluindo as operações CRUD.
- **urls.py**: Configura as rotas da aplicação.
- **settings.py**: Configurações principais do Django, incluindo middleware e aplicações instaladas.
- **manage.py**: Script de gerenciamento do Django, usado para executar comandos administrativos.