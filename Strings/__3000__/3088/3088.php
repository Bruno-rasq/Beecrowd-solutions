<?php 

    function fixText($text){
        $fixed = "";
        for($i = 0; $i < strlen($text); $i++){
            $char = $text[$i];
            if($i < strlen($text) - 1){
                $next = $text[$i + 1];
                if($char == " " && ($next == "," || $next == ".")) continue;
            }
            $fixed .= $char;
        }
        return $fixed;
    }

    while($input = readline()){
        $output = fixText($input);
        echo "$output\n";
    }
?>