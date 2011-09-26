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
        temp_min = temp_desejada - 2
        temp_max = temp_desejada + 2
        tempo = 0
        stop = False

        while tempo < self.tempo_uso:
            self.temperatura = self.temperatura + 0.5
            tempo = tempo + 1

            if self.temperatura == temp_min or stop == True:
                stop = True
                if self.temperatura == temp_max:
                    self.custo = self.custo + 0.5
                    self.reduz_um_grau()
                    stop = False
                continue

            if self.temperatura == temp_max or stop == False:
                self.reduz_um_grau()

            print "%s C, %s minutos, R$ %.2f" % (self.temperatura, tempo, self.custo)

        return (self.temperatura, self.custo)

if __name__ == "__main__":
    print "Vamos refrigerar o ar, entao..."
    dispositivo = ArCondicionado()
    dispositivo.refrigera(30, 20)
    print "O custo total da operacao foi: %.2f" % dispositivo.custo
