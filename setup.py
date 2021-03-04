import pip

_all_ = [
        "ezdxf == 0.15.1",
        "imutils == 0.5.4",
        "matplotlib == 3.0.3",
        "natsort == 7.1.1",
        "opencv-python == 4.5.1.48",
        "pillow == 8.1.0",
        "pyinstaller == 4.2"
        ]


def install(packages):
    for package in packages:
        pip.main(['install', package])

if __name__ == '__main__':
    import platform
    import subprocess

    print("Starting the installation")
    install(_all_) 
    if "arch" in platform.release():
        print("The OS is detected to be ArchLinux")
        # An extra step is required for ArchLinux as PyInstaller
        # doesn't work on ArchLinux as intended in some cases as
        # mentioned in this issue here:
        # https://github.com/pyinstaller/pyinstaller/issues/5540
        # A workaround is provided in a bash script
        subprocess.call(['sh', './arch_pyinstaller.sh'])
    print("The requirements are installed\n" +
            "Generating an executable file...")
    #go_to_dxf2png_dir = subprocess.Popen(["cd", "dxf2png"], shell = True)
    #print(go_to_dxf2png_dir.returncode)
    exe_generation = subprocess.run(["pyinstaller", "-F", "-w",
        "--paths", "./../venv/lib/python3.8/site-packages/",
        "--exclude-module", "tkinter",
        "--onefile", "-n", "dxf2png",
        "dxf2png/main.py"])
    print(exe_generation.returncode)
    print("Installation successful")
