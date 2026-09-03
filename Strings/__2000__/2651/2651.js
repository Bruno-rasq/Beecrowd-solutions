const input = require("fs").readFileSync("/dev/stdin", "utf8").toLowerCase()

console.log(input.includes("zelda") ? "Link Bolado" : "Link Tranquilo")