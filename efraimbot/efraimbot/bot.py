import os
import sys
from botcity.core import DesktopBot
from time import sleep
import logging
logger = logging.getLogger(__name__)

class Bot(DesktopBot):

    def setup_images(self):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # Remember to change here from `botPython` to your bot ID.
            res_path = os.path.join(sys._MEIPASS, "efraimbot", "resources")
            # Add all images needed to the image map
            self.add_image("atualizar", os.path.join(res_path, "atualizar.png"))
            self.add_image("entendi", os.path.join(res_path, "entendi.png"))
            self.add_image("play_painel", os.path.join(res_path, "play_painel.png"))
            self.add_image("publicar", os.path.join(res_path, "publicar.png"))
            self.add_image("salvar_alteracoes", os.path.join(res_path, "salvar_alteracoes.png"))
            self.add_image("selecionar_workspace", os.path.join(res_path, "selecionar_workspace.png"))
            self.add_image("substituir_painel", os.path.join(res_path, "substituir_painel.png"))


    def action(self, execution=None):
        logger.info("Iniciando o Bot...")
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        self.setup_images()

        # Opens the BotCity website.
        self.execute(r'Efraim_painel.pbix')

        sleep(15)

        #Click Atualizar
        if not self.find( "atualizar", matching=0.97, waiting_time=10000):
            self.not_found("atualizar")
        sleep(1)
        self.click(1)

        sleep(10)

        #Click Publicar
        if not self.find( "publicar", matching=0.97, waiting_time=10000):
            self.not_found("publicar")
        self.click(1)

        sleep(10)

        # selecionar workspace
        if not self.find("selecionar_workspace", matching=0.97, waiting_time=10000):
            self.not_found("selecionar_workspace")
        self.click(1)

        sleep(4)

        #substituir painel
        if not self.find( "substituir_painel", matching=0.97, waiting_time=10000):
            self.not_found("substituir_painel")
        self.click(1)

        sleep(5)
        #entendi
        if not self.find( "entendi", matching=0.97, waiting_time=10000):
            self.not_found("entendi")
        self.click(1)

        sleep(5)

        self.alt_f4()

        sleep(2)

        self.execute(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

        #play painel
        sleep(5)
        if not self.find( "play_painel", matching=0.97, waiting_time=10000):
            self.not_found("play_painel")
        self.click(1)

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()





