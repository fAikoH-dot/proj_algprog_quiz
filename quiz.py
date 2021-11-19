#Projeto Game Quiz Educacional - Impactos causados pela pandemia da COVID-19
#Grupo: Amanda Smanioto, Camila Pereira, Daniela Flauto, Fernanda Hamatsu



#definindo as listas alternativas, enunciados, sequência das respostas corretas, e as respostas do usuário
alternativas = ['a) ', 'b) ', 'c) ', 'd) ', 'e) ']
enunciados = ['Em qual dos seguintes países a pandemia começou?', 'No Brasil, quantas pessoas perderam a vida devido ao COVID-19?', 'Qual foi a classe social mais afetada?', 'Em relação a pergunta anterior, qual a razão por tal classe ter sido a mais afetada?', 'O que ajuda no tratamento/prevenção da covid?', 'Qual formato de trabalho e contratação sofreu mais com os impactos da covid?', 'O ENEM 2021 foi o que obteve menor número de candidatos desde 2007, por que isso ocorreu?', 'Micros e pequenas empresas sofreram grande prejuízo durante a pandemia, muitas chegaram inclusive a falir neste período. Qual a razão pela qual isso veio a acontecer?', 'Qual dos problemas de saúde a seguir foi um dos quais aumentou muito durante a pandemia?', 'Governo promulgou, em Julho de 2020, a lei que garante internet gratuita a alunos e professores de escola pública. Os recursos são voltados a: ']
resp_corretas = ['C', 'C', 'E', 'C', 'D', 'B', 'D', 'C', 'E', 'A']
resp_usuario = []

#pergunta 1
um_A = 'Emirados árabes unidos'
um_B = 'Uruguai'
um_C = 'China'
um_D = 'África do Sul'
um_E = 'Noruega'
um_just = 'O primeiro caso oficial de covid-19 na China surgiu em dezembro de 2019 e foi vinculado ao mercado de frutos do mar de Huanan, em Wuhan.'
ex_um = [um_A, um_B, um_C, um_D, um_E]

#pergunta 2
dois_A = 'Entre 10 e 50 mil'
dois_B = 'Entre 100 e 200 mil'
dois_C = 'Entre 600 e 700 mil'
dois_D = 'Entre 1.5 e 1.6 milhão'
dois_E = 'Mais de dois milhões'
dois_just = 'Até o momento (09/11/2021) foram registradas cerca de 610 mil mortes causadas pela COVID-19 dês do início da Pandemia.'
ex_dois = [dois_A, dois_B, dois_C, dois_D, dois_E]

#pergunta 3
tres_A = 'A - Alta Classe'
tres_B = 'B - Baixa Classe Alta e Alta Classe Média'
tres_C = 'C - Média Classe Média e Baixa Classe Média'
tres_D = 'D - Vulneráveis'
tres_E = 'E - Pobres e Extremamente Pobres'
tres_just = 'A Pandemia ameaça particularmente a saúde e a renda dos mais pobres, moradores de periferia e que já tinham vínculos frágeis no mercado de trabalho.'
ex_tres = [tres_A, tres_B, tres_C, tres_D, tres_E]

#pergunta 4
quatro_A = 'Porque quanto menos dinheiro você tem, menor a sua vontade de viver.'
quatro_B = 'Porque ninguém avisou as classes mais baixas sobre o que estava acontecendo no Brasil e no mundo.'
quatro_C = 'Porque nas regiões periféricas, as condições para cumprir o isolamento são piores, dificultando a não contaminação.'
quatro_D = 'Porque eles se revoltaram com o sistema e decidiram que o momento era ideal para exterminar toda a população mundial.'
quatro_E = 'Porque a covid é transmitida pelo esgoto, e nas áreas periféricas o saneamento básico é falho ou, muitas vezes, inexistente.'
quatro_just = 'A contaminação é facilitada pela distribuição desigual da renda. Nas periferias, as condições para cumprir o isolamento social são piores: há mais moradores por domicílio, o acesso a água encanada, vital para a higienização, às vezes não existe ou é intermitente, e a insegurança econômica estimula muitos a saírem de casa para obter algum dinheiro.'
ex_quatro = [quatro_A, quatro_B, quatro_C, quatro_D, quatro_E]

#pergunta 5
cinco_A = 'Antibióticos'
cinco_B = 'Ivermectina'
cinco_C = 'Alho cru'
cinco_D = 'Vacina contra a doença'
cinco_E = 'Cloroquina'
cinco_just = 'Por ser uma doença muito recente, poucos estudos possuem um forte embasamento. Todos os esforços durante o tempo de pandemia foram direcionados à vacina, a tornando o medicamento mais eficaz contra a COVID'
ex_cinco = [cinco_A, cinco_B, cinco_C, cinco_D, cinco_E]

#pergunta 6
seis_A = 'O cujos empregados eram devidamente efetivados.'
seis_B = 'O que mantinha vínculos menos estáveis com os empregados.'
seis_C = 'O que possuía flexibilidade em relação ao home office.'
seis_D = 'O que pagava mais de dois salários-mínimos.'
seis_E = 'Os chamados freelancers.'
seis_just = '"Muitas pessoas que já tinham vínculos frágeis no mercado de trabalho vão perdê-los, e será difícil restabelecê-los", diz Burgos, da FGV-EAESP. Em crises como essa, o sistema de proteção social do país deveria reagir, mas está respondendo de forma frágil.'
ex_seis = [seis_A, seis_B, seis_C, seis_D, seis_E]

#pergunta 7
sete_A = 'Ocorreu pois os estudantes cansaram do modelo de prova do ENEM e migraram para a FUVEST.'
sete_B = 'Ocorreu porque a pandemia levou a óbito grande parte dos jovens no país, levando à falta de pessoas para fazer a prova.'
sete_C = 'Ocorreu devido à um medo que foi desenvolvido por inúmeros jovens após passarem um ano em casa, sem contato com outras pessoas.'
sete_D = 'Ocorreu porque durante a pandemia, inúmeros estudantes sofreram prejuízos devido ao fato de a grande maioria das escolas municipais, estaduais e federais terem fechado durante a mesma, faltando preparo aos possíveis candidatos.'
sete_E = 'Ocorreu pois o governo federal limitou o número de inscrições, fazendo com que houvesse um limite de candidatos, em cenário de pandemia.'
sete_just = '“É reflexo fundamentalmente de duas questões: a primeira é a perda do vínculo com a educação e com os próprios estudos em função de um ensino remoto de baixíssima efetividade e com alcance limitado", apontou Nogueira Filho. E o segundo [motivo] é que é reflexo da necessidade de busca de renda por parte de muitos desses jovens", completa.'
ex_sete = [sete_A, sete_B, sete_C, sete_D, sete_E]

#pergunta 8
oito_A = 'Antes da pandemia, as empresas começaram a estocar seus produtos, e na pandemia, com o prejuízo que sofreu a economia, ninguém tinha dinheiro a comprar, as levando a falência.'
oito_B = 'Os donos dessas empresas não viam futuro nelas, e acabaram declarando falência pois acabaram desistindo.'
oito_C = 'Com o fechamento dos comércios, as empresas ficaram sem renda, ou renda insuficiente para conseguir mantê-las, sofrendo também com a falta de matéria prima e o aumento no preço dos insumos prejudicando assim, muitas delas.'
oito_D = 'Elas sofreram boicote do governo federal, que aumentaram os impostos, levando muitas dela a falência.'
oito_E = 'Com as fronteiras fechadas, o comércio, que, em sua maioria, dependia de turistas, acabaram perdendo sua renda principal, indo então a falência.'
oito_just = 'A pandemia de covid-19 afetou as micro e pequenas empresas das mais diversas maneiras. Recente levantamento do Datafolha aponta que 77% dos negócios de São Paulo tiveram falta de matéria prima, enquanto 91% sofreram com aumento do preço dos insumos.'
ex_oito = [oito_A, oito_B, oito_C, oito_D, oito_E]

#pergunta 9
nove_A = 'Câncer'
nove_B = 'Hipotireoidismo '
nove_C = 'Infarto'
nove_D = 'Paralisia facial'
nove_E = 'Doenças mentais'
nove_just = 'Tanto a pandemia como as medidas de contenção adotadas por governos, como quarentenas e distanciamento social, possuem impactos psicossociais profundos e duradouros, podendo perdurar por meses ou anos, e podendo inclusive ver seu pico após o fim da pandemia em si. Tais impactos incluem mas não se limitam a aumento nos níveis de ansiedade, depressão, stress, e aumento do número de suicídios da população em geral especialmente a mais jovem. O medo de contágio e o isolamento social são alguns dos fatores estressantes resultantes da pandemia e das medidas de controle impostas por autoridades que podem contribuir para uma piora no quadro de saúde mental da população.'
ex_nove = [nove_A, nove_B, nove_C, nove_D, nove_E]

#pergunta 10
dez_A = 'Alunos da rede pública que sejam de famílias inscritas no Cadastro Único para Programas Sociais do Governo Federal (CadÚnico); alunos de comunidades indígenas e quilombolas;professores da educação básica.'
dez_B = 'Alunos somente de escola pública e professores de escola privada.'
dez_C = 'Alunos de escola privada e professores concursados.'
dez_D = 'Alunos de escola privada e professores de escola privada.'
dez_E = 'Somente professores de escola pública e alunos cujo os pais tem 7 salários mínimos.'
dez_just = 'A lei prevê repasses a estados, municípios e DF, que vão aplicá-los conforme a demanda local a alunos da rede pública que sejam de famílias inscritas no Cadastro Único para Programas Sociais do Governo Federal (CadÚnico); alunos de comunidades indígenas e quilombolas; professores da educação básica; sendo a prioridade será, pela ordem: alunos do ensino médio, os alunos do ensino fundamental, os professores do ensino médio e os professores do ensino fundamental. A transferência da União deverá ocorrer em parcela única em até 30 dias. Serão destinados R$ 3,5 bilhões para ações que promovam a conectividade.'
ex_dez = [dez_A, dez_B, dez_C, dez_D, dez_E]


#definir as listas dos exercícios e das justificativas (para caso o usuário erre a questão)
lista_exerc = [ex_um, ex_dois, ex_tres, ex_quatro, ex_cinco, ex_seis, ex_sete, ex_oito, ex_nove, ex_dez]
justificativas = [um_just, dois_just, tres_just, quatro_just, cinco_just, seis_just, sete_just, oito_just, nove_just, dez_just]


#define o valor inicial da nota
nota = 0

#definir a função para receber as respostas do usuário e certificar que sejam válidas, além de utilizar da função .upper() para formatar as respostas
def resp():
    resposta = str(input("\nDigite a resposta: ")).upper()
    while resposta != 'A' and resposta != 'B' and resposta != 'C' and resposta != 'D' and resposta != 'E' :
        resposta = str(input("Digite uma resposta válida: ")).upper()
    resp_usuario.append(resposta)


#define a função verificar, que compara a resposta do usuário com a lista de respostas corretas retornando se resposta está correta ou incorreta, retornando (caso incorreta) a justificativa
def verificar(usuario, correta, i):
    global nota
    if usuario[i] == correta[i]:
        print('_'*21,"CORRETO!",'_'*21,'\n')
        nota += 1
    else:
        print('_'*20,"INCORRETO!",'_'*20)
        print(justificativas[i],'\n')
    return nota


#Informações a serem apresentadas no início do Quiz
print("_"*61)
print('\n',' '*20, "BEM VINDO AO QUIZ")       
print(' '*7, "'IMPACTOS CAUSADOS PELA PANDEMIA DA COVID-19'") 
print(' '*20,"!!IMPORTANTE!!",' ',"\n-Responder apenas a letra da alternativa {a, b, c, d, e}.","\n-As perguntas estão distribuídas em 3 níveis: fácil, médio e difícil; cada uma valendo 1 ponto.","\n-Não é permitida a consulta na internet \n-Há apenas uma tentativa para cada questão.","\n-Aconselhamos que o quiz seja realizado em até 15 minutos.")
print("_"*61)

#Permissão para iniciar o Quiz
iniciar = str(input("Deseja iniciar o quiz? (S/N) \nResposta: ")).upper()
while iniciar == 'N' or (iniciar != 'S' and iniciar != 'N'):
    iniciar = str(input("Deseja iniciar o quiz? (S/N) \nResposta: ")).upper()


#Obter o nome do usuário
nome = str(input("\nDigite o seu nome: "))


#Loop para apresentar os enunciados e alternativas, chamando as funções resp() e verificar() para avaliação de cada questão
questao = 1
while questao <= len(enunciados):
    for i in range (10):
        print('_'*52)
        print(questao,'.', enunciados[questao - 1])
        print('_'*52,"\n")
        exercicio = lista_exerc[i]
        for j in range (5):
            print(alternativas[j], exercicio[j])
        resp()
        verificar(resp_usuario, resp_corretas, (questao-1))
        questao += 1


#Retorna ao usuário a sua nota final e um comentário referente a nota
print("%s, sua nota final é: %d/10" %(nome,nota))
if nota>=0 and nota<5:
    print("Baixo desempenho... Para melhorá-lo, é aconselhável que seja feita uma pesquisa acerca da covid 19 e seus impactos no mundo atual através de fontes de informação confiáveis! #ficadica")
elif nota>=5 and nota<=7:
    print("Bom desempenho... Mas pode melhorar! Já considerou fazer algumas pesquisas para não ficar de fora da situação atual do brasil e do mundo? #ficadica")
elif nota>7 and nota<=10:
    print("Excelente desempenho... Não deixe de se manter atualizado(a) através de fontes de informação confiáveis! #ficadica")