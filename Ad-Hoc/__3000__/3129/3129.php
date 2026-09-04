<?php

$stickers = [];
$repeated_stickers = 0;

$n = (int) fgets(STDIN);
for($i = 0; $i < $n; $i++){
    $sticker = (int) fgets(STDIN);
    $len = count($stickers);
    $stickers[$sticker] = true;
    if(count($stickers) == $len) $repeated_stickers++;
}

echo count($stickers) . "\n";
echo "$repeated_stickers\n";