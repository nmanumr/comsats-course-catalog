import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyApplication(Gtk.Application):

    def do_activate(self):
        # create a Gtk Window belonging to the application itself
        window = Gtk.Window(
            application=self,
            title="Welcome to GNOME",
            default_height=100,
            default_width=200
        )
        # create a label
        label = Gtk.Label(label="Hello GNOME!")
        # add the label to the window
        window.add(label)
        # show the window
        window.show_all()

# create and run the application, exit with the value returned by
# running the program
app = MyApplication()
app.run()