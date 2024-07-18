from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Cheguei!!"
        self.grupos = ["Beatriz"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')

        r
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get('https://web.whatsapp.com')
        input("Pressione Enter após fazer o login no WhatsApp Web...")  

    def EnviarMensagens(self):
        for grupo in self.grupos:
            try:
                
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//span[@title='{grupo}']")))
                grupo = self.driver.find_element(By.XPATH, f"//span[@title='{grupo}']")
                grupo.click()
                time.sleep(2)
                chat_box = self.driver.find_element(By.CLASS_NAME, '_3Uu1_')
                chat_box.click()
                time.sleep(3)
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
                botao_enviar.click()
                time.sleep(2)
            except Exception as e:
                print(f"Erro ao enviar mensagem para {grupo}: {str(e)}")

    def fechar(self):
        self.driver.quit()

bot = WhatsappBot()
bot.EnviarMensagens()
bot.fechar()
