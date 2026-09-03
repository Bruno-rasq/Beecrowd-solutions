<?php 

$mod = 1000000007;

while($abc = readline()){

    $resultado = 0;
    for($i = 0; $i < strlen($abc); $i++){
        $code = ord($abc[$i]) - ord("A");
        $resultado = ($resultado * 26 + $code) % $mod;
    }

    echo "$resultado\n";
}