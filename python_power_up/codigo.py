# Passo a passo do projeto

# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
    
# para instalar: pip install pyautogui
import pyautogui
import time

# tempo de delay para executar as tarefas
pyautogui.PAUSE = 1

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> precionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (ctrl c, ctrl v, alt tab)

# abir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundo pra carregar o site 
time.sleep(3)

# 2. Fazer login
pyautogui.click(x=669, y=472) # achar a posição da caixa de texto do email
pyautogui.write("rafael.castro@gmail.com")

pyautogui.press("tab") # passou para o campo de senha
pyautogui.write("12345rAFaa45")

pyautogui.press("tab") # passou para o botao de logar
pyautogui.press("enter")

time.sleep(3) # garantia para que a proxima pagina abre 

# 3. Abir/Importar a base de dados de produtos para cadastrar 
# pip install pandas numpy openpyxl
import pandas as pd #apelido para a biblioteca

tabela = pd.read_csv("python_hashtag/python_power_up/produtos.csv")

# print(tabela)

# 4. Cadastrar um produto

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])

    # clicar no campo do codigo do produto
    pyautogui.click(x=1166, y=306)

    # preencher o codigo
    pyautogui.write(codigo)
    # passar pro proximo campo
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # passar pro proximo campo
    pyautogui.press("tab")
    
    # apertar o botao
    pyautogui.press("enter")
    pyautogui.scroll(5000) # numero grande para voltar para o inicio da tela