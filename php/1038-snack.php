<?php

$code = trim(fgets( STDIN ));
$qnt = trim(fgets( STDIN ));

$menu = [4.00, 4.50, 5.00, 2.00, 1.50];
$total = ($menu[$code-1]) * $qnt;

echo "Total: R$ " . number_format($total, 2, '.', '');

?>

//ta dando erro no site... pq? não sei...