from selenium import webdriver;
import time;



class defsClass:

    def startBot(username, password, url):
	path = "C:/Users/rmo02/teste e qualidade/chromedriver/chromedriver.exe"
	
	# selenium
	driver = webdriver.Chrome(path),

	
	# abrindo site 
	driver.get(url)
    
	
	# localizando user e passando user
	driver.find_element_by_id(
		"username").send_keys(username)
	
	# localizando senha e passando password
	driver.find_element_by_id(
		"password").send_keys(password)
	
	# submit
	driver.find_element_by_id(
		"loginbtn").click()


# passando as credenciais
username = "*****"
password = "@@@@@"

# URL 
url = "https://undbclassroom.undb.edu.br/login/index.php"


startBot(username, password, url),



def Search049(search, url):
	path = "C:/Users/rmo02/teste e qualidade/chromedriver/chromedriver.exe"
	
	# selenium
	driver = webdriver.Chrome(path),

	
	# abrindo site
	driver.get(url)
    
	
	# localizando elemento e passando parametros
	driver.find_element_by_id(
		"searchinput-630e98b2e7e79630e98b2b56d635").send_keys(search)
	

	
	# submit
	driver.find_element_by_id(
		"yui_3_17_2_1_1661906461136_53").click()


# pesquisa
search = "teste e qualidade"


# URL 
url = "https://undbclassroom.undb.edu.br/"

Search049(search, url),


def Search050(search, url):
	path = "C:/Users/rmo02/teste e qualidade/chromedriver/chromedriver.exe"
	
	# selenium
	driver = webdriver.Chrome(path),

	
	# abrindo site
	driver.get(url)
    
	
	# localizando elemento e passando parametros
	driver.find_element_by_id(
		"searchinput-630e98b2e7e79630e98b2b56d635").send_keys(search)
	

	
	# submit
	driver.find_element_by_id(
		"yui_3_17_2_1_1661906461136_53").click()


# pesquisa
search = "poo"


# URL
url = "https://undbclassroom.undb.edu.br/"

Search050(search, url)


def Search051(search, url):
	path = "C:/Users/rmo02/teste e qualidade/chromedriver/chromedriver.exe"
	
	# selenium
	driver = webdriver.Chrome(path),

	
	# abrindo site
	driver.get(url)
    
	
	# localizando elemento e passando parametros
	driver.find_element_by_id(
		"searchinput-630e98b2e7e79630e98b2b56d635").send_keys(search)
	

	
	# submit
	driver.find_element_by_id(
		"yui_3_17_2_1_1661906461136_53").click()


# pesquisa
search = "engenharia civil"


# URL
url = "https://undbclassroom.undb.edu.br/"

Search051(search, url)


def Search052(search, url):
	path = "C:/Users/rmo02/teste e qualidade/chromedriver/chromedriver.exe"
	
	# selenium
	driver = webdriver.Chrome(path),

	
	# abrindo site
	driver.get(url)
    
	
	# localiazando elemento, passando parametros
	driver.find_element_by_id(
		"searchinput-630e98b2e7e79630e98b2b56d635").send_keys(search)
	

	
	# submit
	driver.find_element_by_id(
		"yui_3_17_2_1_1661906461136_53").click()


# buscas
search = "rodrigo"


# URL 
url = "https://undbclassroom.undb.edu.br/"

Search052(search, url)

def Search053(search, url):
	path = "C:/Users/rmo02/teste e qualidade/chromedriver/chromedriver.exe"
	
	# selenium
	driver = webdriver.Chrome(path),

	
	# abrindo site
	driver.get(url)
    
	
	# Localizando elemnto e passando a busca
	driver.find_element_by_id(
		"searchinput-630e98b2e7e79630e98b2b56d635").send_keys(search)
	

	
	# submit
	driver.find_element_by_id(
		"yui_3_17_2_1_1661906461136_53").click()


# Pesquisa
search = "engenharia"


# URL 
url = "https://undbclassroom.undb.edu.br/"

Search053(search, url)

def Search054(search, url):
	path = "C:/Users/rmo02/teste e qualidade/chromedriver/chromedriver.exe"
	
	# iniciar o webDriver
	driver = webdriver.Chrome(path),

	#abrindo site
	driver.get(url)
    
	
	# Localizando o id do elemento
	driver.find_element_by_id(
		"searchinput-630e98b2e7e79630e98b2b56d635").send_keys(search)
	

	
	# click on submit
	driver.find_element_by_id(
		"yui_3_17_2_1_1661906461136_53").click()


# Buscas
search = "@, -, &"


# URL 
url = "https://undbclassroom.undb.edu.br/"

Search054(search, url)


def Search055(search, url):
	path = "C:/Users/rmo02/teste e qualidade/chromedriver/chromedriver.exe"
	
	# iniciar o webDriver
	driver = webdriver.Chrome(path),

	
	# abrindo navegador
	driver.get(url)
    
	
	# localizando elemento 
	driver.find_element_by_id(
		"searchinput-630e98b2e7e79630e98b2b56d635").send_keys(search)
	

	
	# submit
	driver.find_element_by_id(
		"yui_3_17_2_1_1661906461136_53").click()



# Pesquisa
search = "2022"


# URL 
url = "https://undbclassroom.undb.edu.br/"

Search055(search, url)


def Search056(search, url):
	path = "C:/Users/rmo02/teste e qualidade/chromedriver/chromedriver.exe"
	
	# path Selenium
	driver = webdriver.Chrome(path),

	
	#webSite
	driver.get(url).click

#URL
url = "https://undbclassroom.undb.edu.br/course/view.php?id=5301"

Search056(url)
