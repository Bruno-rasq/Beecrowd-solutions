#include <bits/stdc++.h>
using namespace std;

struct Robot { int x, y; char sense; };

void changeSense(Robot& robot, int shift) {
    static const string senses = "NESW";
    size_t idx = senses.find(robot.sense);
    robot.sense = senses[(idx + shift + 4) % 4];
}

void moveRobot(Robot& robot) {
    static unordered_map<char, array<int,2>> DeltasCMD = {
        {'W', {-1, 0}}, {'N', { 0, 1}}, {'E', { 1, 0}}, {'S', { 0,-1}}};
    robot.x += DeltasCMD[robot.sense][0];
    robot.y += DeltasCMD[robot.sense][1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;

    while(T--) {
        int grid[105][105] = {0};
        int width, height;
        int numRobots, numCmd;

        cin >> width >> height;
        cin >> numRobots >> numCmd;
        vector<Robot> robots(numRobots);
        for(int i = 0; i < numRobots; i++) {
            cin >> robots[i].x >> robots[i].y >> robots[i].sense;
            grid[robots[i].x][robots[i].y] = i + 1; // ID 1-based
        }

        bool collided = false;
        string ans = "OK\n";
        while(numCmd--) {
            int id, reps;
            char cmd;
            cin >> id >> cmd >> reps;
            if(collided) continue;
            Robot &robot = robots[id - 1];
            while(reps--) {
                int cx = robot.x;
                int cy = robot.y;
                // gira
                if(cmd == 'L') {
                    changeSense(robot, -1);
                    continue;
                }
                if(cmd == 'R') {
                    changeSense(robot, 1);
                    continue;
                }
                // move F
                if(cmd == 'F') {
                    moveRobot(robot);
                    // parede
                    if(robot.x <= 0 || robot.x > width || robot.y <= 0 || robot.y > height) {
                        collided = true;
                        ans = "Robot " + to_string(id) + " crashes into the wall\n";
                        break;
                    }
                    // colisão com outro robô
                    if(grid[robot.x][robot.y] != 0 && grid[robot.x][robot.y] != id) {
                        collided = true;
                        ans = "Robot " + to_string(id) + " crashes into robot " + to_string(grid[robot.x][robot.y]) + "\n";
                        break;
                    }
                    // atualiza grid
                    grid[cx][cy] = 0;
                    grid[robot.x][robot.y] = id;
                }
            }
        }
        cout << ans;
    }
}