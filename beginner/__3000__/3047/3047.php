<?php 

    $m = (int) readline();
    $c1 = (int) readline();
    $c2 = (int) readline();
    $c3 = $m - ($c1 + $c2);

    $eldest = $c1;
    if($c2 > $eldest){ $eldest = $c2; }
    if($c3 > $eldest){ $eldest = $c3; }

    echo "$eldest\n";
?>