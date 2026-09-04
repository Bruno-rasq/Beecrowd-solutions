const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
let idx = 0;

let T = Number(input[idx++]);
let output = [];

while (T--) {
  const grid = Array.from({ length: 105 }, () => Array(105).fill(0));

  const width = Number(input[idx++]);
  const height = Number(input[idx++]);

  const numRobots = Number(input[idx++]);
  let numCmd = Number(input[idx++]);

  const robots = [];

  for (let i = 0; i < numRobots; i++) {
    const x = Number(input[idx++]);
    const y = Number(input[idx++]);
    const sense = input[idx++];

    robots.push(new Robot(x, y, sense));
    grid[x][y] = i + 1; // ID 1-based
  }

  let collided = false;
  let ans = "OK\n";

  while (numCmd--) {
    const id = Number(input[idx++]);
    const cmd = input[idx++];
    const reps = Number(input[idx++]);

    if (collided) continue;

    const robot = robots[id - 1];

    for (let r = 0; r < reps; r++) {
      const cx = robot.x;
      const cy = robot.y;

      // turn left
      if (cmd === 'L') {
        changeSense(robot, -1);
        continue;
      }

      // turn right
      if (cmd === 'R') {
        changeSense(robot, 1);
        continue;
      }

      // move forward
      if (cmd === 'F') {
        moveRobot(robot);

        // wall collision
        if (robot.x <= 0 || robot.x > width || robot.y <= 0 || robot.y > height) {
          collided = true;
          ans = `Robot ${id} crashes into the wall\n`;
          break;
        }

        // robot collision
        if (grid[robot.x][robot.y] !== 0 && grid[robot.x][robot.y] !== id) {
          collided = true;
          ans = `Robot ${id} crashes into robot ${grid[robot.x][robot.y]}\n`;
          break;
        }

        // update grid
        grid[cx][cy] = 0;
        grid[robot.x][robot.y] = id;
      }
    }
  }

  output.push(ans);
}

console.log(output.join(""));