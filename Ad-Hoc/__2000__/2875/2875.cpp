#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <string>

using namespace std;

// Tipos personalizados
typedef tuple<int, int> COORD;
typedef vector<COORD> COORDS;
typedef vector<vector<string>> GRID;
typedef map<string, map<string, string>> COMMAND_CASES;
typedef tuple<int, int, string, string> NEXT_MOVE;

const NEXT_MOVE COMMAND_ERROR = {-1, -1, "", ""};

// Direções: T(top), R(right), D(down), L(left)
static const COMMAND_CASES command_cases = {
    {"T", {{"0111", "F"}, {"1011", "RF"}, {"1110", "LF"}}},
    {"R", {{"1011", "F"}, {"1101", "RF"}, {"0111", "LF"}}},
    {"D", {{"1101", "F"}, {"1110", "RF"}, {"1011", "LF"}}},
    {"L", {{"1110", "F"}, {"0111", "RF"}, {"1101", "LF"}}}
};

// Rotação
static const map<string, string> turn_right = {{"T", "R"}, {"R", "D"}, {"D", "L"}, {"L", "T"}};
static const map<string, string> turn_left  = {{"T", "L"}, {"L", "D"}, {"D", "R"}, {"R", "T"}};

// Movimentos
static const map<string, COORD> move_delta = {
    {"T", {-1, 0}}, {"R", {0, 1}}, {"D", {1, 0}}, {"L", {0, -1}}
};

// Função para obter o estado dos vizinhos
string get_adj_state(const GRID& grid, int x, int y) {
    static const COORDS delta = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    string adj_cells = "";

    for (const auto& [dx, dy] : delta) {
        int nx = x + dx;
        int ny = y + dy;

        // verifica se as posicoes nx e ny estão dentro dos limites do grid.
        bool in_bound = nx >= 0 && nx < (int)grid.size() && ny >= 0 && ny < (int)grid[0].size();

        adj_cells += (in_bound ? grid[nx][ny] : "1");
    }
    return adj_cells;
}

// Decide o próximo movimento
NEXT_MOVE decide_next_move(int x, int y, string current_direction, const GRID& grid) {
    string adj_state = get_adj_state(grid, x, y);

    auto dir_it = command_cases.find(current_direction);
    if (dir_it == command_cases.end()) return COMMAND_ERROR;

    const auto& cases = dir_it->second;
    auto case_it = cases.find(adj_state);
    if (case_it == cases.end()) return COMMAND_ERROR;

    string commands = case_it->second;
    string new_direction = current_direction;
    int npos_x = x, npos_y = y;

    for (char cmd : commands) {
        if (cmd == 'R') new_direction = turn_right.at(new_direction);
        else if (cmd == 'L') new_direction = turn_left.at(new_direction);
        else if (cmd == 'F') {
            COORD delta = move_delta.at(new_direction);
            npos_x += get<0>(delta);
            npos_y += get<1>(delta);
        }
    }

    return {npos_x, npos_y, new_direction, commands};
}


string set_command_line(int x, int y, string start_direction, GRID& grid) {
    string command_line = "";
    string current_direction = start_direction;

    grid[x][y] = "1";

    while (true) {
        NEXT_MOVE move = decide_next_move(x, y, current_direction, grid);
        if (move == COMMAND_ERROR) break;

        tie(x, y, current_direction, ignore) = move;
        string commands = get<3>(move);
        grid[x][y] = "1";

        for (char cmd : commands) {
            command_line += cmd;
            command_line += " ";
        }
    }

    return command_line + "E";
}

// Função principal
int main() {
    int rows, cols;

    while (cin >> rows >> cols) {
        GRID grid(rows, vector<string>(cols));
        int pos_x = 0, pos_y = 0;
        string curr_cell;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cin >> curr_cell;
                grid[i][j] = curr_cell;
                if (curr_cell == "X") {
                    pos_x = i;
                    pos_y = j;
                }
            }
        }

        cout << set_command_line(pos_x, pos_y, "D", grid) << endl;
    }

    return 0;
}