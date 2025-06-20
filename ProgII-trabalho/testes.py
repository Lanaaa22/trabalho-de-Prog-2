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
    l = []
    for chave in d:
        l.append(chave)
    return l

def quicksort(l,inf,sup,d):
    if inf < sup:
        pos = particao(l,inf,sup,d)
        quicksort(l,inf,pos-1)
        quicksort(l,pos+1,sup)
 
def particao(l,inf,sup,d):
    pivot = l[inf]
    i = inf+1
    j = sup
    while i<=j:
        while i<=j and l[i] <= pivot: i+=1 #enquanto i for menor que j ou o numero for menor queo numero do pivot
        while j>=i and l[j] > pivot: j-=1
        if i < j: l[i],l[j] = l[j],l[i]
    l[inf], l[j] = l[j],l[inf]
    return j       


def vem_antes(d):
   pass

def main():   
	inf = 0
	sup = -1 
	d = leDicionario()
	l = [2,1,3,9,2,4]
	print(l)   
	quicksort(l,inf,sup,d)
	print(l)
if __name__ == "__main__":
    main()
