import pip

_all_ = [
        "ezdxf == 0.15.1",
        "imutils == 0.5.4",
        "natsort == 7.1.1",
        "opencv-python == 4.5.1.48",
        "pillow == 8.1.0",
        "pyinstaller == 4.2"
        ]

linux = ["matplotlib == 3.0.3"] # doesn't work with later versions on Linux
				# because it begins to require Qt (too bad)

darwin = ["matplotlib == 3.3.4"] # there is no 3,0.3 for macOS

def install(packages):
    for package in packages:
        pip.main(['install', package])

if __name__ == '__main__':
    import platform
    import subprocess

    print("Starting the installation")
    install(_all_)
    current_os = platform.system()
    if current_os == "Linux":
        install(linux)
        if "arch" in platform.release(): # ArchLinux
            print("The OS is detected to be ArchLinux")
  	    # An extra step is required for ArchLinux as PyInstaller
  	    # doesn't work on ArchLinux as intended in some cases as	
	    # as mentioned in this issue here:
      	    # https://github.com/pyinstaller/pyinstaller/issues/5540
            # A workaround is provided in a bash script
            subprocess.call(['sh', './arch_pyinstaller.sh'])
    if platform.system() == "Darwin": #macOS
        install(darwin)
    print("The requirements are installed\n" +
            "Generating an executable file...")
    exe_generation = subprocess.run(["pyinstaller", "-F", "-w",
        "--paths", "./../venv/lib/python3.8/site-packages/",
        "--exclude-module", "tkinter",
        "--onefile", "-n", "dxf2png",
        "dxf2png/main.py"])
    print("Program exited with the return code: "
          + str(exe_generation.returncode))
    print("Installation successful")
