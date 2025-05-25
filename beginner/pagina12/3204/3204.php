<?php

$posebilidades = [
    0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 
    1588356, 8676360, 47977776, 266378112, 1488801600
];

$n = (int) readline();
for($i = 0; $i < $n; $i++){
    $curr = (int) readline() - 1;
    echo $posebilidades[$curr] . "\n";
}