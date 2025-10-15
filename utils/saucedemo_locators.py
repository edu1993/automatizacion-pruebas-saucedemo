"""
Localizadores para elementos de la página SauceDemo
"""
from selenium.webdriver.common.by import By


class SauceDemoLocators:
    """Clase que contiene todos los localizadores para SauceDemo"""
    
    # Página de Login
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    # Página de Inventario
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCTS_TITLE = (By.CSS_SELECTOR, ".title")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    
    # Primer producto específico
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item:first-child .inventory_item_name")
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_item:first-child .inventory_item_price")
    FIRST_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".inventory_item:first-child [data-test^='add-to-cart']")
    
    # Menú y navegación
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    MENU_ITEMS = (By.CSS_SELECTOR, ".bm-item-list a")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    # Carrito de compras
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CART_ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    
    # Filtros
    PRODUCT_SORT_CONTAINER = (By.CSS_SELECTOR, ".product_sort_container")
    
    # Footer
    FOOTER = (By.CSS_SELECTOR, ".footer")
    
    # Botones de remoción del carrito
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "[data-test^='remove']")


class SauceDemoData:
    """Clase que contiene datos de prueba para SauceDemo"""
    
    # Credenciales válidas
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    
    # Credenciales inválidas
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "invalid_password"
    
    # URLs esperadas
    BASE_URL = "https://www.saucedemo.com/"
    LOGIN_URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    CART_URL = "https://www.saucedemo.com/cart.html"
    
    # Textos esperados
    PRODUCTS_PAGE_TITLE = "Products"
    SWAG_LABS_TITLE = "Swag Labs"
    
    # Mensajes de error esperados
    LOGIN_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
