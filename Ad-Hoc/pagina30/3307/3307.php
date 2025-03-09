<?php
fscanf(STDIN, "%d", $n);

for ($i = 0; $i < $n; $i++) {
    fscanf(STDIN, "%d", $area);
    $raio = sqrt($area / (4 * 3.14));

    if ($raio < 12) {
        $valor = $area * 0.09;
        printf("vermelho = R$ %.2f\n", $valor);
    } 
    elseif ($raio >= 12 && $raio <= 15) {
        $valor = $area * 0.07;
        printf("azul = R$ %.2f\n", $valor);
    } 
    else {
        $valor = $area * 0.05;
        printf("amarelo = R$ %.2f\n", $valor);
    }
}
?>