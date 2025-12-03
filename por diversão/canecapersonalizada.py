class Amor:
    def __init__(self, anos):
        self.anos = anos
        self.historia = []
    
    def adicionar_memoria(self, memoria):
        self.historia.append(memoria)
    
    def futuro(self):
        return f"Com você, esses {self.anos} anos foram apenas o começo de uma linda jornada juntos."

    def __str__(self):
        return (
            f"Nosso Amor Começou há {self.anos} anos\n"
            f"Colecionamos memórias, {', '.join(self.historia)}\n"
            f"{self.futuro()}"
        )

nosso_amor = Amor(5)
nosso_amor.adicionar_memoria("risos")
nosso_amor.adicionar_memoria("abraços")
nosso_amor.adicionar_memoria("noites viradas jogando juntos")
nosso_amor.adicionar_memoria("muitooo sorteve")
nosso_amor.adicionar_memoria("sonhos")
nosso_amor.adicionar_memoria("beijos")
nosso_amor.adicionar_memoria("sorrisos")

print(nosso_amor)

