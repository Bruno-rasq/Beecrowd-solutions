<?php

    list($code, $amount) = explode(" ", readline());
    $code = (int) $code;
    $amount = (float) $amount;

    $menu = [4.00, 4.50, 5.00, 2.00, 1.50];
    $total = $menu[$code - 1] * $amount;

    echo "Total: R$ " . number_format($total, 2, '.', '');

?>