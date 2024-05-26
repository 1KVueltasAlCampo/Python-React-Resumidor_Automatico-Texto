# Resumidor de Textos

## Descripción

Esta es una aplicación web que permite resumir textos de entre 300 y 500 palabras. La aplicación está construida con una API en Flask para el backend y una aplicación en React para el frontend.
Adicionalmente, contiene un Notebook de Jupyter en donde se explica a detalle el funcionamiento del algoritmo de resumen.

## Requisitos

- Python 3.7+
- Node.js 14+

## Instalación

Nota: Para ejecutar todos estos comandos, se debe procurar usar una terminal con permisos de administrador.

### 1. Clonar el repositorio

```bash
git clone https://github.com/1KVueltasAlCampo/Python-React-Resumidor_Automatico-Texto
cd Python-React-Resumidor_Automatico-Texto
```

### 2. Configurar el backend (Flask)
#### Crear un entorno virtual e instalar dependencias
##### Para Windows
```bash
py -3 -m venv .venv
.venv\Scripts\activate
pip install flask
pip install nltk
py app.py 
```
##### Para Linux o Mac
```bash
python3 -m venv .venv
.venv\Scripts\activate
pip install flask
pip install nltk
py app.py 
```
### 2. Configurar el backend (Flask)
Preferiblemente en otra terminal:
```bash
cd front-resumidor
npm install
npm start
```

### 3. Abrir la pagina web
Si por defecto no se abre la pagina web de la aplicacion, acceder a ella mediante la direccion indicada en la terminal correspondiente al Front. Por defecto es http://localhost:3000

### 4. Usar la aplicacion
A continuacion, ingresar en el area de texto, aquello que se quiere resumir, al presionar el boton "Resumir" se obtendra el resultado.
