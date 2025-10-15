# 🚀 Automatización de Pruebas - SauceDemo

## 📋 Propósito del Proyecto

Este proyecto implementa una suite de pruebas automatizadas para el sitio web [SauceDemo](https://www.saucedemo.com/), desarrollado como pre-entrega del curso de Automatización QA. El objetivo es demostrar la capacidad de automatizar flujos básicos de navegación web utilizando Selenium WebDriver y Python.

### 🎯 Funcionalidades Automatizadas

- **Login Automatizado**: Validación de credenciales y redirección exitosa
- **Navegación del Catálogo**: Verificación de productos y elementos de la interfaz
- **Interacción con Carrito**: Agregar productos y validar funcionalidad del carrito

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal de desarrollo
- **Selenium WebDriver**: Framework para automatización web
- **Pytest**: Framework de testing y generación de reportes
- **WebDriver Manager**: Gestión automática de drivers del navegador
- **Chrome WebDriver**: Driver para automatización en Google Chrome

### 📦 Dependencias Principales

```
selenium==4.15.2
pytest==7.4.3
pytest-html==4.1.1
webdriver-manager==4.0.1
```

## 📁 Estructura del Proyecto

```
entrega/
├── tests/                      # Directorio de pruebas
│   ├── __init__.py
│   └── test_saucedemo.py      # Suite principal de pruebas
├── utils/                      # Utilidades y funciones auxiliares
│   ├── __init__.py
│   ├── web_driver_utils.py    # Utilidades de WebDriver
│   └── saucedemo_locators.py  # Localizadores y datos de prueba
├── reports/                    # Reportes y capturas de pantalla
│   └── .gitkeep
├── requirements.txt           # Dependencias del proyecto
├── pytest.ini               # Configuración de Pytest
└── README.md                # Documentación del proyecto
```

## 🚀 Instalación y Configuración

### 1. Prerrequisitos

- Python 3.8 o superior
- Google Chrome instalado
- Git (para clonar el repositorio)

### 2. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd entrega
```

### 3. Crear Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

### 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

## 🧪 Ejecución de Pruebas

### Ejecutar Todas las Pruebas

```bash
pytest tests/test_saucedemo.py -v
```

### Generar Reporte HTML

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

### Ejecutar Pruebas Específicas

```bash
# Solo test de login
pytest tests/test_saucedemo.py::TestSauceDemo::test_login_exitoso -v

# Solo test de catálogo
pytest tests/test_saucedemo.py::TestSauceDemo::test_navegacion_y_verificacion_catalogo -v

# Solo test de carrito
pytest tests/test_saucedemo.py::TestSauceDemo::test_interaccion_con_productos_carrito -v
```

### Opciones Adicionales

```bash
# Ejecutar con mayor verbosidad
pytest tests/test_saucedemo.py -vv

# Ejecutar y detener en el primer fallo
pytest tests/test_saucedemo.py -x

# Ejecutar con captura de logs
pytest tests/test_saucedemo.py -v -s
```

## 📊 Casos de Prueba Implementados

### 1. Test de Login Exitoso (`test_login_exitoso`)

**Objetivo**: Validar el proceso de autenticación en SauceDemo

**Pasos**:
1. Navegar a la página de login
2. Ingresar credenciales válidas (`standard_user` / `secret_sauce`)
3. Hacer clic en el botón de login
4. Validar redirección a `/inventory.html`
5. Verificar presencia de elementos clave (título "Products", "Swag Labs")

**Criterios de Éxito**:
- Login exitoso con espera explícita
- Validación de URL `/inventory.html`
- Verificación de título "Products/Swag Labs"

### 2. Test de Navegación y Verificación del Catálogo (`test_navegacion_y_verificacion_catalogo`)

**Objetivo**: Verificar la correcta visualización y funcionalidad del catálogo de productos

**Pasos**:
1. Realizar login automático
2. Verificar título de la página de inventario
3. Comprobar presencia de productos (mínimo uno)
4. Validar elementos de interfaz (menú, filtros, carrito)
5. Extraer y mostrar información del primer producto

**Criterios de Éxito**:
- Validación de título correcto
- Presencia de productos confirmada
- Lista nombre/precio del primer producto
- Elementos de navegación presentes

### 3. Test de Interacción con Productos y Carrito (`test_interaccion_con_productos_carrito`)

**Objetivo**: Validar la funcionalidad de agregar productos al carrito

**Pasos**:
1. Realizar login automático
2. Agregar primer producto al carrito
3. Verificar incremento del contador del carrito
4. Navegar al carrito de compras
5. Comprobar producto en el carrito (nombre y precio)

**Criterios de Éxito**:
- Producto agregado exitosamente
- Contador del carrito actualizado
- Verificación de ítem en carrito con datos correctos

## 🔧 Características Técnicas

### Utilidades Implementadas

#### `WebDriverUtils`
- Configuración automática de ChromeDriver
- Esperas explícitas para elementos
- Métodos seguros para interacción (click, send_keys)
- Captura de screenshots automática
- Gestión de timeouts personalizables

#### `SauceDemoLocators`
- Localizadores organizados por página
- Datos de prueba centralizados
- Constantes para URLs y textos esperados

### Manejo de Errores

- **Screenshots automáticos** en caso de fallo
- **Esperas explícitas** para evitar errores de timing
- **Validaciones robustas** con mensajes descriptivos
- **Cleanup automático** de recursos (driver)

### Reportes y Evidencias

- **Reportes HTML** detallados con Pytest
- **Capturas de pantalla** automáticas en fallos
- **Logs descriptivos** durante la ejecución
- **Timestamps** en archivos de evidencia

## 📈 Interpretación de Resultados

### Reporte HTML

El reporte HTML generado incluye:
- **Resumen ejecutivo** con estadísticas de pruebas
- **Detalles de cada test** con pasos ejecutados
- **Tiempos de ejecución** por prueba
- **Enlaces a screenshots** en caso de fallos
- **Logs detallados** de la ejecución

### Estados de Pruebas

- ✅ **PASSED**: Prueba ejecutada exitosamente
- ❌ **FAILED**: Prueba falló, revisar detalles y screenshot
- ⚠️ **SKIPPED**: Prueba omitida (si aplica)

## 🐛 Solución de Problemas

### Problemas Comunes

1. **ChromeDriver no encontrado**
   - Solución: WebDriver Manager se encarga automáticamente

2. **Timeouts en elementos**
   - Verificar conectividad a internet
   - Aumentar timeout en `WebDriverUtils(timeout=15)`

3. **Elementos no encontrados**
   - Verificar que SauceDemo esté disponible
   - Revisar localizadores en `saucedemo_locators.py`

### Logs y Debugging

```bash
# Ejecutar con logs detallados
pytest tests/test_saucedemo.py -v -s --log-cli-level=INFO
```

## 🤝 Contribución

Para contribuir al proyecto:

1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📝 Notas Adicionales

- Las pruebas están diseñadas para ser **independientes** entre sí
- Se utiliza **Page Object Model** parcial con localizadores centralizados
- **Esperas explícitas** implementadas para mayor estabilidad
- **Cleanup automático** de recursos en cada prueba

## 📞 Contacto

Para dudas o sugerencias sobre este proyecto, contactar al desarrollador.

---

**Desarrollado como parte del curso de Automatización QA** 🎓
