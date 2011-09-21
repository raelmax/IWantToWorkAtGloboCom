# -*- coding: utf-8 -*-


class ArCondicionado:
    def __init__(self, tempo_uso=360):
        self.custo = 0.5
        self.tempo_uso = tempo_uso

    def reduz_um_grau(self):
        self.temperatura = self.temperatura - 1
        self.custo = self.custo + 0.1

    def refrigera(self, temp_atual, temp_desejada):
        self.temperatura = temp_atual
        tempo = 0
        while tempo <= self.tempo_uso:
            if self.temperatura > temp_desejada:
                self.reduz_um_grau()
            self.temperatura = self.temperatura + 0.5
            tempo = tempo + 1

        return (self.temperatura, self.custo)

if __name__ == "__main__":
    print "Vamos refrigerar o ar, entao..."
    dispositivo = ArCondicionado()
    dispositivo.refrigera(30, 20)
    print "O custo total da operação foi: %.2f" % dispositivo.custo
