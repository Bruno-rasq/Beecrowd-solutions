<?php 
    list($a, $b) = explode(" ", readline());

    if($b == 0){ exit(0); }

    $quo = intval($a, $b);
    $r = $a - ($b * $quo);

    if($r < 0){
        $r += abs($b);
        $quo -= ($b > 0) ? 1 : -1;
    }

    echo "$quo $r\n";
?>