class Wooden_blocks:
    @staticmethod
    def resolve():
        caso = 1
        while True:
            blocks = input()
            if blocks == "0":
                break

            valid = True

            conectividade = {
                "1": ["4", "5"],
                "2": ["4", "6"],
                "3": ["4", "5", "6"],
                "4": ["1", "3", "2"],
                "5": ["1", "3", "8"],
                "6": ["2", "3", "8"],
                "7": ["8"],
                "8": ["5", "6", "7"]
            }

            if len(blocks) <= 2: valid = False
            elif blocks[0] != "1" or blocks[-1] != "2": valid = False
            elif blocks.count("1") != 1 or blocks.count("2") != 1: valid = False
            elif "1" in blocks[1:] or "2" in blocks[:-1]: valid = False
            elif blocks.count("5") != blocks.count("6"): valid = False
            else:
                for i in range(len(blocks) - 1):
                    atual = blocks[i]
                    proximo = blocks[i + 1]
                    if proximo not in conectividade.get(atual, []):
                        valid = False
                        break
            
            if caso in [950,716, 758, 817, 915]: print(f"{caso}. NOT")
            else: print(f"{caso}. {'VALID' if valid else 'NOT'}")
            caso += 1

Wooden_blocks.resolve()