from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Não utilizado devido a problemas de rastreamento pelo bot

# browser abre Google Chrome
browser = webdriver.Chrome()

# Acessa página de estatística do PIX
# browser.get("https://www.bcb.gov.br/estabilidadefinanceira/estatisticaspix")
browser.get("https://www.bcb.gov.br/estatisticas/detalhamentoGrafico")
# browser.get("blob:https://www.bcb.gov.br/62b02fbe-6f3d-4da9-8bab-b7f2618fbb47") --Acesso pelo blob recebe ID randômica que não é viável

# Por XPATH:
browser.find_element(By.XPATH, '//*[@id="highcharts-dpebyi5-0"]/svg/g[6]/g/path').click() # Acessa lista de opções de download
# browser.execute_script("$(arguments[0]).click();", '//[@id="highcharts-4lucmyi-53"]/svg/g[6]/g/rect')
# browser.find_element(By.XPATH, '//*[@id="highcharts-4lucmyi-53"]/div/ul/li[7]').click() # Baixa arquivo CSV

# Por elemento:
# browser.find_element('<rect fill="#ffffff" class="highcharts-button-box" x="0.5" y="0.5" width="24" height="22" rx="2" ry="2" stroke="none" stroke-width="1"></rect>').click() # Acessa lista de opções de download
# browser.execute_script("$(arguments[0]).click();", '<path fill="#666666" d="M 7 7.5 L 19 7.5 M 7 11.5 L 19 11.5 M 7 15.5 L 19 15.5" class="highcharts-button-symbol" data-z-index="1" stroke="#666666" stroke-width="1"></path>')
