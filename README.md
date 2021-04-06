<h1 align="center"><b>CAD-Mixer</b></h1>
  
<p align="center">
    <a href="https://github.com/GRAD4/CAD-Mixer/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/GRAD4/CAD-Mixer" /></a>
    <a href="https://github.com/GRAD4/CAD-Mixer/blob/main/LICENSE" alt="License">
        <img src="https://img.shields.io/github/license/GRAD4/CAD-Mixer" /></a>
    <a href="https://github.com/GRAD4/CAD-Mixer/issues" alt="Issues">
        <img src="https://img.shields.io/github/issues/GRAD4/CAD-Mixer" /></a>
    <! -- Widget setting need to be enabled to show discord info, see here: https://vimeo.com/364220040 -->
    <a href="https://discord.gg/xgkuw5x6">
        <img src="https://img.shields.io/discord/801140631262068747?logo=discord"
            alt="chat on Discord"></a>
</p>

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
