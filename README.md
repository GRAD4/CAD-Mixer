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

## Available converters
### DXF to PNG
This program converts DXF files to PNG image format.

#### Usage of the command-line interface (CLI)
One may run the CLI version of the application as follows:
```bash
python main.py --cli -i input.dxf -o output.png
```
or
```bash
python main.py --cli --input input.dxf --output output.png
```
Both input and output files are set relative to the script's root directory, i.e. should be located in the same directory.

#### Setup with Anaconda
This assumes that you have the Conda package installed.
* Create a virtual environment: `conda env create --name cad-mixer -f environment.yml`
* Activate the environment: `conda activate cad-mixer`
* Go to the dxf2png folder: `cd dxf2png`
* Run the program: `python main.py`
* Deactivate the environment when done: `conda deactivate`
