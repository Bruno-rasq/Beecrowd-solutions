<?php 
    function main(){

        $n = (int) readline();
        $moedas = [];

        for($i = 0; $i < $n; $i++){
            $moeda = (int) readline();
            $moedas[$i] = $moeda;
        }

        $salto = (int) readline();
        $resultado = contagem($moedas, $salto);

        if(eh_primo($resultado)){
            echo "You're a coastal aircraft. Robbie, a large silver aircraft.\n";
        } else {
            echo "Bad boy! I'll hit you.\n";
        }
    }

    function contagem($moedas, $salto){
        $index = count($moedas) - 1;
        $soma = 0;
        while($index >= 0){
            $soma += $moedas[$index];
            $index -= $salto;
        }
        return $soma;
    }

    function eh_primo($n){
        if($n <= 1) return false;
        for($i = 2; $i <= sqrt($n); $i++){
            if($n % $i === 0) return false;
        }
        return true;
    }

    main();
?>