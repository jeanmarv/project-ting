def exists_word(word, instance):
    occurrence = []
    all_files = []
    for index in range(len(instance)):
        searched = instance.search(index)
        for index2, itens in enumerate(searched["linhas_do_arquivo"]):
            if word.lower() in itens.lower():
                occurrence.append({"linha": index2 + 1})
            else:
                all_files.append({
                    "arquivo": searched["nome_do_arquivo"],
                    "ocorrencias": occurrence,
                    "palavra": word,
                })
    if len(occurrence) == 0:
        return []
    else:
        return all_files


def search_by_word(word, instance):
    occurrence = []
    all_files = []
    for index in range(len(instance)):
        searched = instance.search(index)
        for index2, itens in enumerate(searched["linhas_do_arquivo"]):
            if word.lower() in itens.lower():
                occurrence.append({"linha": index2 + 1, "conteudo": itens})
            else:
                all_files.append({
                    "arquivo": searched["nome_do_arquivo"],
                    "ocorrencias": occurrence,
                    "palavra": word,
                })
    if len(occurrence) == 0:
        return []
    else:
        return all_files