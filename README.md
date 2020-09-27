# Bibtex Thinner

Small Python 3 script that shortens a bibtex file depending on the citations used in a target .tex file.

## Installation
You need to have [Python 3](https://www.python.org/downloads/) installed for this script to work.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the regex module if needs be.

```bash
pip install regex
```

## Usage
From the command line, launch the program using python then add your .tex file as a first argument and your .bib file as your second argument, like so:
```bash
python thinner.py a_latex_file.tex a_bibliography.bib
```
The output will be a file with the prefix "THINNED_" located in the same folder than your input files.

### Notes
please refer to the code to see which citing commands are supported. For now the "cite","parencite","citep","citet" are parsed. If you wish to process more commands, simply add them to the list of strings in the "CITE_STYLES" variable.

## License
[MIT](https://choosealicense.com/licenses/mit/)
