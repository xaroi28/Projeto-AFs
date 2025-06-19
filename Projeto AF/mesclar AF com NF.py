import fitz  # PyMuPDF
import os
import re

# Função para extrair a AF do texto do PDF
def extrair_af_do_texto(texto):
    match = re.search(r'AF (\d+_\d+)', texto)
    if match:
        return match.group(1)
    return None

# Função para extrair o número da nota fiscal do nome do arquivo
def extrair_numero_nota_fiscal(nome_arquivo):
    match = re.search(r'(\d+)_', nome_arquivo)
    if match:
        return match.group(1)
    return None

# Função para mesclar PDFs
def mesclar_pdfs(pdf_nf, lista_afs, caminho_saida, pdf_informe):
    pdf_saida = fitz.open()  # Cria um novo documento PDF vazio
    
    # Adiciona o PDF da nota fiscal primeiro
    if pdf_nf:
        pdf_nf_doc = fitz.open(pdf_nf)
        pdf_saida.insert_pdf(pdf_nf_doc)
        pdf_nf_doc.close()
    
    # Adiciona os PDFs relacionados às AFs em seguida
    for pdf_af in lista_afs:
        pdf_af_doc = fitz.open(pdf_af)
        pdf_saida.insert_pdf(pdf_af_doc)  # Insere o PDF de entrada no PDF de saída
        pdf_af_doc.close()
    
    # Adiciona o PDF do comunicado ao final, se existir
    if pdf_informe:
        pdf_informe_doc = fitz.open(pdf_informe)
        pdf_saida.insert_pdf(pdf_informe_doc)
        pdf_informe_doc.close()
    
    pdf_saida.save(caminho_saida)
    pdf_saida.close()

# Função para buscar PDFs em uma pasta e suas subpastas
def buscar_pdfs_em_pasta(pasta_base, af):
    arquivos_encontrados = []
    for root, dirs, files in os.walk(pasta_base):
        for file in files:
            if file.endswith('.pdf') and af in file:
                arquivos_encontrados.append(os.path.join(root, file))
    return arquivos_encontrados

# Função principal para processar e mesclar PDFs
def processar_e_mesclar_pdfs(pasta_base, pasta_af, pasta_informe):
    arquivos_pdf = [f for f in os.listdir(pasta_af) if f.endswith('.pdf')]
    
    # Caminho para a pasta 'mesclados'
    pasta_mesclados = os.path.join(os.path.dirname(__file__), 'mesclados')
    if not os.path.exists(pasta_mesclados):
        os.makedirs(pasta_mesclados)
    
    # Verifica se o arquivo COMUNICADO.pdf existe
    pdf_informe = os.path.join(pasta_informe, "COMUNICADO.pdf")
    if not os.path.exists(pdf_informe):
        print(f"Arquivo '{pdf_informe}' não encontrado. O comunicado não será adicionado aos PDFs mesclados.")

    for arquivo_pdf in arquivos_pdf:
        caminho_pdf = os.path.join(pasta_af, arquivo_pdf)
        print(f"Processando: {caminho_pdf}")
        
        texto = extrair_texto_pdf(caminho_pdf)
        af = extrair_af_do_texto(texto)
        numero_nota_fiscal = extrair_numero_nota_fiscal(arquivo_pdf)
        
        if not af or not numero_nota_fiscal:
            print(f"AF ou número da nota fiscal não encontrados em: {caminho_pdf}")
            continue
        
        # Mantém o número da nota fiscal completo
        numero_nota_fiscal_completo = numero_nota_fiscal
        
        # Buscar PDFs que contenham a AF em suas pastas
        arquivos_para_melgar = buscar_pdfs_em_pasta(pasta_base, af)
        
        # Adiciona o PDF atual à lista de arquivos a serem mesclados
        # Considera o PDF atual como a NF
        pdf_nf = caminho_pdf
        
        # Nome do arquivo mesclado baseado no número da nota fiscal
        caminho_saida = os.path.join(pasta_mesclados, f"{numero_nota_fiscal_completo}.pdf")
        
        # Mesclar arquivos e salvar com o novo nome
        mesclar_pdfs(pdf_nf, arquivos_para_melgar, caminho_saida, pdf_informe)
        print(f"Arquivo mesclado salvo em: {caminho_saida}")

# Função para extrair texto de um PDF (necessária para o script principal)
def extrair_texto_pdf(caminho_pdf):
    doc = fitz.open(caminho_pdf)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    doc.close()
    return texto

# Definições de caminhos
pasta_af = r"C:\Users\Visitante\Desktop\teste AF"  # Pasta onde estão os arquivos PDF
pasta_base = r"C:\Users\Visitante\Desktop\AFs"  # Pasta base para buscar arquivos
pasta_informe = r"C:\Users\Visitante\Desktop\teste AF\informe"  # Pasta onde está o PDF do comunicado

# Executar o processo
processar_e_mesclar_pdfs(pasta_base, pasta_af, pasta_informe)
