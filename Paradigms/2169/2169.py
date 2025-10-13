from typing import List

SUCESS = "Missao completada com sucesso"
FAIL = "You Are Dead"

# armas e seu dano por munição 
WEAPONS = {
    "HANDGUN":      2,
    "RED9":         3.5,
    "BLACKTAIL":    3.5,
    "MATILDA":      2,
    "HANDCANNON":   60,
    "STRIKER":      12,
    "TMP":          1.2,
    "RIFLE":        12
}

# monstros e quantidade de vida HP
MONSTERS = {
    "GANADOS":          50,
    "COBRAS":           40,
    "ZEALOT":           75,
    "COLMILLOS":        60,
    "GARRADOR":         125,
    "LASPLAGAS":        100,
    "GATLINGMAN":       150,
    "REGENERATOR":      250,
    "ELGIGANTE":        500,
    "DR.SALVADOR":      350
}


def knapsack_problem(itens: List[List[int]], capacity: int) -> int:
    
    dp = [[0] * (capacity + 1) for _ in range(len(itens) + 1)]
    
    for i in range(1, len(itens) + 1):
        curr_item_value, curr_item_weight = itens[i - 1][0], itens[i - 1][1]
        
        for j in range(capacity + 1):
            if j < curr_item_weight: dp[i][j] = dp[i - 1][j]
            else:
                remaining_capacity = j - curr_item_weight
                added_value = dp[i - 1][remaining_capacity] + curr_item_value
                dp[i][j] = max(dp[i - 1][j], added_value)
    return dp
    


while True:
    try:
    
        n_weapons = int(input())
        weapons = []
        for _ in range(n_weapons):
            weapon_name, amount_ammunation = input().split()
            damage = WEAPONS[weapon_name]
            qnt_ammunation = int(amount_ammunation)
            weapons.append([damage * qnt_ammunation, qnt_ammunation])
          
        n_monsters = int(input())  
        total_HP_monsters = 0
        for _ in range(n_monsters):
            monster, qnt = input().split()
            total_HP_monsters += MONSTERS[monster] * int(qnt)
            
        capacity_ammunation = int(input())
        
        
        dp = knapsack_problem(weapons, capacity_ammunation)
        max_damage = dp[n_weapons][capacity_ammunation]
        
        monster_HP_final = total_HP_monsters - max_damage
        
        
        print(SUCESS if monster_HP_final <= 0 else FAIL)
        print()

    except EOFError: break 