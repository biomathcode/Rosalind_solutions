## GenBank introduction
from Bio import Entrez


def GenBank(genus, dtstart, dtend):
    Entrez.email = 'sharma.pratik2016@gmail.com'
    term = '%s[Organism] AND (%s[Publication Date]: %s[Publication Date])' %(genus, dtstart, dtend)
    handle = Entrez.esearch(db="nucleotide", term=term)
    record = Entrez.read(handle)
    return record['Count']

def parser_file(file_name):
    with open(file_name) as f:
        line = f.read().splitlines()
        print(line)
        genus = line[0]
        dtstart = line[1]
        dtend = line[2]
        print(genus, dtstart, dtend)
    return genus, dtstart, dtend

if __name__ == "__main__":
    file_name = "docs/" + input("write the file_name here :- ")
    genus, dtstart, dtend = parser_file(file_name)
    print(GenBank("Anthoxanthum", "2003/7/25", "2005/12/27"))
    print(GenBank(genus, dtstart, dtend))





