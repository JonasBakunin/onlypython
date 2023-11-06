#Faça um programa em Python que leia uma data de nascimento no formato dd/mm/aaaa e imprima a data com o mês escrito por extenso.

dic = {'01':'Janeiro','02':'Fevereiro','03':'Março', '04':'Abril', '05':'Maio', '06':'Junho','07':'Julho',
       '08':'Agosto', '09':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'}

data = input('Informe a data no formatado dd/mm/aaaa : ')
data = data.split('/')


print(f'Você nasceu em {data[0]} de {dic[data[1]]} de {data[2]}')
