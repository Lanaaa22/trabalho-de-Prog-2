import pickle

#entrada - (24,6,2025)
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
    with open("entrada20.bin", "rb") as f:
        dic = pickle.load(f)
    return dic

def criarLista(d):
    cat0 = 0
    cat1 = 0
    cat2 = 0
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
            cat2 += 1
            l.append(chave)
    return l,cat0,cat1,cat2

def quickSort(l,inf,sup,d): 
    if inf < sup:
        pos = particao(l,inf,sup,d)
        quickSort(l,inf,pos-1,d)
        quickSort(l,pos+1,sup,d)
def particao(l,inf,sup,d):
    pivot = l[inf]
    i = inf +1
    j = sup
    while i <= j:
        while i <= j and d[l[i]][2] >= d[pivot][2]: # compara repetições
            if d[l[i]][2] == d[pivot][2]: # se empatar em repetições.... próximo critério
                if d[l[i]][3] < d[pivot][3]: # compara menor tempo
                    i +=1
                elif d[l[i]][3] == d[pivot][3]: # se empatar no tempo.... próximo critério
                    if d[l[i]][0] < d[pivot][0]: # compara nome (ordem alfabética)
                        i += 1
                    elif d[l[i]][0] == d[pivot][0]: # se tiver mesmo nome ... próximo critério
                        if l[i] < l[j]: # compar n° de inscricao
                            i +=1
            else: i += 1
        while j >= i and d[l[i]][2] >= d[pivot][2]:
            if d[l[i]][2] == d[pivot][2]: # se empatar em repetições.... próximo critério
                if d[l[i]][3] > d[pivot][3]: # compara menor tempo
                    j -=1
                elif d[l[i]][3] == d[pivot][3]: # se empatar no tempo.... próximo critério
                    if d[l[i]][0] > d[pivot][0]: # compara nome (ordem alfabética)
                        j -= 1
                    elif d[l[i]][0] == d[pivot][0]: # se tiver mesmo nome ... próximo critério
                        if l[i] > l[j]: # compar n° de inscricao
                            j -=1
            else:
                j -= 1
# (’Miguel Pinto Alves’, (9, 9, 1984), 8, 1440)
#def comparaMenor(i,j):
 #   if categoria

"""
def finalistas(d):
    l,cat0,cat1,cat2 = criarLista(d)


"""


def main():    
    d = leDicionario()
    l,cat0,cat1,cat2 = criarLista(d)
    quickSort(l,0,cat0-1,d)#ordenando sub20
    print(l)
    


if __name__ == "__main__":
    main()

