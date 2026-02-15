
```markdown
# Flex y Metacompiladores con Python (PL/Y)

Este repositorio contiene la implementación de un **Analizador Léxico** utilizando Python 3.11 y la librería **PL/Y (Python Lex-Yacc)**, simulando el comportamiento de la herramienta FLEX.

El proyecto se enfoca en la aplicación de técnicas de compilación en el área de **Seguridad Informática**, específicamente para la tokenización de reglas de firewall y sistemas de detección de intrusos.
---

## 🛠️ Tecnologías Utilizadas
* **Python 3.11**: Lenguaje de programación.
* **PL/Y (Python Lex-Yacc)**: Librería para el análisis léxico y sintáctico.
* **Pipenv**: Gestor de entornos virtuales y dependencias.

---

## 📋 Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado Python 3.11 y Pipenv.

```bash
# Instalar pipenv si no lo tienes
pip install pipenv

```

---

## 🚀 Instalación y Configuración

1. **Clonar el repositorio o descargar los archivos.**
2. **Instalar las dependencias** definidas en el `Pipfile` ejecutando el siguiente comando en la raíz del proyecto:

```bash
pipenv install

```

3. **Activar el entorno virtual**:

```bash
pipenv shell

```

---

## 💻 Ejecución del Proyecto

### 1. Analizador de Reglas de Snort (Seguridad Informática)

Este script procesa una regla IDS y la divide en tokens (ACCION, PROTOCOLO, IP, etc.).

```bash
python lexer_snort.py

```

### 2. Analizador de Iptables

Este script procesa archivos de configuración de iptables.

```bash
python main.py

```

---

## 📝 Documentación Técnica (Punto 4 - Informe)

### Reflexión sobre la aplicación en Seguridad

El uso de metacompiladores como **PL/Y** permite la validación sintáctica en tiempo real de reglas de seguridad complejas. Al definir el lenguaje mediante expresiones regulares, garantizamos que el sistema de seguridad (Firewall/IDS) solo cargue configuraciones válidas, evitando vulnerabilidades por errores humanos en la escritura de reglas.

### Nota sobre el funcionamiento de PL/Y

El código utiliza introspección de Python. Las variables definidas con el prefijo `t_` son cargadas automáticamente por el motor de PLY para construir el autómata finito determinístico (AFD) sin necesidad de invocaciones manuales en el bucle principal.

---

## 👨‍💻 Autores

* **Cristian** (Punto 4)
* [Tu nombre/Otros integrantes]

```



Con este README actualizado, tendrás documentado el proyecto conforme a las exigencias del informe. ¿Necesitas añadir alguna otra sección técnica para la exposición grabada?

```