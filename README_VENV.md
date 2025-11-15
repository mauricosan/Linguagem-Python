README - Ativando o venv (passo a passo, direto e simples)

Este arquivo mostra apenas os passos essenciais para ativar o ambiente virtual (venv) do projeto.
Feito para ser rápido de seguir se você tem TDAH: frases curtas, só o necessário.

1) Onde estou

 - Projeto: C:\Users\felip\Desktop\Linguagem-Python
 - venv: C:\Users\felip\Desktop\Linguagem-Python\venv

2) Ativar no PowerShell (recomendado)

 - Abra PowerShell na pasta do projeto.
 - Copie e cole EXATAMENTE uma linha abaixo e dê Enter:

   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force; . 'C:\Users\felip\Desktop\Linguagem-Python\venv\Scripts\Activate.ps1'

 - Você verá o prompt com (venv) no começo. Exemplo: (venv) PS C:\Users\felip\Desktop\Linguagem-Python>

3) Verificar que está ativo

 - Rode:
   python -V
   where.exe python

 - Saída esperada: versão do Python (ex.: Python 3.x.x) e o primeiro caminho apontando para
   C:\Users\felip\Desktop\Linguagem-Python\venv\Scripts\python.exe

4) Desativar o venv

 - No mesmo terminal, rode:
   deactivate

5) Se preferir usar CMD (prompt do Windows)

 - Abra cmd.exe na pasta do projeto e rode:
   C:\Users\felip\Desktop\Linguagem-Python\activate.bat

6) Dicas rápidas (útil quando a atenção some)

 - Se algo der errado: copie a saída do terminal e cole aqui (ou no seu bloco de notas).
 - Faça uma coisa por vez: ativar, verificar, rodar o script.
 - Precisa rodar um arquivo Python agora? Diga qual arquivo (ex.: projeto\PROJETO_APR1.py) e eu executo aqui.

7) Quero ajuda prática

 - Posso executar um script seu agora dentro do venv e mostrar a saída. Diga o nome do arquivo.

---
Arquivo criado automaticamente em: C:\Users\felip\Desktop\Linguagem-Python\README_VENV.md
