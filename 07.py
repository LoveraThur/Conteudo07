while True:
    tipo = str(input('Digite um tipo[Vertebrado/Invertebrado]\n>>> ')).title()
    print('-'*30)
    if tipo == 'Vertebrado' or tipo == 'Invertebrado':
        if tipo == 'Vertebrado':
            tipo = str(input('Digite um tipo[Ave/Mamifero]\n>>> ')).title()
            if tipo == 'Ave' or tipo == 'Mamifero':
                if tipo == 'Ave':
                    tipo = str(input('Digite um tipo[Carnivoro/Onivoro]\n>>> ')).title()
                    if tipo == 'Carnivoro' or tipo == 'Onivoro':
                        if tipo == 'Carnivoro':
                            print('You is Aguia')
                            break
                        else:
                            print('You is Pomba')
                            break
                else:
                    tipo = str(input('Digite um tipo[Onivoro/Herbivoro]\n>>> ')).title()
                    if tipo == 'Onivoro' or tipo == 'Herbivoro':
                        if tipo == 'Onivoro':
                            print('You is Homem')
                            break
                        else:
                            print('You is Vaca')
                            break
                    
        else:
            tipo = str(input('Digite um tipo[Inseto/Anelideo]\n>>> ')).title()
            if tipo == 'Inseto' or tipo == 'Anelideo':
                if tipo == 'Inseto':
                    tipo = str(input('Digite um tipo[Hematofago/Herbivoro]\n>>> ')).title()
                if tipo == 'Hematofago' or tipo == 'Herbivoro':
                    if tipo == 'Hematofago':
                        print('You is Pulga')
                        break
                    else:
                        print('You is Lagarta')
                        break
                else:
                    tipo = str(input('Digite um tipo[Hematofago/Onivoro]\n>>> ')).title()
                    if tipo == 'Hematofago' or tipo == 'Onivoro':
                        if tipo == 'Hematofago':
                            print('You is Sanguessuga')
                            break
                        else:
                            print('You is Minhoca')
                            break
print('\033[34mEnd Of Program\033[m')       