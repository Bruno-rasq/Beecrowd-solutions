<?php

$nokia_keyboard = [
    "a" => "2", "b" => "2", "c" => "2",
    "d" => "3", "e" => "3", "f" => "3",
    "g" => "4", "h" => "4", "i" => "4",
    "j" => "5", "k" => "5", "l" => "5",
    "m" => "6", "n" => "6", "o" => "6",
    "p" => "7", "q" => "7", "r" => "7", "s" => "7",
    "t" => "8", "u" => "8", "v" => "8",
    "w" => "9", "x" => "9", "y" => "9", "z" => "9"
];

while (($input = readline()) !== false) {
    $output = "";
    $len = strlen($input);

    for ($i = 0; $i < $len; $i++) {
        $char = $input[$i];

        if (ctype_alpha($char)) {
            $output .= $nokia_keyboard[strtolower($char)];
        } elseif (ctype_digit($char) || $char === "*" || $char === "#") {
            $output .= $char;
        }
        // outros símbolos são ignorados
    }

    echo $output . "\n";
}