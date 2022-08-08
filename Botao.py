import aniversariantes_do_dia as aniv
import passageiros_em_transito as pet
from time import sleep
# from efraimbot.efraimbot.bot import Bot


def Atualizar ():
    aniv.Encontrar_Aniversariante()
    sleep(1.5)
    pet.Check_in_Aberto()



