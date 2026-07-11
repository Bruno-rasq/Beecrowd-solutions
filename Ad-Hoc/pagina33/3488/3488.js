const input = Number(require("fs").readFileSync("/dev/stdin", "utf8").trim());
const IPOT = (n) => (n > 0 && (n & (n - 1)) == 0);
console.log(IPOT(input) ? "true" : "false")