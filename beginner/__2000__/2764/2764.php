<?php 

    while($data = readline()){

        list($dd, $mm, $yy) = explode("/", $data);
        echo  "$mm/$dd/$yy\n";
        echo  "$yy/$mm/$dd\n";
        echo  "$dd-$mm-$yy\n";
    }

?>