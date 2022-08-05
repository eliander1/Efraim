import Program.Aniversariantes.aniversariantes_do_dia as aniv
import Program.passageiros_em_transito.passageiros_em_transito as pet
from time import sleep
from Program.efraimbot.efraimbot.bot import Bot


def Atualizar ():
    aniv.Encontrar_Aniversariante()
    sleep(1.5)
    pet.Check_in_Aberto()
    sleep(1.5)
    Bot.main()


