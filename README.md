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
### DXF to PNG
This program converts DXF files to PNG image format.

#### Usage of the command-line interface (CLI)
One may run the application in CLI as follows:
```bash
python main.py -i input.dxf -o output.png
```
or
```bash
python main.py --input input.dxf --output output.png
```
Both input and output files are set relative to the script's root directory, i.e. should be located in the same directory.

#### Setup with Virtualenv
* Create a virtual environment: `virtualenv -p /usr/bin/python3 cad-mixer`
* Activate the environment: `source cad-mixer/bin/activate`
* Install the requirements (PIP is required): `pip install -r requirements.txt`
* Go to the dxf2png folder: `cd dxf2png`
* Run the probram: `python main.py`
* Deactivate the environment when done: `deactivate`

#### Setup with Anaconda
This assumes that you have the Conda package installed.
* Create a virtual environment: `conda env create --name cad-mixer -f environment.yml`
* Activate the environment: `conda activate cad-mixer`
* Go to the dxf2png folder: `cd dxf2png`
* Run the program: `python main.py`
* Deactivate the environment when done: `conda deactivate`
