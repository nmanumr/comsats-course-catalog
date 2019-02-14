# Hello Gnome

Gnome share similar API across all the supported languages. Here we are going to implement Hello World Gnome application.

## Prerequistes
In order to proceed with following documentation you should have [gnome development envirnoment setup](../setup-gnome-env). 

## Gtk Application
[`GtkApplication`](https://developer.gnome.org/gtk3/stable/GtkApplication.html) is the base class that handles many aspects of an application. But here we are going to use it with [`GtkApplicationWindow`](https://developer.gnome.org/gtk3/stable/GtkApplicationWindow.html).

``` python tab="Python"
# Its recommanded to specify Gtk version
# our app is going to use
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class MyApplication(Gtk.Application):

    # connected to activate signal
    # which will be called when MyApplication
    # is launched with run()
    def do_activate(self):
        # create a Gtk Window belonging to the application itself
        window = Gtk.Window(
            application=self,
            title="Welcome to GNOME",
            default_height=100,
            default_width=200
        )
        # show the window
        window.show_all()

# create and run the application, exit with the value returned by
# running the program
app = MyApplication()
app.run(sys.argv)
```

``` javascript tab="Javascript"
// Its recommanded to specify Gtk version
// our app is going to use
imports.gi.versions.Gtk = '3.0';
const Gtk = imports.gi.Gtk;

// this in onActivate function will refer to app
// as its binded on line 24
function onActivate() {
    // Create Gtk Window
    let window = new Gtk.Window({
        title: "Welcome to GNOME",
        application: this, // add the current app
        default_height: 100,
        default_width: 200
    });
    // show all window content
    window.show_all();
}

let app = new Gtk.Application();

// activate signal will be called when app
// is launched with run()
app.connect('activate', onActivate.bind(app));
app.run(ARGV);
```

### Application signals
In this app we are only listening to [`activate` signal](https://developer.gnome.org/gio/stable/GApplication.html#GApplication-activate) below are some usefull other signals:

`shutdown` signal
:   The `shutdown` signal is emitted only on the registered primary instance immediately after the main loop terminates.

`startup` signal
:   The `startup` signal is emitted on the primary instance immediately after registration.

See more on application signals at [GApplication Documentation](https://developer.gnome.org/gio/stable/GApplication.html)

## Adding a Label

Now, we are going to add a label to our application with text `Hello GNOME!`. To do so we have to create a label using `Gtk.Label` and then add it to our `window`.

!!! note ""
    Highlighted lines are added

``` python tab="Python" hl_lines="11 12 13 14"
# (Content skiped) ...

def do_activate(self):
    # create a Gtk Window belonging to the application itself
    window = Gtk.Window(
        application=self,
        title="Welcome to GNOME",
        default_height=100,
        default_width=200
    )
    # create a label with text
    label = Gtk.Label(label="Hello GNOME!")
    # add the label to the window
    window.add(label)
    # show the window
    window.show_all()

# (Content skiped) ...
```

``` javascript tab="Javascript" hl_lines="11 12 13 14"
// (Content skiped) ...

function onActivate() {
    // Create Gtk Window
    let window = new Gtk.Window({
        title: "Welcome to GNOME",
        application: this, // add the current app
        default_height: 100,
        default_width: 200
    });
    // create gtk label
    var label = new Gtk.Label({ label: "Hello GNOME!" });
    // add label to window
    window.add(label);
    // show all window content
    window.show_all();
}

// (Content skiped) ...
```

We can also use markup in label text by simply assigning some [Pango Markup](https://developer.gnome.org/pango/stable/PangoMarkupFormat.html) to `label` and set [`use_markup`](https://developer.gnome.org/gtk3/stable/GtkLabel.html#GtkLabel--use-markup) to `true` or use [`set_markup`](https://developer.gnome.org/gtk3/stable/GtkLabel.html#gtk-label-set-markup) function to set label markup.

## Full Code
```python tab="python"
# Its recommanded to specify Gtk version
# our app is going to use
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class MyApplication(Gtk.Application):

    # connected to activate signal
    # which will be called when MyApplication
    # is launched with run()
    def do_activate(self):
        # create a Gtk Window belonging to the application itself
        window = Gtk.Window(
            application=self,
            title="Welcome to GNOME",
            default_height=100,
            default_width=200
        )
        # create a label with text
        label = Gtk.Label(label="Hello GNOME!")
        # add the label to the window
        window.add(label)
        # show the window
        window.show_all()

# create and run the application, exit with the value returned by
# running the program
app = MyApplication()
app.run(sys.argv)
```

```js tab="Javascript"
// Its recommanded to specify Gtk version
// our app is going to use
imports.gi.versions.Gtk = '3.0';
const Gtk = imports.gi.Gtk;

// this in onActivate function will refer to app
// as its binded on line 24
function onActivate() {
    // Create Gtk Window
    let window = new Gtk.Window({
        title: "Welcome to GNOME",
        application: this, // add the current app
        default_height: 100,
        default_width: 200
    });
    // create gtk label
    var label = new Gtk.Label({ label: "Hello GNOME!" });
    // add label to window
    window.add(label);
    // show all window content
    window.show_all();
}

let app = new Gtk.Application();

// activate signal will be called when app
// is launched with run()
app.connect('activate', onActivate.bind(app));
app.run(ARGV);
```


## Run App
```bash tab="Python"
python filename.py
```

```bash tab="Javascript"
gjs filename.js
```

It should show an app like this:

![Hello Gnome App](../assets/images/hello-gnome.png?center)

## Further Reading
* https://developer.gnome.org/gnome-devel-demos/stable/label.py.html.en
* https://developer.gnome.org/gnome-devel-demos/stable/label.js.html.en
* https://developer.gnome.org/gtk3/stable/gtk-getting-started.html