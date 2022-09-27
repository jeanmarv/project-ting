import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    for itens in instance._data:
        if itens["nome_do_arquivo"] == path_file:
            return
    txt_archive = txt_importer(path_file)
    archives = {
      "nome_do_arquivo": path_file,
      "qtd_linhas": len(txt_archive),
      "linhas_do_arquivo": txt_archive
    }
    instance.enqueue(archives)
    print(archives)


def remove(instance):
    try:
        remove = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {remove} removido com sucesso\n")
    except IndexError:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        sys.stdout.write(str(metadata))
    except IndexError:
        sys.stderr.write("Posição inválida")

