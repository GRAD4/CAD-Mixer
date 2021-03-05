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
    import sys

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
        print("The OS is detected to be macOS")
        install(darwin)
    print("The requirements are installed\n" +
            "Generating an executable file...")
    python_ver = str(sys.version_info.major) + "." + str(sys.version_info.major)
    exe_generation = subprocess.run(["pyinstaller", "-F", "-w",
        "--paths",
        "./../venv/lib/python" + python_ver + "/site-packages/",
        "--exclude-module", "tkinter",
        "--onefile", "-n", "dxf2png",
        "dxf2png/main.py"])
    return_code = exe_generation.returncode
    if return_code == 0:
        print("Installation successful")
    if return_code == 1:
        print("There were errors during the installation")
    sys.exit(return_code)
