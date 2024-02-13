# Classificação brasileira de ocupações - CBO

## Descrição

A Classificação Brasileira de Ocupações - CBO é o documento normalizador do reconhecimento (1) , da nomeação e da codificação dos títulos e conteúdos das ocupações do mercado de trabalho brasileiro. É ao mesmo tempo uma classificação enumerativa e uma classificação descritiva.
Fonte: [CBO](http://www.mtecbo.gov.br/cbosite/pages/informacoesGerais.jsf)

## Dados

Fonte: [CBO Downloads](http://www.mtecbo.gov.br/cbosite/pages/downloads.jsf)

### Arquivos e formatos

Existem dois arquivos disponíveis para download:
1. ZIP com arquivos CSV que possuem as dimensões da CBO separadas;
2. PDF com a lista normativa de profissões.

Usaremos este arquivo para extrair os dados, pdf: `CBO2002.pdf` datado de **22/06/2023**.

![](D:\Git\profissoes_brasil_gov_cbo\img\cbo_pdf.png)

## Objetivo

O projeto tem dois objetivos simples:

1. Disseminar a informação pública da lista normativa de profissões do Brasil;
1. Criar um pacote de dados para uso em projetos de análise de dados usando fonte PDF e CSV.

## O código python

O repositório possui os códigos que:
1. Extrai texto do PDF e exporta para um TXT bruto;
2. Consome o TXT e faz uma limpeza para exportar para CSV;

O objetivo também é trabalhar com data frames do pandas como aprendizado.
