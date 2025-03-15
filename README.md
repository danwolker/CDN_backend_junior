# Análise e Recomendação de Filmes com TMDb API

Este projeto utiliza a **API do The Movie Database (TMDb)** para analisar e recomendar filmes e contém dois scripts em Python:

- **`teste_1.py`**: Analisa uma lista de filmes e gera estatísticas sobre **atores, gêneros e bilheteria**.
- **`teste_2.py`**: Recomenda **5 filmes baseados no gênero** do filme selecionado.

---

## 🚀 **Pré-requisitos**
Antes de rodar o projeto, verificar se está instalado:
- **Python 3.7+**
- **pip**
- **Git**

Obter **Chave de API do TMDb** em: [TMDb API Key](https://www.themoviedb.org/settings/api)

---

## 📌 **Passo a Passo para Rodar a Aplicação**

1. Clone este repositório ou extraia o arquivo ZIP.

2. Criar um Ambiente Virtual:

   #### **Linux / Mac**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

   #### **Windows (PowerShell)**
   ```sh
   python -m venv venv
   venv\Scripts\Activate
   ```

3. Instalação de Dependências
   ```sh
   pip install -r requirements.txt
   ```

4. Configuração de **Chave da API TMDb**
   - Crie um arquivo **`.env`** no diretório do projeto:
   - Edite o arquivo e adicione sua **API Key** do TMDb (utilizar como exemplo arquivo `example.env`):
      ```ini
      TMDB_API_KEY=COLOQUE_SUA_CHAVE_AQUI
      ```

5. Execução dos scripts no terminal:
   ```
   python teste_1.py
   ```
   Ou
   ```
   python teste_2.py
   ```
---
