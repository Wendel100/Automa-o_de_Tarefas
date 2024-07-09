import pyautogui
import time
import pandas as pd

tabela = pd.read_csv("produtos.csv")

pyautogui.PAUSE =0.8
pyautogui.press("win")
pyautogui.write("Microsoft Edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# espera para carregar
time.sleep(3)
pyautogui.click(x=549, y=360)
pyautogui.hotkey("ctrl, a")
pyautogui.write("pymeuemal@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.press("tab")
pyautogui.press("enter")
# espera para carregar
time.sleep(3)
for linha in tabela.index:
    pyautogui.click(x=679, y=242)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))  
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    if not pd.isna(tabela.loc[linha,"obs"]):
        pyautogui.write(str(tabela.loc[linha,"obs"]))

#volta para o inicio do loop
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)