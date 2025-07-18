import pickle
import math

#entrada - (24,6,2025)
def categoria(data): 
    idade_atual = idade(data) # Calcula apenas uma vez 
    if idade_atual < 20: 
        return 0 
    elif 20 <= idade_atual <= 39: 
        return 1 
    else: return 2

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
    if idade(data) < 20:
        return 0
    elif idade(data) >= 20 and idade(data) <=39:
        return 1
    else:
        return 2
    
def leDicionario():
    with open("entrada10000.bin", "rb") as f:
        dic = pickle.load(f)
    return dic

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
    """
    for key in l:
        print(d[key])
    """
    
    return l,cat0,cat1

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

def chave_ord(chave, d):
    nome, data, reps, tempo = d[chave]
    nome_min = nome#.lower()
    return (-reps, tempo, nome_min, chave)

def finalistas0(d,l):
    aux = 1
    primeiraVez = True
    __,cat0,__, = criarLista(d)
    vagas = math.ceil(cat0*(1/3))
    for posicao in range(cat0):
        if posicao < vagas:
            if primeiraVez:
                pos = 1
                adicionaArquivo(d,l,posicao, "SUB20", primeiraVez,pos)
                primeiraVez = False
                pos+=1
            else:
                adicionaArquivo(d,l,posicao, "SUB20", primeiraVez,pos)
                pos+=1
                if pos == vagas:
                    ultimoPont = posicao
                    if d[l[ultimoPont]][2] != d[l[posicao+aux]][2] or d[l[ultimoPont]][3] != d[l[posicao+aux]][3]:
                        adicionaArquivo(d,l,posicao+aux, "SUB20", primeiraVez,pos)
                    while d[l[ultimoPont]][2] == d[l[posicao + aux]][2] and d[l[ultimoPont]][3] == d[l[posicao + aux]][3]:
                        if aux == 2:
                            pos+=1
                        adicionaArquivo(d,l,posicao + aux, "SUB20", primeiraVez,pos)
                        aux +=1
                    return


def finalistas1(d,l):
    aux = 1
    primeiraVez = True
    __,cat0,cat1 = criarLista(d)
    inicio = cat0
    vagas = math.ceil(cat1*(1/3))
    for posicao in range(cat0,cat1+cat0):
        if posicao - inicio < vagas:
            if primeiraVez:
                pos = 1
                adicionaArquivo(d,l,posicao, "20-39", primeiraVez,pos)
                primeiraVez = False
                pos+=1
            else:
                adicionaArquivo(d,l,posicao, "20-39", primeiraVez,pos)
                pos+=1
                if pos == vagas:
                    ultimoPont = posicao+aux
                    if d[l[ultimoPont]][2] != d[l[posicao+aux]][2] or d[l[ultimoPont]][3] != d[l[posicao+aux]][3]:
                        adicionaArquivo(d,l,posicao+aux, "20-39", primeiraVez,pos)
                    while d[l[ultimoPont]][2] == d[l[posicao + aux]][2] and d[l[ultimoPont]][3] == d[l[posicao + aux]][3]:
                        if aux == 2:
                            pos+=1
                        adicionaArquivo(d,l,posicao + aux, "20-39", primeiraVez,pos)
                        aux +=1
                    return



            
def finalistas2(d,l):
    aux = 1
    primeiraVez = True
    __,cat0,cat1 = criarLista(d)
    inicio = cat0+cat1
    vagas = math.ceil((len(l)-cat0-cat1)*(1/3))
    pos = 1
    for posicao in range(cat1+cat0,len(l)):
        if posicao - inicio < vagas: #2
            if primeiraVez:
                    adicionaArquivo(d,l,posicao, "40+", primeiraVez,pos)
                    primeiraVez = False
                    pos+=1
            else:
                adicionaArquivo(d,l,posicao, "40+", primeiraVez,pos)
                pos+=1
                if pos == vagas:
                    ultimoPont = posicao+aux
                    if d[l[ultimoPont]][2] != d[l[posicao+aux]][2] or d[l[ultimoPont]][3] != d[l[posicao+aux]][3]:
                        adicionaArquivo(d,l,posicao+aux, "40+", primeiraVez,pos)
                    while d[l[ultimoPont]][2] == d[l[posicao+aux]][2] and d[l[ultimoPont]][3] == d[l[posicao+aux]][3]:#printa os empatados
                        if aux == 2:
                            pos+=1
                        adicionaArquivo(d,l,posicao + aux, "40+", primeiraVez,pos)
                        aux +=1
                    return
                            
    
#FUNCIONANDO
def adicionaArquivo(d,l,i,categoria,primeiraVez,pos):
    chave = l[i]
    f = open("saida.txt", "a")
    if primeiraVez:
        f.write(f"Classificados {categoria}:\n")
    f.write(f"{pos}. {chave} ({d[chave][0]}): {d[chave][2]} reps, {d[chave][3]}s\n")
    f.close()

def main():  
    
    d = leDicionario()
    l,cat0,cat1 = criarLista(d)

    quickSort(l,0,cat0-1,d)#ordenando sub20

    quickSort(l,cat0,cat1+cat0-1,d)#ordenando 20 a 39
  
    quickSort(l,cat1+cat0,len(l)-1,d)#ordenando 40+
    

    open("saida.txt", "w").close()
    finalistas0(d,l)
    finalistas1(d,l)
    finalistas2(d,l)
  

if __name__ == "__main__":
    main()



