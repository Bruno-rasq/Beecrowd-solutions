<?php 
    $text = readline();

    if(strlen($text) <= 140){
        echo "TWEET\n";
    } else {
        echo "MUTE\n";
    }

?>