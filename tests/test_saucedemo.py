"""
Tests automatizados para SauceDemo
Incluye pruebas de login, navegación del catálogo e interacción con productos
"""
import pytest
import os
import sys
from datetime import datetime

# Agregar el directorio padre al path para importar utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.web_driver_utils import WebDriverUtils
from utils.saucedemo_locators import SauceDemoLocators, SauceDemoData


class TestSauceDemo:
    """Clase principal de pruebas para SauceDemo"""
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """
        Fixture que se ejecuta antes y después de cada test
        Configura el driver y lo cierra al finalizar
        """
        # Setup
        self.web_utils = WebDriverUtils(timeout=10)
        self.driver = self.web_utils.setup_driver()
        
        yield
        
        # Teardown
        self.web_utils.quit_driver()
    
    def test_login_exitoso(self):
        """
        Prueba de login exitoso
        
        Pasos:
        1. Navegar a la página de login
        2. Ingresar credenciales válidas
        3. Hacer clic en el botón de login
        4. Validar redirección a página de inventario
        5. Validar presencia de elementos clave
        """
        # Paso 1: Navegar a la página de login
        self.driver.get(SauceDemoData.LOGIN_URL)
        
        # Paso 2 y 3: Ingresar credenciales y hacer login
        self.web_utils.safe_send_keys(
            SauceDemoLocators.USERNAME_INPUT, 
            SauceDemoData.VALID_USERNAME
        )
        self.web_utils.safe_send_keys(
            SauceDemoLocators.PASSWORD_INPUT, 
            SauceDemoData.VALID_PASSWORD
        )
        self.web_utils.safe_click(SauceDemoLocators.LOGIN_BUTTON)
        
        # Paso 4: Validar redirección a página de inventario
        self.web_utils.wait_for_url_contains("/inventory.html")
        current_url = self.driver.current_url
        assert "/inventory.html" in current_url, f"URL esperada contiene '/inventory.html', actual: {current_url}"
        
        # Paso 5: Validar presencia de elementos clave
        # Verificar título "Products"
        products_title = self.web_utils.get_element_text(SauceDemoLocators.PRODUCTS_TITLE)
        assert products_title == SauceDemoData.PRODUCTS_PAGE_TITLE, f"Título esperado: {SauceDemoData.PRODUCTS_PAGE_TITLE}, actual: {products_title}"
        
        # Verificar que el título de la página contiene "Swag Labs"
        page_title = self.driver.title
        assert SauceDemoData.SWAG_LABS_TITLE in page_title, f"El título de la página debe contener '{SauceDemoData.SWAG_LABS_TITLE}', actual: {page_title}"
        
        # Verificar presencia del contenedor de inventario
        assert self.web_utils.is_element_present(SauceDemoLocators.INVENTORY_CONTAINER), "El contenedor de inventario debe estar presente"
        
        print("✅ Prueba de login exitoso completada")
    
    def test_navegacion_y_verificacion_catalogo(self):
        """
        Prueba de navegación y verificación del catálogo
        
        Pasos:
        1. Realizar login
        2. Verificar título de la página de inventario
        3. Comprobar presencia de productos
        4. Validar elementos de la interfaz
        5. Listar información del primer producto
        """
        # Paso 1: Realizar login
        self._realizar_login()
        
        # Paso 2: Verificar título de la página de inventario
        products_title = self.web_utils.get_element_text(SauceDemoLocators.PRODUCTS_TITLE)
        assert products_title == SauceDemoData.PRODUCTS_PAGE_TITLE, f"Título esperado: {SauceDemoData.PRODUCTS_PAGE_TITLE}, actual: {products_title}"
        
        # Paso 3: Comprobar presencia de productos (al menos uno)
        productos = self.web_utils.get_elements(SauceDemoLocators.PRODUCT_ITEMS)
        assert len(productos) > 0, "Debe haber al menos un producto visible en la página"
        print(f"✅ Se encontraron {len(productos)} productos en el catálogo")
        
        # Paso 4: Validar elementos importantes de la interfaz
        # Verificar menú hamburguesa
        assert self.web_utils.is_element_present(SauceDemoLocators.BURGER_MENU), "El menú hamburguesa debe estar presente"
        
        # Verificar filtros
        assert self.web_utils.is_element_present(SauceDemoLocators.PRODUCT_SORT_CONTAINER), "Los filtros deben estar presentes"
        
        # Verificar carrito de compras
        assert self.web_utils.is_element_present(SauceDemoLocators.SHOPPING_CART_LINK), "El carrito de compras debe estar presente"
        
        # Paso 5: Listar información del primer producto
        primer_producto_nombre = self.web_utils.get_element_text(SauceDemoLocators.FIRST_PRODUCT_NAME)
        primer_producto_precio = self.web_utils.get_element_text(SauceDemoLocators.FIRST_PRODUCT_PRICE)
        
        assert primer_producto_nombre, "El primer producto debe tener un nombre"
        assert primer_producto_precio, "El primer producto debe tener un precio"
        
        print(f"✅ Primer producto - Nombre: {primer_producto_nombre}, Precio: {primer_producto_precio}")
        
        print("✅ Prueba de navegación y verificación del catálogo completada")
    
    def test_interaccion_con_productos_carrito(self):
        """
        Prueba de interacción con productos y carrito
        
        Pasos:
        1. Realizar login
        2. Añadir primer producto al carrito
        3. Verificar incremento del contador del carrito
        4. Navegar al carrito
        5. Comprobar que el producto aparece en el carrito
        """
        # Paso 1: Realizar login
        self._realizar_login()
        
        # Obtener información del primer producto antes de agregarlo
        primer_producto_nombre = self.web_utils.get_element_text(SauceDemoLocators.FIRST_PRODUCT_NAME)
        primer_producto_precio = self.web_utils.get_element_text(SauceDemoLocators.FIRST_PRODUCT_PRICE)
        
        # Paso 2: Añadir primer producto al carrito
        self.web_utils.safe_click(SauceDemoLocators.FIRST_ADD_TO_CART_BUTTON)
        print(f"✅ Producto '{primer_producto_nombre}' agregado al carrito")
        
        # Paso 3: Verificar incremento del contador del carrito
        contador_carrito = self.web_utils.wait_for_element(SauceDemoLocators.SHOPPING_CART_BADGE)
        contador_texto = contador_carrito.text
        assert contador_texto == "1", f"El contador del carrito debe mostrar '1', actual: {contador_texto}"
        print(f"✅ Contador del carrito actualizado correctamente: {contador_texto}")
        
        # Paso 4: Navegar al carrito
        self.web_utils.safe_click(SauceDemoLocators.SHOPPING_CART_LINK)
        self.web_utils.wait_for_url_contains("/cart.html")
        
        current_url = self.driver.current_url
        assert "/cart.html" in current_url, f"Debe estar en la página del carrito, URL actual: {current_url}"
        
        # Paso 5: Comprobar que el producto aparece correctamente en el carrito
        items_carrito = self.web_utils.get_elements(SauceDemoLocators.CART_ITEMS)
        assert len(items_carrito) == 1, f"Debe haber exactamente 1 item en el carrito, actual: {len(items_carrito)}"
        
        # Verificar que el nombre del producto en el carrito coincide
        nombre_en_carrito = self.web_utils.get_element_text(SauceDemoLocators.CART_ITEM_NAMES)
        assert nombre_en_carrito == primer_producto_nombre, f"Nombre en carrito '{nombre_en_carrito}' debe coincidir con '{primer_producto_nombre}'"
        
        # Verificar que el precio del producto en el carrito coincide
        precio_en_carrito = self.web_utils.get_element_text(SauceDemoLocators.CART_ITEM_PRICES)
        assert precio_en_carrito == primer_producto_precio, f"Precio en carrito '{precio_en_carrito}' debe coincidir con '{primer_producto_precio}'"
        
        print(f"✅ Producto verificado en carrito - Nombre: {nombre_en_carrito}, Precio: {precio_en_carrito}")
        print("✅ Prueba de interacción con productos y carrito completada")
    
    def _realizar_login(self):
        """
        Método auxiliar para realizar login
        Utilizado por múltiples tests para evitar duplicación de código
        """
        self.driver.get(SauceDemoData.LOGIN_URL)
        self.web_utils.safe_send_keys(SauceDemoLocators.USERNAME_INPUT, SauceDemoData.VALID_USERNAME)
        self.web_utils.safe_send_keys(SauceDemoLocators.PASSWORD_INPUT, SauceDemoData.VALID_PASSWORD)
        self.web_utils.safe_click(SauceDemoLocators.LOGIN_BUTTON)
        self.web_utils.wait_for_url_contains("/inventory.html")
    
    @pytest.fixture(autouse=True)
    def capture_screenshot_on_failure(self, request):
        """
        Fixture para capturar screenshot en caso de fallo
        """
        yield
        
        # Verificar si el test falló
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            # Crear directorio de reportes si no existe
            reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
            os.makedirs(reports_dir, exist_ok=True)
            
            # Generar nombre de archivo con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = request.node.name
            screenshot_name = f"failure_{test_name}_{timestamp}.png"
            screenshot_path = os.path.join(reports_dir, screenshot_name)
            
            # Tomar screenshot
            if hasattr(self, 'web_utils') and self.web_utils.driver:
                self.web_utils.take_screenshot(screenshot_path)
                print(f"📸 Screenshot guardado: {screenshot_path}")


# Hook global para pytest
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar el resultado del test"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
