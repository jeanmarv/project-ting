import sys

def txt_importer(path_file):
    try:
        if '.txt' not in path_file:
            return sys.stderr.write("Formato inválido\n")
        with open(path_file) as file:
            file_open = file.read().splitlines()
            return file_open
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")