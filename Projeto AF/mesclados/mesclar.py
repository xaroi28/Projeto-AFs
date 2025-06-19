import os
from PyPDF2 import PdfWriter, PdfReader

# Obtém o diretório onde o script está localizado
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cria uma lista de arquivos PDF no diretório do script
pdf_files = [f for f in os.listdir(script_dir) if f.endswith('.pdf')]

# Filtra apenas os arquivos que são números
pdf_files = [f for f in pdf_files if f.split('.')[0].isdigit()]

# Ordena os arquivos pelo nome (números)
pdf_files.sort(key=lambda x: int(x.split('.')[0]))

# Cria um objeto PdfWriter
pdf_writer = PdfWriter()

# Lê e mescla cada PDF
for pdf_file in pdf_files:
    pdf_reader = PdfReader(os.path.join(script_dir, pdf_file))
    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])

# Define o caminho do diretório de saída
output_dir = r"C:\Users\Visitante\Desktop"

# Garante que o diretório de saída existe
os.makedirs(output_dir, exist_ok=True)

# Define o nome do arquivo de saída
output_file = os.path.join(output_dir, 'NFs mescladas HOSP.pdf')

# Salva o PDF mesclado
with open(output_file, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

# Obtém o caminho completo do arquivo mesclado
full_path = os.path.abspath(output_file)

print(f"PDFs mesclados com sucesso em '{full_path}'")
