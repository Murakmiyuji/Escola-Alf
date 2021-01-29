#Neste bloco de código é inserido a quantidade de alunos que realizaram as provas e deverão ser corrigidas.
#Há uma restrição através do comando while para que haja sempre mais que zero e menos que 100 alunos.
qnt_aluno = int(input("Quantidade de alunos que realizaram a prova: "))
while qnt_aluno < 0 or qnt_aluno > 100:
    print("Você digitou uma quantidade menor que zero ou maior que 100. Lembre-se o limite máximo na realização da "
          "prova é 100, e no mínimo 1 deve fazer a prova.")
    qnt_aluno = int(input("Quantidade de alunos que realizaram a prova: "))
#Neste comando for é inserido o aluno para poder corrigir suas provas.
for k in range(1,qnt_aluno+1):
    nota_final = 0
    aluno = str(input("Insira o nome do aluno que realizou as provas a serem corrigidas agora: "))
    qnt_provas_realizadas = int(input("Insira a quantidade de provas que o aluno {} realizou:".format(aluno)))
    #Comando for para inserir a quantidade de provas que o aluno realizou.
    for i in range(1, qnt_provas_realizadas + 1):
        qnt_questoes = int(input("Prova {} tem quantas questões?: ".format(i)))
        nota_aluno = 0
        #Inserir a quantidade de questões que há em cada prova.
        for j in range(1, qnt_questoes + 1):
            gabarito = str(input("Qual é a alternativa correta na questao {}?: ".format(j)))
            questao_do_aluno = str(input("Alternativa que o aluno marcou: "))
            #Condição para verificar se o aluno acertou a questão ou não.
            if gabarito == questao_do_aluno:
                print("Ok, a correção está de acordo.")
                #Caso a correção da questão estiver correta será atribuido um valor referente àquela nota.
                #Levando em conta o peso de cada questão.
                peso_questao = int(input("Insira o peso da questao sendo avaliada: "))
                #Comando while para evitar que o peso da questão seja inserido com valor igual ou menor que zero.
                while peso_questao <= 0:
                    peso_questao = int(input("O peso da questão deve ser um inteiro maior que zero. Tente de novo: "))
                nota_aluno = float((1 * peso_questao) + nota_aluno)
            #Caso o aluno erre a questão não será atribuida nenhum valor a nota dele.
            else:
                print("Ok, a correção não está de acordo.")
                nota_aluno = nota_aluno
        #Cálculo da média ponderada para devolver um valor que será atribuida a nota da prova.
        nota_aluno = float(nota_aluno / qnt_questoes)
        #Soma das provas para posteriormente realizar a média aritmética das provas.
        nota_final = float(nota_final + nota_aluno)
        print("A nota do aluno {} na prova {} foi de {}".format(aluno, i, nota_aluno))
    #Divisão da média aritmética.
    nota_final = float(nota_final / qnt_provas_realizadas)
    print("Concluído o processo de correção. A nota final do aluno {} é {}".format(aluno, nota_final))
    #Condição para verificar se o aluno foi aprovado ou reprovado.
    if nota_final > 7:
        print("Situação do aluno {}: Aprovado!".format(aluno))
    else:
        print("Situação do aluno {}: Reprovado!".format(aluno))