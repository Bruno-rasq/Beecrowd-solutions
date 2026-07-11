const input = Number(require("fs").readFileSync("/dev/stdin", "utf8").trim());
const char = String.fromCharCode(96 + input);
console.log(char);