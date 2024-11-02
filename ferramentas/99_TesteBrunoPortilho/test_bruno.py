import time
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

## Bruno Portilho - 1525165@sga.pucminas.br

# Start/Install driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Teste com EDGE
#driver = webdriver.Edge() 

# clear cache
driver.execute_cdp_cmd("Network.clearBrowserCache", {})

def test_bruno():
    driver.get("file:///C:/Users/bruno/Desktop/Testes_Bruno/sample-exercise-bruno.html")

    # Clique no botão “generate”. Um código será gerado abaixo do botão como na figura ao lado
    driver.find_element(by=By.NAME, value="generate").click()

    # Capture o código e ...
    code = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "my-value")))
    code_text = code.text

    # ... e preencha o campo de texto com ele
    input_box = driver.find_element(by=By.ID, value="input")
    input_box.clear()
    input_box.send_keys(code_text)

    # Clique no botão “test”
    driver.find_element(by=By.NAME, value="button").click()

    # Um alerta com o texto “Done!” será exibido
    Alert(driver).accept()

    # Uma mensagem no formato “It workls! <código>!” será exibida
    msg = driver.find_element(by=By.ID, value="result").text
    msg_ok = f"It workls! {code_text}!"
    
    # Capture a mensagem e verifique se o valor está correto
    if msg == msg_ok:
        print("Valor OK!")
    else:
        print("Valor Errado!")
    
# Loop 3x
for _ in range(3):
    test_bruno()
    time.sleep(2)
    
# Encerrar webdriver
driver.quit()