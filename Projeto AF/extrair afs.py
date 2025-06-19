import fitz  # PyMuPDF
import os
import re
import shutil  # Para mover arquivos
 
# Função para extrair texto de um PDF
def extrair_texto_pdf(caminho_pdf):
    doc = fitz.open(caminho_pdf)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    doc.close()
    return texto
 
# Função para extrair a AF do texto do PDF
def extrair_af_do_texto(texto):
    match = re.search(r'AF (\d+_\d+)', texto)
    if match:
        return match.group(1)
    return None
 
# Função para extrair o número da nota fiscal do texto do PDF
def extrair_numero_nota_fiscal(texto):
    match = re.search(r'N°\s*(\d{6})', texto)
    if match:
        return match.group(1)
    return None
 
# Função para processar todos os PDFs na pasta de entrada
def processar_pdfs(pasta_pdf, caminho_arquivo_txt, caminho_arquivo_sem_af_txt):
    arquivos_pdf = [f for f in os.listdir(pasta_pdf) if f.endswith('.pdf')]
    afs = []
    contador_sem_af = 1  # Contador para renomear arquivos sem AF
    nf_sem_af = []  # Lista para armazenar notas fiscais sem AF

    # Criar a pasta SEM AF se não existir
    pasta_sem_af = os.path.join(pasta_pdf, 'SEM AF')
    os.makedirs(pasta_sem_af, exist_ok=True)

    for arquivo_pdf in arquivos_pdf:
        caminho_pdf = os.path.join(pasta_pdf, arquivo_pdf)
        print(f"Processando: {caminho_pdf}")
        texto = extrair_texto_pdf(caminho_pdf)
        af = extrair_af_do_texto(texto)
        numero_nota_fiscal = extrair_numero_nota_fiscal(texto)

        if not numero_nota_fiscal:
            print(f"Não foi possível extrair o número da nota fiscal de: {caminho_pdf}")
            continue

        if af:
            afs.append(af)
            # Renomear o arquivo PDF para "numero_nota_fiscal_AF.pdf"
            novo_nome = f"{numero_nota_fiscal}_{af}.pdf"
            novo_caminho = os.path.join(pasta_pdf, novo_nome)
            os.rename(caminho_pdf, novo_caminho)
        else:
            nf_sem_af.append(numero_nota_fiscal)
            print(f"AF não encontrada em: {caminho_pdf}")
            # Mover o arquivo PDF para a pasta SEM AF
            shutil.move(caminho_pdf, pasta_sem_af)
            # Renomear o arquivo PDF ao movê-lo
            novo_nome = f"{numero_nota_fiscal}_SEM_AF_{contador_sem_af}.pdf"
            novo_caminho = os.path.join(pasta_sem_af, novo_nome)
            os.rename(os.path.join(pasta_sem_af, arquivo_pdf), novo_caminho)
            contador_sem_af += 1

    # Escreve as AFs extraídas em um arquivo TXT
    with open(caminho_arquivo_txt, 'w') as arquivo_txt:
        for af in afs:
            arquivo_txt.write(f"{af}\n")

    # Escreve as notas fiscais sem AF em um arquivo TXT
    with open(caminho_arquivo_sem_af_txt, 'w') as arquivo_sem_af:
        for nf in nf_sem_af:
            arquivo_sem_af.write(f"{nf}\n")

    print(f"AFs escritas em: {caminho_arquivo_txt}")
    print(f"Notas fiscais sem AF escritas em: {caminho_arquivo_sem_af_txt}")
 
# Definições de caminhos
pasta_pdf = r"C:\Users\Visitante\Desktop\teste AF"
caminho_arquivo_txt = os.path.join(pasta_pdf, 'afs_extraidas.txt')
caminho_arquivo_sem_af_txt = os.path.join(pasta_pdf, 'nf_sem_af.txt')
 
# Executar o processo
processar_pdfs(pasta_pdf, caminho_arquivo_txt, caminho_arquivo_sem_af_txt)
