"""
Utilidades para manejo de WebDriver y operaciones comunes de Selenium
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time


class WebDriverUtils:
    """Clase utilitaria para operaciones comunes con WebDriver"""
    
    def __init__(self, timeout=10):
        """
        Inicializa las utilidades de WebDriver
        
        Args:
            timeout (int): Tiempo de espera por defecto en segundos
        """
        self.timeout = timeout
        self.driver = None
    
    def setup_driver(self):
        """
        Configura e inicializa el WebDriver de Chrome
        
        Returns:
            webdriver.Chrome: Instancia del driver configurado
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Ejecutar en modo headless
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Usar chromedriver del sistema directamente
        service = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return self.driver
    
    def wait_for_element(self, locator, timeout=None):
        """
        Espera a que un elemento sea visible
        
        Args:
            locator (tuple): Tupla con (By, valor) para localizar el elemento
            timeout (int): Tiempo de espera personalizado
            
        Returns:
            WebElement: Elemento encontrado
            
        Raises:
            TimeoutException: Si el elemento no se encuentra en el tiempo especificado
        """
        wait_time = timeout if timeout else self.timeout
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_clickable(self, locator, timeout=None):
        """
        Espera a que un elemento sea clickeable
        
        Args:
            locator (tuple): Tupla con (By, valor) para localizar el elemento
            timeout (int): Tiempo de espera personalizado
            
        Returns:
            WebElement: Elemento clickeable
        """
        wait_time = timeout if timeout else self.timeout
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_url_contains(self, url_fragment, timeout=None):
        """
        Espera a que la URL contenga un fragmento específico
        
        Args:
            url_fragment (str): Fragmento de URL a esperar
            timeout (int): Tiempo de espera personalizado
            
        Returns:
            bool: True si la URL contiene el fragmento
        """
        wait_time = timeout if timeout else self.timeout
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.url_contains(url_fragment))
    
    def safe_click(self, locator, timeout=None):
        """
        Hace clic de forma segura en un elemento, esperando a que sea clickeable
        
        Args:
            locator (tuple): Tupla con (By, valor) para localizar el elemento
            timeout (int): Tiempo de espera personalizado
        """
        element = self.wait_for_clickable(locator, timeout)
        element.click()
    
    def safe_send_keys(self, locator, text, timeout=None):
        """
        Envía texto de forma segura a un elemento, esperando a que sea visible
        
        Args:
            locator (tuple): Tupla con (By, valor) para localizar el elemento
            text (str): Texto a enviar
            timeout (int): Tiempo de espera personalizado
        """
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def get_element_text(self, locator, timeout=None):
        """
        Obtiene el texto de un elemento de forma segura
        
        Args:
            locator (tuple): Tupla con (By, valor) para localizar el elemento
            timeout (int): Tiempo de espera personalizado
            
        Returns:
            str: Texto del elemento
        """
        element = self.wait_for_element(locator, timeout)
        return element.text
    
    def is_element_present(self, locator):
        """
        Verifica si un elemento está presente en la página
        
        Args:
            locator (tuple): Tupla con (By, valor) para localizar el elemento
            
        Returns:
            bool: True si el elemento está presente
        """
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def get_elements(self, locator, timeout=None):
        """
        Obtiene una lista de elementos
        
        Args:
            locator (tuple): Tupla con (By, valor) para localizar los elementos
            timeout (int): Tiempo de espera personalizado
            
        Returns:
            list: Lista de WebElements
        """
        wait_time = timeout if timeout else self.timeout
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)
    
    def take_screenshot(self, filename):
        """
        Toma una captura de pantalla
        
        Args:
            filename (str): Nombre del archivo para guardar la captura
        """
        self.driver.save_screenshot(filename)
    
    def quit_driver(self):
        """Cierra el navegador y termina la sesión del driver"""
        if self.driver:
            self.driver.quit()
            self.driver = None
