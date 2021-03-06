"""
This script concatenates all PDF files in a given folder.
"""

import pathlib
import os

import PyPDF2

import HelperClasses

# Path to directory that contains the PDF documents with our answers
working_directory = pathlib.Path(
    'd:/Studium_ForestInformationTechnology/Scientific_Internet_Colloquium/'
    'Assignment_4/colleagues_evaluations/other_group/'
)

if not working_directory.exists():
    print("Error: The folder with the PDF documents could not be found!")
    exit(code=1)

output_file_name = 'SIC_04_group_01_all_answers.pdf'
output_file_path = working_directory / output_file_name

# Delete an existing PDF collection with the same name
if pathlib.Path(output_file_path).exists():
    os.remove(output_file_path)

# Get paths to all PDF files in the working directory
pdf_file_paths = working_directory.glob('*.pdf')

my_PDF_merger = PyPDF2.PdfFileMerger()

# Append all files to the merger object
for file_path_obj in pdf_file_paths:
    my_PDF_merger.append(
        str(file_path_obj),
        bookmark=HelperClasses.SICFileName(file_path_obj).extract_header()
    )

# Write the collection PDF to a file
my_PDF_merger.write(str(output_file_path))
