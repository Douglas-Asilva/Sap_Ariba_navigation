from selenium import webdriver
from selenium.common.exceptions import * #importando os tipos de exceções
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait #importando a espera
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as condicao_esperada
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


Avaliadores_Pilar_Interno_teste = []         

class Sap_Ariba():

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def start_driver(self,address_driver,address_download,background = False):
        """
        Essa função seta o caminho do driver e o caminho do download e abre o navegador
        """

        logging.info(f"Conexão | Iniciando conexão com o Navegador | WEB")
        chrome_options = Options()


        if background:
            arguments = ['--lang=pt-BR', '--headless', '--disable-infobars',
                    '--no-sandbox', '--disable-gpu','--start-maximized']

        else:
            arguments = ['--lang=pt-BR','--start-maximized','--disable-infobars'] 


        for argument in arguments:
            chrome_options.add_argument(argument)

        chrome_options.add_experimental_option('prefs', {
        #Alterar o local padrão de download de arquivos
        'download.default_directory': address_download,
        'savefile.default_directory':address_download,
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True, 
        'download.prompt_for_download': False,

        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

        #Defini se deve ou não abrir o pdf no navegador
        # Definindo como TRUE ele não abre, e quando fizermos um get no link do pdf baixa diretamente
        'plugins.always_open_pdf_externally': True

            })
        
        try:
            
            self.driver = webdriver.Chrome(options=chrome_options)
      
        except:    

            self.driver = webdriver.Chrome(service=ChromeService(address_driver), options=chrome_options)
           
        
        self.wait = WebDriverWait(
        self.driver,
        30,
        poll_frequency=1, #de quantos em quantos segundos ele vai tentar interagir com o elemento
        ignored_exceptions=[
            NoSuchElementException, # não encontrou o elemento
            ElementNotVisibleException, # o elemento não esta visivel
            ElementNotSelectableException,# o elemento não esta selecionavel
            
        ] #são as exceções que serão ignoradas durante o tempo de espera definido
        )
        return self.driver, self.wait
    
    def make_login(self):
        """
        Esta função realiza o processo de login no Sap Ariba
        """

        username_field = self.wait.until(condicao_esperada.element_to_be_clickable(((By.ID, "UserName"))))
        password_field = self.wait.until(condicao_esperada.element_to_be_clickable(((By.ID, "Password"))))

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

        login_button = self.wait.until(condicao_esperada.element_to_be_clickable(((By.XPATH,'//input[@type="submit"]')))))
        login_button.click()

    def choose_options(self,option):
        """
        Choose need option for action:
        option = create, manage, recent
        """
        if option == 'create':
            option_create = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@_mid="Create"]')))
            option_create.click()
        elif option == 'manage':
            option_manage = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@_mid="Manage"]')))
            option_manage.click()
        else:
            option_recent = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@_mid="RecentlyViewed"]')))
            option_recent.click()

    def select_option_menu_list_front(self,option):
        options_menu = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,f'//a[@title="{option}"]')))
        options_menu.click()

    def button_create(self):
        sleep(1)
        try:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_arg5ed"]')))
        except:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_2t9nd"]')))
            
        button.click()

    def button_cancel(self):
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_g862r"]')))
        button.click()

    def button_ok(self):
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_9mwapd"]')))
        button.click()

    def button_ok_stop_event(self):
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_or6pxc"]')))
        button.click()

    def button_ok_event(self):
        sleep(1.5)
        try:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_i1irhb"]')))
        except:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_unvlac"]')))

        button.click()

    def button_advance(self):
        sleep(1)
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_0guilc"]')))
        name_button = button.text
        if name_button == 'Avançar':
            button.click()
        else:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_v3gq3d"]')))
            button.click()

    def button_invite_participants(self):
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_ynrewc"]')))
        button.click()

    def button_add_participants(self):
        try:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_kc7koc"]')))
        except:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_95bxmb"]')))
        button.click()

    def button_option_filter(self):
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_eykxgb"]')))
        button.click()

    def button_event_options_table(self):
        sleep(2)
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@id="_8wmqi"]')))
        button.click()

    def button_project_return(self):
        sleep(2)
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@id="_wn$ltc"]')))
        button.click()

    def button_option_menu_content(self):
        self.scrool_page_down()
        sleep(1)
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@id="_bmevqb"]')))
        button.click()

    def button_option_menu_participants(self):
        self.scrool_page_down()
        sleep(2)
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@id="_iqbn4"]')))
        sleep(1)
        button.click()

    def button_remove_content(self):
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_twpvcb"]')))
        button.click()

    def button_actions(self):
        self.driver.refresh()
        sleep(1)
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_rjo0yb"]')))
        button.click()

    def button_exclude_content(self):
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_tyoe4c"]')))
        button.click()

    def button_publish(self):
        self.driver.refresh()
        try:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_v3gq3d"]')))
        except:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_6jx8hd"]')))

        button.click()

    def button_completed(self):
        """
        Clica no botao CONCLUÍDO do formulário
        """
        try:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_mbeyvc"]')))
        except:
            button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_qjzssb"]')))

        button.click()

    def button_back(self):
        """
        Clica no botao '<' da página
        """
        sleep(1)
        button = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//a[@class="aw7_back-action"]')))
        while button[0].is_enabled() == False:
            sleep(1)
            button = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//a[@class="aw7_back-action"]')))

        button[0].click()

    def button_download_relatorio(self):
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_gyxz_"]')))
        button.click()

    def button_download_anexo(self):
        self.driver.refresh()
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_5wq_j"]')))
        button.click()

    def claro_icon(self):        
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@id="_yjxo0b"]')))
        button.click()

    def company_logo(self):  
        sleep(1)      
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a//img[@alt="Logotipo da empresa"]')))
        button.click()

    def claro_icon_back_initial_page(self):        
        button = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@id="_hfkuid"]')))
        button.click()

    def select_model(self, model):
        sleep(1)
        # Rolar pagina até o final
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        models = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//table[@class="tableBody"]//tr//td/label')))
        for itens in range(len(models)):
            item = self.driver.find_elements("xpath",'//table[@class="tableBody"]//tr//td/label')
            texto = item[itens].text
            if texto.upper() == model.upper():
                select_model = self.driver.find_elements("xpath",'//table[@class="tableBody"]//tr//td//label[@bh = "RDO"]')[itens]
                select_model.click()
                logging.info(f"TIPO DE GESTAO {model} SELECIONADO")
                break
    
    def insert_name_project(self,name_project):
        sleep(1)
        input_name_project_field = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//table[@class="mls mlsI is-iblock vaT"]//td/input')))
        input_name_project_field.clear()
        input_name_project_field.send_keys(name_project)
        sleep(2)

    def find_provider(self,acm_coding):

        """
        Essa função realiza a busca do fornecedor pelo ACM Coding
        """

        field_provider = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//div[@class = "w-chWrapRight"]')))
        field_provider[3].click()
        
        self.select_menu_option('pesquisar mais')

        field_research = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//td[@class="a-ssb-srch-pr"]/input')))
        field_research.send_keys(acm_coding)
        field_research.send_keys(Keys.ENTER)
        sleep(1)
        field_select = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//span[@class="selectColumnMarker"]')))
        field_select.click()
        sleep(1)
        self.button_ok()

    def select_menu_option(self,option):
        """
        Esta função seleciona a opção aberta no menu após clicarmos no documento
        """
        sleep(1)
        selected = False
        options_menu = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//div[@class="awmenu w-pm-menu"]//a')))
        for index, opcao in enumerate(options_menu):
            nome_opcao = options_menu[index].text
            # sleep(1)
            if option.upper() == nome_opcao.upper():
                # sleep(1)
                options_menu[index].click()
                selected = True
                break

        if selected == False:
            try:
                title = self.driver.find_element('xpath','//div//td//span[@class="w-page-head"]')
                sleep(1)
                title.click()
            except:
                options_menu[0].send_keys(Keys.ESCAPE)

    def select_sheet(self,name_sheet):
        '''
        Esta função refere-se a seleção das opções 
            - Visão Geral
            - Documentos
            - Tarefas
            - Equipe
            - Painel de Mensagens
            - Mensagens do Evento
            - Histórico
        '''
        sleep(2)
        self.driver.refresh()
        sheets = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//div[@type="pageTabs"]//li')))
        for sheet in sheets:
            if sheet.text == name_sheet:
                sheet.click()
                break
    
    def select_field(self,field):
        sleep(1)
        field_list = self.wait.until(condicao_esperada.visibility_of_any_elements_located((By.XPATH,f'//a[text()="{field}")]')))
        field_list[0].click()

    def select_field_column_nome(self,field):
        """
        Esta função seleciona as pastas/arquivos que estão na coluna "Nome"
        """
        sleep(1)
        fields_column = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,f'//table[@class="w-oc-table"]//td')))
        for index, opcao in enumerate(fields_column):
            field_name = fields_column[index].text
            field_name = field_name.strip()
            if field.upper() in field_name.upper():
                sleep(1)
                fields_column[index].click()
                break

    def select_field_column_document(self,field):
        """
        Esta função seleciona as pastas/arquivos que estão na coluna "Documento"
        """
        sleep(1)
        fields_column = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,f'//a[@class="hoverArrow hoverLink"]')))
        located = False
        for index, opcao in enumerate(fields_column):
            field_name = fields_column[index].text
            field_name = field_name.replace('\n',' ').upper()
            if field.upper() in field_name:
                sleep(1)
                fields_column[index].click()
                located = True
                break
        return located

    def data_event_field(self, data, reopen = False):
        """
        Esta função preenche o campo de data e hora do evento
        """

        if reopen:
            id_data = "_lbuldd"
            id_hour = "_wlixr"
        else:
            id_data = "_kbqgxd"
            id_hour = "_2_jtvc"

        field_data = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,f'//input[@id="{id_data}"]')))
        field_data.clear()
        field_data.send_keys(data)            
        field_hour = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,f'//input[@id="{id_hour}"]')))
        field_hour.clear()
        field_hour.send_keys('18:00') 
      
    def event_duration_field(self, days):
        """
            Esta função preenche o campo de duração do evento
        """	
        data_field = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//input[@id="_lrhcwd"]')))
        data_field.clear()
        data_field.send_keys(days)            
           
    def add_participant_event(self,email):
        """
        Esta função adiciona um participante ao evento
        """
        self.scrool_page_up()
        field_research = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//td[@id="_huxzwb"]/input')))
        field_research.click()
        field_research.clear()
        field_research.send_keys(email)
        field_research.send_keys(Keys.ENTER)
        sleep(2)
        self.driver.refresh()

        field_select = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//span[@class="selectColumnMarker"]')))
        sleep(2)
        field_select[1].click()
        sleep(1)
        try:
            participante_ja_adicionado = self.driver.find_element('xpath','//div[@class="w-msg-banner-close"]')
            participante_ja_adicionado.click()
        except:
            self.button_add_participants()

    def find_participants_in_content_interno(self,content,model):
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        participants_list = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//td[@align="left"]/span')))

        email_participant = Avaliadores_Pilar_Interno_teste[content]

        participants_count = int(len(participants_list) / 2)

        if model.upper() == 'GESTÃO DE FORNECEDORES - MATERIAIS':
            n_participantes = 2
        elif model.upper() == 'GESTÃO DE FORNECEDORES - SERVIÇOS':
            n_participantes = 3
        else:
            n_participantes = 4

        participants_removed = 0

        for id, email in enumerate(participants_list):
            if id % 2 != 0:
                if email_participant != participants_list[id].text:
                    participants_list[id - 1].click()
                    participants_removed +=1
                    if participants_removed == n_participantes:
                        self.button_remove_content()
                        sleep(1)
                        self.button_ok()
                        break

                if participants_count == 1:
                    self.button_ok()

    def find_participants_in_content_performance(self,content,qtd_participante_performance,participante_logistica):
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        participants_list = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//td[@align="left"]/span')))

        qtd_participantes_logistica = len(participante_logistica)
        participants_add_count = int(len(participants_list) / 2) #participantes adicionados
        n_participantes = qtd_participante_performance
        participants_removed = 0

        if n_participantes != participants_add_count:

                for id, email in enumerate(participants_list):
                    if id % 2 != 0:
                        email_participant = participants_list[id].text
                        if content != '5   LOGÍSTICA':
                            if email_participant in participante_logistica:
                                participants_list[id - 1].click()
                                participants_removed +=1
                                if participants_removed == qtd_participantes_logistica:
                                    self.button_remove_content()
                                    sleep(1)
                                    self.button_ok()
                                    break
                        elif content == '5   LOGÍSTICA':
                            if not email_participant in participante_logistica:
                                participants_list[id - 1].click()
                                participants_removed +=1
                                if participants_removed == n_participantes:
                                    self.button_remove_content()
                                    sleep(1)
                                    self.button_ok()
                                    break

        else:
            self.button_ok()

    def get_number_project(self):
        """
        Esta função retorna o número do projeto que estamos criando
        """
        ws_number = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//table[@class="leg-p-l-5 a-project-highlights-tbl"]/tbody/tr//td')))
        ws = ws_number[1].text

        return ws

    def selecionar_opcao_menu_tipo_documento(self,tipo_documento):
            sleep(1)
            selecionado = 'não'
            opcoes_menu = self.driver.find_elements('xpath','//div[@id="SearchBarCategoryMenuId"]//a')
            for index, opcao in enumerate(opcoes_menu):
                nome_opcao = opcoes_menu[index].text
                if tipo_documento == nome_opcao:
                    sleep(1)
                    opcoes_menu[index].click()
                   
                    selecionado = 'sim'

            return selecionado

    def selecionar_tipo_de_documento(self,tipo_documento):
        """
        Esta função realiza a seleção do tipo de documento que iremos consultar. Ex:
            - Solicitação de sourcing
            - Projeto de sourcing
        """
        tipo_documento_pesquisa = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//td[@class ='a-srch-bar-category']/a/span")))
        nome_documento_ja_selecionado = tipo_documento_pesquisa.text

        if nome_documento_ja_selecionado != tipo_documento:
            tipo_documento_pesquisa.click() 
            sleep(1)
            self.selecionar_opcao_menu_tipo_documento(tipo_documento)
        sleep(1) 

        try:
            botao_pesquisar = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//input[@id="_2wupab"]')))
            botao_pesquisar[0].send_keys(Keys.ENTER)
        except:
            botao_pesquisar = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_oshrwb"]')))
            botao_pesquisar.click()

    def click_in_project(self):
        """
        Abre o projeto pesquisado
        """
        sleep(1)
        self.driver.refresh()
        icone_projeto = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@id="_hjbmbc"]')))
        icone_projeto.click()

    def find_project(self, number_project):
        """
        Realiza a pesquisa do documento após a seleção do tipo do mesmo
        """
        input_field = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//tbody//td[@class="a-ssb-srch-pr"]/input')))

        input_field[0].clear()
        input_field[0].send_keys(number_project)

        input_field[1].clear()
        input_field[1].send_keys(number_project)
        input_field[1].send_keys(Keys.ENTER)

    def participants_invited(self):
        sleep(2)
        self.driver.refresh()
        try:

            participants_list = self.driver.find_element('xpath','//td[contains(text(),"Não há itens")]')
            count_participants = 0
        except:
            participants_list = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//tbody//td[@align="left"]')))
            count_participants = int(len(participants_list)/2)

        return count_participants
    
    def get_participants_email(self):
        email_list = []
        sleep(2)

        try:
            participants_list = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//tbody//td[@align="left"]/span')))
            
            for id, email in enumerate(participants_list):
                
                participant_data = participants_list[id].text
                if '@' in participant_data:
                    email_list.append(participant_data)
        except:
            pass

        return email_list

    def scrool_page_down(self):
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scrool_page_up(self):
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, 0);")

    def content_lgpd_excluded(self):
        """
        Esta função exclui o conteúdo LGPD do projeto
        """
        sleep(1)
        button_filter = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@id="_c9rd6c"]')))
        button_filter.click()
        sleep(2)
        self.select_menu_option('3 GOVERNANÇA')
        sleep(2)
        topics_list = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//tr[@class="awtDrg_outline awtDrp_outline stSectionRow"]')))

        for index, name in enumerate(topics_list):
            name_topic = topics_list[index].text
            if 'LGPD' in name_topic:
                sleep(2)
                topics_list[index].click()
                self.button_exclude_content()
                button_exclude = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_du3x8c"]')))
                button_exclude.click()

    def content_logistica_excluded(self):
        """
        Esta função exclui o conteúdo LOGÍSTICA do projeto
        """
        sleep(1)
        button_filter = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//a[@id="_c9rd6c"]')))
        button_filter.click()
        sleep(2)
        self.select_menu_option('5 LOGÍSTICA')
        sleep(2)

        topics_list = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//div[@class="yScroll tableBody"]//tr')))

        for index, name in enumerate(topics_list):
            name_topic = topics_list[index].text
            if 'LOGÍSTICA' in name_topic:
                sleep(2)
                topics_list[index].click()
                self.button_exclude_content()
                button_exclude = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//button[@id="_du3x8c"]')))
                button_exclude.click()
                break

    def close_search(self):
        sleep(2)
        try:
            button_close =self.driver.find_element('xpath','//div/img[@src="https://siteintercept.qualtrics.com/static/q-siteintercept/~/img/svg-close-btn-black-7.svg"]')
            
            button_close.click()
        except:
            pass

    def count_responses(self):
        
        sleep(2)
        table_responses = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//tr[@dr="1"]')))
        qtd_perguntas = len(table_responses)
        respondeu = 0
        participante_nao_respondeu = ''
        for id,response in enumerate(table_responses):
            id+=1
            teste = self.driver.find_elements('xpath',f'//tr[@dr="1"][{id}]/td')
            nome = teste[2].text
            email = teste[4].text
            resposta = teste[-1].text
            if resposta == ' ':
                participante_nao_respondeu = email + '; ' + participante_nao_respondeu
            else:
                respondeu +=1

            qtd_respostas = respondeu
        return qtd_perguntas,qtd_respostas,participante_nao_respondeu

    def select_all_itens_attachment(self):
        """
        Esta função seleciona todos os itens do anexo 
        """
        sleep(2)
        button_actions = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,'//div[@id="_rzeoqd"]')))
        button_actions.click()

    def attachment_count(self):
        """
        Esta função conta a quantidade de anexos que temos no projeto
        """
        sleep(1)
        attachments = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//td//div[@id="_ua63e"]')))
        count = int(attachments[0].text)

        return count
    
    def assumir_controle(self,nome):

        sleep(1)
        name = self.wait.until(condicao_esperada.element_to_be_clickable((By.XPATH,f'//tr//a[contains(text(),"{nome}")]')))
        name.click()
        sleep(1)
