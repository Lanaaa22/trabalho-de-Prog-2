import pickle
import math
import time
#entrada - (24,6,2025)
def categoria(data): 
    idade_atual = idade(data) # Calcula apenas uma vez 
    if idade_atual < 20: 
        return 0 
    elif 20 <= idade_atual <= 39: 
        return 1 
    else: return 2
    
# Retorna a idade do competidor quando colocamos a data de nascimento
def idade(data):
    data_ref = (24,6,2025)
    dia_r,mes_r,ano_r = data_ref
    dia,mes,ano = data
    idade = ano_r - ano
    if mes > mes_r:
        idade -= 1
    elif mes == mes_r:
        if dia > dia_r:
            idade -= 1
    return idade

#categoria 1: sub 20
#categoria 2: 20 a 39
#categoria 3: 40+
def categoria(data):
    idade_atual = idade(data)
    if idade_atual < 20:
        return 0
    elif idade_atual <= 39:
        return 1
    else:
        return 2

#Recebe o arquivo .bin e coloca em uma variável
def leDicionario():
    with open("entrada1000000.bin", "rb") as f: #  <------------ AQUI QUE MUDA A ENTRADA .BIN 
        dic = pickle.load(f)
    return dic

#Cria a lista do dicionário
def criarLista(d):
    cat0 = 0
    cat1 = 0
    l = []
    for chave in d:
        if categoria(d[chave][1]) == 0:
            cat0 += 1
            l.append(chave)
    for chave in d:
        if categoria(d[chave][1]) == 1:
            cat1 += 1
            l.append(chave)
    for chave in d:
        if categoria(d[chave][1]) == 2:
            l.append(chave)
    return l,cat0,cat1

#QuickSort
def quickSort(l, inf, sup, d): 
    if inf < sup:
        pos = particao(l, inf, sup, d)
        quickSort(l, inf, pos - 1, d)
        quickSort(l, pos + 1, sup, d)

def particao(l, inf, sup, d):
    pivot = l[inf]
    i = inf + 1
    j = sup
    while i <= j:
        while i <= j and chave_ord(l[i], d) < chave_ord(pivot, d):
            i += 1
        while i <= j and chave_ord(l[j], d) > chave_ord(pivot, d):
            j -= 1
        if i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
    l[j], l[inf] = l[inf], l[j]
    return j

#Retorna os parâmetros para a partição do quicksort
def chave_ord(chave, d):
    nome, data, reps, tempo = d[chave]
    nome_min = nome#.lower()
    return (-reps, tempo, nome_min, chave)

#DEFINE FINALISTAS SUB20
def finalistas0(d, l, cat0, f):
    vagas = math.ceil(cat0 * (1/3))
    primeiraVez = True
    pos = 1
    for posicao in range(cat0):
        if posicao < vagas:
            adicionaArquivo(f, d, l, posicao, "SUB20", primeiraVez, pos)
            primeiraVez = False
            pos += 1

        if posicao == vagas - 1:
            # Verifica empates com o último classificado
            ultimo_reps = d[l[posicao]][2]
            ultimo_tempo = d[l[posicao]][3]

            i = posicao + 1
            while i < cat0 and d[l[i]][2] == ultimo_reps and d[l[i]][3] == ultimo_tempo:
                adicionaArquivo(f, d, l, i, "SUB20", False, pos)
                i += 1
            return  # Sai do loop principal depois do grupo de empatados


#DEFINE FINALISTAS 20-39
def finalistas1(d, l, cat0, cat1, f):
    inicio = cat0
    fim = cat0 + cat1
    vagas = math.ceil(cat1 * (1/3))
    primeiraVez = True
    pos = 1

    for i in range(inicio, fim):
        if i - inicio < vagas:
            adicionaArquivo(f, d, l, i, "20-39", primeiraVez, pos)
            primeiraVez = False
            pos += 1
        # Verifica empates com o último classificado
        if i - inicio == vagas - 1:
            ultimo_reps = d[l[i]][2]
            ultimo_tempo = d[l[i]][3]

            j = i + 1
            while j < fim and d[l[j]][2] == ultimo_reps and d[l[j]][3] == ultimo_tempo:
                adicionaArquivo(f, d, l, j, "20-39", False, pos)
                j += 1
            return # Sai do loop principal depois do grupo de empatados

#DEFINE FINALISTAS 40+
def finalistas2(d, l, cat0, cat1, f):
    inicio = cat0 + cat1
    fim = len(l)
    cat2 = fim - inicio
    vagas = math.ceil(cat2 * (1/3))
    primeiraVez = True
    pos = 1
    # Verifica empates com o último classificado
    for i in range(inicio, fim):
        if i - inicio < vagas:
            adicionaArquivo(f, d, l, i, "40+", primeiraVez, pos)
            primeiraVez = False
            pos += 1

        if i - inicio == vagas - 1:
            ultimo_reps = d[l[i]][2]
            ultimo_tempo = d[l[i]][3]

            j = i + 1
            while j < fim and d[l[j]][2] == ultimo_reps and d[l[j]][3] == ultimo_tempo:
                adicionaArquivo(f, d, l, j, "40+", False, pos)
                j += 1
            return # Sai do loop principal depois do grupo de empatados

                            
    
#Adiciona finalistas no arquivo saida.txt
def adicionaArquivo(f, d, l, i, categoria, primeiraVez, pos):
    chave = l[i]
    if primeiraVez:
        f.write(f"Classificados {categoria}:\n")
    f.write(f"{pos}. {chave} ({d[chave][0]}): {d[chave][2]} reps, {d[chave][3]}s\n")

#Programa principal
def main():
    start_time = time.time()
    d = leDicionario()
    l, cat0, cat1 = criarLista(d)

    quickSort(l, 0, cat0-1, d)
    quickSort(l, cat0, cat0+cat1-1, d)
    quickSort(l, cat0+cat1, len(l)-1, d)

    with open("saida.txt", "w") as f:
        finalistas0(d, l, cat0, f)
        finalistas1(d, l, cat0, cat1, f)
        finalistas2(d, l, cat0, cat1, f)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time:.4f} segundos")

if __name__ == "__main__":
    main()



