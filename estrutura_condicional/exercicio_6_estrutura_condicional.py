# O professor Rui está desenvolvendo um sistema automático para
# identificar se uma cobra é uma coral verdadeira ou uma falsa coral. A
# cobra coral verdadeira é venenosa e os anéis coloridos no seu corpo
# seguem o padrão ...BVBP BVBPBVBP..., onde B,V e P representam as
# cores branco, vermelho e preto, respectivamente. Já a falsa coral não é
# venenosa e os anéis seguem o padrão ...BVPB VPBVPBVP....
# O problema é que os sensores do sistema do professor Rui produzem
# apenas uma sequência de quatro números representando um pedaço do
# padrão de cores. Só que ele não sabe qual número representa qual cor.
# Mas, por exemplo, se a sequência for 5 3 9 3, podemos dizer com certeza
# que é uma coral verdadeira, mesmo sem saber qual número representa
# qual cor! Você deve ajudar o professor Rui e escrever um programa que
# diga se a coral é verdadeira ou falsa.

n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 3° número: "))
n4 = int(input("Digite o 4° número: "))


coral = False

if n1 == n3 or n2 == n4:
    coral = True
    print(coral)
elif n1 != n2 and n2 != n3 and n3 != n4:
    coral = False
    print(coral)