<?php

    $n = (int) trim(fgets(STDIN));
    
    for ($i = 0; $i < $n; $i++) {
        $word = trim(fgets(STDIN));
        $ans = "";
    
        // 97 - 122 (a - z)
        foreach (str_split($word) as $char) {
            $ascii = ord($char);
            if ($ascii >= 97 && $ascii <= 122) {
                $ans .= $char;
            }
        }
    
        echo strrev($ans) . "\n";
    }