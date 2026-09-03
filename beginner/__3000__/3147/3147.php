<?php 

    list($h, $a, $e, $o, $w, $x) = explode(" ", readline());

    $h = (int) $h;
    $a = (int) $a;
    $e = (int) $e;
    $o = (int) $o;
    $w = (int) $w;
    $x = (int) $x;

    if( ($h + $a + $e + $x) >= ($o + $w)){
        echo "Middle-earth is safe.\n";
    } else {
        echo "Sauron has returned.\n";
    }
?>