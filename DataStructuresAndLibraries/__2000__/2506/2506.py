class Solucao:
    @staticmethod
    def resolve():
        while True:
            try:
                tamanho_fila = int(input())
                prox_horario_livre = 7 * 60 
                qnt_pacientes_estado_critico = 0
                
                for _ in range(tamanho_fila):
                    p_hora, p_min, p_tempo = [int(x) for x in input().split()]
                    
                    horario_chegada_paciente = p_hora * 60 + p_min
                    horario_critico_paciente = horario_chegada_paciente + p_tempo
                    
                    # Define o horário real de início de atendimento (múltiplo de 30)
                    horario_inicip_atendimento = max(horario_chegada_paciente, prox_horario_livre)
                    
                    if horario_inicip_atendimento % 30 != 0:
                        horario_inicip_atendimento += 30 - (horario_inicip_atendimento % 30)
                    
                    if horario_inicip_atendimento > horario_critico_paciente:
                        qnt_pacientes_estado_critico += 1
                        
                    prox_horario_livre = horario_inicip_atendimento + 30
                    
                print(qnt_pacientes_estado_critico)
                
            except EOFError: 
                break

Solucao.resolve()