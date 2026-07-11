const input: number = Number(require("fs").readFileSync("/dev/stdin", "utf8").trim());
const char: string = String.fromCharCode(96 + input);
console.log(char);