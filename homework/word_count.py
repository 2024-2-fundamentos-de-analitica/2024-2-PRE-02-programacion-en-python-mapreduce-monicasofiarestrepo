# pylint: disable=broad-exception-raised

import os
import shutil
import glob
from itertools import groupby


def load_input(input_directory):
    """
    Recibe un folder y retorna una lista de tuplas donde el primer elemento
    de cada tupla es el nombre del archivo y el segundo es una línea del archivo.
    """
    result = []
    for filepath in glob.glob(os.path.join(input_directory, '*.txt')):
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                result.append((filename, line.strip()))
    return result


def line_preprocessing(sequence):
    """
    Recibe una lista de tuplas (archivo, línea) y retorna una lista de tuplas
    (clave, valor), donde se realiza el preprocesamiento de las líneas de texto.
    """
    processed = []
    for filename, line in sequence:
        # Procesar eliminando puntuación y llevando a minúsculas
        words = ''.join([char.lower() if char.isalnum() or char.isspace() else ' ' for char in line]).split()
        for word in words:
            processed.append((word, 1))
    return processed


def mapper(sequence):
    """
    Recibe una lista de tuplas (clave, valor) y retorna una lista de tuplas
    (clave, 1) para realizar el conteo de palabras.
    """
    return [(word, 1) for word, _ in sequence]


def shuffle_and_sort(sequence):
    """
    Recibe la lista de tuplas del mapper y retorna una lista ordenada por clave.
    """
    return sorted(sequence, key=lambda x: x[0])


def reducer(sequence):
    """
    Recibe el resultado de shuffle_and_sort y reduce los valores asociados a
    cada clave sumándolos.
    """
    reduced = []
    for key, group in groupby(sequence, lambda x: x[0]):
        count = sum(value for _, value in group)
        reduced.append((key, count))
    return reduced


def create_output_directory(output_directory):
    """
    Crea un directorio. Si el directorio existe, lo borra y lo crea de nuevo.
    """
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)
    os.makedirs(output_directory)


def save_output(output_directory, sequence):
    """
    Almacena el resultado del reducer en un archivo de texto llamado part-00000
    en el directorio dado, donde cada línea contiene una tupla separada por un tabulador.
    """
    output_path = os.path.join(output_directory, 'part-00000')
    with open(output_path, 'w', encoding='utf-8') as file:
        for key, value in sequence:
            file.write(f"{key}\t{value}\n")


def create_marker(output_directory):
    """
    Crea un archivo llamado _SUCCESS en el directorio dado.
    """
    success_path = os.path.join(output_directory, '_SUCCESS')
    with open(success_path, 'w', encoding='utf-8') as file:
        file.write('')


def run_job(input_directory, output_directory):
    """
    Orquesta todas las funciones anteriores en un flujo de trabajo completo.
    """
    create_output_directory(output_directory)
    data = load_input(input_directory)
    preprocessed_data = line_preprocessing(data)
    mapped_data = mapper(preprocessed_data)
    sorted_data = shuffle_and_sort(mapped_data)
    reduced_data = reducer(sorted_data)
    save_output(output_directory, reduced_data)
    create_marker(output_directory)


if __name__ == "__main__":
    run_job("input", "output")
