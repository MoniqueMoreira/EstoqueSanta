#SISTEMA DE DADOS(LISTAS)
import pickle
lista_produtos_cadrastados_s1=pickle.load(open( "s1p.pickls", "rb" ))
lista_quantidade_produtos_s1=pickle.load(open( "s1q.pickls", "rb" ))
lista_codigos_cadrastrados_s1=pickle.load(open( "s1c.pickls", "rb" ))
lista_produtos_cadrastados_s2=pickle.load(open( "s2p.pickls", "rb" ))
lista_quantidade_produtos_s2=pickle.load(open( "s2q.pickls", "rb" ))
lista_codigos_cadrastrados_s2=pickle.load(open( "s2c.pickls", "rb" ))
lista_produtos_cadrastados_s3=pickle.load(open( "s3p.pickls", "rb" ))
lista_quantidade_produtos_s3=pickle.load(open( "s3q.pickls", "rb" ))
lista_codigos_cadrastrados_s3=pickle.load(open( "s3c.pickls", "rb" ))
lista_produtos_cadrastados_s4=pickle.load(open( "s4p.pickls", "rb" ))
lista_quantidade_produtos_s4=pickle.load(open( "s4q.pickls", "rb" ))
lista_codigos_cadrastrados_s4=pickle.load(open( "s4c.pickls", "rb" ))
lista_produtos_cadrastados_s5=pickle.load(open( "s5p.pickls", "rb" ))
lista_quantidade_produtos_s5=pickle.load(open( "s5q.pickls", "rb" ))
lista_codigos_cadrastrados_s5=pickle.load(open( "s5c.pickls", "rb" ))
lista_produtos_cadrastados_geral=lista_produtos_cadrastados_s1+lista_produtos_cadrastados_s2+lista_produtos_cadrastados_s3+lista_produtos_cadrastados_s4+lista_produtos_cadrastados_s5
lista_quantidade_produtos_geral=lista_quantidade_produtos_s1+lista_quantidade_produtos_s2+lista_quantidade_produtos_s3+lista_quantidade_produtos_s4+lista_quantidade_produtos_s5
lista_codigos_cadrastrados_geral=lista_codigos_cadrastrados_s1+lista_codigos_cadrastrados_s2+lista_codigos_cadrastrados_s3+lista_codigos_cadrastrados_s4+lista_codigos_cadrastrados_s5
def menu():
    print(' '*20,'OLÁ BEM VINDO AO ESTOQUE DA SANTA CASA\nESCOLHA UMA OPÇÃO ABAIXO:')
    z=int(input('[1]Setor\n[2]Produto\n[3]Adicionar Produto\n[4]Retirar um produto\n[5]Sair\n>>>'))
    if z == 1:
        setores()
    elif z==2:
        selecionando_produto()
    elif z==3:
        adicionar_novo_produto()
    elif z==4:
        retira_produto()
    elif z==5:
        sair()
    else:
        print('OPÇÃO INVÁLIDA')
        menu()
#SELECIONANDO UM PRODUTO
def selecionando_produto():
    print('PRODUTOS DISPONÍVEIS :')
    for i in range(len(lista_produtos_cadrastados_geral)):
        print('[{}]{} {} quantidade atual {} '.format(i, lista_produtos_cadrastados_geral[i],lista_codigos_cadrastrados_geral[i],lista_quantidade_produtos_geral[i]))
    r = int(input('Escolha o produto:\n>>>'))
    if lista_produtos_cadrastados_geral[r] in lista_produtos_cadrastados_s1:
        for c in range(len(lista_produtos_cadrastados_s1)):
            if lista_produtos_cadrastados_geral[r]==lista_produtos_cadrastados_s1[c]:
                k = lista_produtos_cadrastados_s1[c]
                listap=lista_produtos_cadrastados_s1
                y = lista_quantidade_produtos_s1[c]
                listaq=lista_quantidade_produtos_s1
                p = lista_codigos_cadrastrados_s1[c]
                listac=lista_quantidade_produtos_s1
                item = c
                ARQP="s1p.pickls"
                ARQQ="s1q.pickls"
                ARQC="s1c.pickls"
                produtos(k, y, p, item,listap,listaq,listac,ARQP,ARQQ,ARQC)
    elif lista_produtos_cadrastados_geral[r] in lista_produtos_cadrastados_s2:
        for c in range(len(lista_produtos_cadrastados_s2)):
            if lista_produtos_cadrastados_geral[r]==lista_produtos_cadrastados_s2[c]:
                k = lista_produtos_cadrastados_s2[c]
                listap=lista_produtos_cadrastados_s2
                y = lista_quantidade_produtos_s2[c]
                listaq=lista_quantidade_produtos_s2
                p = lista_codigos_cadrastrados_s2[c]
                listac=lista_quantidade_produtos_s2
                item = c
                ARQP="s2p.pickls"
                ARQQ="s2q.pickls"
                ARQC="s2c.pickls"
                produtos(k, y, p, item,listap,listaq,listac,ARQP,ARQQ,ARQC)
    elif lista_produtos_cadrastados_geral[r] in lista_produtos_cadrastados_s3:
        for c in range(len(lista_produtos_cadrastados_s3)):
            if lista_produtos_cadrastados_geral[r]==lista_produtos_cadrastados_s3[c]:
                k = lista_produtos_cadrastados_s3[c]
                listap=lista_produtos_cadrastados_s3
                y = lista_quantidade_produtos_s3[c]
                listaq=lista_quantidade_produtos_s3
                p = lista_codigos_cadrastrados_s3[c]
                listac=lista_quantidade_produtos_s3
                item = c
                ARQP="s3p.pickls"
                ARQQ="s3q.pickls"
                ARQC="s3c.pickls"
                produtos(k, y, p, item,listap,listaq,listac,ARQP,ARQQ,ARQC)
    elif lista_produtos_cadrastados_geral[r] in lista_produtos_cadrastados_s4:
        for c in range(len(lista_produtos_cadrastados_s4)):
            if lista_produtos_cadrastados_geral[r]==lista_produtos_cadrastados_s4[c]:
                k = lista_produtos_cadrastados_s4[c]
                listap=lista_produtos_cadrastados_s4
                y = lista_quantidade_produtos_s4[c]
                listaq=lista_quantidade_produtos_s4
                p = lista_codigos_cadrastrados_s4[c]
                listac=lista_quantidade_produtos_s4
                item = c
                ARQP="s4p.pickls"
                ARQQ="s4q.pickls"
                ARQC="s4c.pickls"
                produtos(k, y, p, item,listap,listaq,listac,ARQP,ARQQ,ARQC)
    elif lista_produtos_cadrastados_geral[r] in lista_produtos_cadrastados_s5:
        for c in range(len(lista_produtos_cadrastados_s5)):
            if lista_produtos_cadrastados_geral[r]==lista_produtos_cadrastados_s5[c]:
                k = lista_produtos_cadrastados_s5[c]
                listap=lista_produtos_cadrastados_s5
                y = lista_quantidade_produtos_s5[c]
                listaq=lista_quantidade_produtos_s5
                p = lista_codigos_cadrastrados_s5[c]
                listac=lista_quantidade_produtos_s5
                item = c
                ARQP="s5p.pickls"
                ARQQ="s5q.pickls"
                ARQC="s5c.pickls"
                produtos(k, y, p, item,listap,listaq,listac,ARQP,ARQQ,ARQC)
#SELECIONANDO O SETOR
def setores():
    print('Escolha o setor que deseja acessar :')
    print('[1]CENTRO CIRURGICO GERAL  ')
    print('[2]NUTRIÇÃO')
    print('[3]LABORATÓRIO ')
    print('[4]HOTELARIA')
    print('[5]FARMÁCIA')
    print('[6]Voltar ao menu inicial ')
    x = input('>>>')
    if x == '1':
        s1()
    elif x == '2':
        s2()
    elif x == '3':
        s3()
    elif x == '4':
        s4()
    elif x == '5':
        s5()
    elif x == '6':
        menu()
    else:
        print('COMANDO INVÁLIDO')
        setores()
#SETORES
def s1():
    for i in range(len(lista_produtos_cadrastados_s1)):
        print('[{}]{}'.format(i, lista_produtos_cadrastados_s1[i]))
    s1=int(input('>>>'))
    k = lista_produtos_cadrastados_s1[s1]
    listap=lista_produtos_cadrastados_s1
    y = lista_quantidade_produtos_s1[s1]
    listaq=lista_quantidade_produtos_s1
    p = lista_codigos_cadrastrados_s1[s1]
    listac=lista_quantidade_produtos_s1
    item = s1
    ARQP="s1p.pickls"
    ARQQ="s1q.pickls"
    ARQC="s1c.pickls"
    produtos(k, y, p, item,listap,listaq,listac,ARQP,ARQQ,ARQC)
def s2():
    for i in range(len(lista_produtos_cadrastados_s2)):
        print('[{}]{}'.format(i, lista_produtos_cadrastados_s2[i]))
    s2=int(input('>>>'))
    k = lista_produtos_cadrastados_s2[s2]
    listap=lista_produtos_cadrastados_s2
    y = lista_quantidade_produtos_s2[s2]
    listaq=lista_quantidade_produtos_s2
    p = lista_codigos_cadrastrados_s2[s2]
    listac=lista_quantidade_produtos_s2
    item = s2
    ARQP="s2p.pickls"
    ARQQ="s2q.pickls"
    ARQC="s2c.pickls"
def s3():
    for i in range(len(lista_produtos_cadrastados_s3)):
        print('[{}]{}'.format(i, lista_produtos_cadrastados_s3[i]))
    s3=int(input('>>>'))
    k = lista_produtos_cadrastados_s3[s3]
    listap=lista_produtos_cadrastados_s3
    y = lista_quantidade_produtos_s3[s3]
    listaq=lista_quantidade_produtos_s3
    p = lista_codigos_cadrastrados_s3[s3]
    listac=lista_quantidade_produtos_s3
    item = s3
    ARQP="s3p.pickls"
    ARQQ="s3q.pickls"
    ARQC="s3c.pickls"
def s4():
    for i in range(len(lista_produtos_cadrastados_s4)):
        print('[{}]{}'.format(i, lista_produtos_cadrastados_s4[i]))
    s4=input('>>>')
    k = lista_produtos_cadrastados_s4[s4]
    listap=lista_produtos_cadrastados_s4
    y = lista_quantidade_produtos_s4[s4]
    listaq=lista_quantidade_produtos_s4
    p = lista_codigos_cadrastrados_s4[s4]
    listac=lista_quantidade_produtos_s4
    item = s4
    ARQP="s4p.pickls"
    ARQQ="s4q.pickls"
    ARQC="s4c.pickls"
def s5():
    for i in range(len(lista_produtos_cadrastados_s5)):
        print('[{}]{}'.format(i, lista_produtos_cadrastados_s5[i]))
    s5=int(input('>>>'))
    k = lista_produtos_cadrastados_s5[s5]
    listap=lista_produtos_cadrastados_s5
    y = lista_quantidade_produtos_s5[s5]
    listaq=lista_quantidade_produtos_s5
    p = lista_codigos_cadrastrados_s5[s5]
    listac=lista_quantidade_produtos_s5
    item = s5
    ARQP="s5p.pickls"
    ARQQ="s5q.pickls"
    ARQC="s5c.pickls"

#MODIFICANDO PRODUTO
def produtos(produto,quantidade,codigo,ordem,listap,listaq,listac,arqp,arqq,arqc):
    print('Você escolheu:', produto)
    volta= ''
    while volta!=2:
        print('[1]ADICIONAR\n[2]RETIRAR\n[3]ALTERAR CÓDIGO\n[4]VOLTAR PARA O MENU INCIAL')
        l = input('>>>')
        if l == '1':
            add = int(input('Digite a quantidade de caixas que deseja adicionar:'))
            quantidade += add
            print('Adicionado com sucesso')
            print('Quantidade atual é de {}'.format(quantidade))
            lista_quantidade_produtos_geral[ordem]=quantidade
            listaq[ordem]=quantidade
            lista=listaq
            arq=arqq
            pickle.dump(lista, open( arq, "wb" ) )
            print('Deseja realiza outra operação neste produto?')
            volta= int(input('[1]SIM\n[2]NÃO\n>>'))
            if volta == 1:
                pass
            elif volta==2:
                menu()
            else:
                print('Comando inválido')
        elif l == '2':
            ret = int(input('Digite a quantidade de caixas que deseja retirar:'))
            if ret > quantidade:
                print('Valor indisponível no momento')
                pass
            else:
                quantidade -= ret
                listaq[ordem]=quantidade
                lista_quantidade_produtos_geral[ordem]=quantidade
                lista=listaq
                arq=arqq
                pickle.dump(lista, open( arq, "wb" ) )
                print('Retirado com sucesso')
                print('Quantidade atual é de {}'.format(quantidade))
                print('Deseja realiza outra operação neste produto?')
                volta = int(input('[1]SIM\n[2]NÃO\n>>>'))
                if volta== 1:
                    pass
                elif volta==2:
                    menu()
                else:
                    print('Comando inválido')
        elif l == '3':
            print('{} {}'.format(produto,codigo))
            print('Deseja modificar?')
            mod=input('[1]Sim\n[2]Não\n>>>')
            if mod== '1':
                novocod=input('Digite "cód" mais o novo código:\n>>>')
                listac[ordem]=novocod
                lista_codigos_cadrastrados_geral[ordem]=novocod
                lista=listac
                arq=arqc
                pickle.dump(lista, open( arq, "wb" ) )
                print('Deseja realiza outra operação neste produto?')
                volta = input('[1]SIM\n[2]NÃO\n>>>')
                if volta == '1':
                    pass
                elif volta=='2':
                    menu()
                else:
                    print('Comando inválido')    
        else:
            menu()
#ADICIONANDO UM PRODUTO POR SETORES
def adicionar_novo_produto():
    print('Selecione o setor que dezeja adicionar:')
    print('[1]CENTRO CIRURGICO GERAL  ')
    print('[2]NUTRIÇÃO')
    print('[3]LABORATÓRIO ')
    print('[4]HOTELARIA')
    print('[5]FARMÁCIA')
    print('[6]Volta ao menu inicial')
    x = input('>>>')
    if x == '1':
        add(lista_produtos_cadrastados_s1,lista_quantidade_produtos_s1,lista_codigos_cadrastrados_s1,"s1p.pickls","s1q.pickls","s1c.pickls")
    elif x == '2':
        add(lista_produtos_cadrastados_s2,lista_quantidade_produtos_s2,lista_codigos_cadrastrados_s2,"s2p.pickls","s2q.pickls","s2c.pickls")
    elif x == '3':
        add(lista_produtos_cadrastados_s3,lista_quantidade_produtos_s3,lista_codigos_cadrastrados_s3,"s3p.pickls","s3q.pickls","s3c.pickls")
    elif x == '4':
        add(lista_produtos_cadrastados_s4,lista_quantidade_produtos_s4,lista_codigos_cadrastrados_s4,"s4p.pickls","s4q.pickls","s4c.pickls")
    elif x == '5':
        add(lista_produtos_cadrastados_s5,lista_quantidade_produtos_s5,lista_codigos_cadrastrados_s5,"s5p.pickls","s5q.pickls","s15c.pickls")
    elif x=='6':
        menu()
    else:
        print('Comando inválido')
        adicionar_novo_produto()
def add(prod,quant,cod,arqp,arqq,arqc):
    print('Produtos disponíveis no estoque:')
    for i in range(len(prod)):
        print(prod[i])
    a = input('Digite o "NOME" do produto que deseja adicionar:\n>>>')
    prod.append(a)
    salvap=prod
    arquivop=arqp
    pickle.dump( salvap, open( arquivop, "wb" ) )
    q = int(input('Digite a "QUANTIDADE" de caixas que deseja adicionar deste produto:\n>>>'))
    quant.append(q)
    salvaq=quant
    arquivoq=arqq
    pickle.dump( salvaq, open( arquivoq, "wb" ) )
    v = input('Digite o "CÓDIGO" do produto:\n>>>')
    cod.append(v)
    salvac=cod
    arquivoc=arqc
    pickle.dump( salvac, open( arquivoc, "wb" ) )
    print('Adicionado com sucesso')
    volta=input('Deseja adicionar outro produto?\n[1]SIM\n[2]NÃO\n[3]SAIR\n>>>')
    if volta=='1':
        adicionar_novo_produto()
    elif volta=='2':
        menu()
    elif volta=='3':
        sair()
    else:
        print('Comando inválido')
#RETIRANDO UM PRODUTO POR SETOR
def retira_produto():
    print('Selecione o setor que dezeja adicionar:')
    print('[1]CENTRO CIRURGICO GERAL  ')
    print('[2]NUTRIÇÃO')
    print('[3]LABORATÓRIO ')
    print('[4]HOTELARIA')
    print('[5]FARMÁCIA')
    print('[6]VOLTAR AO MENU INICIAL')
    print('[7]SAIR DO PROGRAMA')
    x = input('>>>')
    if x == '1':
        ret(lista_produtos_cadrastados_s1,lista_quantidade_produtos_s1,lista_codigos_cadrastrados_s1,"s1p.pickls","s1q.pickls","s1c.pickls")
    elif x == '2':
        ret(lista_produtos_cadrastados_s2,lista_quantidade_produtos_s2,lista_codigos_cadrastrados_s2,"s2p.pickls","s2q.pickls","s2c.pickls")
    elif x == '3':
        ret(lista_produtos_cadrastados_s3,lista_quantidade_produtos_s3,lista_codigos_cadrastrados_s3,"s3p.pickls","s3q.pickls","s3c.pickls")
    elif x == '4':
        ret(lista_produtos_cadrastados_s4,lista_quantidade_produtos_s4,lista_codigos_cadrastrados_s4,"s4p.pickls","s4q.pickls","s4c.pickls")
    elif x == '5':
        ret(lista_produtos_cadrastados_s5,lista_quantidade_produtos_s5,lista_codigos_cadrastrados_s5,"s5p.pickls","s5q.pickls","s15c.pickls")
    elif x=='6':
        menu()
    elif x=='7':
        sair()
    else:
        print('Comando inválido')
        retira_produto()
def ret(prod,quant,cod,arqp,arqq,arqc):
    for i in range(len(prod)):
        print('[{}]{}'.format(i, prod[i]))
    a = int(input('Digite o número do produto que deseja retira\n>>>'))
    prod.remove(prod[a])
    salvap=prod
    arquivop=arqp
    pickle.dump( salvap, open( arquivop, "wb" ) )
    quant.remove(quant[a])
    salvaq=quant
    arquivoq=arqq
    pickle.dump( salvaq, open( arquivoq, "wb" ) )
    cod.remove(cod[a])
    salvac=cod
    arquivoc=arqc
    pickle.dump( salvac, open( arquivoc, "wb" ) )
    print('Retirado com sucesso')
    try:
        volta=input('Deseja retirar outro produto?\n[1]SIM\n[2]NÃO\n[3]SAIR\n>>>')
        if volta=='1':
            retira_produto()
        elif volta=='2':
            menu()
        elif volta=='3':
            sair()
        else:
            print('Comando inválido')
    except:
        print('Comando inválido')
        retira_produto()

        
#SAINDO DO PROGRAMA
def sair():
    print('OBRIGADO POR USAR!')
    break
menu()

