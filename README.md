# 🎵 Buscador de Letras de Músicas

![Licença](https://img.shields.io/badge/Licença-MIT-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-red)
![Status](https://img.shields.io/badge/Status-Funcional-success)

## 📋 Descrição do Projeto

Aplicação web desenvolvida com Streamlit que permite buscar letras de músicas de forma rápida e simples. O usuário informa o nome do artista e da música, e a aplicação consulta a API lyrics.ovh para exibir a letra completa em uma interface amigável.

### 🎯 Funcionalidades

- Busca de letras de músicas por artista e título
- Interface web intuitiva e responsiva
- Exibição da letra em formato estilizado com degradê
- Feedback visual sobre disponibilidade da letra

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Streamlit**: Framework para criação de aplicações web com Python
- **Requests**: Biblioteca para requisições HTTP
- **Poetry**: Gerenciador de dependências e pacotes

## 📦 Pré-requisitos

Antes de começar, você precisará ter instalado:

- Python 3.12 ou superior
- Poetry (gerenciador de pacotes)

## ⚙️ Instalação

1. Clone este repositório:
```bash
git clone https://github.com/ezerodrigues/projeto-letra-musica.git
cd projeto-letra-musica
```

2. Instale as dependências com Poetry:
```bash
poetry install
```

3. Ou, se preferir usar pip:
```bash
pip install -r requirements.txt  # Caso você crie um arquivo requirements.txt
# Ou instale diretamente:
pip install streamlit requests
```

## 🎮 Como Usar

1. Inicie a aplicação:
```bash
poetry run streamlit run app.py
```

2. Ou, se não estiver usando Poetry:
```bash
streamlit run app.py
```

3. A aplicação será aberta no navegador (geralmente em http://localhost:8501)

4. Digite o nome do artista e da música desejada

5. Clique em "Pesquisar" para visualizar a letra

## 📸 Demonstração

A aplicação apresenta uma interface simples e intuitiva:

1. Campo para inserir o nome do artista
2. Campo para inserir o nome da música
3. Botão para realizar a pesquisa
4. Área de exibição da letra com estilo personalizado

## 🔍 Exemplos de Uso

- Buscar letras de músicas para karaokê
- Estudar letras para aprender idiomas
- Analisar composições musicais
- Criar playlists temáticas baseadas em conteúdo lírico

## 🛠️ Possíveis Melhorias

- Adicionar histórico de pesquisas recentes
- Implementar tradução automática das letras
- Criar opção para baixar a letra em formato PDF
- Adicionar reprodução da música via integração com APIs de streaming
- Implementar busca por trecho de letra

## 🔄 API Utilizada

O projeto utiliza a API pública [lyrics.ovh](https://lyrics.ovh/), que fornece letras de músicas gratuitamente.

Endpoint utilizado:
```
https://api.lyrics.ovh/v1/{artista}/{musica}
```

## 👨‍💻 Autor

**Eliézer Rodrigues**

- GitHub: [ezerodrigues](https://github.com/ezerodrigues)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
