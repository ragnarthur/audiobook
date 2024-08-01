# Audiobook do Livro "O Elefante em Apuros"

Este projeto cria um audiobook do livro "O Elefante em Apuros" a partir de um arquivo PDF utilizando as bibliotecas `pyttsx3` e `pdfplumber` em Python.

## Sumário

- [Introdução](#introdução)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução

O objetivo deste projeto é automatizar a criação de um audiobook a partir de um livro em formato PDF. Utilizando o Python, extraímos o texto do PDF e o convertimos em áudio, que é então salvo como um arquivo MP3.

## Requisitos

Antes de executar o script, certifique-se de ter o seguinte:

- Python 3.x instalado
- Bibliotecas Python:
  - `pyttsx3`
  - `pdfplumber`

## Instalação

1. Clone este repositório em sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/audiobook-elefante-apuros.git
    cd audiobook-elefante-apuros
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv env
    source env/bin/activate  # No Windows: env\Scripts\activate
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Coloque o arquivo PDF do livro "O Elefante em Apuros" no diretório do projeto com o nome `O elefante em apuros.pdf`.

2. Execute o script `audiobook.py`:

    ```bash
    python audiobook.py
    ```

   O script irá:
   - Ler as páginas do livro, exceto as páginas 1, 2, 27, 28 e 29.
   - Extrair o texto das páginas especificadas.
   - Converter o texto em áudio.
   - Salvar o áudio como `audiobook.mp3`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

1. Faça um fork do projeto
2. Crie uma nova branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Envie para o repositório remoto (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Script

Aqui está o script completo usado para gerar o audiobook:

```python
import pyttsx3
import pdfplumber

# Inicializando a engine de NLP
engine = pyttsx3.init()

# Lendo arquivo PDF
pdf = pdfplumber.open("O elefante em apuros.pdf")

# Gerando lista de páginas do livro, exceto as páginas 1, 2, 27, 28 e 29
paginas = pdf.pages[2:26]

texto_livro = ''
for pagina in paginas:
    texto_livro += pagina.extract_text()

texto_final = texto_livro.replace('.', '. ').replace(',', ', ')

engine.save_to_file(texto_final, "audiobook.mp3")
engine.runAndWait()
