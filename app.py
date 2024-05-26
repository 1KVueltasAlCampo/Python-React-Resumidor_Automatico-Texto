import heapq
from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)
CORS(app)

def calcular_frecuencia(texto):
    frecuencia_palabras = {}
    palabras_vacias = set(stopwords.words('spanish'))

    for palabra in word_tokenize(texto, language="spanish"):
        if palabra.isalpha() and palabra not in palabras_vacias:
            if palabra not in frecuencia_palabras:
                frecuencia_palabras[palabra] = 1
            else:
                frecuencia_palabras[palabra] += 1

    return frecuencia_palabras

def seleccionar_mejores_oraciones(lista_oraciones, puntuacion_oraciones, max_palabras):
    resumen = []
    cantidad_palabras = 0

    for oracion in lista_oraciones:
        palabras = word_tokenize(oracion, language="spanish")
        if cantidad_palabras + len(palabras) <= max_palabras:
            resumen.append(oracion)
            cantidad_palabras += len(palabras)
        else:
            break

    return resumen

def obtener_palabras_clave(texto):
    frecuencia_palabras = calcular_frecuencia(texto)
    palabras_clave = heapq.nlargest(5, frecuencia_palabras, key=frecuencia_palabras.get)
    palabras_clave_filtradas = [palabra for palabra in palabras_clave if palabra.lower() not in ['para', 'sobre', 'de', 'en', 'con', 'los', 'las', 'del', 'la', 'el', 'y', 'a', 'un', 'una', 'su', 'sus', 'sus', 'se', 'es', 'que', 'no', 'al', 'o', 'por', 'como', 'lo', 'si', 'para', 'más', 'también', 'hasta', 'pero', 'ante', 'sí', 'sobre', 'tras', 'durante', 'aunque', 'entre', 'así', 'mientras', 'ya', 'cuando', 'donde', 'quien', 'cual', 'cada', 'todo', 'otro', 'otra', 'otros', 'otras', 'algo', 'alguien', 'nadie', 'ninguno', 'ninguna', 'cómo', 'cuál', 'cuáles', 'cuán', 'cuánto', 'cuánta', 'cuántos', 'cuántas', 'qué', 'dónde', 'cómo', 'por qué', 'para qué', 'quién', 'quiénes', 'cuál', 'cuáles']]
    
    return palabras_clave_filtradas

def resumir_texto(texto):
    lista_oraciones = [oracion for oracion in texto.split('.') if oracion]

    frecuencia_palabras = calcular_frecuencia(texto)

    frecuencia_maxima = max(frecuencia_palabras.values())
    for palabra in frecuencia_palabras.keys():
        frecuencia_palabras[palabra] = frecuencia_palabras[palabra] / frecuencia_maxima

    puntuacion_oraciones = {}
    for oracion in lista_oraciones:
        for palabra in word_tokenize(oracion, language="spanish"):
            if palabra.isalpha() and palabra in frecuencia_palabras.keys():
                if oracion not in puntuacion_oraciones.keys():
                    puntuacion_oraciones[oracion] = frecuencia_palabras[palabra]
                else:
                    puntuacion_oraciones[oracion] += frecuencia_palabras[palabra]

    oraciones_resumen = heapq.nlargest(5, puntuacion_oraciones, key=puntuacion_oraciones.get)

    resumen = seleccionar_mejores_oraciones(lista_oraciones, puntuacion_oraciones, 100)
    resumen = '.'.join(resumen)
    resumen = resumen.replace('\n\n', '\n')

    palabras_titulo = obtener_palabras_clave(texto)
    titulo = ', '.join(palabras_titulo).title()
    
    resultado = f"Palabras Clave:\n{titulo}\n\nResumen:\n{resumen}"
    return resultado

@app.route('/api/resumir', methods=['POST'])
def resumir():
    data = request.get_json()
    texto = data.get('texto', '')
    if len(texto.split()) < 300 or len(texto.split()) > 500:
        length = len(texto.split())
        return jsonify({'error': 'El texto debe tener entre 300 y 500 palabras. Actualmente tiene {}'.format(length)}), 400
    try:
        return jsonify({'resumen': resumir_texto(texto)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
