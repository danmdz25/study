#A DONA DE UM MERCADO CHAMADO OLIVIA, DESEJA VENDER MAÇAS
# AS MAÇAS CUSTAM 0,30R$ SE FOREM COMPRADAS MAIS DE UMA DUZIA
# CASO COMPREM MAIS DE UMA DUZIA O PREÇO CAI PARA0,25R$

macasCompradas=int(input("Insira quantas maças você comprou: "))

if macasCompradas>12: 
    print(f"Você comprou {macasCompradas} maçãs e isso da um valor de {macasCompradas*0.25} R$")
else: print(f"Você comprou {macasCompradas} maçãs e isso da um valor de {macasCompradas*0.30} R$")