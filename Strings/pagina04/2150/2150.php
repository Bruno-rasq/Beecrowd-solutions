<?php
$input = fopen("php://stdin", "r");

while (($alien_vowels = fgets($input)) !== false) {
    $alien_vowels = trim($alien_vowels);

    $frases = fgets($input);
    if ($frases === false) break;

    $frases = trim($frases);
    $contador = 0;

    for ($i = 0; $i < strlen($frases); $i++) {
        if (strpos($alien_vowels, $frases[$i]) !== false) {
            $contador++;
        }
    }

    echo $contador . PHP_EOL;
}

fclose($input);
?>
