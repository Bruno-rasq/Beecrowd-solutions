class robot_move_system:
    # Direções: T(top), R(right), D(down), L(left)
    command_cases = {
        "T": {"0111": "F",  "1011": "RF", "1110": "LF"},
        "R": {"1011": "F",  "1101": "RF", "0111": "LF"},
        "D": {"1101": "F",  "1110": "RF", "1011": "LF"},
        "L": {"1110": "F",  "0111": "RF", "1101": "LF"}
    }

    # Rotação
    turn_right = {"T": "R", "R": "D", "D": "L", "L": "T"}
    turn_left = {"T": "L", "L": "D", "D": "R", "R": "T"}

    # Movimentos relativos à direção
    move_delta = {"T": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

    @staticmethod
    def get_adj_cells_state(pos, matrix):
        """Retorna a string de 4 dígitos representando as células T,R,D,L"""
        r, c = pos
        # Ordem fixa T, R, D, L
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        state = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                state.append(matrix[nr][nc])  # "0" ou "1"
            else:
                state.append("1")  # Fora do mapa = bloqueado
        return "".join(state)  # Ex: "1101"

    @classmethod
    def decide_next_move(cls, pos, sentido, matrix):
        """
        Decide o próximo movimento do robô.
        pos -> (row, col)
        sentido -> direção atual (T,R,D,L)
        matrix -> mapa
        Retorna:
          (nova_pos, novo_sentido, comando)
        ou None se não houver movimento possível.
        """
        # 1. Lê as células adjacentes
        adj_state = cls.get_adj_cells_state(pos, matrix)

        # 2. Verifica se existe comando para essa situação
        cases = cls.command_cases.get(sentido, {})
        comando = cases.get(adj_state, None)
        if not comando:
            return None  # Não há movimento possível

        # 3. Aplica o comando passo a passo
        novo_sentido = sentido
        nova_pos = pos

        for cmd in comando:  # pode ser "F", "RF" ou "LF"
            if cmd == "R":
                novo_sentido = cls.turn_right[novo_sentido]
            elif cmd == "L":
                novo_sentido = cls.turn_left[novo_sentido]
            elif cmd == "F":
                dr, dc = cls.move_delta[novo_sentido]
                nova_pos = (nova_pos[0] + dr, nova_pos[1] + dc)

        return nova_pos, novo_sentido, comando

class Tunnel_Game:
    @staticmethod
    def set_command_line(start_pos, start_dir, matrix):
        command_line = []
        rrow, rcol = start_pos
        rsen = start_dir  # direção inicial

        # Marca posição inicial como visitada
        matrix[rrow][rcol] = "1"

        while True:
            result = robot_move_system.decide_next_move((rrow, rcol), rsen, matrix)
            if result is None:
                break  # não há mais movimento possível

            # Desempacota o resultado
            (new_row, new_col), new_dir, comando = result
            matrix[new_row][new_col] = "1"

            # Atualiza estado do robô
            rrow, rcol, rsen = new_row, new_col, new_dir

            # Adiciona cada ação do comando separadamente (RF -> "R", "F")
            for c in comando:
                command_line.append(c)

        # Finaliza com "E" (end)
        command_line.append("E")
        print(" ".join(command_line))

    @staticmethod
    def resolve():
        while True:
            try:
                line = input().strip()
                if not line:
                    break
                rows, cols = map(int, line.split())
                robot = None
                matrix = []

                for row in range(rows):
                    line = input().split()
                    for col in range(cols):
                        if robot is None and line[col] == "X":
                            robot = (row, col)
                    matrix.append(line)

                # Começa olhando para baixo por padrão
                Tunnel_Game.set_command_line(robot, "D", matrix)

            except EOFError:
                break
            
Tunnel_Game.resolve()