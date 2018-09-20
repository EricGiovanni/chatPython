import Cliente
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Interfaz(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Chat")
        self.button = Gtk.Button(label="Enviar mensaje")
        self.button.connect("Enviado", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")

if __name__ == "__main__":
    win = Interfaz()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()