import regex as re
latex_file = open("2_background.tex", "r")
bibtex_file = open("bibliography.bib", "r")
cite_styles = ["cite","parencite"]
head_regex = "(?<="
tail_regex = "\{)(.*?)(?=\})"
citations_found = []

####

get_entries = re.compile("(?<=@.*\{)(.*?)(?=\,)")
entries_to_keep = ""
recording = False

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
  for citing in cite_styles:
    compiled_regex = re.compile(head_regex+citing+tail_regex)
    for line in latex_file:
      m = compiled_regex.findall(line)
      if m:
        process_citations(m)

if __name__ == '__main__':
  main()

citations_found.sort()
print("Citations to look for:",citations_found)

print(">>>",entries_to_keep)

def update_full_entries(a_string):
  global entries_to_keep
  entries_to_keep += a_string

def process_bibliography_file():
  for line in bibtex_file:
    m = get_entries.findall(line)
    if m and m[0] in citations_found:
      # print(m[0],line)
      recording = True
    elif line.startswith("@"):
      recording = False
    if recording == True:
      update_full_entries(line)

process_bibliography_file()
print("Full found entries:",entries_to_keep)
