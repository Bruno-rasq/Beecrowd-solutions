<?php

const LIMIT = 100000;

function BFS($source, $target, $nums)
{
    $visited = array_fill(0, LIMIT + 1, false);

    $queue = [];
    $head = 0;

    $queue[] = [$source, 0];
    $visited[$source] = true;

    while ($head < count($queue)) {

        [$curr, $step] = $queue[$head++];

        if ($curr == $target)
            return $step;

        foreach ($nums as $a) {

            // Soma
            $next = $curr + $a;
            if ($next <= LIMIT && !$visited[$next]) {
                $visited[$next] = true;
                $queue[] = [$next, $step + 1];
            }

            // Subtração
            $next = $curr - $a;
            if ($next >= 1 && !$visited[$next]) {
                $visited[$next] = true;
                $queue[] = [$next, $step + 1];
            }

            // Multiplicação
            $next = $curr * $a;
            if ($next <= LIMIT && !$visited[$next]) {
                $visited[$next] = true;
                $queue[] = [$next, $step + 1];
            }

            // Divisão
            if ($curr % $a == 0) {
                $next = intdiv($curr, $a);

                if (!$visited[$next]) {
                    $visited[$next] = true;
                    $queue[] = [$next, $step + 1];
                }
            }
        }
    }

    return -1;
}

[$X, $Y, $N] = array_map('intval', explode(' ', trim(fgets(STDIN))));
$nums = array_map('intval', explode(' ', trim(fgets(STDIN))));

echo BFS($X, $Y, $nums) . PHP_EOL;