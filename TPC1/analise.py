import os

# 0 - 0
# 1 - index
# 2 - dataEMD
# 3 - primeiro nome
# 4 - ultimo nome
# 5 - idade
# 6 - genero
# 7 - morada
# 8 - modalidade
# 9 - clube
# 10 - email
# 11 - federado
# 12 - resultado

dataset = open('emd.csv', 'r')
next(dataset)

data = []
modalidades = []
escaloes = [0] * 20
atletas_count = 0
atletas_federados = 0


def calc_array_pos(idade):
    return idade // 5


for line in dataset:
    atletas_count += 1
    parsed_data = line.split(',')
    if parsed_data[11] == "true":
        atletas_federados += 1
    pos = calc_array_pos(int(parsed_data[5]))
    if parsed_data[8] not in modalidades:
        modalidades.append(parsed_data[8])
    escaloes[pos] += 1
    data.append(line)


def percentagens_atletas():
    if atletas_federados != 0:
        aptos = (atletas_federados / atletas_count) * 100
    inaptos = ((atletas_count - atletas_federados) / atletas_count) * 100

    return aptos, inaptos


#def get_modalidade(line):
 #   return line.split(',')[8]


# modalidades ordenadas alfabeticamente
#modalidades_alf = sorted(data, key=get_modalidade)

output = open("results.txt", "w")


def output_gen():
    percentagens = percentagens_atletas()
    output.write(f'Atletas Aptos = {percentagens[0]:.2f}%\n')
    output.write(f'Atletas Inaptos = {percentagens[1]:.2f}%\n\n')

    output.write("Escalões: \n")
    escalao_idade = 0
    for escalao in escaloes:
        if escalao != 0:
            output.write(f'{escalao_idade}-{escalao_idade + 4} = {(escalao / atletas_count) * 100:.2f}%\n')
        escalao_idade += 5
    output.write("\n")

    output.write("Modalidades: \n")
    modalidades.sort()
    for linha in modalidades:
        output.write(f' - {linha}\n')


output_gen()
