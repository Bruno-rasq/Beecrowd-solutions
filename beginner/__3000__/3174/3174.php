<?php 

    $n = (int) readline();
    $gifts = 0;
    $restB = 0;
    $restA = 0;
    $restM = 0;
    $restD = 0;

    for($i = 0; $i < $n; $i++){
        list($name, $group, $h) = explode(" ", readline());
        $hours = (int) $h;

        if($group == 'bonecos'){
            $gifts += intdiv($hours + $restB, 8);
            $restB = ($hours + $restB) % 8;
        }
        if($group == 'arquitetos'){
            $gifts += intdiv($hours + $restA, 4);
            $restA = ($hours + $restA) % 4;
        }
        if($group == 'musicos'){
            $gifts += intdiv($hours + $restM, 6);
            $restM = ($hours + $restM) % 6;
        }
        if($group == 'desenhistas'){
            $gifts += intdiv($hours + $restD, 12);
            $restD = ($hours + $restD) % 12;
        }
    }
        
    echo "$gifts\n";
?>