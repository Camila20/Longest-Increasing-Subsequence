def subsequence(A):
    B=[]
    C=[]
    for x in range(len(A)):
        ind=A[x]+x  # El indicador sera la suma del elemanto más su posición
        B.append(ind)   # Se crea una lista de los indicadores
        C.extend([ind,x])   # Se agrega a una lista la posición y el indicador
    B=order(B)  # Se ordena la lista de indicadores
    D=[A[0]]
    ans=0
    for i in range(len(B)):
        j=C.index(B[i])+1   # Indicador de la posición de la lista ordenada
        v=C[j]  # Valor que corresponde al indicador de posicion
        if D[len(D)-1]<A[v] and ans<v:  # El número y la posición son mayores al último en la lista
            D.append(A[v])
            ans=v
    #print (D)
    return(len(D))

# Esta función ordena los elementos en una lista
def order(A):
    n=len(A)
    B=[]
    for y in range (n):
        minimum=min(A)  # Encuentra el mínimo elemento
        B.append(minimum)   # Agrega el elemento a otra lista
        A.remove(minimum)   # Eliminia el número mínimo en la lista original
    return (B)


print (subsequence([1,2,5,1]))
print (subsequence([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))
