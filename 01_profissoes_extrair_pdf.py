# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader

def extrair_e_salvar(caminho_arquivo_pdf, nome_arquivo_saida):
    # Abre o arquivo PDF
    with open(caminho_arquivo_pdf, 'rb') as arquivo:
        # Lê o arquivo PDF
        leitor_pdf = PdfReader(arquivo)

        # Cria um arquivo de texto para escrever
        with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            # apaga conteudo do arquivo de saida se houver
            arquivo_saida.seek(0)

            # Itera sobre as páginas do PDF
            for pagina_num in range(len(leitor_pdf.pages)):
                pagina = leitor_pdf.pages[pagina_num]
                texto = pagina.extract_text()

                # Escreve as linhas no arquivo de saída
                arquivo_saida.write(texto)
                arquivo_saida.write('\n')  # Adiciona uma quebra de linha entre as páginas

# Substitua 'caminho_do_arquivo.pdf' pelo caminho do seu arquivo PDF
caminho_do_arquivo_pdf = 'in/CBO2002_LISTA.pdf'

# Substitua 'nome_do_arquivo_saida.txt' pelo nome desejado para o arquivo de saída
nome_do_arquivo_saida = 'out/CBO2002_LISTA.txt'

# Chama a função para extrair e salvar o texto
extrair_e_salvar(caminho_do_arquivo_pdf, nome_do_arquivo_saida)

print(f'Texto extraído e salvo em {nome_do_arquivo_saida}')
