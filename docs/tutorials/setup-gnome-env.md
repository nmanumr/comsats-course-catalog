# Setup Gnome Development Envirnoment

In order to proceed with following documentation you should have any of following envirnoments setted up. 

### For Python
```bash
pip install pygobject
```

For more details check [`PyGObjects` getting Started Guide](https://pygobject.readthedocs.io/en/latest/getting_started.html)

### For Javascript (`Gjs`)

```bash
# On Debain/Ubuntu
apt-get install gjs libgjs-dev

# On Fedora
dnf install gjs gjs-devel

# On Arch
pacman -S gjs
```

For more details see [gjs installation guide](https://gjs-tutorial.readthedocs.io/en/latest/install.html)

### For Vala
```bash
# On Debain/Ubuntu
apt-get install valac

# On Fedora
dnf install vala

# On CentOS
yum install vala
```

For more detail see [vala on linux installation guide](https://wiki.gnome.org/Projects/Vala/ValaOnLinux)


!!! note
    Vala code snipets will be available soon.

## Run App
```bash tab="Python"
python filename.py
```

```bash tab="Javascript"
gjs filename.js
```

```bash tab="Vala"
valac --pkg gtk+-3.0 filename.vala && ./filename
```