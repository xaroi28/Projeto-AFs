# Projeto de Automatização de AFs e NFs com Interface em Tkinter

Este projeto foi desenvolvido em Python com o objetivo de automatizar o fluxo de trabalho de análise e organização de arquivos de AF (Autorização de Fornecimento) e NFs (Notas Fiscais) em formato PDF. Com foco em operações logísticas, o sistema realiza desde a extração de dados até a mesclagem inteligente dos documentos, com interface gráfica amigável, extração de texto, filtros, renomeações e exclusões automatizadas.

 Funcionalidades
 Extração de AFs de documentos PDF usando OCR e expressões regulares;

 Mesclagem automática de arquivos (AF + NF + comunicado padrão) com base no número da nota;

 Separação de arquivos sem AF em pastas dedicadas e controle por TXT;

 Renomeação e padronização de arquivos baseada nas informações extraídas;

 Limpeza automática de arquivos temporários (.pdf e .txt);

 Barra de progresso visual integrada via Tkinter;

 Interface gráfica simples e funcional para executar os processos com um clique;

 Mesclagem final ordenada de todos os PDFs numericamente.

Tecnologias Utilizadas
Python 3

Tkinter — Interface gráfica

PyMuPDF (fitz) — Leitura e manipulação de PDFs

PyPDF2 — Mesclagem de arquivos PDF

re, os, shutil, glob — Manipulação de arquivos e expressões regulares

⚠️ Observações
O sistema foi desenvolvido de forma simples e direta, focado na funcionalidade e agilidade operacional.

Algumas operações foram adaptadas a um ambiente com restrições de TI, o que exigiu soluções locais (como leitura direta de pastas e arquivos nomeados manualmente).

A lógica pode ser facilmente expandida ou adaptada a outros fluxos com pequenas alterações.
