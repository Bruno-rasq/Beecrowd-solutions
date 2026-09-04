class Dracarys:
    @staticmethod
    def area_of_the_larger_possible_square(wd, hd, wv, hv) -> None:
        best = 0
        # Testa todas as rotações possíveis dos dois retângulos
        for Wd, Hd in [(wd, hd), (hd, wd)]:
            for Wv, Hv in [(wv, hv), (hv, wv)]:
                inside1 = min(Wd, Hd)
                inside2 = min(Wv, Hv)
                span_h = min(Wd + Wv, min(Hd, Hv))  # lado a lado
                span_v = min(Hd + Hv, min(Wd, Wv))  # empilhado
                s = max(inside1, inside2, span_h, span_v)
                best = max(best, s)
        print(best * best)

wd, hd, wv, hv = [int(x) for x in input().split()]
Dracarys.area_of_the_larger_possible_square(wd, hd, wv, hv)
