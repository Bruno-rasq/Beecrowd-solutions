major_scales = {
    "do":    ["do", "re", "mi", "fa", "sol", "la", "si"],
    "do#":   ["do#", "re#", "fa", "fa#", "sol#", "la#", "do"],
    "re":    ["re", "mi", "fa#", "sol", "la", "si", "do#"],
    "re#":   ["re#", "fa", "sol", "sol#", "la#", "do", "re"],
    "mi":    ["mi", "fa#", "sol#", "la", "si", "do#", "re#"],
    "fa":    ["fa", "sol", "la", "la#", "do", "re", "mi"],
    "fa#":   ["fa#", "sol#", "la#", "si", "do#", "re#", "fa"],
    "sol":   ["sol", "la", "si", "do", "re", "mi", "fa#"],
    "sol#":  ["sol#", "la#", "do", "do#", "re#", "fa", "sol"],
    "la":    ["la", "si", "do#", "re", "mi", "fa#", "sol#"],
    "la#":   ["la#", "do", "re", "re#", "fa", "sol", "la"],
    "si":    ["si", "do#", "re#", "mi", "fa#", "sol#", "la#"]
}

class Musical_Scale:
    scale = [
        "do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"
    ]
    
    @staticmethod
    def solve(keys):
        # converter teclas para notas (ajuste: % 12 - 1 pq tecla 1 = "do")
        notes = [Musical_Scale.scale[(key-1) % 12] for key in keys]
        notes_set = set(notes)
        
        for scale_name, scale_notes in major_scales.items():
            if notes_set.issubset(set(scale_notes)):
                print(scale_name)
                return
        
        print("desafinado")


n_keys = int(input())
keys = [int(input()) for _ in range(n_keys)]
Musical_Scale.solve(keys)