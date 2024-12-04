import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Aplicativo(Gtk.Window):
    def __init__(self):
        super().__init__(title="Selecionar Arquivo")
        
        # Criação do layout principal
        self.set_size_request(400, 100)
        
        # Caixa de texto para mostrar o caminho do arquivo (somente leitura)
        self.caminho_label = Gtk.Label()
        self.caminho_label.set_text("Selecione um arquivo...")
        
        # Botão para abrir o diálogo de seleção de arquivo
        self.botao_abrir = Gtk.Button(label="Abrir Arquivo")
        self.botao_abrir.connect("clicked", self.abrir_dialogo)
        
        # Layout vertical
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.pack_start(self.caminho_label, True, True, 0)
        vbox.pack_start(self.botao_abrir, False, False, 0)
        
        self.add(vbox)
        
    def abrir_dialogo(self, widget):
        # Cria o diálogo de seleção de arquivo
        dialog = Gtk.FileChooserDialog(
            title="Escolha um arquivo",
            parent=self,
            action=Gtk.FileChooserAction.OPEN
        )
        
        # Adiciona botões ao diálogo
        dialog.add_buttons(
            "Cancelar", Gtk.ResponseType.CANCEL,
            "Abrir", Gtk.ResponseType.OK
        )
        
        # Filtro para arquivos Python
        filtro_py = Gtk.FileFilter()
        filtro_py.set_name("Arquivos Python (*.py)")
        filtro_py.add_pattern("*.py")
        dialog.add_filter(filtro_py)
        
        # Filtro geral
        filtro_geral = Gtk.FileFilter()
        filtro_geral.set_name("Todos os arquivos")
        filtro_geral.add_pattern("*.*")
        dialog.add_filter(filtro_geral)
        
        # Exibe o diálogo e pega a resposta
        response = dialog.run()
        
        if response == Gtk.ResponseType.OK:
            arquivo = dialog.get_filename()
            self.caminho_label.set_text(arquivo)  # Exibe o caminho na label
        dialog.destroy()

# Cria a janela principal
window = Aplicativo()
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()  # Necessário para manter a interface aberta

