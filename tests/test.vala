/* This is the application. */
public class Application : Gtk.Application {

	/* Constructor */
	public Application () {
		Object (application_id: "org.example.window");
	}

	/* Override the 'activate' signal of GLib.Application,
	 * which is inherited by Gtk.Application. */
	public override void activate () {

		var window = new Gtk.Window ();
		window.title = "Welcome to GNOME";

		/* Create GTK Label */
		var label = new Gtk.Label ("Hello GNOME!");

		/* Add to Window */
		window.add (label);

		/* Show all window content */
		window.show_all();

		/* Add the window to this application. */
		this.add_window (window);

		/* Show the window. */
		window.show ();
	}
}

/* The main function creates the application and runs it.*/
int main (string[] args) {
	var app = new Application ();
	return app.run (args);
}