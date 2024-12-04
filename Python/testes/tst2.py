import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class ExemploGTK4(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(title="Exemplo Completo GTK 4", application=app)

        # Layout principal (box vertical)
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_child(layout)

        # Adicionando um Label
        label = Gtk.Label(label="Este é um exemplo de GTK 4")
        layout.append(label)

        # Adicionando um Button
        button = Gtk.Button(label="Clique-me")
        button.connect("clicked", self.on_button_click)
        layout.append(button)

        # Adicionando um Entry (campo de texto)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Digite algo aqui...")
        layout.append(entry)

        # Adicionando um ToggleButton
        toggle_button = Gtk.ToggleButton(label="Ativar / Desativar")
        toggle_button.connect("toggled", self.on_toggle_button)
        layout.append(toggle_button)

        # Adicionando uma Caixa de Seleção (CheckButton)
        check_button = Gtk.CheckButton(label="Aceito os termos")
        layout.append(check_button)

        # Adicionando uma Caixa de Combinação (ComboBox)
        combo_box = Gtk.ComboBoxText()
        combo_box.append_text("Opção 1")
        combo_box.append_text("Opção 2")
        combo_box.append_text("Opção 3")
        layout.append(combo_box)

        # Adicionando um SpinButton (botão de incremento)
        adjustment = Gtk.Adjustment.new(0, 0, 10, 1, 1, 0)
        spin_button = Gtk.SpinButton(adjustment=adjustment)
        layout.append(spin_button)

        # Adicionando um Slider (Scale)
        slider = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1)
        layout.append(slider)

        # Simulando Botões de Rádio com ToggleButton
        radio_button_1 = Gtk.ToggleButton(label="Opção A")
        radio_button_1.connect("toggled", self.on_radio_button_toggled, radio_button_1)
        radio_button_2 = Gtk.ToggleButton(label="Opção B")
        radio_button_2.connect("toggled", self.on_radio_button_toggled, radio_button_2)

        layout.append(radio_button_1)
        layout.append(radio_button_2)

        # Adicionando uma Barra de Progresso
        progress_bar = Gtk.ProgressBar()
        progress_bar.set_fraction(0.5)
        layout.append(progress_bar)

        # Adicionando um Image (Imagem)
        try:
            image = Gtk.Image.new_from_file("path_to_image.png")  # Substitua pelo caminho de uma imagem válida
            layout.append(image)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")

        # Adicionando uma Caixa de Texto (TextView)
        text_view = Gtk.TextView()
        text_buffer = text_view.get_buffer()
        text_buffer.set_text("Texto de exemplo no TextView")
        layout.append(text_view)

    def on_button_click(self, widget):
        print("Botão clicado!")

    def on_toggle_button(self, widget):
        if widget.get_active():
            print("Toggle Button Ativado")
        else:
            print("Toggle Button Desativado")

    def on_radio_button_toggled(self, widget, button):
        if widget.get_active():
            print(f"{button.get_label()} ativado!")
        else:
            print(f"{button.get_label()} desativado!")

class MinhaAplicacao(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.exemplo.GTK4App")

    def do_activate(self):
        janela = ExemploGTK4(self)
        janela.show()

# Cria e executa a aplicação
app = MinhaAplicacao()
app.run()

