<?php 

    while($line = readline()){
        $decrypt = "";

        for($j = 0; $j < strlen($line); $j++){
            if ($line[$j] == "@"){$decrypt .= 'a';}
            else if ($line[$j] == "&"){$decrypt .= 'e';}
            else if ($line[$j] == "!"){$decrypt .= 'i';}
            else if ($line[$j] == "*"){$decrypt .= 'o';}
            else if ($line[$j] == "#"){$decrypt .= 'u';}
            else {$decrypt .= $line[$j];}
        }

        echo "$decrypt\n";
    }
?>