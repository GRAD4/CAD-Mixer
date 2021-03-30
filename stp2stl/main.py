"""
Copyright (c) 2021 Nikita Letov (letovnn@gmail.com)
Distributed under the MIT software license, see the accompanying
file COPYING or http://www.opensource.org/licenses/mit-license.php.

This script converts STEP files to STL file.
Usage:
    python main.py -i input.dxf -o output.png
or
    python main.py --input input.dxf --output output.png

For more info see the PythonOCC Tutorial:
https://pythonocc-doc.readthedocs.io/en/latest/convert/
"""
import os 
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
from OCC.Core.StlAPI import StlAPI_Writer
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
from OCC.Core.IGESControl import IGESControl_Reader
from optparse import OptionParser

"""
Converts STEP to STL file format.

Example:
step_to_stl("input.stp", "output.stl")
"""
def step_to_stl(input_filename, # input STEP (AP203/AP214 file) path
                output_filename,   # output STL file path
                definition = 0.1 # accuracy of conversion
                ): 
    if definition <= 0:
        raise ValueError('The conversion definition should be a positive number')
    if not os.path.exists(input_filename):
        raise ValueError('File does not exist')
    # Checking the file extensions
    input_extension = os.path.splitext(input_filename)[1]
    input_extension = input_extension.lower()
    if not input_extension in [".stp", ".step"]:
        raise ValueError('Incorrect input file format. The input file must be STEP (or STP)')
    output_extension = os.path.splitext(output_filename)[1]
    output_extension = output_extension.lower()
    if output_extension != ".stl":
        raise ValueError('Incorrect output file format. The output file must be STL')

    # Reading the file
    step_reader = STEPControl_Reader()
    status = step_reader.ReadFile(input_filename)
    if status == IFSelect_RetDone:
        failsonly = False
        step_reader.PrintCheckLoad(failsonly, IFSelect_ItemsByEntity)
        step_reader.PrintCheckTransfer(failsonly, IFSelect_ItemsByEntity) 
        ok = step_reader.TransferRoot(1)
        _nbs = step_reader.NbShapes()
        myshape = step_reader.Shape(1)
        print("File readed")
    else:
        # In case the file is corrupted or the error is unknown
        raise ValueError('Cannot read the file. It could be corrupted.')
    # Export to STL    
    directory = os.path.split(__name__)[0]
    stl_output_dir = os.path.abspath(directory)
    assert os.path.isdir(stl_output_dir)
    stl_file = os.path.join(stl_output_dir, output_filename)
    stl_writer = StlAPI_Writer()
    stl_writer.SetASCIIMode(False)
    mesh = BRepMesh_IncrementalMesh(myshape, definition)
    mesh.Perform()
    assert mesh.IsDone()
    stl_writer.Write(myshape, stl_file)
    assert os.path.isfile(stl_file)
    print("Written")

if __name__ == '__main__':
    # Setting up the parcer
    parser = OptionParser()
    parser.add_option("-i", "--input", dest = "input_filename",
                      help = "Input STEP file name")
    parser.add_option("-o", "--output", dest = "output_filename",
                      help = "Output stl file name")
    (options, args) = parser.parse_args()
    input_filename = str(options.input_filename)
    output_filename = str(options.output_filename)
    step_to_stl(input_filename, output_filename)
