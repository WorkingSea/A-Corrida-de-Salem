import random
import time
from rich.console import Console
console = Console()

#Valores do protagonista
class Personagem:
    def __init__(self, Nome, Ordem, Popularidade, Bônus, AmigoDoRei, Traidor, Vitória, Vivo, Rei):
        self.Nome = Nome
        self.Ordem = Ordem
        self.Popularidade = Popularidade
        self.Bônus = Bônus
        self.AmigoDoRei = AmigoDoRei
        self.Traidor = Traidor
        self.Vitória = Vitória
        self.Vivo = Vivo
        self.Rei = Rei

#Valores do rival do protagonista no torneio
class Rival:        
    def __init__(self, Nome, Ordem, Bônus):
        self.Nome = Nome
        self.Ordem = Ordem
        self.Bônus = Bônus

#Código da rebelião
def rebelião():
    def linchamento(chance):
        if chance >= 50:
            console.print('A população furiosa invade o campo de corrida e uma multidão se vira em sua direção, visando lhe linchar, com sorte, você consegue escapar',
            'e com ajuda da guarda real, foge para o castelo aonde se refugia.')
            console.print('Você se esconde no palácio com o rei e a família real, parece que vai ficar tudo bem, mas em poucas horas a população cerca o castelo e começa',
            'a tentar invadi-lo, sendo repelidos pela guarda real. Rumores se espalham no castelo que membros da nobreza estão participando da conspiração e seus soldados',
            'pessoais participam do cerco ao castelo.')
            console.print('Ao observar pelas janelas do palácio, é possível ver a cidade em chamas, milhares de casas e zonas comerciais sendo queimadas e agitação',
            'em todas as ruas. Após alguns dias nos quais milhares morrem, o rei se apróxima de você.')
            console.print('O Rei lhe informa que há um túnel secreto pelo qual pretende fugir.')
            console.print('1. Fugir com o Rei.')
            console.print('2. Dizer ao Rei que vai ficar')
            console.print('3. Aconselhar o Rei a ficar e lutar.')
            if Personagem.Traidor == True:
                print('4. Dizer ao Rei que vai ficar e vazar a localização do túnel para os partidários de Henrique.')
            console.print()
            Escolha = input('')

            if Escolha == '1':
                console.print(Personagem.Nome + ' foge do palácio junto com a família real através de um túnel secreto, o Rei se refugia junto com a corte em uma cidade',
                'próxima e o palácio é tomado pela nobreza, que coroa Conde Henrique como o novo Rei de Salém, o Reino se divide entre os dois candidatos, assim como as',
                'ordens de cavalaria, tanto a capital quanto o reino entram em sangrentos conflitos.')
                Vencedor = dado(2)
                if Vencedor == 1:
                    console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Jefferson retoma o controle de Salém e derrota os demais rebeldes,',
                    Personagem.Nome, 'se torna o novo Grão-Mestre dos' + Personagem.Ordem + '.')
                    fim_do_jogo()
                elif Vencedor == 2:
                    console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Henrique mata o Rei Jefferson na Batalha do Vale da Morte,',
                    Personagem.Nome,'morre durante a batalha ferido pela lança de um dos cavaleiros inimigos. Conde Henrique, agora Rei Henrique se torna o Rei indubitável de Salém.')
                    Personagem.Vivo = False
                    fim_do_jogo()

            elif Escolha == '2':
                console.print(Personagem.Nome + ' fica no castelo enquanto a família real foge, eventualmente os guardas cedem e o exército dos aristocratas', 
                'junto com parte da população invade o castelo.')
                console.print('Você:')
                console.print('1. Se rende aos invasores.')
                console.print('2. Luta até a morte contra os invasores')
                rendição = input('')
                if rendição == '1':
                    console.print('Se rendendo ao aos invasores, você é imediatamente preso enquanto Henrique é coroado Rei de Salém.')
                    console.print('Uma semana após sua prisão, o Grão Mestre de sua ordem negocia sua libertação em troca de suporte a Henrique, o que é aceito e',
                    'você é prontamente libertado. Distante de Salém, Jefferson tenta organizar um contra-ataque, mas com a maioria das ordens apoiando Henrique,',
                    'sua tentativa falha e Jefferson foge de Salém, se refugiando em outro reino.')
                
                elif rendição == '2':
                    console.print('Você morre em batalha junto da guarda real, o Rei, longe da capital, se organiza com os vassalos que o apoiavam e inicia',
                    'a contra-revolução contra Henrique.')
                    Personagem.Vivo = False
                    Vencedor = dado(2)
                    if Vencedor == 1:
                        console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Jefferson retoma o controle de Salém',
                        'e derrota os demais rebeldes e restabelece seu reinado.')
                        fim_do_jogo()
                    elif Vencedor == 2:
                        console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Henrique mata o Rei Jefferson na Batalha do Vale da Morte,', 
                        'Conde Henrique, agora Rei Henrique se torna o Rei indubitável de Salém')
                        fim_do_jogo()
            
            elif Escolha == '3':
                Rebeldia = dado(100)
                if Personagem.Popularidade >= Rebeldia:
                    console.print('O Rei concorda, e cria um plano, lhe enviando com um sacos de ouro para distribuir para a população visando distrai-la,',
                    'o plano dá certo e não só a população como vários dos soldados fieis a Henrique se distraem com a chance de ouro, e Jefferson aproveita', 
                    'a situação para lançar seu contra-ataque, pegando os rebeldes de surpresa e iniciando uma batalha no centro da cidade, os',
                    Personagem.Ordem,'chegam em meio a batalha auxiliando o Rei e em pouco tempo os rebeldes são esmagados e Henrique é preso,',
                    'sendo executado uma semana depois em praça pública pelo crime de traição, a Ordem dos', Rival.Ordem,'é expurgada e a aristocracia', 
                    'traidora que não morreu durante a batalha sofre o mesmo destino de Henrique, incluindo', Rival.Nome +'.')
                    fim_do_jogo()
                elif Personagem.Popularidade < Rebeldia:
                    console.print('O Rei concorda, e cria um plano, lhe enviando com um sacos de ouro para distribuir para a população visando distrai-la,',
                    'o plano dá errado e assim que você sai com as moedas de ouro você é atacado pela população e é espancado até a morte, algumas semanas',
                    'depois o assalto ao palácio tem sucesso e o Rei Jefferson é capturado e executado, Conde Henrique é coroado o novo Rei indisputável de Salém.')
                    Personagem.Vivo = False
                    fim_do_jogo()    
            elif chance < 50:
                console.print('A população furiosa invade o campo de corrida e uma multidão se vira em sua direção, visando lhe linchar.',
                'Eles conseguem lhe capturar e você é espancado até a morte pela multidão.')
                Personagem.Vivo = False
                fim_do_jogo()

            elif Escolha == '4':
                console.print('Barão Jacques de Molai viaja com seus soldados até o fim do túnel e assassina o Rei quando este tenta sair,',
                'o palácio é eventualmente assaltado e você é poupado, Henrique é coroado o novo Rei indisputável de Salém. Você é presenteado',
                'com títulos em uma cidade costeira e rapidamente se torna um dos homens mais ricos de Salém.')
                fim_do_jogo()    

        elif chance <= 50:
            console.print('A população furiosa invade o campo de corrida e parte da multidão se vira em sua direção, visando lhe linchar,',
            'você tenta escapar mas não consegue, sendo espancado até a morte pele público.')
            Personagem.Vivo = False
            fim_do_jogo()   

    if Personagem.Vitória == True and Personagem.AmigoDoRei == True:
        console.print('A população furiosa invade o campo de corrida e uma multidão se vira em sua direção, visando lhe linchar. Por sorte,',
        'membros da guarda real intervem e um deles lhe agarra pelo braço e lhe puxa para fora do domo e você é levado para o palácio real,',
        'nas ruas a rebelião parece ter se espalhado, e todos parecem querer a sua cabeça, mas ao menos no palácio você estará seguro.')
        console.print('Você se esconde no palácio com o rei e a família real, parece que vai ficar tudo bem, mas em poucas horas a população',
        'cerca o castelo e começa a tentar invadi-lo, sendo repelidos pela guarda real. Rumores se espalham no castelo que membros da nobreza', 
        'estão participando da conspiração e seus soldados pessoais participam do cerco ao castelo.')
        console.print('Ao observar pelas janelas do palácio, é possível ver a cidade em chamas, milhares de casas e zonas comerciais sendo queimadas', 
        'e agitação em todas as ruas. Após alguns dias nos quais milhares morrem, o rei se apróxima de você.')
        console.print('O Rei lhe informa que há um túnel secreto pelo qual pretende fugir.')
        console.printprint('1. Fugir com o Rei.')
        console.print('2. Dizer ao Rei que vai ficar')
        console.print('3. Aconselhar o Rei a ficar e lutar.')
        console.print()
        Escolha = input('')

        if Escolha == '1':
            console.print(Personagem.Nome,'foge do palácio junto com a família real através de um túnel secreto,', 
            'o Rei se refugia junto com a corte em uma cidade próxima e o palácio é tomado pela nobreza, que coroa Conde Henrique como o novo Rei de Salém', 
            'o Reino se divide entre os dois candidatos, assim como as ordens de cavalaria, tanto a capital quanto o reino entram em sangrentos conflitos.')
            Vencedor = dado(2)
            if Vencedor == 1:
                console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Jefferson retoma o controle de Salém e derrota os demais rebeldes,',
                Personagem.Nome,'se torna o novo líder da Ordem dos Cavaleiros da Noite e devido a sua lealdade e comando na guerra civil, se torna o novo marechal do Reino,',
                'substituindo o Barão Jacques de Molai, que havia se aliado aos traidores.')
                fim_do_jogo()
            elif Vencedor == 2:
                console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Henrique mata o Rei Jefferson na Batalha do Vale da Morte,',
                Personagem.Nome,'morre durante a batalha ferido pela lança de um dos cavaleiros inimigos. Conde Henrique, agora Rei Henrique se torna o Rei', 
                'indubitável de Salém e',Rival.Nome,'se torna o novo marechal do reino como recompensa devido a sua lealdade a Henrique e comando durante', 
                'a guerra civil, eventualmente se tornando também o Grão-Mestre da Ordem dos Cavaleiros do Sol Nascente.')
                Personagem.Vivo = False
                fim_do_jogo()

        elif Escolha == '2':
            console.print(Personagem.Nome + ' fica no castelo enquanto a família real foge, eventualmente os guardas cedem e o exército dos aristocratas',
            'junto com parte da população invade o castelo.')
            console.print('Você:')
            print('1. Se rende aos invasores.')
            print('2. Luta até a morte contra os invasores')
            rendição = input('')
            if rendição == '1':
                console.print('Se rendendo ao aos invasores, você é imediatamente preso enquanto Henrique é coroado Rei de Salém.')
                console.print('Uma semana após sua prisão, o Grão Mestre de sua ordem negocia sua libertação em troca de suporte a Henrique,',
                'o que é aceito e você é prontamente libertado. Distante de Salém, Jefferson tenta organizar um contra-ataque, mas com a maioria',
                'das ordens apoiando Henrique, sua tentativa falha e Jefferson foge de Salém, se refugiando em reino vizinho.')
                fim_do_jogo()

            elif rendição == '2':
                console.print('Você morre em batalha junto da guarda real, o Rei, longe da capital, se organiza com os vassalos que o apoiavam',
                'e inicia a contra-revolução contra Henrique.')
                Personagem.Vivo = False
                Vencedor = dado(2)
                if Vencedor == 1:
                    console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Jefferson retoma o controle de Salém', 
                    'e derrota os demais rebeldes e restabelece seu reinado.')
                elif Vencedor == 2:
                    console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Henrique mata o Rei Jefferson na Batalha do Vale da Morte,',
                    'Conde Henrique, agora Rei Henrique se torna o Rei indubitável de Salém e',Rival.Nome,'se torna o novo marechal do reino como recompensa devido',
                    'a sua lealdade a Henrique e comando durante a guerra civil, eventualmente se tornando também o grão-mestre da Ordem dos Cavaleiros do Sol Nascente.')

            fim_do_jogo()
        elif Escolha == '3':
            Rebeldia = dado(100)
            if Personagem.Popularidade >= Rebeldia:
                console.print('O Rei concorda, e cria um plano, lhe enviando com um sacos de ouro para distribuir para a população visando distrai-la,',
                'o plano dá certo e não só a população como vários dos soldados fieis a Henrique se distraem com a chance de ouro, e Jefferson aproveita',
                'a situação para lançar seu contra-ataque, pegando os rebeldes de surpresa e iniciando uma batalha no centro da cidade,',
                'os Cavaleiros da Noite chegam em meio a batalha auxiliando o Rei e em pouco tempo os rebeldes são esmagados e Henrique é preso,', 
                'sendo executado uma semana depois em praça pública pelo crime de traição, a Ordem dos Cavaleiros do Sol Nascente é expurgada e a',
                'aristocracia traidora que não morreu durante a batalha sofre o mesmo destino de Henrique.')
                fim_do_jogo()
            elif Personagem.Popularidade < Rebeldia:
                console.print('O Rei concorda, e cria um plano, lhe enviando com um sacos de ouro para distribuir para a população visando distrai-la,', 
                'o plano dá errado e assim que você sai com as moedas de ouro você é atacado pela população e é espancado até a morte, algumas semanas', 
                'depois o assalto ao palácio tem sucesso e o Rei Jefferson é capturado e executado, Conde Henrique é coroado o novo Rei indisputável de Salém.')
                Personagem.Vivo = False
                fim_do_jogo()    

    if Personagem.Vitória == True and Personagem.AmigoDoRei == False:
        linchamento(dado(100))

    if Personagem.Vitória == False and Personagem.AmigoDoRei == True:
        console.print('Em meio a confusão um mensageiro do Rei também se aproxima e lhe convida para o castelo, afirmando que lá é mais seguro.')
        print('Você se refugia no palácio real com o Rei, por 3 dias chamas e corpos vão se acumulando na cidade.')
        console.print('No terceiro ele faz faz um discurso ao público com você ao lado afirmando que de foram descobertas intervenções estrangeiras,', 
        'os eletrianos haviam envenenado o cavalo de ' + Personagem.Nome + ' antes do torneio, o que o causou a não correr tão rápido quanto devia.')
        console.print(Rival.Nome + ' é preso por conspiração e executado em praça pública, isso parece ser o suficiente para acalmar a população',
        'enquanto você é considerado vencedor a posteriori.')
        fim_do_jogo()

    if Personagem.Vitória == False and Personagem.Traidor == True:
            console.print('Em meio a rebelião, os nobres insatisfeitos com o rei aproveitam a situação para tentar organizar a população se rebelando',
            'junto de seus próprios exércitos para atacar o palácio.')
            console.print('Você:')
            console.print('1. Se une a eles e marcha até o palácio real para depor o Rei em favor de Conde Henrique.')
            console.print('2. Retorna para a base dos Cavaleiros do Sol Nascente, já cumpriu o seu papel e agora tudo está nas mãos do Único.')
            if Personagem.Popularidade > 75:
                console.print('3. Organizo meu próprio exército dentre os rebeldes visando me impor como Rei.')

            RebeliãoSucedida = input()
            if RebeliãoSucedida == '1':
                console.print('Você marcha até o palácio junto do Barão e do Conde e o cerca, a cidade entra em chamas enquanto o exército',
                'de vocês tentam tomar o palácio, quando finalmente conseguem duas semanas depois, não encontram o Rei em lugar nenhum,',
                'sendo informado por um dos guardas que ele fugiu por um túnel.')
                console.print('Henrique é coroado Rei e você abandona os Cavaleiros do Sol Nascente e recebe o titulo de Conde de Lisopolis,',
                'mas nem tudo é tão fácil. O Rei organiza seus aliados e enquanto metade das ordens de cavalaria suportam Henrique, a outra metade suporta',
                'Jefferson e o reino cai em guerra civil.')
                Vencedor = dado(2)
                if Vencedor == 1:
                    console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Henrique mata o Rei Jefferson na Batalha do Vale da Morte,',
                    'devido a sua lealdade e comando na guerra civil,',Personagem.Nome,'se torna o novo marechal do Reino, substituindo o Barão Jacques de Molai,',
                    'que morreu pela lança de um dos cavaleiros inimigos durante a Batalha do Vale das Sombras.')
                    fim_do_jogo()
                elif Vencedor == 2:
                    console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Jefferson finalmente marcha sobre Salem novamente como seu rei,',
                    Personagem.Nome,'morre durante o cerco de Salém alvejado por uma flecha inimiga. Jefferson se restabelece como Rei indubitável de Salém.')
                    Personagem.Vivo = False
                    fim_do_jogo()

            elif RebeliãoSucedida == '2':
                Vencedor = dado(2)
                if Vencedor == 1:
                    console.print('Henrique marcha até o palácio e após alguns dais de cerco, consegue o tomar de assalto da guarda real, entretanto,', 
                    'Jefferson havia fugido em um túnel secreto e se refugiado nas cidades vizinhas, Henrique é coroado Rei em Salém, mas Jefferson',
                    'levanta um exército dentre seus apoiadores e com o reino dividido, uma guerra civil se inicia.')
                    console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Henrique mata o Rei Jefferson na Batalha do Vale da Morte.',
                    Personagem.Nome,'se torna eventualmente o novo Grão-Mestre dos Cavaleiros do Sol Nascente, seu papel na conspiração um segredo para a história,',
                    'mas necessário para salvar Salém da incompetência de Jefferson.')
                    fim_do_jogo()
                elif Vencedor == 2:
                    DedoDuro = dado(2)
                    if DedoDuro == 1:
                        console.print('Henrique marcha até o palácio e após alguns dais de cerco, consegue o tomar de assalto da guarda real, entretanto,',
                        'Jefferson havia fugido em um túnel secreto e se refugiado nas cidades vizinhas, Henrique é coroado Rei em Salém, mas Jefferson',
                        'levanta um exército dentre seus apoiadores e com o reino dividido, uma guerra civil se inicia.')
                        console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Jefferson finalmente marcha sobre Salem',
                        'novamente como seu rei. O papel de',Personagem.Nome,'na conspiração é revelado pelo Barão Jacques após ser torturado, e ',Personagem.Nome,
                        'é preso e degolado alguns dais depois em praça pública. Jefferson se restabelece como o Rei indubitável de Salém até o fim de sua vida.')
                        Personagem.Vivo = False
                        fim_do_jogo()
                    elif DedoDuro == 2: 
                        console.print('Henrique marcha até o palácio e após alguns dais de cerco, consegue o tomar de assalto da guarda real, entretanto,',
                        'Jefferson havia fugido em um túnel secreto e se refugiado nas cidades vizinhas, Henrique é coroado Rei em Salém, mas Jefferson',
                        'levanta um exército dentre seus apoiadores e com o reino dividido, uma guerra civil se inicia.')
                        console.print('Após anos de sangrenta guerra e diversos expurgos nas ordens de cavalaria, Jefferson finalmente marcha sobre',
                        'Salem novamente como seu rei, com os conspiradores e traidores degolados em praça pública Jefferson se restabelece como o Rei',
                        'indubitável de Salém até o fim de sua vida.')
                        console.print(Personagem.Nome ,'se torna eventualmente o novo Grão-Mestre dos Cavaleiros do Sol Nascente, seu papel na vergonhosa',
                        'conspiração um segredo para a história que nunca foi revelado.')
                        fim_do_jogo()

            elif RebeliãoSucedida == '3':
                console.print('Henrique marcha até o palácio, cercando-o com o objetivo de assalta-lo, mas suas ações não são despercebidas e logo os soldados',
                'da facção de Henrique começam a entrar em combate com os seus, até o ponto de briga generalizada na cidade que agora ardia em chamas. Jefferson',
                'vê a divisão entre os rebeldes como oportunidade para um contra-ataque e logo as ruas são tomadas por brigas entre os diferentes partidários,',
                'com Henrique comandando um grupo, Jefferson outro e você o resto. As ordens de cavalaria se dividem entre os três grupos e logo começam a',
                'batalhar entre si também, o resto do Reino aguarda o resultado da batalha para decidir qual lado tomar.')
                Vencedor = dado(3)
                if Vencedor == 1:
                    console.print('Após semanas de caos na cidade, o Rei e seus aliados conseguem subjulgar as outras facções,',
                    'Henrique é capturado e enforcado em praça pública, enquanto',Personagem.Nome,'morre em combate fatiado pela espada de',Rival.Nome,
                    'em um combate pessoal. A ordem é restabelecida em Salém.')
                    Personagem.Vivo = False
                    fim_do_jogo()

                elif Vencedor == 2:
                    console.print('Após semanas de caos na cidade, Henrique consegue subjulgar as outras facções, o Rei é morto por Henrique',
                    'em um combate pessoal enquanto ' + Personagem.Nome + ' é capturado em batalha e após a coroação de Henrique, executado em',
                    'praça pública, sendo marcado pela história como um oportunista que falhou.')
                    Personagem.Vivo = False
                    fim_do_jogo()
                elif Vencedor == 3:
                    console.print('Após semanas de caos na cidade,',Personagem.Nome,'consegue subjulgar as outras facções, Henrique é derrotado',
                    'em um combate pessoal enquanto Jefferson é encurralado enquanto tentava fugir e linchado pela população.',
                    Personagem.Nome,' é coroado o novo Rei de Salém. Vida Longa ao Rei!')
                    Personagem.Rei = True
                    fim_do_jogo()               

    if Personagem.Vitória == False and Personagem.AmigoDoRei == False and Personagem.Traidor == False:
        console.print('A população irada invade o campo e pula encima de',
        Rival.Nome + ', linchando-o vivo em uma cena horrorosa e brutal, em meio a confusão alguns de seus camaradas',Personagem.Ordem,'invadem o campo e ajudam',
        'a te proteger, lhe guiando para fora do hipódromo e de volta para a base da ordem.')
        console.print('O Grão-Mestre organiza os membros da ordem.')

        GuerraCivil = dado(2)
        if GuerraCivil == 1:
            Personagem.Popularidade -= dado(100)
            if Personagem.Ordem == "Cavaleiros do Sol Nascente":    
                console.print('Grão-Mestre: É nosso dever manter a ordem na cidade durante as manhãs, e hoje não é diferente. ',
                'A cidade está em chamas, o que era para ser um evento esportivo se tornou um mar de sangue. É hora de nos organizamos',
                'e pormos um fim a essa rebelião e restaurar ordem a Salém. Por Lisandros, por Salém, pelo Único!')
                console.print('Você, junto dos demais cavaleiros equipam suas armas e montam em seus cavalos, e partem para conter a rebelião,',
                'o dia é longo e difícil: Muitos daqueles que gritaram seu nome estavam entre os rebeldes e muitos deles mortos por sua própria espada.',
                'Mais tarde, membros de outras ordens se unem para ajudar a conter a rebelião, incluindo Cavaleiros da Noite, a Liga Dourada e até mesmo',
                'os Escudeiros da Fenix, que normalmente só lutavam em guerras e ignoravam os acontecimentos da cidade.') 
                print('A noite chega e vocês estão exaustos, mas a rebelião é contida com sucesso, cerca de 30.000 habitantes foram mortos,',
                'mas a ordem é mantida e vocês retornam para a base.')
                fim_do_jogo()
            if Personagem.Ordem == "Cavaleiros da Noite":
                console.print('Grão-Mestre: É nosso dever manter a ordem na cidade durante as noites, mas os Cavaleiros do Sol Nascente claramente falharam.',
                'A cidade está em chamas, o que era para ser um evento esportivo se tornou um mar de sangue. É hora de nos organizamos e pormos um fim',
                'a essa rebelião e restaurar ordem a Salém, se não nós, quem? Por Lisandros, por Salém, pelo Único!')
                console.print('Você, junto dos demais cavaleiros equipam suas armas e montam em seus cavalos, e partem para conter a rebelião,',
                'o dia é longo e difícil: Muitos daqueles que gritaram seu nome estavam entre os rebeldes e muitos deles mortos por sua própria espada.', 
                'Mais tarde, os Cavaleiros do Sol Nascente finalmente chegam, trazendo junto a Liga Dourada e até mesmo os Escudeiros da Fenix, que normalmente',
                'só lutavam em guerras e ignoravam os acontecimentos da cidade.') 
                print('A noite chega e vocês estão exaustos, mas a rebelião é contida com sucesso, cerca de 30.000 habitantes foram mortos,',
                'mas a ordem é mantida, mesmos cansados, ainda havia o resto da noite para patrulhar e você se empurra pela noite')
                fim_do_jogo()
        if GuerraCivil == 2:
            console.print('Grão-Mestre: Eu fui informado por Nestor Genrikh da Ordem do Sangue que a rebelião que ocorreu é uma conspiração',
            'da nobreza contra o Rei, ele me aconselhou a não agir até realizarmos uma convocação do Conselho Real e irei tomar o conselho dele.')         
            print('Algumas semanas depois...')
            time.sleep(3)
            console.print('Grão-Mestre: O conselho está feito, com o Conde Henrique, ou melhor, Rei Henrique tomando o castelo e sendo coroado Rei,',
            'tivemos de , os Cavaleiros da Noite, os Guardiões do Pergaminho e os Guardiões da Prece declaramos neutralidade, mas as demais ordens votaram',
            'em favor de reconhecer Henrique como Rei e forçar a abdicação de Jefferson, aparentemente Henrique é um dos descendentes de Willalme, quem adivinharia? Huh.')
            console.print('Jefferson foge de Salém e se recusa a reconhecer as decisões do Conselho, mas sem suporte de nenhuma das ordens ou da nobreza,' 
            ,'ele é incapaz de levantar um exército e abandona o continente. Vida Longa ao Novo Rei Henrique!')
            fim_do_jogo()

#Código de fim de jogo
def fim_do_jogo():
    console.print('Este é o fim do jogo, espero que tenha gostado. Existem outros finais dependendo de suas escolhas e sua sorte.')
    console.print('Seu nome é ' + Personagem.Nome + '.')
    console.print('Você foi um membro dos ' + Personagem.Ordem + '.')
    print('Seu nível de popularidade entre a população era de ' + str(Personagem.Popularidade) + '%.')
    console.print('Seu rival era ' + Rival.Nome + " da ordem dos " + Rival.Ordem + '.')
    if Personagem.Vivo == True:
        console.print('Você sobreviveu aos eventos da Corrida de Salém.')
    if Personagem.Vivo == False:
        console.print('Você morreu durante os eventos da Corrida de Salém.')
    if Personagem.AmigoDoRei == True:
        console.print('Você foi amigo do Rei Jefferson.')
    if Personagem.AmigoDoRei == False:
        console.print('Você não era amigo do Rei Jefferson.')
    if Personagem.Traidor == True:
        console.print('Você fazia parte da conspiração contra o Rei Jefferson.')
    if Personagem.Traidor == False:
        console.print('Você não fazia parte da conspiração contra o Rei Jefferson')
    if Personagem.Vitória == True:
        console.print('Você venceu o torneio.')
    if Personagem.Vitória == False:
        console.print('Você não venceu o torneio.')
    if Personagem.Rei == True:
        console.print('Você se tornou Rei de Salém.')
    if Personagem.Rei == False:
        console.print('Você não se tornou Rei de Salém.')
    print('')
    console.print('Obrigado por Jogar, digite 1 e aperte enter para jogar novamente, 2 para fechar o programa ou qualquer outra coisa para amar Lain.')
    Restart = input()

    if Restart == '1':
        main()
    elif Restart == '2':    
        raise SystemExit()
    #Ama lain    
    else:
        string='VAMOS TODOS AMAR LAIN '
        for i in range(20):
            print(string)
            string = string + string  
            time.sleep(0.5)
        input('Feliz aniversário.')
        fim_do_jogo()

#Dado a ser rolado
def dado(lados):
    return random.randint(1, lados)

#Eventos da corrida
def corrida():
    #Mostra quem está ganhando a corrida
    def velocidade_cheque():
        if ProtagonistaVelocidade > InimigoVelocidade:
                console.print('No momento você está ganhando a corrida.')
        elif InimigoVelocidade > ProtagonistaVelocidade:
                console.print('No momento ' + Rival.Nome + ' está ganhando a corrida.')

    #Verifica se o cavalo morre durante a corrida devido as ações do jogador
    def cavalo_morte(Energia):
        EnergiaLimite = 30    
        if Energia <= EnergiaLimite:
            console.print('Um de seus cavalos sofre um ataque cardíaco durante a corrida e a carroça capota')
            Personagem.Vitória = False
    #Código de cada uma das voltas, ocorre 3 vezes no total.
    def volta():
        console.print('1. Forçar os cavalos')
        console.print('2. Manter a velocidade atual')
        console.print('3. Forçar menos o Cavalo')
        ação = input()
        if ação == '1':
            cavalo_morte(dado(100))
            return 20
        elif ação =='2':
            cavalo_morte(dado(500))
            return 0
        elif ação == '3':
            return -20

    ProtagonistaVelocidade = dado(100) + Personagem.Bônus + volta()
    InimigoVelocidade = dado(100) + Rival.Bônus
    if Personagem.Vitória == False:
        return None
    velocidade_cheque()

    ProtagonistaVelocidade += dado(100) + Personagem.Bônus + volta() 
    InimigoVelocidade += dado(100) + Rival.Bônus
    if Personagem.Vitória == False:
        return None
    velocidade_cheque()


    ProtagonistaVelocidade += dado(100) + Personagem.Bônus + volta() 
    InimigoVelocidade += dado(100) + Rival.Bônus
    if Personagem.Vitória == False:
        return None

    if ProtagonistaVelocidade > InimigoVelocidade:
        Personagem.Vitória = True
    elif InimigoVelocidade > ProtagonistaVelocidade:
        Personagem.Vitória = False    

#Jogo
def main():
    Personagem.AmigoDoRei = False
    Personagem.Popularidade = 25
    Personagem.Bônus = 0
    Personagem.Vitória = None
    Personagem.Traidor = False
    Personagem.Vivo = True
    Personagem.Rei = False

    Rival.Bônus = dado(50)

    console.print(
        "Esse é um jogo baseado em texto, em certos momentos, você será dado "
    "diversas opções pelo qual escolher sua ação, por exemplo:")
    console.print("1.Beber água")
    console.print("2.Beber refrigerante ")
    console.print("3.Beber suco"
    )
    console.print("Em uma situação como essa, você escolhe a sua ação simplesmente digitando o número, por exemplo, caso queira beber água",
    "você simplesmente digita 1 e aperta enter."
    )

    console.print("Quando estiver pronto para jogar, aperte enter")
    input()
    print('')
    print('''\
                                          .o.                                                                             
                                         .888.                                                                                           
                                        .8"888.                                                                           
                                       .8' `888.                                            
                                      .88ooo8888.   
                                     .8'     `888.                                       
                                    o88o     o8888o 
                                                                                             
                                                    
                                                                                                         
            .oooooo.                                o8o        .o8                                      
           d8P'  `Y8b                               `"'       "888                            
          888           .ooooo.  oooo d8b oooo d8b oooo   .oooo888   .oooo.                                         
          888          d88' `88b `888""8P `888""8P `888  d88' `888  `P  )88b  
          888          888   888  888      888      888  888   888   .oP"888                   
          `88b    ooo  888   888  888      888      888  888   888  d8(  888                  
           `Y8bood8P'  `Y8bod8P' d888b    d888b    o888o `Y8bod88P" `Y888""8o              
                                                                                            
                                                                              
                                                                                              
                                       .o8                                                                              
                                      "888                                         
                                  .oooo888   .ooooo.                  
                                 d88' `888  d88' `88b                              
                                 888   888  888ooo888                 
                                 888   888  888    .o              
                                 `Y8bod88P" `Y8bod8P'                                  
                                                      
                                                      
                                                      
                 .oooooo..o           oooo                              
                d8P'    `Y8           `888                              
                Y88bo.       .oooo.    888   .ooooo.  ooo. .oo.  .oo.   
                 `"Y8888o.  `P  )88b   888  d88' `88b `888P"Y88bP"Y88b  
                     `"Y88b  .oP"888   888  888ooo888  888   888   888  
                oo     .d8P d8(  888   888  888    .o  888   888   888  
                8""88888P'  `Y888""8o o888o `Y8bod8P' o888o o888o o888o 
                          ''')
    time.sleep(3)

    print('''\

                                                                       
      Yb,     ________            
       Y8baadP""""""""Yba,_      
    aaadP"'             `""Yb,   
    `Y8(                    `"Yb,
      `Y,                      `Yba,
        Y,  (O)                   `Yba,
        `Y,                          ""Yba,________,,aaddddbbbaa,,____,aa,_
         `Y,       ,aa                   `""""""""""''          ``""""''  "Y,
           Y,      d'8                                                "Ya   `Y,
           `b      8 8                                                  `Y,   Y,
            Ya o  ,8 8                                                    b   `b
             Yb,_,dP 8                                                    Y    8
              `""""  Y                                                    8    8
                     I,                                                   8    8
                     `b                                                   P    [
                      `b                                                 d'    [
                       d                                                ,P     [
                     ,d'    ,PY,         ,P"YaaaaaaP"Ybaaa,,_           d'     [
                    d"    ,P"  Y,        d'           8'  `""db,       d'      8
                   d'   ,P"    `Y,       8            I,     d'"b,     8a      P
                  d(    (       `Y,      P            `b    ,P  `Y,    8`Ya___d'
                  "Y,   "b,      `Y,    ,I             8    d'   `8    8  `"""'
                    "Y,   "b,  __ `8,   d'            ,8   ,P     8    8
                      "Y,   "bd88b `b   8             I'   d'     Y,   8
                        "Y,    888b 8   8             8   ,P      `b   8
                          "Ya,,d888b8   P            d'  ,P'       8   Y,
                             `"""",d"  ,I        ,adPb__aP'        Y   `b
                               ,a8P,__aP'       d888888P'         ,d    8
                              d8888888'         88888888       ,d888bbaaP
                              88888888                         88888888'

                                    ASCII by Normand Veilleux
                              ''')
    time.sleep(3)
    print("O ano é 25 AGC, os Estados Cruzados (ou Reino de Salém, como é chamado por seus nativos) é governado por Jefferson de Nika,",
    "que herdou o reino de seu infértil tio. ")
    console.print("Jefferson se encontra em uma situação difícil, a guerra contra os pagãos de Eletria começou com sucesso, mas recentemente",
    "o exército de Salém havia sido massacrado na Batalha do Rio Negro, causando um grande dano a popularidade de Jefferson e até mesmo fazendo",
    "com que suporte ao Conde Henrique") 
    console.print("Henrique, diferente de Jefferson, não teve a reputação manchada por perder alguma batalha e é bem jovem ainda, é conhecido por sua devoção",
    "religiosa ao Único e havia aconselhado o Rei a recuar ao invés de lutar a Batalha do Rio Negro")
    console.print('Para evitar rebelião, o Rei Jefferson decide distrair a população com uma grande corrida de bigas.')
    console.print("Para participar na corrida, Jefferson convoca os Cavaleiros da Noite e os Cavaleiros do Sol Nascente")
    console.print("Ambas as ordens aceitam imediatamente a ordem e começam a se preparar para a corrida, que para elas representa algo muito maior: ")
    console.print("Ambas as ordens tem um grande sentimento de rivalidade, os Cavaleiros do Sol Nascente normalmente patrulham a cidade de dia e os Cavaleiros da Noite," ,
    "bem, a noite.")
    console.print("O resultado é que, quando problemas ocorrem, ambas passam a culpar uma a outra por não terem cumprido bem o seu papel afirmando que a" ,
    "origem do problema é a negligência da outra, essas disputas já resultaram em batalhas em tavernas, e a população, sempre mesmerizada com os fantásticos",
    "cavaleiros, começa a tomar lados também, de forma que o conflito é, não só uma questão de prestigio, mas também de popularidade para ambas as ordens," ,
    "que agora tem uma válvula de escape para a sua rivalidade em forma de corrida.")
    console.print("")
    console.print("Qual é o seu nome?")
    Personagem.Nome = input()
    if Personagem.Nome == '':
        Personagem.Nome = 'Pedro de Alcântara João Carlos Leopoldo Salvador Bibiano Francisco Xavier de Paula Leocádio Miguel Gabriel Rafael Gonzaga de Bragança e Bourbon'
    console.print("Certo " + Personagem.Nome + ", de qual ordem você pertence?")
    console.print("1. Cavaleiros da Noite")
    console.print("2. Cavaleiros do Sol Nascente")
    firstchoice = input()
    if firstchoice == "1":
        Personagem.Ordem = "Cavaleiros da Noite"
    elif firstchoice == "2":
        Personagem.Ordem = "Cavaleiros do Sol Nascente" 
    elif firstchoice == '3':
        Personagem.Ordem = "Cavaleiros do Calculo Oriental"
        Personagem.Popularidade = int(input('Popularidade: '))
        Personagem.Bônus = int(input('Bônus: '))
        Personagem.AmigoDoRei = int(input('Amigo do Rei (1 ou 0): '))
        Personagem.Traidor = int(input('Traidor (1 ou 0): '))
        Rival.Ordem = input('Ordem do Rival: ')

    console.print("")    
    console.print("Como membro dos "+ Personagem.Ordem+ ", você passa a boa parte do seu tempo patrulhando os subúrbios de Salem a procura de encrenqueiros",
    "e ladrões ou escoltando os arredores em seu cavalo a procura de coisas suspeitas.") 
    console.print("Quando não se há nada de interessante, para passar o tempo, você costuma competir em corridas com seus irmãos em armas e após ganhar",
    "grande parte delas, você passa a ganhar uma fama dentro na Ordem como um dos mais rápidos cavaleiros, por isso, não é com surpresa que logo após a",
    "corrida ser anunciada você foi escolhido para representar os " + Personagem.Ordem + '.')

    if Personagem.Ordem == "Cavaleiros da Noite":
        console.print("Algumas semanas antes da competição, Jefferson revelou bêbado em um jantar que está torcendo para os Cavaleiros da Noite,",
        "com o suporte dele sua popularidade cresce mais do que nunca")
        Rival.Ordem = "Cavaleiros do Sol Nascente"
        Rival.Nome = 'Julius'
    else:
        console.print("Algumas semanas antes da competição, o traidor do Rei disse que está torcendo para os Cavaleiros da Noite, será que o idiota não" 
        ,"percebe que sem nós a cidade estaria em caos?")
        console.print("O Grão-Mestre está furioso, e proíbe que os membros da Ordem participem de festas com o Rei ou digam coisas positivas a seu respeito", 
        "em uma especie de boicote.")
        Personagem.Popularidade += 25
        Rival.Ordem = "Cavaleiros da Noite"
        Rival.Nome = 'Bomani'
    #Opções para Cavaleiros da Noite
    if Personagem.Ordem == "Cavaleiros da Noite":
        print('Falta 1 mês até o torneio, como você passa a maior parte do seu tempo?')
        console.print('1. Participando de jantares e festas com o Rei')
        console.print('2. Aproveitando da popularidade para festejar na cidade com outros membros da Ordem sem ter de gastar um único denário')
        console.print('3. Treinando para o torneio')
        PrimeiraEscolha = input()
        if PrimeiraEscolha == '1':
            console.print('Durantes as festas, qual é sua prioridade?')
            console.print('1. Tentar fazer o Rei ficar bêbado de novo')
            console.print('2. Se divertir.')
            OutraEscolha = input()
            if OutraEscolha == "1":
                def rei_bebado(rolagem):
                    if rolagem <50:
                        console.print('Após beber um pouco ele decide parar para evitar que passe mal')
                    elif rolagem >=50 and rolagem<75:
                        console.print('O Rei fica bêbado o suficiente para que com lábia você seja capaz de convence-lo a lhe emprestar os cavalos mais',
                        'rápidos do estabulo real para o torneio')
                        Personagem.Bônus += random.randint(1, 100)
                    else:
                        console.print('O rei tem o tempo da vida dele com você, após beberem, conversarem e cantarem juntos você pode dizer que é praticamente amigo do rei')
                        Personagem.AmigoDoRei = True
                rei_bebado(dado(100))        
            elif OutraEscolha == "2":
                def amigo_do_rei(diversão):
                    if Diversão <=50:
                        console.print('O Rei fica satisfeito com sua presença e apreciação da festa, ambos definitivamente se tornam mais próximos')
                        Personagem.AmigoDoRei = True
                    else:
                        console.print('Você se diverte como nunca antes e está satisfeito com sua escolha, nunca que uma taverna da cidade poderia lhe',
                        'causar tanta diversão quanto a estupidez do bobo-da-corte ou o vinho exportado diretamente de Iolia, isso para não falar da deliciosa comida...')  
                amigo_do_rei(dado(100) + 25) 
        elif PrimeiraEscolha == '2':
            console.print("O anuncio do torneio e os rumores de que o Rei pessoalmente está torcendo para os Cavaleiros da Noite aumentaram",
            "a sua popularidade e você agora não só é reconhecido na cidade, como alguns burgueses passam a oferecer refeições gratuitas para você",
            "em algumas tavernas na esperança de atrair mais clientes interessados em estar perto de um dos competidores")
            console.print("Você:")
            console.print('1. Festejar longe dos camponeses, eles fedem.')
            console.print('2. Se une aos plebeus para festejar')
            OutraEscolha = input()
            if OutraEscolha == '1':
                console.print('Você se diverte bastante com seus companheiros e passam boa parte do tempo se lembrando de antigas batalhas e problemas da cidade.')
                Personagem.Popularidade += dado(10)
            elif OutraEscolha == '2':
                console.print('Você decide festejar dentre os mais-humildes e conta diversas histórias a eles, que se impressionam bastante e um bardo',
                'até mesmo decide improvisar em seu alaúde um pequeno Hino à ' + Personagem.Nome + '.')
                Personagem.Popularidade += 25
        elif PrimeiraEscolha == '3':
            console.print('Você decide treinar com os cavalos para o torneio em um planalto próximo a cidade.')
            Personagem.Bônus += 50
        Rival.Ordem = 'Cavaleiros do Sol Nascente'    
    #Opções para Cavaleiros do Sol Nascente
    if Personagem.Ordem == "Cavaleiros do Sol Nascente":
        console.print('Falta 1 mês até o torneio, como você passa a maior parte do seu tempo?')
        console.print('1. Festejando com os nobres')
        console.print('2. Aproveitando da popularidade para festejar na cidade com outros membros da Ordem sem ter de gastar um único denário')
        console.print('3. Treinando para o torneio')
        PrimeiraEscolha = input()
        if PrimeiraEscolha == '1':
            console.print('Ofendidos com o Rei dar suporte público aos Larápios da Noite na competição, sua ordem obviamente recusa os convites'
            ,'do rei para festas, mas isso não quer dizer que você não pode festejar com outros membros da nobreza')
            console.print('A maioria das festas são hospedadas pelo Barão Jacques de Molai em seu forte próximo a Salém, antes do jantar,', 
            'você é convidado para sentar na mesa principal, aonde o Barão  levanta um copo em honra a ' + Personagem.Nome + ', ao Único ao seu falecido pai,',
            'Hugues de Molai, perguntando em seguida se esqueceu de alguém.')
            console.print('1. "Você esqueceu do Rei Jefferson, vida longa ao Rei!"')
            console.print('2. "Você esqueceu do Rei Henrique, vida longa ao Rei!"')
            console.print('3. "Você não se esqueceu de ninguém."')
            console.print('4. Ficar calado.')
            resposta=input()
            if resposta == '1':
                console.print('Barão Jacques de Molai: "Mas é claro, vida longa ao Rei Jefferson!"')
            elif resposta == '2':
                console.print('Barão Jacques de Molai: "Mas é claro, vida longa ao Conde Henrique!"')
                console.print('Após o jantar e enquanto você se preparava para ir embora, o Barão se aproxima e lhe chama para uma conversa em particular.')
                console.print('Barão Jacques de Molai: "Você faz parte da facção que deseja Henrique como Rei?')
                console.print("1. Mas é claro, Jeffeson é um bêbado incompetente que só trás desgraça a Salem.")
                console.print("2. Não, eu simplesmente me confundi na mesa.")
                VidaLongaAoRei = input ()
                if VidaLongaAoRei == '1':
                    Personagem.Traidor = True
                    console.print('Barão Jacques de Molai: "Entendo... Bem, nós temos um plano: A sua Ordém é mais popular com  a plebe do que os',
                    'Cavaleiros da Noite já que patrulham de dia e a maioria das pessoas dormem a noite, faremos caridade em seu nome, isso irá fazer',
                    'com que você seja ainda mais popular do que ' + Rival.Nome + ' dos ' + Rival.Ordem + '.')
                    console.print('Barão Jacques de Molai: Então tudo que você precisa fazer é perder de propósito, a população ficará irada enquanto',
                    'nossos agentes irão espalhar que houve trapaça, uma rebelião ocorrerá e com ela Henrique terá a oportunidade de tomar o trono."')
                    console.print(Personagem.Nome + ': Certo.')
                    Personagem.Popularidade += dado(100)
                elif VidaLongaAoRei == '2':
                    console.print('Barão Jacques de Molai: "Guardas, este homem é um traidor ao Rei, prendam-o"')
                    console.print('Os guardas que estavam vigiando a fortaleza rapidamente lhe cercam e te forçam a se render, ',
                    'e a despeito de seus protestos, te levam até a masmorra. Uma semana depois você é queimado vivo pelo crime de Lesa Majestade', 
                    'e substituído por outro membro para a competição')
                    Personagem.Vivo = False
                    Personagem.Vitória = False
                    fim_do_jogo() 
            elif resposta == '3':
                console.print('Barão Jacques de Molai: "Iniciemos o jantar então"')  
            elif resposta == '4':
                console.print('Após alguns segundos de silêncio o Barão declara o inicio do jantar')

        elif PrimeiraEscolha == "2":
            console.print("O anuncio do torneio e os rumores de que o Rei pessoalmente está torcendo para os Cavaleiros da Noite aumentaram",
            "a sua popularidade dentre aqueles que não gostam dele e você agora não só é reconhecido na cidade, como alguns burguese passam a",
            "oferecer refeições gratuitas para você em algumas tavernas na esperança de atrair mais clientes interessados em estar perto de um dos competidores")
            console.print("Você:")
            console.print('1. Festejar longe dos camponeses, eles fedem.')
            console.print('2. Se une aos plebeus para festejar')
            OutraEscolha = input()
            if OutraEscolha == '1':
                console.print('Você se diverte bastante com seus companheiros e passam boa parte do tempo se lembrando de antigas batalhas e problemas da cidade.')
                Personagem.Popularidade += dado(10)
            elif OutraEscolha == '2':
                console.print('Você decide festejar dentre os mais-humildes e conta diversas histórias a eles, que se impressionam bastante e um bardo',
                'até mesmo decide improvisar em seu alaúde um pequeno Hino à ' + Personagem.Nome + '.')
                Personagem.Popularidade += 25
        elif PrimeiraEscolha == '3':
            console.print('Você decide treinar com os cavalos para o torneio em um planalto próximo a cidade.')
            Personagem.Bônus += 50
    #Corrida
    console.print('')
    console.print('Finalmente chega o dia da Grande Corrida, o hipódromo está lotado com dezenas de milhares de pessoas.')
    if Personagem.Popularidade >= 50:
        console.print('A maioria delas parece estar gritando ' + Personagem.Nome + ', o que ajuda a levantar seu ânimo.')
    else:
        console.print('A maioria delas parece estar gritando ' + Rival.Nome + ', o que parece enche-lo de arrogância.') 

    console.print('Ambos montam em suas carruagens e ficam um do lado do outro: ' + Personagem.Nome + ' dos ' + Personagem.Ordem + ' e ' +Rival.Nome + ' dos ' + Rival.Ordem + '.')
    console.print('O chifre é soado e a corrida começa')
    console.print('')
    corrida()

    RebeliãoChance = dado(100)
    if Personagem.Vitória == True:
        console.print('Você vence a corrida deixando seu oponente para trás!')
        if Personagem.Popularidade >= RebeliãoChance:
            console.print('Graças a você o reino está a salvo!')
            fim_do_jogo()
        elif Personagem.Popularidade < RebeliãoChance:
            console.print('A torcida não aceita o resultado e rumores de trapaça se espalham, uma rebelião começa!')
            rebelião()    

    elif Personagem.Vitória == False:
        console.print('Você perde a corrida, seu oponente o deixa para trás comendo poeira')
        if Personagem.Popularidade > RebeliãoChance:
            console.print('A torcida não aceita o resultado e rumores de trapaça por seu adversário se espalham como fogo, uma rebelião começa!')
            rebelião()
        elif Personagem.Popularidade <= RebeliãoChance:
            console.print('Apesar da humilhação sofrida por sua ordem, o objetivo da corrida é cumprido e a população comemora junto com seu oponente a vitória,', 
            'acalmando   de rebelião.')
            fim_do_jogo()

#Verifica erros e inicia o jogo.
def start() :
    try: 
        main()
    except Exception as erro:
        print('')
        print('Erro:')
        print (erro)
        print('')
        console.print('Oh não, um erro. Você provavelmente digitou algo que não era um número quando dado uma escolha ou um número diferente dos que apareceram.')
        console.print('O jogo será reiniciado após você apertar enter. Caso você acredite que o problema é outro, entre em contato: workingsea@protonmail.com')
        input('')
        start()
        
start()