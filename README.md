# CAD-Mixer
CAD Mixer is a simple cad file converter licensed under MIT!

## Project Management
We are using Github Projects as a Kanban Board + Github Issues tracker. Since we are working on this on the side the release will be sporadic for a while until things stabilize.

## Code of Conduct
Please read the code of conduct before participating on the project so that we are all on the same page!

## Contributing
If you notice a bug or you want to propose a new feature please fill up a issue!
If you want to contribute to the project please join our discord server and let us know what you want to work on!

To add a contribution make a fork of the project, notify which issue you are working on and then when ready make a Pull Request.

## Communication
The communication for this project happens on our [CAD Mixer Community Discord Server](https://discord.gg/3ErkNJZmsa) you can join by clicking on this invite: https://discord.gg/3ErkNJZmsa

## CI/CD
We use Github Actions to triggers some continuous integration steps. So far we have the following:
- Linting with flake8
- Run tests with pytest

It's important to add the proper tests when you create a new functionality to have sufficient coverage. We might also change testing framework if we happen to move from python to C++. However at the time of writing dxf2png main function is in python!

## Available converters

### STEP to STL
This program converts STEP files to STL files.

This project includes the [PythonOCC](https://github.com/tpaviot/pythonocc-core) CAD converter from STEP to STL file format.

STEP is the most popular file format defined by the [ISO 10303-21](https://www.iso.org/standard/63141.html) standard.

#### Usage of the command-line interface (CLI)
One may run the application in CLI as follows:
```bash
python main.py -i input.stp -o output.stl
```
or
```bash
python main.py --input input.dxf --output output.png
```
Both input and output files are set relative to the script's root directory, i.e. should be located in the same directory.

#### Manual installation
Since PythonOCC used for convertion is not available with pip, the installation requires [conda](https://anaconda.org/) installed.

##### Prepare a virtual environment
* Create a virtual environment: `conda create -n cad-mixer`
* Activate the environment: `conda activate cad-mixer`
* Install PythonOCC: `conda install -c dlr-sc pythonocc-core=7.4.0`
* Deactivate the environment when done: `conda deactivate`

##### Building the binary executable
This assumes that the dependencies were installed with conda in a virtual environment. It also requires PyInstaller instelled `pip install pyinstaller`.

* Go to the stp2stl folder (if not there already): `cd stp2stl`
* Run the installation: `pyinstaller --onefile --windowed main.py`

### DXF to PNG
This program converts DXF files to PNG image format.

#### Usage of the CLI
One may run the application in CLI as follows:
```bash
python main.py -i input.dxf -o output.png
```
or
```bash
python main.py --input input.dxf --output output.png
```
Both input and output files are set relative to the script's root directory, i.e. should be located in the same directory.

#### Automatic installation
* Create a virtual environment: `virtualenv -p /usr/bin/python3 venv`
* Activate the environment: `source venv/bin/activate`
* Run the atomatic installer: `python setup.py`
* Deactivate the environment when done: `deactivate`

The resulting executable file is placed to the `dist` folder at the same path as `main.py`. It can be used as follows:
```sh
cd dist
./dxf2png -i input_file.dxf -o output_file.png
```

#### Manual installation

##### Prepare a virtual environment
* Create a virtual environment: `virtualenv -p /usr/bin/python3 venv`
* Activate the environment: `source venv/bin/activate`
* Install the requirements (PIP is required): `pip install -r requirements.txt`
* Deactivate the environment when done: `deactivate`

##### Building the binary executable
This assumes that the dependencies were installed with PIP in a virtual environment (see the **Setup with Virtualenv** section). Conda handles dependencies in a trickier way and this might not work.

* Go to the dxf2png folder (if not there already): `cd dxf2png`
* Run the installation: `pyinstaller -F -w --paths "./../venv/lib/python3.8/site-packages/" --exclude-module tkinter --onefile -n dxf2png main.py`
