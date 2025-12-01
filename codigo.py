class Tabuleiro:
    def __init__(self):
        self._grade = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],

            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],

            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    def mostrar(self):
        print("****************************************")
        print("        BEM-VINDO AO SUDOKU 9x9         ")
        print("****************************************")

        for i, linha in enumerate(self._grade):
            if i % 3 == 0 and i != 0:
                print("------+-------+------")

            linha_formatada = ""
            for j, valor in enumerate(linha):
                if j % 3 == 0 and j != 0:
                    linha_formatada += "| "
                linha_formatada += f"{valor if valor != 0 else '.'} "
            
            print(linha_formatada)
        print()

    def obter(self, l, c):
        return self._grade[l][c]

    def colocar(self, l, c, v):
        self._grade[l][c] = v

    def completo(self):
        return all(0 not in linha for linha in self._grade)


class RegraSudoku:
    def valido(tabuleiro, l, c, v):
        for i in range(9):
            if tabuleiro.obter(l, i) == v or tabuleiro.obter(i, c) == v:
                return False
        
        bloco_l = (l // 3) * 3
        bloco_c = (c // 3) * 3

        for i in range(3):
            for j in range(3):
                if tabuleiro.obter(bloco_l + i, bloco_c + j) == v:
                    return False

        return True


class JogoSudoku:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.regra = RegraSudoku()

    def iniciar(self):
        print("Bem-vindo ao Sudoku 9x9!")
        self.tabuleiro.mostrar()

        while not self.tabuleiro.completo():
            try:
                l = int(input("Linha (0-8): "))
                c = int(input("Coluna (0-8): "))
                v = int(input("Valor (1-9): "))

                if self.tabuleiro.obter(l, c) != 0:
                    print("Essa posição já está preenchida!")
                    continue

                if self.regra.valido(self.tabuleiro, l, c, v):
                    self.tabuleiro.colocar(l, c, v)
                    self.tabuleiro.mostrar()
                else:
                    print("Jogada inválida!\n")

            except:
                print("Entrada inválida.\n")

        print("Parabéns, você completou o Sudoku!")
        self.tabuleiro.mostrar()


if __name__ == "__main__":
    jogo = JogoSudoku()
    jogo.iniciar()

