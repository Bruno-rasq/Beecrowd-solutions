<?php 

    $tag = false;

    while($line = fgets(STDIN)){

        if(strpos($line, "<body>") !== false){
            $tag= true;
            continue;
        }

        if(strpos($line, "</body>") !== false){
            break;
        }

        if($tag){
            echo "$line\n";
        }
    }

?>