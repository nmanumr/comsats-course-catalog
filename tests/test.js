#!/usr/bin/gjs
const Gtk = imports.gi.Gtk;
imports.gi.versions.Gtk = '3.0';

function onActivate() {

    // Create Gtk Window
    let myWindow = new Gtk.Window({
        title: "Welcome to GNOME",
        application: this, // add the current app
        default_height: 100,
        default_width: 200
    });

    // create a label
    var myLabel = new Gtk.Label({ label: '<span foreground="blue" size="x-large">Blue text</span> is <a href="https://www.gtk.org/api/2.6/pango/PangoMarkupFormat.html" title="Click to find out more">internet</a>!', use_markup: true });

    // add label to window
    myWindow.add(myLabel);

    // show all window content
    myWindow.show_all();
}

let app = new Gtk.Application();
app.connect('activate', onActivate.bind(app));
app.run(ARGV);