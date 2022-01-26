import re     
from itertools import product
from sys       import exit
from os        import walk
from pathlib   import Path

class medianString:

    def __init__(self) -> None:
        self.getFiles()

    ALPHABET      = ['A','C','T','G']
    DNA_LIST      = []
    INPUT_FILES   = []
    KMER_LIST     = []

    BEST_KMER     = ""
    BEST_KMER_D   = 101
    K             = 0

    # Finds input files from the current directory
    def getFiles(self):
        # Gets the path of the current directory
        myPath = Path(__file__).parent.resolve() 

        # Loop through files in the given directory 'myPath'
        for file in next(walk(myPath), (None, None, []))[2]:
            # Will grab all text input files that have the naming convention
            if re.search("^input_.*.txt$",file): 
                self.INPUT_FILES.append(file)
 
    def fillKmerList(self,k):
        for kmer in product(self.ALPHABET, repeat = k):
            self.KMER_LIST.append(kmer)

    def distance(self,kmer):
        distance = 0

        for dna in self.DNA_LIST:
            if len(dna) == len(kmer):
                for i,char in enumerate(dna):
                    if char != kmer[i]:
                        distance += 1

        return distance
        

    def median(self,myFile):
        # Refresh class lists for each incoming file
        self.DNA_LIST.clear() 
        self.KMER_LIST.clear() 

        # Fill the DNA_LIST class variable with DNA from a given input file
        try: 
            with open(myFile,"r",encoding='utf-8',errors='ignore') as file:
                lines = file.readlines()
                self.K = int(re.split('[\s\n]',lines[0])[0])# Gets 'K' from the file
                # Splits up the DNA from the input file into an array then loops over it saving each strand as a list to the class variable DNA_LIST
                for dna in re.split('[\s\n]',lines[1]):
                    self.DNA_LIST.append(list(dna))
        except OSError:
            print("Could not open file " + myFile + ".")
            exit()

        self.fillKmerList(self.K)

        for kmer in self.KMER_LIST:
            if self.distance(kmer) < self.BEST_KMER_D:
                self.BEST_KMER = kmer
                self.BEST_KMER_D = self.distance(kmer)

        return ''.join(map(str, self.BEST_KMER)) # Will return a string instead of a tuple

    def run(self):
        for file in self.INPUT_FILES:
            print(file + " produced a best-k-mer of")
            print(self.median(file))


program = medianString()
program.run()