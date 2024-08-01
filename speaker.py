import pyttsx3
import pdfplumber

#inicializando a engine de NLP
engine = pyttsx3.init()

#lendo arquivo pdf
pdf = pdfplumber.open("O elefante em apuros.pdf")

# gerando lista de paginas do livro exceto as páginas 1, 2 , 27 ,28 e 29
paginas = pdf.pages[2:26]

texto_livro = ''
for pagina in paginas:
    texto_livro += pagina.extract_text()

texto_final = texto_livro.replace('.', '. ').replace(',', ', ')

engine.save_to_file(texto_final, "audiobook.mp3")
engine.runAndWait()