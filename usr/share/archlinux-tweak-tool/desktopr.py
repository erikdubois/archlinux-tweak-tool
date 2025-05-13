# ============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
# ============================================================

import datetime
import numpy as np
from gi.repository import GLib, Gtk  # noqa
import functions as fn
import os

# import Settings
# import gi
# import distro
# import os

# gi.require_version('Gtk', '3.0')

default_app = ["nano", "ttf-hack"]

# =================================================================
# =                         Desktops                             =
# =================================================================

desktops = [
    "awesome",
    "bspwm",
    "budgie-desktop",
    "cinnamon",
    "chadwm",
    "gnome",
    "i3",
    "leftwm",
    "mate",
    "plasma",
    "qtile",
    "xfce",
]
pkexec = ["pkexec", "pacman", "-S", "--needed", "--noconfirm", "--ask=4"]
pkexec_reinstall = ["pkexec", "pacman", "-S", "--noconfirm", "--ask=4"]
copy = ["cp", "-Rv"]

# =================================================================
# =                         Distros                               =
# =================================================================


# =================================================================
# =================================================================
# =================================================================
# =                         ARCOLINUX                             =
# =================================================================
# =================================================================
# =================================================================

if fn.distr:
    awesome = [
        "alacritty",
        "edu-awesome-git",
        "autorandr",
        "awesome",
        "dmenu",
        "feh",
        "lxappearance",
        "noto-fonts",
        "picom-git",
        "polkit-gnome",
        "rofi",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "vicious",
        "volumeicon",
        "xfce4-terminal",
    ]
    bspwm = [
        "alacritty",
        "edu-bspwm-git",
        "edu-polybar-git",
        "archlinux-logout-git",
        "edu-rofi-git",
        "edu-rofi-themes-git",
        "awesome-terminal-fonts",
        "bspwm",
        "dmenu",
        "feh",
        "lxappearance",
        "picom-git",
        "polybar",
        "polkit-gnome",
        "rofi",
        "sutils-git",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    budgie = [
        "budgie-desktop",
        "budgie-extras",
        "dconf-editor",
        "guake",
        "ttf-hack",
    ]
    cinnamon = [
        "cinnamon",
        "cinnamon-translations",
        "gnome-screenshot",
        "gnome-system-monitor",
        "gnome-terminal",
        "iso-flag-png",
        "mintlocale",
        "nemo-fileroller",
    ]
    chadwm = [
        "alacritty",
        "archlinux-logout-git",
        "edu-rofi-git",
        "edu-rofi-themes-git",
        "edu-xfce-git",
        "dmenu",
        "feh",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "rofi",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "ttf-jetbrains-mono-nerd",
        "ttf-meslo-nerd-font-powerlevel10k",
        "volumeicon",
        "xfce4-notifyd",
        "xfce4-power-manager",
        "xfce4-screenshooter",
        "xfce4-settings",
        "xfce4-taskmanager",
        "xfce4-terminal",
    ]
    gnome = [
        "dconf-editor",
        "extension-manager",
        "file-roller",
        "gnome",
        "gnome-tweaks",
        "guake",
        "ttf-hack",
    ]
    i3 = [
        "alacritty",
        "edu-i3-git",
        "archlinux-logout-git",
        "edu-rofi-git",
        "edu-rofi-themes-git",
        "edu-xfce-git",
        "autotiling",
        "dmenu",
        "feh",
        "i3blocks",
        "i3-wm",
        "i3status",
        "lxappearance",
        "nitrogen",
        "picom-git",
        "polkit-gnome",
        "rofi",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    leftwm = [
        "alacritty",
        "archlinux-logout-git",
        "edu-leftwm-git",
        "edu-polybar-git",
        "edu-rofi-git",
        "edu-rofi-themes-git",
        "edu-xfce-git",
        "dmenu",
        "feh",
        "leftwm-git",
        "leftwm-theme-git",
        "lxappearance",
        "picom-git",
        "polybar",
        "polkit-gnome",
        "rofi",
        "sxhkd",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "ttf-iosevka-nerd",
        "ttf-material-design-iconic-font",
        "ttf-meslo-nerd-font-powerlevel10k",
        "volumeicon",
        "xfce4-appfinder",
        "xfce4-screenshooter",
        "xfce4-taskmanager",
        "xfce4-terminal",
    ]
    mate = [
        "mate",
        "mate-extra",
        "mate-tweak",
    ]
    plasma = [
        "plasma",
        "kde-system-meta",
        "ark",
        "breeze",
        "cryfs",
        "discover",
        "dolphin",
        "dolphin-plugins",
        "encfs",
        "ffmpegthumbs",
        "gocryptfs",
        "gwenview",
        "kate",
        "kde-gtk-config",
        "kdeconnect",
        "kdenetwork-filesharing",
        "ktorrent",
        "ocs-url",
        "okular",
        "packagekit-qt6",
        "partitionmanager",
        "spectacle",
        "surfn-plasma-dark-icons-git",
        "yakuake",
    ]
    qtile = [
        "alacritty",
        "archlinux-logout-git",
        "edu-qtile-git",
        "edu-rofi-git",
        "edu-rofi-themes-git",
        "edu-xfce-git",
        "awesome-terminal-fonts",
        "dmenu",
        "feh",
        "lxappearance",
        "picom-git",
        "polkit-gnome",
        "python-setuptools",
        "python-psutil",
        "qtile",
        "rofi",
        "thunar",
        "thunar-archive-plugin",
        "thunar-volman",
        "ttf-hack",
        "volumeicon",
        "xfce4-terminal",
    ]
    xfce = [
        "alacritty",
        "xfce4",
        "xfce4-goodies",
        "catfish",
        "dmenu",
        "mugshot",
        "polkit-gnome",
        "ttf-hack",
    ]

def check_desktop(desktop):
    """check if desktop is installed"""
    # /usr/share/xsessions/xfce.desktop
    if os.path.exists("/usr/share/xsessions"):
        lst = fn.listdir("/usr/share/xsessions/")
        for xsession in lst:
            if desktop + ".desktop" == xsession:
                return True
    if os.path.exists("/usr/share/wayland-sessions"):
        lst = fn.listdir("/usr/share/wayland-sessions/")
        for wsession in lst:
            if desktop + ".desktop" == wsession:
                return True

    return False


def check_lock(self, desktop, state):
    """check pacman lock"""
    if fn.path.isfile("/var/lib/pacman/db.lck"):
        mess_dialog = Gtk.MessageDialog(
            parent=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Lock File Found",
        )
        mess_dialog.format_secondary_markup(
            "pacman lock file found, do you want to remove it and continue?"
        )  # noqa

        result = mess_dialog.run()
        mess_dialog.destroy()

        if result in (Gtk.ResponseType.OK, Gtk.ResponseType.YES):
            fn.unlink("/var/lib/pacman/db.lck")
            # print("YES")
            t1 = fn.threading.Thread(
                target=install_desktop,
                args=(self, self.d_combo.get_active_text(), state),
            )
            t1.daemon = True
            t1.start()
    else:
        # print("NO FILE")
        t1 = fn.threading.Thread(
            target=install_desktop, args=(self, self.d_combo.get_active_text(), state)
        )
        t1.daemon = True
        t1.start()

    return False


def check_package_and_remove(self, package):
    """remove a package if exists"""
    if fn.check_package_installed(package):
        fn.remove_package(self, package)


def install_desktop(self, desktop, state):
    src = []
    twm = False
    # error = False
    # make backup of your .config
    now = datetime.datetime.now()
    if not fn.path.exists(fn.home + "/.config-att"):
        fn.makedirs(fn.home + "/.config-att")
        fn.permissions(fn.home + "/.config-att")
    # for all users that have now root permissions
    if fn.path.exists(fn.home + "/.config-att"):
        fn.permissions(fn.home + "/.config-att")
    fn.copy_func(
        fn.home + "/.config/",
        fn.home + "/.config-att/config-att-" + now.strftime("%Y-%m-%d-%H-%M-%S"),
        isdir=True,
    )
    fn.permissions(
        fn.home + "/.config-att/config-att-" + now.strftime("%Y-%m-%d-%H-%M-%S")
    )

    if fn.distr == "archcraft":
        fn.clear_skel_directory()

    check_package_and_remove(self, "rofi-lbonn-wayland-git")
    check_package_and_remove(self, "rofi-lbonn-wayland-only-git")

    if desktop == "awesome":
        command = list(np.append(awesome, default_app))
        src.append("/etc/skel/.config/awesome")
        twm = True
    elif desktop == "bspwm":
        command = list(np.append(bspwm, default_app))
        src.append("/etc/skel/.config/bspwm")
        src.append("/etc/skel/.config/polybar")
        twm = True
    elif desktop == "budgie-desktop":
        check_package_and_remove(self, "catfish")
        command = budgie
    elif desktop == "chadwm":
        command = list(np.append(chadwm, default_app))
        src.append("/etc/skel/.config/arco-chadwm")
        src.append("/etc/skel/.config/eww")
        twm = True
    elif desktop == "cinnamon":
        command = cinnamon
    elif desktop == "gnome":
        command = gnome
    elif desktop == "i3":
        command = list(np.append(i3, default_app))
        src.append("/etc/skel/.config/i3")
        twm = True
    elif desktop == "leftwm":
        command = list(np.append(leftwm, default_app))
        src.append("/etc/skel/.config/leftwm")
        twm = True
    elif desktop == "mate":
        command = mate
    elif desktop == "plasma":
        check_package_and_remove(self, "qt5ct")
        command = plasma
        src.append("/etc/skel/.config")
        src.append("/etc/skel/.local/share")
        twm = True
    elif desktop == "qtile":
        command = list(np.append(qtile, default_app))
        src.append("/etc/skel/.config/qtile")
        twm = True
    elif desktop == "xfce":
        command = list(np.append(xfce, default_app))

    GLib.idle_add(self.desktopr_prog.set_fraction, 0.2)

    timeout_id = None
    timeout_id = GLib.timeout_add(100, fn.do_pulse, None, self.desktopr_prog)
    print("----------------------------------------------------------------")
    print("Packages list to install")
    print("----------------------------------------------------------------")
    print(command)
    print("----------------------------------------------------------------")

    if state == "reinst":
        com1 = pkexec_reinstall
        if self.ch1.get_active():
            GLib.idle_add(self.desktopr_stat.set_text, "Clearing cache .....")
            fn.subprocess.call(
                ["sh", "-c", "yes | pkexec pacman -Scc"],
                shell=False,
                stdout=fn.subprocess.PIPE,
            )
    else:
        com1 = pkexec

    # print(list(np.append(com1, command)))
    GLib.idle_add(
        self.desktopr_stat.set_text,
        "Installing " + self.d_combo.get_active_text() + "...",
    )

    for line in command:
        package_name = line if isinstance(line, str) else line[0]
        print(f"   Installing: {package_name}")
        GLib.idle_add(
            self.desktopr_stat.set_text,
            f"   Installing {package_name}...",
        )

        try:
            process = fn.subprocess.Popen(
                list(np.append(com1, line)),
                bufsize=1,
                stdout=fn.subprocess.PIPE,
                stderr=fn.subprocess.PIPE,  # Capture stderr for error handling
                universal_newlines=True,
            )

            stdout, stderr = process.communicate()  # Read both stdout and stderr
            process_return_code = process.returncode  # Get the return code

            for output_line in stdout.splitlines():
                GLib.idle_add(self.desktopr_stat.set_text, output_line.strip())

            # List of group packages
            group_packages = [
                "budgie-desktop",
                "budgie-extras",
                "cinnamon",
                "gnome-extra",
                "gnome",
                "mate-extra",
                "mate",
                "plasma",
                "xfce4-goodies",
                "xfce4",
            ]

            try:
                # Check the return code for success or failure
                if process_return_code == 0:
                    if package_name in group_packages:
                        print(
                            "There is no way to check if a group package is installed"
                        )
                        GLib.idle_add(
                            self.desktopr_stat.set_text,
                            "There is no way to check if a group package is installed.",
                        )
                    elif fn.check_package_installed(package_name):
                        print(f"{package_name} is installed")
                        GLib.idle_add(
                            self.desktopr_stat.set_text,
                            f"Successfully installed {package_name}.",
                        )
                    else:
                        print(
                            f"{package_name} IS NOT INSTALLED - REMOVE CONFLICTING PACKAGE(S)"
                        )
                        GLib.idle_add(
                            self.desktopr_stat.set_text,
                            f"Failed to install {package_name}. Possible conflicts detected.",
                        )
                else:
                    # Check for package conflicts in stderr
                    conflict_message = None
                    for line in stderr.splitlines():
                        if "conflicting dependencies" in line or "in conflict" in line:
                            conflict_message = line
                            break  # Stop searching once we find a conflict message

                    if conflict_message:
                        print(f"Installation failed due to package conflict: {conflict_message}")
                        GLib.idle_add(
                            self.desktopr_stat.set_text,
                            f"Installation failed: {conflict_message}",
                        )
                    else:
                        print(f"Failed to install {package_name}: {stderr}")
                        GLib.idle_add(
                            self.desktopr_stat.set_text,
                            f"Failed to install {package_name}. Error: {stderr}",
                        )

            except Exception as e:
                print(f"An error occurred while installing {package_name}: {str(e)}")
                GLib.idle_add(
                    self.desktopr_stat.set_text,
                    f"An error occurred: {str(e)}",
                )
        except Exception as e:
            print(f"An error occurred while installing {package_name}: {str(e)}")
            GLib.idle_add(
                self.desktopr_stat.set_text,
                f"An error occurred: {str(e)}",
            )

    # with fn.subprocess.Popen(
    #     list(np.append(com1, command)),
    #     bufsize=1,
    #     stdout=fn.subprocess.PIPE,
    #     universal_newlines=True,
    # ) as p:
    #     for line in p.stdout:
    #         GLib.idle_add(self.desktopr_stat.set_text, line.strip())
    # print("----------------------------------------------------------------")

    GLib.source_remove(timeout_id)
    timeout_id = None
    GLib.idle_add(self.desktopr_prog.set_fraction, 0)

    if check_desktop(desktop):
        print(src)
        if twm is True:
            for x in src:
                if fn.path.isdir(x) or fn.path.isfile(x):
                    print(x)
                    dest = x.replace("/etc/skel", fn.home)
                    # print(dest)
                    if fn.path.isdir(x):
                        dest = fn.path.split(dest)[0]
                    l1 = np.append(copy, [x])
                    l2 = np.append(l1, [dest])
                    GLib.idle_add(
                        self.desktopr_stat.set_text, "Copying " + x + " to " + dest
                    )

                    with fn.subprocess.Popen(
                        list(l2),
                        bufsize=1,
                        stdout=fn.subprocess.PIPE,
                        universal_newlines=True,
                    ) as p:
                        for line in p.stdout:
                            GLib.idle_add(self.desktopr_stat.set_text, line.strip())
                    fn.permissions(dest)

        GLib.idle_add(self.desktopr_stat.set_text, "")
        GLib.idle_add(self.desktop_status.set_text, "This desktop is installed")
        GLib.idle_add(
            fn.show_in_app_notification, self, desktop + " has been installed"
        )
        print("----------------------------------------------------------------")
        print(desktop + " has been installed")
        print("----------------------------------------------------------------")
    else:
        GLib.idle_add(
            self.desktop_status.set_markup, "This desktop is <b>NOT</b> installed"
        )
        GLib.idle_add(
            self.desktopr_error.set_text, "Install " + desktop + " via terminal"
        )
        # GLib.idle_add(self.desktopr_stat.set_text, "An error has occured in installation")
        GLib.idle_add(
            fn.show_in_app_notification, self, desktop + " has not been installed"
        )
        print("----------------------------------------------------------------")
        print(desktop + " has NOT been installed")
        print("----------------------------------------------------------------")
    fn.create_log(self)
