<?php

$crypt = [
    ["GQaku", "0"],
    ["ISblv", "1"],
    ["EOYcmw", "2"],
    ["FPZdnx", "3"],
    ["JTeoy", "4"],
    ["DNXfpz", "5"],
    ["AKUgq", "6"],
    ["CMWhr", "7"],
    ["BLVis", "8"],
    ["HRjt", "9"]
];

$lines = explode("\n", trim(file_get_contents("php://stdin")));
$n = intval(array_shift($lines));

for ($i = 0; $i < $n; $i++) {
    $frase = $lines[$i];
    $incrypt = "";

    for ($j = 0; $j < strlen($frase); $j++) {
        $char = $frase[$j];
        if ($char == ' ') continue;

        foreach ($crypt as $c) {
            if (strpos($c[0], $char) !== false) {
                $incrypt .= $c[1];
                break;
            }
        }

        if (strlen($incrypt) >= 12) break;
    }

    echo substr($incrypt, 0, 12) . "\n";
}
?>