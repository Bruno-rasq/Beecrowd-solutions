class Polynomial_Derivative:
    @staticmethod
    def derivate_function(n_polynomials: int, func: str) -> None:
        derivative = []
        for term in func.split():
            if term == "+": derivative.append("+")
            else:
                coefficient, exponent = term.split('x')
                new_coeff = int(coefficient) * int(exponent)
                new_expoe = int(exponent) - 1
                
                new_term = str(new_coeff) + "x"
                if new_expoe > 1:
                    new_term += str(new_expoe)
                
                derivative.append(new_term)
                
        print(" ".join(derivative))
    
    @staticmethod
    def resolve():
        while True:
            try:
                n_polynomials = int(input())
                function = input()
                Polynomial_Derivative.derivate_function(
                    n_polynomials, function
                )
            except EOFError: break

Polynomial_Derivative.resolve()