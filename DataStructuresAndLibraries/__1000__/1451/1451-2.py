import sys
from collections import deque

def process_text():
    # sys.stdin.read().splitlines() lê todas as linhas de uma vez de forma muito rápida
    lines = sys.stdin.read().splitlines()
    
    for line in lines:
        if not line:
            continue
            
        result_deque = deque()
        current_segment = []
        # True significa que estamos inserindo no final (padrão), False no início
        insert_at_end = True 
        
        for char in line:
            if char == '[':
                # Antes de mudar de posição, descarrega o que já foi digitado
                if current_segment:
                    text = "".join(current_segment)
                    if insert_at_end:
                        result_deque.append(text)
                    else:
                        result_deque.appendleft(text)
                    current_segment = [] # Limpa o segmento
                insert_at_end = False # Próximos caracteres vão para o início
                
            elif char == ']':
                # Antes de mudar de posição, descarrega o que já foi digitado
                if current_segment:
                    text = "".join(current_segment)
                    if insert_at_end:
                        result_deque.append(text)
                    else:
                        result_deque.appendleft(text)
                    current_segment = []
                insert_at_end = True # Próximos caracteres vão para o final
                
            else:
                current_segment.append(char)
        
        # Descarrega o último segmento que sobrou no final do loop
        if current_segment:
            text = "".join(current_segment)
            if insert_at_end:
                result_deque.append(text)
            else:
                result_deque.appendleft(text)
                
        # Junta todas as partes do deque em uma única string eficiente
        print("".join(result_deque))

if __name__ == '__main__':
    process_text()
    