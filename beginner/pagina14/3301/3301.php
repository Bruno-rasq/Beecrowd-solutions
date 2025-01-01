<?php 

    list($a, $b, $c) = explode(" ", readline());

    $a = (int) $a;
    $b = (int) $b;
    $c = (int) $c;

    $data = [$a, $b, $c];
    $sobrinhos = ["huguinho", "zezinho", "luisinho"];

    function get_middle_index($list){
        $mmin = min($list);
        $mmax = max($list);

        for($i = 0; $i < 3; $i++){
            if($list[$i] != $mmin && $list[$i] != $mmax){
                return $i;
            }
        }
        return -1;
    }

    $response = $sobrinhos[get_middle_index($data)];

    echo "$response\n";

?>