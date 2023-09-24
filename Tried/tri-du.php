<?php

$input = fgets(STDIN);
$arry = explode(" ", $input);

$A = intval($arry[0]);
$B = intval($arry[1]);

if($A > $B){
    echo "$A\n";
} else if($A < $B){
    echo "$b\n";
} else if ($A == $B){
    echo "$A\n";
};

?>