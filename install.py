#!/usr/bin/env python3

import argparse
import sys
import time
import os
import signal
import subprocess
import platform
import shutil

# Define los colores
class Colors:
    GREEN = '\e[0;32m\033[1m'
    END = '\033[0m\e[0m'
    RED = '\e[0;31m\033[1m'
    BLUE = '\e[0;34m\033[1'
    YELLOW = '\e[0;33m\033[1m'
    PURPLE = '\e[0;35m\033[1m'
    TURQUOISE = '\e[0;36m\033[1m'
    GRAY = '\e[0;37m\033[1m'

def help_panel():
    """Muestra el panel de ayuda."""
    print(f"\n{Colors.RED}[!] Uso: {sys.argv[0]} -v [1/0]")
    print(f"{Colors.RED}{'═'*80}{Colors.END}")
    print(f"\n\t{Colors.BLUE}\u2503{Colors.END}  {Colors.PURPLE}[-v]{Colors.END} {Colors.YELLOW}Agregar verbose{Colors.END}")
    print(f"\n\t\t{Colors.PURPLE}({Colors.END}{Colors.GREEN}1{Colors.END}{Colors.PURPLE}){Colors.END} {Colors.TURQUOISE}si{Colors.END} {Colors.BLUE}[{Colors.YELLOW}Util para ver lo que está pasando{Colors.BLUE}]{Colors.END}")
    print(f"\t\t{Colors.PURPLE}({Colors.END}{Colors.GREEN}0{Colors.END}{Colors.PURPLE}){Colors.END} {Colors.TURQUOISE}no{Colors.END} {Colors.BLUE}[{Colors.YELLOW}Output más bonito y organizado{Colors.BLUE}]{Colors.END}")
    print(f"\n\t{Colors.BLUE}\u2503{Colors.END}  {Colors.PURPLE}[-h]{Colors.END}{Colors.YELLOW} Mostrar este panel de ayuda{Colors.END}\n")

def banner():
    """Muestra el banner del script."""
    os.system("clear")
    print(f"\n{Colors.GREEN}███████{Colors.TURQUOISE}╗{Colors.GRAY}░{Colors.GREEN}█████{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}██████{Colors.TURQUOISE}╗{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░░{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░░░░░{Colors.GREEN}██████{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░░░░░░{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GREEN}███{Colors.TURQUOISE}╗{Colors.GRAY}░░░{Colors.GREEN}███{Colors.TURQUOISE}╗")
    time.sleep(0.05)
    print(f"{Colors.GREEN}██{Colors.TURQUOISE}╔════╝{Colors.GREEN}██{Colors.TURQUOISE}╔══{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GREEN}██{Colors.TURQUOISE}╔════╝╚{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GRAY}░░░░░░{Colors.GREEN}██{Colors.TURQUOISE}╔══{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GREEN}████{Colors.TURQUOISE}╗{Colors.GRAY}░{Colors.GREEN}████{Colors.TURQUOISE}║\t\t      {Colors.GRAY}BY {Colors.PURPLE}Invertebrado")
    time.sleep(0.05)
    print(f"{Colors.GREEN}█████{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}███████{Colors.TURQUOISE}║╚{Colors.GREEN}█████{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}{Colors.TURQUOISE}╚{Colors.GREEN}████{Colors.TURQUOISE}╔╝{Colors.GRAY}░{Colors.GREEN}█████{Colors.TURQUOISE}╗{Colors.GREEN}██████{Colors.TURQUOISE}╔╝{Colors.GRAY}░{Colors.TURQUOISE}╚{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GREEN}████{Colors.TURQUOISE}╗{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GREEN}██{Colors.TURQUOISE}╔{Colors.GREEN}████{Colors.TURQUOISE}╔{Colors.GREEN}██{Colors.TURQUOISE}║\t{Colors.GRAY}PERSONAL PAGE {Colors.YELLOW}https://invertebr4do.github.io")
    time.sleep(0.05)
    print(f"{Colors.GREEN}██{Colors.TURQUOISE}╔══╝{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}╔══{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░{Colors.TURQUOISE}╚═══{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.TURQUOISE}╚{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GRAY}░░{Colors.TURQUOISE}╚════╝{Colors.GREEN}██{Colors.TURQUOISE}╔═══╝{Colors.GRAY}░░░{Colors.GREEN}████{Colors.TURQUOISE}╔═{Colors.GREEN}████{Colors.TURQUOISE}║{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}║╚{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GREEN}██{Colors.TURQUOISE}║\t   {Colors.GRAY}GITHUB {Colors.TURQUOISE}https://github.com/invertebr4do")
    time.sleep(0.05)
    print(f"{Colors.GREEN}███████{Colors.TURQUOISE}╗{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GREEN}██████{Colors.TURQUOISE}╔╝{Colors.GRAY}░░░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░░░░░░░░░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░░░░░░░{Colors.TURQUOISE}╚{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GRAY}░{Colors.TURQUOISE}╚{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}║\t  {Colors.GRAY}INSPIRED IN {Colors.RED}s4vitar {Colors.GRAY}BSPWM CONFIGURATIONS")
    time.sleep(0.05)
    print(f"{Colors.TURQUOISE}╚══════╝╚═╝{Colors.GRAY}░░{Colors.TURQUOISE}╚═╝╚═════╝{Colors.GRAY}░░░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░░░░░░░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░░░░░░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░░░░{Colors.TURQUOISE}╚═╝{Colors.END}")
    time.sleep(0.05)
    print(f"{Colors.PURPLE}{'-'*80}{Colors.END}")

def banner2():
    """Muestra el banner del script (segunda versión)."""
    #os.system("tput civis; clear") #Estos comandos son dificiles de replicar
    os.system("clear")
    print(f"\n\t\t{Colors.GREEN}███████{Colors.TURQUOISE}╗{Colors.GRAY}░{Colors.GREEN}█████{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}██████{Colors.TURQUOISE}╗{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░░{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░░░░░{Colors.GREEN}██████{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░░░░░░{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GREEN}███{Colors.TURQUOISE}╗{Colors.GRAY}░░░{Colors.GREEN}███{Colors.TURQUOISE}╗")
    time.sleep(0.05)
    print(f"\t\t{Colors.GREEN}██{Colors.TURQUOISE}╔════╝{Colors.GREEN}██{Colors.TURQUOISE}╔══{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GREEN}██{Colors.TURQUOISE}╔════╝╚{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GRAY}░░░░░░{Colors.GREEN}██{Colors.TURQUOISE}╔══{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GREEN}████{Colors.TURQUOISE}╗{Colors.GRAY}░{Colors.GREEN}████{Colors.TURQUOISE}║")
    time.sleep(0.05)
    print(f"\t\t{Colors.GREEN}█████{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}███████{Colors.TURQUOISE}║╚{Colors.GREEN}█████{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.GREEN}{Colors.TURQUOISE}╚{Colors.GREEN}████{Colors.TURQUOISE}╔╝{Colors.GRAY}░{Colors.GREEN}█████{Colors.TURQUOISE}╗{Colors.GREEN}██████{Colors.TURQUOISE}╔╝{Colors.GRAY}░{Colors.TURQUOISE}╚{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GREEN}████{Colors.TURQUOISE}╗{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GREEN}██{Colors.TURQUOISE}╔{Colors.GREEN}████{Colors.TURQUOISE}╔{Colors.GREEN}██{Colors.TURQUOISE}║")
    time.sleep(0.05)
    print(f"\t\t{Colors.GREEN}██{Colors.TURQUOISE}╔══╝{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}╔══{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░{Colors.TURQUOISE}╚═══{Colors.GREEN}██{Colors.TURQUOISE}╗{Colors.GRAY}░░{Colors.TURQUOISE}╚{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GRAY}░░{Colors.TURQUOISE}╚════╝{Colors.GREEN}██{Colors.TURQUOISE}╔═══╝{Colors.GRAY}░░░{Colors.GREEN}████{Colors.TURQUOISE}╔═{Colors.GREEN}████{Colors.TURQUOISE}║{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}║╚{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GREEN}██{Colors.TURQUOISE}║")
    time.sleep(0.05)
    print(f"\t\t{Colors.GREEN}███████{Colors.TURQUOISE}╗{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GREEN}██████{Colors.TURQUOISE}╔╝{Colors.GRAY}░░░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░░░░░░░░░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░░░░░░░{Colors.TURQUOISE}╚{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GRAY}░{Colors.TURQUOISE}╚{Colors.GREEN}██{Colors.TURQUOISE}╔╝{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}║{Colors.GRAY}░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░{Colors.GREEN}██{Colors.TURQUOISE}║")
    time.sleep(0.05)
    print(f"\t\t{Colors.TURQUOISE}╚══════╝╚═╝{Colors.GRAY}░░{Colors.TURQUOISE}╚═╝╚═════╝{Colors.GRAY}░░░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░░░░░░░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░░░░░░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░{Colors.TURQUOISE}╚═╝{Colors.GRAY}░░░░░{Colors.TURQUOISE}╚═╝{Colors.END}")
    time.sleep(0.05)
    print(f"\n\t\t\t\t\t      {Colors.GRAY}BY {Colors.PURPLE}Invertebrado")
    time.sleep(0.05)
    print(f"\t\t\t\t${Colors.GRAY}PERSONAL PAGE {Colors.YELLOW}https://invertebr4do.github.io")
    time.sleep(0.05)
    print(f"\t\t\t\t   {Colors.GRAY}GITHUB {Colors.TURQUOISE}https://github.com/invertebr4do")
    time.sleep(0.05)
    print(f"\t\t\t\t  {Colors.GRAY}INSPIRED IN {Colors.RED}s4vitar {Colors.GRAY}BSPWM CONFIGURATIONS")
    time.sleep(0.05)
    print(f"\t\t\t{Colors.RED}s4vitar's {Colors.GRAY}YOUTUBE CHANNEL {Colors.RED}https://www.youtube.com/s4vitar")
    time.sleep(0.05)
    print(f"\t\t\t {Colors.RED}s4vitar's {Colors.GRAY}TWITCH CHANNEL {Colors.PURPLE}https://www.twitch.tv/S4vitaar{Colors.END}")

def ctrl_c_handler(sig, frame):
    """Maneja la interrupción del script (Ctrl+C)."""
    print(f"\n\n{Colors.RED}[!] Exiting...{Colors.END}\n")
    sys.exit(1)

def status_code(process):
    """Verifica el código de salida de un proceso."""
    if process.returncode != 0:
        print(f"\n{Colors.RED}[X] OCURRIÓ UN PROBLEMA{Colors.END}\n")
        sys.exit(1)

def check_user():
    """Verifica si el script se está ejecutando como root."""
    if os.geteuid() == 0:
        print(f"\n{Colors.RED}[!] NO EJECUTAR ESTE SCRIPT COMO ROOT{Colors.END}\n")
        sys.exit(1)

def check_internet():
    """Verifica la conexión a Internet."""
    try:
        process = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True, check=False)
        if process.returncode == 0:
            print(f"\n{Colors.GREEN}[✔] CON CONECCIÓN A INTERNET{Colors.END}")
            time.sleep(1.5)
            return True
        else:
            print(f"\n{Colors.RED}[X] COMPRUEBA TU CONECCIÓN A INTERNET{Colors.END}")
            sys.exit(1)
    except FileNotFoundError as e:
        print(f"{Colors.RED}[!] Error: Comando no encontrado: {e}{Colors.END}")
        sys.exit(1)

def iface():
    """Solicita al usuario que ingrese el nombre de su interfaz de red."""
    print(f"\n{Colors.PURPLE}█ {Colors.GRAY}INGRESE EL NOMBRE DE SU INTERFAZ DE RED {Colors.PURPLE}█{Colors.END}\n")
    try:
        process = subprocess.run(["ip", "a"], capture_output=True, text=True, check=True)
        interfaces = [line.split(":")[1].strip() for line in process.stdout.splitlines() if ":" in line and not line.strip().startswith("lo")]
        for i in interfaces:
            print(f"\t{Colors.BLUE}· {Colors.YELLOW}{i}{Colors.END}")

        ni = input(f"\n{Colors.GREEN}» {Colors.GRAY}")
        while not ni:
            print(f"{Colors.RED}[X] VALOR REQUERIDO{Colors.END}\n")
            ni = input(f"{Colors.GREEN}» {Colors.GRAY}")

        # Aquí, en lugar de usar sed, simplemente retornamos el valor ingresado.
        # La sustitución en los archivos se hará después.
        return ni

    except FileNotFoundError as e:
        print(f"{Colors.RED}[!] Error: Comando no encontrado: {e}{Colors.END}")
        sys.exit(1)

def package_installer(packages, verbose):
    """Instala una lista de paquetes usando apt."""
    try:
        if verbose == 1:
            for package in packages:
                print(f"\t{Colors.YELLOW}[{Colors.BLUE}*{Colors.YELLOW}] INSTALANDO {Colors.TURQUOISE}{package}{Colors.END}\n")
                process = subprocess.run(["sudo", "apt", "install", package, "-y"], capture_output=False, text=True, check=False)
                status_code(process)
                print("\t" + Colors.YELLOW + "." * 7 + f" {Colors.YELLOW}[{Colors.GREEN}\u2713{Colors.YELLOW}]{Colors.END}")
                time.sleep(1)
        else:
            for package in packages:
                print(f"\t{Colors.YELLOW}[{Colors.BLUE}*{Colors.YELLOW}] INSTALANDO {Colors.TURQUOISE}{package}{Colors.END}", end="")
                process = subprocess.run(["sudo", "apt", "install", package, "-y"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                status_code(process)
                print(" " + Colors.YELLOW + "." * 7 + f" {Colors.YELLOW}[{Colors.GREEN}\u2713{Colors.YELLOW}]{Colors.END}")
                time.sleep(1)
    except FileNotFoundError as e:
        print(f"{Colors.RED}[!] Error: Comando no encontrado: {e}{Colors.END}")
        sys.exit(1)

def dependencies(verbose):
    """Instala las dependencias del sistema."""
    banner()

    print(f"\n{Colors.YELLOW}[*] BUSCANDO ACTUALIZACIONES{Colors.END}")
    time.sleep(1)

    try:
        process = subprocess.run(["sudo", "apt", "update"], capture_output=True, text=True, check=False)
        status_code(process)

        # Analizar la salida de apt update (esto es una simplificación, se puede mejorar)
        updates_available = False
        for line in process.stdout.splitlines():
            if "packages can be upgraded" in line:
                updates_available = True
                break

        if updates_available:
            print(f"\n{Colors.PURPLE}█ {Colors.GRAY}HAY PAQUETES POR ACTUALIZAR {Colors.PURPLE}█{Colors.END}")
            print(f"\n{Colors.YELLOW}[*] ACTUALIZANDO PAQUETES DEL SISTEMA{Colors.END}")
            if verbose == 1:
                upgrade_process = subprocess.run(["sudo", "apt", "upgrade", "-y"], capture_output=False, text=True, check=False)
            else:
                upgrade_process = subprocess.run(["sudo", "apt", "upgrade", "-y"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            status_code(upgrade_process)
            print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}SISTEMA ACTUALIZADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        else:
            print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}NO SE ENCONTRARON PAQUETES POR ACTUALIZAR {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] INSTALANDO ALGUNOS PAQUETES NECESARIOS...{Colors.END}\n")
        required_packages = [
            "build-essential", "libxcb-util0-dev", "libxcb-ewmh-dev", "libxcb-randr0-dev",
            "libxcb-icccm4-dev", "libxcb-keysyms1-dev", "libxcb-xinerama0-dev", "libasound2-dev",
            "libxcb-xtest0-dev", "libxcb-shape0-dev", "libxinerama1", "libxinerama-dev",
            "kitty", "flameshot", "brightnessctl", "pamixer", "moreutils"
        ]

        package_installer(required_packages, verbose)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}PAQUETES INSTALADOS CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")

    except FileNotFoundError as e:
        print(f"{Colors.RED}[!] Error: Comando no encontrado: {e}{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}[!] Error inesperado: {e}{Colors.END}")
        sys.exit(1)

def kitty_config():
    """Configura la terminal Kitty"""
    print(f"\n{Colors.YELLOW}[*] CONFIGURANDO TERMINAL KITTY{Colors.END}")
    try:
        os.makedirs(os.path.expanduser("~/.config/kitty"), exist_ok=True) # Crea el directorio si no existe
        # Copiar archivos de configuracion (Asumiendo que los archivos 'Files/kitty/kitty.conf' y 'Files/kitty/color.ini' existen en el mismo directorio que este script)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        shutil.copy(f"{script_dir}/Files/kitty/kitty.conf", os.path.expanduser("~/.config/kitty/kitty.conf"))
        shutil.copy(f"{script_dir}/Files/kitty/color.ini", os.path.expanduser("~/.config/kitty/color.ini"))
    except OSError as e:
        print(f"{Colors.RED}[!] Error al configurar Kitty: {e}{Colors.END}")

def bspwm_sxhkd(verbose):
    """Clona e instala BSPWM y SXHKD."""
    banner()
    try:
        print(f"\n{Colors.YELLOW}[*] CLONANDO BSPWM{Colors.END}")
        if verbose == 1:
            bspwm_process = subprocess.run(["git", "clone", "https://github.com/baskerville/bspwm.git"], capture_output=False, text=True, check=False)
        else:
            bspwm_process = subprocess.run(["git", "clone", "https://github.com/baskerville/bspwm.git"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        status_code(bspwm_process)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}BSPWM CLONADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] CLONANDO SXHKD{Colors.END}")
        if verbose == 1:
            sxhkd_process = subprocess.run(["git", "clone", "https://github.com/baskerville/sxhkd.git"], capture_output=False, text=True, check=False)
        else:
            sxhkd_process = subprocess.run(["git", "clone", "https://github.com/baskerville/sxhkd.git"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        status_code(sxhkd_process)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}SXHKD CLONADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        def install_make(directory):
            """Función auxiliar para ejecutar 'make' e 'install'."""
            try:
                cwd = os.getcwd()
                os.chdir(directory)
                make_process = subprocess.run(["make"], capture_output=True, text=True, check=False)
                status_code(make_process)
                install_process = subprocess.run(["sudo", "make", "install"], capture_output=True, text=True, check=False)
                status_code(install_process)
                os.chdir(cwd)
            except OSError as e:
                print(f"{Colors.RED}[!] Error al compilar o instalar: {e}{Colors.END}")
                sys.exit(1)

        print(f"\n{Colors.YELLOW}[*] INSTALANDO BSPWM (make){Colors.END}")
        install_make("bspwm")
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}BSPWM INSTALADO CORRECTAMENTE (make) {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] INSTALANDO SXHKD (make){Colors.END}")
        install_make("sxhkd")
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}SXHKD INSTALADO CORRECTAMENTE (make) {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] INSTALANDO BSPWM (apt){Colors.END}")
        if verbose == 1:
            apt_bspwm_process = subprocess.run(["sudo", "apt", "install", "bspwm", "-y"], capture_output=False, text=True, check=False)
        else:
            apt_bspwm_process = subprocess.run(["sudo", "apt", "install", "bspwm", "-y"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        status_code(apt_bspwm_process)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}BSPWM INSTALADO CORRECTAMENTE (apt) {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] CARGANDO ALGUNOS FICHEROS DE BSPWM Y SXHKD{Colors.END}")
        os.makedirs(os.path.expanduser("~/.config/bspwm"), exist_ok=True)
        os.makedirs(os.path.expanduser("~/.config/sxhkd"), exist_ok=True)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        shutil.copy(f"{script_dir}/Files/bspwmrc", os.path.expanduser("~/.config/bspwm/bspwmrc"))
        status_code(subprocess.run(["chmod", "+x", os.path.expanduser("~/.config/bspwm/bspwmrc")], capture_output=True, text=True, check=False))

        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}FICHEROS CARGADOS CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] CONFIGURANDO BSPWMRC{Colors.END}")
        username = os.getlogin()
        with open(f"{script_dir}/Files/bspwmrc", "r") as infile, open(os.path.expanduser("~/.config/bspwm/bspwmrc"), "w") as outfile:
            for line in infile:
                outfile.write(line.replace("USER", username))
        status_code(subprocess.run(["chmod", "+x", os.path.expanduser("~/.config/bspwm/bspwmrc")], capture_output=True, text=True, check=False))
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}BSPWMRC CONFIGURADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] CONFIGURANDO SXHKDRC{Colors.END}")
        with open(f"{script_dir}/Files/sxhkdrc", "r") as infile, open(os.path.expanduser("~/.config/sxhkd/sxhkdrc"), "w") as outfile:
            for line in infile:
                outfile.write(line.replace("USER", username))
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}SXHKDRC CONFIGURADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] CONFIGURANDO BSPWM_RESIZE{Colors.END}")
        os.makedirs(os.path.expanduser("~/.config/bspwm/scripts/"), exist_ok=True)
        shutil.copy(f"{script_dir}/Files/bspwm_resize", os.path.expanduser("~/.config/bspwm/scripts/bspwm_resize"))
        status_code(subprocess.run(["chmod", "+x", os.path.expanduser("~/.config/bspwm/scripts/bspwm_resize")], capture_output=True, text=True, check=False))
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}BSPWM_RESIZE CONFIGURADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

    except FileNotFoundError as e:
        print(f"{Colors.RED}[!] Error: Comando no encontrado: {e}{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}[!] Error inesperado: {e}{Colors.END}")
        sys.exit(1)

def Polybar(verbose):
        """Clona e instala Polybar"""
        banner()

        print(f"\n{Colors.YELLOW}[*] INSTALANDO PAQUETES NECESARIOS PARA LA POLYBAR...{Colors.END}\n")
        required_packages = [
            "cmake", "cmake-data", "pkg-config", "python3-sphinx", "libcairo2-dev",
            "libxcb1-dev", "libxcb-randr0-dev", "libxcb-composite0-dev", "python3-xcbgen",
            "xcb-proto", "libxcb-image0-dev", "libxcb-xkb-dev", "libxcb-xrm-dev",
            "libxcb-cursor-dev", "libasound2-dev", "libpulse-dev", "libjsoncpp-dev",
            "libmpdclient-dev", "libuv1-dev", "libnl-genl-3-dev"
        ]

        package_installer(required_packages, verbose)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}PAQUETES INSTALADOS CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")

        try:
            def install_polybar():
                """Función auxiliar para clonar e instalar Polybar."""
                try:
                    process = subprocess.run(["git", "clone", "--recursive", "https://github.com/polybar/polybar"], capture_output=True, text=True, check=False)
                    status_code(process)
                    os.chdir("polybar")
                    os.makedirs("build", exist_ok=True)
                    os.chdir("build")
                    cmake_process = subprocess.run(["cmake", ".."], capture_output=True, text=True, check=False)
                    status_code(cmake_process)
                    make_process = subprocess.run(["make", "-j", str(os.cpu_count())], capture_output=True, text=True, check=False)
                    status_code(make_process)
                    install_process = subprocess.run(["sudo", "make", "install"], capture_output=True, text=True, check=False)
                    status_code(install_process)
                    os.chdir("../..") # Regresa al directorio principal
                except OSError as e:
                    print(f"{Colors.RED}[!] Error al compilar o instalar: {e}{Colors.END}")
                    sys.exit(1)

            print(f"\n{Colors.YELLOW}[*] CLONANDO E INSTALANDO POLYBAR{Colors.END}")
            if verbose == 1:
                install_polybar()
            else:
                # Redirige la salida para el modo no verbose
                with open(os.devnull, 'w') as fnull:
                    # Redirige la salida para el modo no verbose
                    stdout = sys.stdout
                    stderr = sys.stderr
                    sys.stdout = fnull
                    sys.stderr = fnull
                    install_polybar()
                    sys.stdout = stdout
                    sys.stderr = stderr
            print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}POLYBAR INSTALADA CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")

            os.makedirs(os.path.expanduser("~/.config/polybar"), exist_ok=True)
        except Exception as e:
            print(f"{Colors.RED}[!] Error inesperado: {e}{Colors.END}")
            sys.exit(1)

def picom_rofi(verbose):
    """Instala y configura Picom y Rofi."""
    banner()

    print(f"\n{Colors.YELLOW}[*] ACTUALIZANDO EL SISTEMA{Colors.END}")
    time.sleep(1)
    try:
        if verbose == 1:
            update_process = subprocess.run(["sudo", "apt", "update"], capture_output=False, text=True, check=False)
        else:
            update_process = subprocess.run(["sudo", "apt", "update"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        status_code(update_process)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}SISTEMA ACTUALIZADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] INSTALANDO PAQUETES NECESARIOS PARA PICOM...{Colors.END}\n")
        required_packages = [
            "meson", "libxext-dev", "libxcb-damage0-dev", "libxcb-xfixes0-dev", "libxcb-shape0-dev",
            "libxcb-render-util0-dev", "libxcb-render0-dev", "libxcb-present-dev", "libpixman-1-dev",
            "libconfig-dev", "libgl1-mesa-dev", "libpcre3", "libpcre3-dev", "libevdev-dev",
            "uthash-dev", "libev-dev", "libx11-xcb-dev", "libxcb-glx0-dev", "libdbus-1-dev"
        ]

        package_installer(required_packages, verbose)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}PAQUETES INSTALADOS CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        def install_picom():
            """Función auxiliar para clonar e instalar Picom."""
            try:
                process = subprocess.run(["git", "clone", "https://github.com/ibhagwan/picom.git"], capture_output=True, text=True, check=False)
                status_code(process)
                os.chdir("picom")
                submodule_process = subprocess.run(["git", "submodule", "update", "--init", "--recursive"], capture_output=True, text=True, check=False)
                status_code(submodule_process)
                meson_process = subprocess.run(["meson", "--buildtype=release", ".", "build"], capture_output=True, text=True, check=False)
                status_code(meson_process)
                ninja_process = subprocess.run(["ninja", "-C", "build"], capture_output=True, text=True, check=False)
                status_code(ninja_process)
                install_process = subprocess.run(["sudo", "ninja", "-C", "build", "install"], capture_output=True, text=True, check=False)
                status_code(install_process)
                os.chdir("..")  # Regresa al directorio principal
            except OSError as e:
                print(f"{Colors.RED}[!] Error al compilar o instalar: {e}{Colors.END}")
                sys.exit(1)

        print(f"\n{Colors.YELLOW}[*] INSTALANDO PICOM{Colors.END}")
        if verbose == 1:
            install_picom()
        else:
            with open(os.devnull, 'w') as fnull:
                stdout = sys.stdout
                stderr = sys.stderr
                sys.stdout = fnull
                sys.stderr = fnull
                install_picom()
                sys.stdout = stdout
                sys.stderr = stderr
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}PICOM INSTALADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] INSTALANDO ROFI{Colors.END}")
        if verbose == 1:
            rofi_process = subprocess.run(["sudo", "apt", "install", "rofi", "-y"], capture_output=False, text=True, check=False)
        else:
            rofi_process = subprocess.run(["sudo", "apt", "install", "rofi", "-y"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        status_code(rofi_process)

        # Eliminar y crear el directorio de configuración de Rofi
        rofi_config_dir = os.path.expanduser("~/.config/rofi")
        if os.path.exists(rofi_config_dir):
            shutil.rmtree(rofi_config_dir)  # Elimina el directorio y su contenido

        try:
            os.makedirs(rofi_config_dir, exist_ok=False)  # Crea el directorio
        except OSError as e:
            print(f"{Colors.RED}[!] Error al crear el directorio de configuración de Rofi: {e}{Colors.END}")
            sys.exit(1)

        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}ROFI INSTALADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] CONFIGURANDO TEMA DE ROFI{Colors.END}")
        script_dir = os.path.dirname(os.path.abspath(__file__))

        if verbose == 1:
            git_process = subprocess.run(["git", "clone", "https://github.com/adi1090x/rofi.git"], capture_output=False, text=True, check=False)
        else:
            git_process = subprocess.run(["git", "clone", "https://github.com/adi1090x/rofi.git"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        status_code(git_process)

        try:
          rofi_src = os.path.join(script_dir,"rofi", "files")
          rofi_dst = os.path.expanduser("~/.config/rofi")
          shutil.copytree(rofi_src,rofi_dst,dirs_exist_ok=True)
          shutil.rmtree(os.path.join(script_dir,"rofi"))
        except Exception as e:
            print(f"{Colors.RED}[!] Ocurrio un error al configurar ROFI: ", e ,Colors.END)
            sys.exit(1)

        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}TEMA DE ROFI CONFIGURADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

    except FileNotFoundError as e:
        print(f"{Colors.RED}[!] Error: Comando no encontrado: {e}{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}[!] Error inesperado: {e}{Colors.END}")
        sys.exit(1)
                                          

def feh_ilock(verbose):
    """Instala Feh e I3lock."""
    banner()
    script_dir = os.path.dirname(os.path.abspath(__file__)) # Definimos script_dir aqui
    print(f"\n{Colors.YELLOW}[*] INSTALANDO FEH{Colors.END}")
    try:
        if verbose == 1:
            feh_process = subprocess.run(["sudo", "apt", "install", "feh", "-y"], capture_output=False, text=True, check=False)
        else:
            feh_process = subprocess.run(["sudo", "apt", "install", "feh", "-y"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        status_code(feh_process)

        wallpaper_source = os.path.join(script_dir, "EASY-PWM", "Files", "Wallpaper.jpg")  # Confirmar si este path es correcto
        wallpaper_dest = os.path.expanduser("~/Pictures/") # Cambié la creación del directorio por exist_ok=True abajo

        try:
             shutil.copy(wallpaper_source, wallpaper_dest)
        except FileNotFoundError:
            print(f"{Colors.RED}[!] No se encontró el archivo Wallpaper.jpg{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}[!] Error al copiar el wallpaper: {e}{Colors.END}")

        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}FEH INSTALADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] INSTALANDO DEPENDENCIAS PARA I3LOCK{Colors.END}\n")
        required_packages = [
            "autoconf", "gcc", "make", "pkg-config", "libpam0g-dev", "libcairo2-dev",
            "libfontconfig1-dev", "libxcb-composite0-dev", "libev-dev", "libx11-xcb-dev",
            "libxcb-xkb-dev", "libxcb-xinerama0-dev", "libxcb-randr0-dev", "libxcb-image0-dev",
            "libxcb-util0-dev", "libxcb-xrm-dev", "libxkbcommon-dev", "libxkbcommon-x11-dev",
            "libjpeg-dev"
        ]
        package_installer(required_packages, verbose)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}DEPENDENCIAS INSTALADAS CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

    except FileNotFoundError as e:
        print(f"{Colors.RED}[!] Error: Comando no encontrado: {e}{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}[!] Error inesperado: {e}{Colors.END}")
        sys.exit(1)

def extra_utilities(verbose):
    """Instala utilidades extra."""
    banner()

    print(f"\n{Colors.YELLOW}[*] INSTALANDO ALGUNAS UTILIDADES EXTRA...{Colors.END}\n")
    required_packages = [
        "xclip", "caja", "flameshot", "scrub", "brightnessctl"
    ]

    package_installer(required_packages, verbose)
    print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}UTILIDADES INSTALADAS CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
    time.sleep(1)

def fonts(verbose):
    """Instala Hack Nerd Fonts."""
    banner()

    print(f"\n{Colors.YELLOW}[*] INSTALANDO HACK NERD FONTS{Colors.END}")
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fonts_dir = os.path.join(script_dir, "Files")
        hack_zip = os.path.join(fonts_dir, "Hack.zip")

        # Descargar Hack Nerd Fonts
        print(f"\n{Colors.YELLOW}[*] DESCARGANDO HACK NERD FONTS{Colors.END}")
        if verbose == 1:
            wget_process = subprocess.run(["wget", "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.2/Hack.zip"], cwd=fonts_dir, capture_output=False, text=True, check=False)
        else:
            wget_process = subprocess.run(["wget", "-q", "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.2/Hack.zip"], cwd=fonts_dir, capture_output=True, text=True, check=False)
        status_code(wget_process)

        # Descomprimir y mover los archivos .ttf
        print(f"\n{Colors.YELLOW}[*] DESCOMPRIMIENDO HACK NERD FONTS{Colors.END}")
        unzip_process = subprocess.run(["unzip", "Hack.zip"], cwd=fonts_dir, capture_output=True, text=True, check=False)
        status_code(unzip_process)
        ttf_files = [f for f in os.listdir(fonts_dir) if f.endswith(".ttf")]
        for ttf_file in ttf_files:
            source = os.path.join(fonts_dir, ttf_file)
            dest = "/usr/local/share/fonts/"
            shutil.move(source, dest)

        # Eliminar archivos innecesarios
        print(f"\n{Colors.YELLOW}[*] LIMPIANDO ARCHIVOS{Colors.END}")
        os.remove(hack_zip)
        os.remove(os.path.join(fonts_dir,"LICENSE.md"))
        os.remove(os.path.join(fonts_dir, "readme.md"))
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}HACK NERD FONTS INSTALADAS CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        
        print(f"\n{Colors.YELLOW}[*] ACTUALIZANDO CACHÉ DE FUENTES...{Colors.END}")
        fc_cache_process = subprocess.run(["fc-cache", "-v"], capture_output=True, text=True, check=False)
        status_code(fc_cache_process)
        time.sleep(1)
        
    except FileNotFoundError as e:
        print(f"{Colors.RED}[!] Error: Comando no encontrado: {e}{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}[!] Error inesperado: {e}{Colors.END}")
        sys.exit(1)

def configs(verbose, interface_name):
    """Añade y configura Polybar, Picom e I3lock."""
    banner()

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        polybar_scripts_dir = os.path.join(script_dir, "EASY-PWM", "Files", "polybar", "scripts") #verificar directorio
        user_config_polybar = os.path.expanduser("~/.config/polybar")
        bin_dir = os.path.expanduser("~/.config/bin") #verificar directorio
        picom_config_path = os.path.join(script_dir, "Files", "picom.conf") #verificar directorio
        lock_script_dir = os.path.join(script_dir,"i3lock-color")

        print(f"\n{Colors.YELLOW}[*] AÑADIENDO Y CONFIGURANDO POLYBAR{Colors.END}")
        # Reemplazar USER en los scripts de Polybar
        for script_name in ["powermenu", "powermenu_alt"]:
            script_path = os.path.join(polybar_scripts_dir, script_name)
            with open(script_path, "r") as infile:
                script_content = infile.read()
            with open(script_path, "w") as outfile:
                outfile.write(script_content.replace("USER", os.getlogin()))

        # Copiar directorio polybar
        try:
            shutil.copytree(polybar_scripts_dir, user_config_polybar, dirs_exist_ok=True)  # Copia el directorio
            shutil.copytree(polybar_scripts_dir,user_config_polybar,dirs_exist_ok=True)
        except OSError as e:
            print(f"{Colors.RED}[!] Error al copiar archivos de Polybar: {e}{Colors.END}")
            sys.exit(1)

        #Damos permisos de ejecucion a los script de polybar
        launch_path = os.path.join(user_config_polybar, "launch.sh")
        try:
           subprocess.run(["chmod", "+x", launch_path], check=True)

        except Exception as e:
           print(f"{Colors.RED}[!] Error al dar permisos: {e}{Colors.END}")
           sys.exit(1)

        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}POLYBAR AÑADIDA Y CONFIGURADA CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] CONFIGURANDO PICOM{Colors.END}")
        picom_dest = os.path.expanduser("~/.config/picom/")
        os.makedirs(picom_dest, exist_ok=True)

        if os.path.exists(picom_config_path):
          shutil.copy(picom_config_path, picom_dest)
        else:
            print(f"{Colors.RED}[!] Error: No se encontró el archivo picom.conf.{Colors.END}")
            sys.exit(1)

        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}PICOM CONFIGURADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] ACTUALIZANDO EL SISTEMA{Colors.END}")
        time.sleep(1)

        if verbose == 1:
            update_process = subprocess.run(["sudo", "apt", "update"], capture_output=False, text=True, check=False)
        else:
            update_process = subprocess.run(["sudo", "apt", "update"], capture_output=True, text=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        status_code(update_process)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}SISTEMA ACTUALIZADO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] INSTALANDO I3LOCK Y PAQUETES NECESARIOS PARA I3LOCK-COLOR...{Colors.END}\n")
        required_packages = [
            "libpam0g-dev", "libxrandr-dev", "libfreetype6-dev", "libxft-dev", "i3lock",
            "autoconf", "gcc", "make", "pkg-config", "libcairo2-dev", "libfontconfig1-dev",
            "libxcb-composite0-dev", "libev-dev", "libx11-xcb-dev", "libxcb-xkb-dev",
            "libxcb-xinerama0-dev", "libxcb-randr0-dev", "libxcb-image0-dev",
            "libxcb-util0-dev", "libxcb-xrm-dev", "libxcb-xtest0-dev", "libxkbcommon-dev",
            "libxkbcommon-x11-dev", "libjpeg-dev"
        ]

        package_installer(required_packages, verbose)
        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}I3LOCK Y DEPENDENCIAS INSTALADAS CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)
    except Exception as e:
        print(f"{Colors.RED}[!] Errores en el codigo de configuracion", e , Colors.END)
        sys.exit(1)


def zsh_config(verbose):
    """Configura Zsh."""
    banner()
    try:

        username= os.getlogin()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"\n{Colors.YELLOW}[*] Sincronizando  zshrc para root{Colors.END}")
        sudo_source_process = subprocess.run(["sudo", "ln", "-s", "-f", f"/home/{username}/.zshrc", "/root/.zshrc"], capture_output=False, text=True, check=False)
        status_code(sudo_source_process)

        print(f"\n{Colors.YELLOW}[*] CLONANDO Y AÑADIENDO POWERLEVEL10K PARA EL USUARIO {Colors.GRAY}{username}{Colors.END}")
        powerlevel10k_destination_user = os.path.expanduser("~/powerlevel10k")
        git_user_process = subprocess.run(["git", "clone", "--depth=1", "https://github.com/romkatv/powerlevel10k.git", powerlevel10k_destination_user], capture_output=True, text=True, check=False)

        if git_user_process.returncode == 0:
            status_code(git_user_process)
            with open(os.path.expanduser("~/.zshrc"),"a") as outfile:
                 outfile.write('\nsource ~/powerlevel10k/powerlevel10k.zsh-theme')
        else:
            print(f"Error al instalar POWERLEVEL10K con error: {git_user_process.stderr}")
            sys.exit(1)

        print(f"\n{Colors.YELLOW}[*] CLONANDO Y AÑADIENDO POWERLEVEL10K PARA EL USUARIO root{Colors.END}")
        powerlevel10k_destination_root = "/root/powerlevel10k"
        git_root_process = subprocess.run(["sudo", "git", "clone", "--depth=1", "https://github.com/romkatv/powerlevel10k.git", powerlevel10k_destination_root], capture_output=True, text=True, check=False)

        if git_root_process.returncode == 0:
            status_code(git_root_process)
        else:
           print(f"Error al instalar POWERLEVEL10K con error: {git_root_process.stderr}")
           sys.exit(1)

        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}POWELEVEL10K INSTALADO Y AÑADIDO CORRECTAMENTE PARA LOS DOS USUARIOS {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] AÑADIENDO BAT Y LSD A LA ZSH{Colors.END}")
        batlsd = ["bat","lsd"]
        package_installer(batlsd, verbose)

        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}BAT Y LSD INSTALADO Y AÑADIDO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[*] AÑADIENDO PLUGIN DE SUDO A LA ZSH{Colors.END}")
        pluginszsh_dir = "/usr/share/zsh-plugins"
        sudo_pluginzsh_file = os.path.join(script_dir, "Files", "sudo.plugin.zsh") #verificar directorio

        os.makedirs(pluginszsh_dir, exist_ok=True)

        try:
          shutil.copy(sudo_pluginzsh_file,pluginszsh_dir)
        except Exception as e:
           print(f"{Colors.RED}[!] Faltan archivos de instalacion en el directorio file: {e}{Colors.END}")
           sys.exit(1)

        zshadds_file = os.path.join(script_dir,"Files","zsh-adds")
        if os.path.exists(zshadds_file):

          with open(zshadds_file,"r") as infile, open(os.path.expanduser("~/.zshrc"),"a") as outfile:
             text = infile.read()
             outfile.write(text)

          """Modifica Los permisos y cambio de propietario de archivos y directorios"""
          chown1_process = subprocess.run(["sudo", "chown", f"{username}:{username}", pluginszsh_dir], capture_output=True, text=True, check=False)
          status_code(chown1_process)
          sudo_pluginzsh_file= os.path.join(pluginszsh_dir,"sudo.plugin.zsh")
          chown2_process = subprocess.run(["sudo", "chown", f"{username}:{username}", sudo_pluginzsh_file], capture_output=True, text=True, check=False)
          status_code(chown2_process)

        else:
           print("No se encontro el directorio zsh-adds")
           sys.exit(1)

        print(f"\n{Colors.TURQUOISE}█ {Colors.GRAY}PLUGIN DE SUDO AÑADIDO CORRECTAMENTE {Colors.TURQUOISE}█{Colors.END}")
        time.sleep(1)
    except Exception as e:
          print(f"\n{Colors.RED}[!] Ocurrio un error Inesperado", e , Colors.END)
          sys.exit(1)

def change_session():
  """Cierra la sesión actual para iniciar la nueva configuración."""
  confirmation = input(f"\n\t\t{Colors.PURPLE}█ {Colors.GRAY}¿DESEA CERRAR ESTA SESIÓN PARA INICIAR LA NUEVA CONFIGURACIÓN? [Y/N]{Colors.PURPLE} █> {Colors.END}").lower()
  if confirmation == "y":
    print(f"\n{Colors.RED}█ CERRANDO SESIÓN - INICIE SESIÓN EN BSPWM COMO EL USUARIO {os.getlogin()} = {Colors.END}")
    time.sleep(5)
    subprocess.run(["kill", "-9", "-1"])  # Fuerza el cierre de sesión (esto puede tener consecuencias)
    sys.exit(0)  # Salir después de la confirmación.
  else:
    print(f"\n{Colors.YELLOW}[!] No se cerrará la sesión actual.{Colors.END}")

if __name__ == "__main__":
    # Configura el manejo de la señal SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, ctrl_c_handler)

    parser = argparse.ArgumentParser(description="Script de instalacion con funcionalidades.")
    parser.add_argument("-v", "--verbose", type=int, choices=[0, 1], help="Agregar verbose (1: si, 0: no)")
    parser.add_argument("-h", "--help", action="help", help="Muestra este panel de ayuda")

    args = parser.parse_args()

    if args.verbose is None:
        help_panel()
    else:
        verbose = args.verbose
        banner()
        print(f"Verbose mode: {verbose}")
        check_user()
        check_internet()
        interface_name = iface()
        print(f"Interfaz seleccionada: {interface_name}")

        dependencies(verbose)
        kitty_config()
        bspwm_sxhkd(verbose)
        Polybar(verbose)
        picom_rofi(verbose)
        feh_ilock(verbose)
        extra_utilities(verbose)
        fonts(verbose)
        configs(verbose, interface_name)
        zsh_config(verbose)
        #banner2()  #TODO: Implentar banner2
        change_session() # TODO: Implentar change_session