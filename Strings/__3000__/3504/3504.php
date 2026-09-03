<?php
$word = trim(fgets(STDIN));
$pointer_left = 0;
$pointer_right = strlen($word) - 1;

$isPalindrome = true;
while($pointer_left != $pointer_right){
    if($word[$pointer_left] != $word[$pointer_right]){
        $isPalindrome = false;
        break;
    }
    $pointer_left++;
    $pointer_right--;
}

if($isPalindrome){
    echo "A frase [" . $word . "] eh palindrome\n";
} else {
    echo "A frase [" . $word . "] nao eh palindrome\n";
}