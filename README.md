      
# BSPWM_PYTHON

Este proyecto es un script de instalación para automatizar la configuración de un entorno Linux, diseñado principalmente para Parrot OS y Kali Linux. Originalmente escrito en Bash, ha sido portado a Python para mejorar su fluidez, robustez y seguridad.

## Descripción

BSPWM_PYTHON automatiza la instalación y configuración de un entorno BSPWM (Binary Space Partitioning Window Manager) con Polybar, Picom, Rofi y otras utilidades. El objetivo es proporcionar una configuración inicial funcional y personalizable para usuarios que buscan un entorno de escritorio ligero y eficiente.

## Características

*   **Instalación automatizada:** Simplifica el proceso de instalación de BSPWM, SXHKD, Polybar, Picom y otras utilidades.
*   **Configuración predefinida:** Proporciona una configuración inicial funcional con atajos de teclado y temas predefinidos.
*   **Personalización:** Permite a los usuarios personalizar la instalación y la configuración según sus preferencias.
*   **Soporte para Parrot OS y Kali Linux:** Detecta automáticamente el sistema operativo y adapta la instalación en consecuencia.
*   **Código Python:** Migrado de Bash a Python para mejorar la legibilidad, mantenibilidad y seguridad.
*   **Verbose Mode:** Permite ver el detalle de lo que está pasando en la instalación.

## Dependencias

El script requiere las siguientes dependencias:

*   Python 3.10 o superior
*   `argparse`
*   `os`
*   `sys`
*   `time`
*   `signal`
*   `subprocess`
*   `platform`
*   `shutil`
*   `apt` (para instalar paquetes del sistema)
*   `git` (para clonar repositorios)

## Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd BSPWM_PYTHON
    ```

2.  **Ejecutar el script:**
    ```bash
    sudo python3 install.py -v [1/0]
    ```
    *   `-v 1`: Ejecutar en modo verbose (muestra todos los comandos y la salida).
    *   `-v 0`: Ejecutar en modo silencioso (no muestra la salida de los comandos).
    *   `-h`: Mostrar el panel de ayuda.

## Estructura del proyecto

    

IGNORE_WHEN_COPYING_START
Use code with caution.Markdown
IGNORE_WHEN_COPYING_END

BSPWM_PYTHON/
├── install.py # Script principal de instalación en Python
├── Files/
│ ├── bspwmrc # Archivo de configuración de BSPWM
│ ├── sxhkdrc # Archivo de configuración de SXHKD
│ ├── bspwm_resize # Script para redimensionar ventanas
│ ├── kitty/ # Configuración de Kitty
│ │ ├── kitty.conf
│ │ └── color.ini
│ ├── polybar/ # Configuración de Polybar
│ │ ├── ...
│ ├── picom.conf # Archivo de configuración de Picom
│ ├── bin/ # Scripts adicionales
│ │ ├── ethernet_status.sh
│ │ ├── hackthebox_status.sh
│ │ └── target_ip.sh
│ ├── i3lock-color/ # Scripts y configuraciones para i3lock-color
│ │ └── examples/
│ │ └── lock.sh
│ ├── zsh-adds # Configuraciones adicionales para Zsh
│ └── sudo.plugin.zsh #Plugin para el autocompletado de sudo en zsh
├── EASY-PWM/ #Ajuste del directorio que por error se crea doble
│ └──Files
│ └──Wallapaper.jpg # Imagen de fondo de escritorio
├── README.md # Este archivo
└── ...

      
## Configuración

La mayoría de las opciones de configuración se encuentran en los archivos dentro del directorio `Files/`. Puedes editar estos archivos para personalizar el entorno a tu gusto.

## Próximos pasos

*   Implementar `banner2` con el comando system para ver si es necesario eliminarlo.
*   Implementar Change sesion con kill (validar seguridad)
*   Implementar Tests
*   Completar la conversión de las funciones restantes y revisar el código en general.
*   Añadir tests unitarios
*   Creación de un archivo de configuración en formato YAML o JSON.

## Contribución

¡Las contribuciones son bienvenidas! Si encuentras algún error, tienes alguna sugerencia o quieres añadir alguna nueva funcionalidad, por favor, abre un "issue" o envía un "pull request".

## Créditos

Este proyecto está inspirado en la configuración BSPWM de [s4vitar](https://www.youtube.com/s4vitar).

    