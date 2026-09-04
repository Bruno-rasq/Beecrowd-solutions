<?php

$i1 = (int) fgets(STDIN);
$i2 = (int) fgets(STDIN);

if((($i1 >= 14 && $i2 >= 14) || ($i1 >= 18 || $i2 >= 18)) && $i1 >= 6 && $i2 >= 6){
    echo "YES\n";
} else {
    echo "NO\n";
}