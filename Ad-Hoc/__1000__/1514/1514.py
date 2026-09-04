class Contest:
    @staticmethod
    def amount_of_caracteristics(amount_players, amount_questions):
        """
        Regras:
        1) Ninguém resolveu todos os problemas.
        2) Todo problema foi resolvido por pelo menos uma pessoa.
        3) Não existe problema resolvido por todos.
        4) Cada jogador resolveu pelo menos um problema.
        """
        # Inicializa dicionário: problema -> lista de quem resolveu
        questions = {x: [] for x in range(amount_questions)}
        
        perfect_score = False         # Alguém acertou todas as questões?
        perfect_response_rate = True  # Todos os problemas foram resolvidos por pelo menos 1?
        only_one_accept = True        # Todos acertaram pelo menos 1?
        problem_solved_by_everyone = False  # Algum problema foi resolvido por todos?

        for player_idx in range(amount_players):
            player_results = input().split()
            
            # Alguém acertou todas? (só '1', sem '0')
            if not "0" in player_results: perfect_score = True
                
            # Alguém errou tudo? (nenhum '1')
            if not "1" in player_results: only_one_accept = False
            
            # Registra quem resolveu cada problema
            for idx, result in enumerate(player_results):
                if result == "1": questions[idx].append(player_idx)
        
        # Verifica os problemas após processar todos os jogadores
        for idx, solvers in questions.items():
            if len(solvers) == 0: perfect_response_rate = False 
            if len(solvers) == amount_players: problem_solved_by_everyone = True
        
        
        amount_caracteristics = 0      
        if not perfect_score:              amount_caracteristics += 1
        if perfect_response_rate:          amount_caracteristics += 1
        if only_one_accept:                amount_caracteristics += 1
        if not problem_solved_by_everyone: amount_caracteristics += 1
        
        print(amount_caracteristics)
        
    
    @staticmethod
    def resolve():
        while True:
            amount_players, amount_questions = [int(x) for x in input().split()]
            if amount_players == amount_questions == 0: break 
            
            Contest.amount_of_caracteristics(amount_players, amount_questions)
        
Contest.resolve()