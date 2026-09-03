<?php
$ans = 1;
for($idx = 0; $idx < 3; $idx++){
    $ans *= (int) fgets(STDIN);
}
echo $ans . "\n";