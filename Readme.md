# PDF Concatenator

Hey there,

I created this project for a university course and also a little bit as a coding and design exercise.

### Problem Setting
During the course all participants analyzed a scientific paper every three weeks. They were required to hand in answers to specific questions on the paper within two weeks. The lecturer then published all these answers as PDF files so that the participants could discuss their answers during the third week.

### What the Program Does
This program concatenates PDF files and adds a bookmark with each file. The bookmark is supposed to have the author's name or some other distinctive content so that readers of the concatenated file can navigate within this long document easily. As the participants had to name their answer files following a certain pattern that also included their name, the program just tries to extract the author's name from the file name.

### This Project's Structure
You can find the software design, i.e. some pseudo code describing the program's work flow in the file [SoftwareDesign.md](SoftwareDesign.md). Besides that there is just some python code that is all being called in [Main.py](Main.py).
