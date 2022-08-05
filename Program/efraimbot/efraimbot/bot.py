

from botcity.core import DesktopBot
from time import sleep

class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.execute(r'C:\Users\eliander\Desktop\Efraim_painel.pbix')

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

        #Salvar alteracoes
        if not self.find( "salvar_alteracoes", matching=0.97, waiting_time=10000):
            self.not_found("salvar_alteracoes")
        self.click(1)

        sleep(4)

        #selecionar workspace
        if not self.find( "selecionar_workspace", matching=0.97, waiting_time=10000):
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





