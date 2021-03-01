# PGEN
PGEN is a fast project generator in your terminal
# Installation
You can download the pre built binaries here or use pyinstaller to build this repo to an executable file
``` bash
pyinstaller --name pgen --noconfirm --onedir --console --add-data "C:/Users/josti/Desktop/Projects/projectGeneratorCLI/src/generator;generator/"  "C:/Users/josti/Desktop/Projects/projectGeneratorCLI/src/main.py"
```
add the executable file to path so you can use it anywhere in your system
# Usage
### Example 
This command will create a new python project 
``` bash
pgen --fp /path/to/your/folder -l python
```
You can read the documentation to get more indepth with the cli argumentents, adding and editing generator file
**I am still working in the documentation**
