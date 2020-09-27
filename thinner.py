"""
*** BIBTEX THINNER 1.0 ***
This simple programs reduces the number of entries present in a .bib file by only keeping
the ones used in a target .tex file.
Example usage:
> thinner.py my_latex_file.tex my_bibliography.bib
the output will be stored in a new file located in the same folder with the prefix "THINNED_"
"""

# Importing required librairies (use pip install if you don't have them yet)
import regex as re
import sys

# getting target files from command line arguments
latex_file = open(str(sys.argv[1]), "r")
bibtex_file = open(str(sys.argv[2]), "r")

# initialising variables to find occurences of citations and where to store them
CITE_STYLES = ["cite","parencite","citep","citet"]
HEAD_REGEX = "(?<="
TAIL_REGEX = "(\[.*\])?\{)(.*?)(?=\})"
get_entries = re.compile("(?<=@.*\{)(.*?)(?=\,)")

citations_found = []
entries_to_keep = ""
recording = False

###################

def output_results():
  output = open("THINNED_"+str(sys.argv[1]), "w")
  output.write(entries_to_keep)
  output.close()
  print("Done! Output file saved in current folder as '"+"THINNED_"+str(sys.argv[1])+"'")

def update_full_entries(a_string):
  global entries_to_keep
  entries_to_keep += a_string

def process_bibliography_file():
  citations_found.sort()
  print("- Info: currently looking for the following patterns:",str(CITE_STYLES),
  "(feel free to add new ones if you need to)")
  print("- Number of entries to keep:",len(citations_found))
  for line in bibtex_file:
    m = get_entries.findall(line)
    if m and m[0] in citations_found:
      recording = True
    elif line.startswith("@"):
      recording = False
    if recording == True:
      update_full_entries(line)
  output_results()

def process_citations(a_list):
  for v in a_list:
    if "," in v:
      all_elements = v.split(",")
      [update_findings(e) for e in all_elements]
    else:
      update_findings(v)

def update_findings(a_string):
  if a_string not in citations_found:
    citations_found.append(a_string)

def main():
  for line in latex_file:
    for citing in CITE_STYLES:
      compiled_regex = re.compile(HEAD_REGEX+citing+TAIL_REGEX)
      m = compiled_regex.findall(line)
      if m:
        result = []
        [result.append(r[1]) for r in m]
        process_citations(result)
  process_bibliography_file()

if __name__ == '__main__':
  main()
