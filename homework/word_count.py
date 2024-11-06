# pylint: disable=broad-exception-raised

import os
import shutil
import glob
from itertools import groupby

def load_input(input_directory):
    """Funcion load_input"""
    sequence = []
    files = glob.glob(f"{input_directory}/*")
    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append((fileinput.filename(), line))
    return sequence


  
def run_job(input_directory, output_directory):
    """Job"""
    files = load_input(input_directory)

    from pprint import pprint
    pprint(files)

if __name__ == "__main__":
    run_job(
        "files/input",
        "files/output",
    )
  


  
def line_preprocessing(sequence):
    """Line Preprocessing"""
    sequence = [
        (key, value.translate(str.maketrans("", "", string.punctuation)).lower().strip())
        for key, value in sequence
    ]
    return sequence
  
  
  
  
def run_job(input_directory, output_directory):
    """Job"""
    sequence = load_input(input_directory)
    sequence = line_preprocessing(sequence)

    from pprint import pprint
    
    pprint(sequence)

    
    
    
    
def mapper(sequence):
    """Mapper"""
    # result = []
    # for _, value in sequence:
    #     for word in value.split():
    #         result.append( (word, 1) )  
    # return result
    return [(word, 1) for _, value in sequence for word in value.split()]
  
  
  
def run_job(input_directory, output_directory):
    """Job"""
    sequence = load_input(input_directory)
    sequence = line_preprocessing(sequence)
    sequence = mapper(sequence)

    from pprint import pprint
    pprint(sequence)
    
    
    
    
    }
  
def run_job(input_directory, output_directory):
    """Job"""
    sequence = load_input(input_directory)
    sequence = line_preprocessing(sequence)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)

    from pprint import pprint
    pprint(sequence)

    
    
    
def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])
  
  
  
def reducer(sequence):
    """Reducer"""
    result = {}
    for key, value in sequence:
        if key not in result.keys():
            result[key] = 0
        result[key] += value
    return list(result.items())
  
  


    
def run_job(input_directory, output_directory):
    """Job"""
    sequence = load_input(input_directory)
    sequence = line_preprocessing(sequence)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)

    from pprint import pprint
    pprint(sequence)

    
def create_ouptput_directory(output_directory):
    """Create Output Directory"""
    if os.path.exists(output_directory):
        for file in glob.glob(f"{output_directory}/*"):
            os.remove(file)
        os.rmdir(output_directory)
    os.makedirs(output_directory)
    
    

def run_job(input_directory, output_directory):
    """Job"""
    sequence = load_input(input_directory)
    sequence = line_preprocessing(sequence)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    create_ouptput_directory(output_directory)

    from pprint import pprint
    pprint(sequence)
