import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        while (in.hasNextLine()) {
            String[] data = in.nextLine().split(" ");
            String[] conto = in.nextLine().split(" ");

            int max_linha = Integer.parseInt(data[1]);
            int max_char = Integer.parseInt(data[2]);
            int qnt_paginas = 0, ind = 0;

            while (ind < conto.length) {
                int linhas = 0;

                while (linhas < max_linha && ind < conto.length) {
                    int linha_len = 0;

                    while (ind < conto.length) {
                        String palavra = conto[ind];

                        if (linha_len == 0) {
                            if (palavra.length() <= max_char) {
                                linha_len = palavra.length();
                                ind++;
                            } else {
                                break;
                            }
                        } else if (linha_len + 1 + palavra.length() <= max_char) {
                            linha_len += 1 + palavra.length();
                            ind++;
                        } else {
                            break;
                        }
                    }

                    linhas++;
                }

                qnt_paginas++;
            }

            System.out.println(qnt_paginas);
        }

        in.close();
    }
}
