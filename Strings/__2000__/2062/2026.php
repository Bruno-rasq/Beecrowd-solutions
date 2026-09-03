<?php 

    $n = (int) readline();
    $words = explode(' ', readline());
    $response = '';

    for($i = 0; $i < $n; $i++){
        $word = $words[$i];

        if(!empty($response)){ $response .= ' '; }

        if(strlen($word) == 3){
            if(substr($word, 0, 2) == "OB"){
                $response .= 'OBI';
                continue;
            }
            if(substr($word, 0, 2) == "UR"){
                $response .= 'URI';
                continue;
            }
        }
        $response .= $word;
    }

    echo "$response\n";
?>