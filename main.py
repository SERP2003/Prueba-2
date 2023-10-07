from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class Ui(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class HoyScreen(Screen):
    pass


class CitaScreen(Screen):
    def regresar_a_main(self):
        screen_manager = self.manager  # Accede al administrador de pantallas desde el propio Screen
        screen_manager.current = 'main_screen'  # Cambia a la pantalla MainScreen
        print("OptionScreen")


    def ir_a_consultacion(self):
        screen_manager = self.manager  # Accede al administrador de pantallas desde el propio Screen
        screen_manager.current = 'paciente_screen'  # Cambia a la pantalla MainScreen
        print("ir a cosultacion")


class PacienteScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file('design.kv')
        print("build")


        return Ui()

    def ir_buscar_paciente(self):
        self.root.current = 'cita_screen'
        print("consulta")

    def ir_añadir_paciente(self):
        self.root.current = 'paciente_screen'
        print("consulta")

    def hoy(self):
        self.root.current = 'hoy_screen'

    def enviar(self):
        print("enviar")







if __name__ == "__main__":
    MainApp().run()