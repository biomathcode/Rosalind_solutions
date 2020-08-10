##Conda install biopython
## pip install biopython

from Bio.Seq import Seq
def parser(file_name):
    seq = ''
    bases = [ "A", "C", "G", "T"]
    output = ''
    with open(file_name) as f:
        print(f)
        seq += f.readlines()[0]
        for base in bases:
            output += str(seq.count(base)) + " "
    return output    

def submission_write(output):
    with open('submission.txt', 'w') as f:
        print(output, file=f)

if __name__ == "__main__":
    file_name = "docs/" + input("write the file_name here :- ")
    counter = parser(file_name)
    submission_write(counter)
