import re     
from itertools import product
from sys       import exit
from os        import walk
from pathlib   import Path

class medianString:

    def __init__(self) -> None:
        self.getFiles()

    ALPHABET      = ['A','C','G','T']
    DNA_LIST      = []
    INPUT_FILES   = []
    KMER_LIST     = []

    BEST_KMER     = ""
    BEST_KMER_D   = [0]
    K             = 0

    # Finds input files from the current directory
    def getFiles(self):
        # Gets the path of the current directory
        myPath = Path(__file__).parent.resolve() 
        # Loop through files in the given directory 'myPath'
        for file in next(walk(myPath), (None, None, []))[2]:
            # Will grab all text input files that have the naming convention input_*.txt where * = to a number
            # This assumes input files have the correct file structure
            if re.search("^input_.*.txt$",file): 
                self.INPUT_FILES.append(file)
 
    def fillKmerList(self,k):
        for kmer in product(self.ALPHABET, repeat = k):
            self.KMER_LIST.append(''.join(kmer))

    def fillDNAList(self,myFile):
        # Refresh class lists for each incoming file
        self.DNA_LIST.clear() 
        self.KMER_LIST.clear() 
        self.BEST_KMER = ""

        # Fill the DNA_LIST class variable with DNA from a given input file
        try: 
            with open(myFile,"r",encoding='utf-8',errors='ignore') as file:
                lines = file.readlines()
                self.K = int(re.split('[\s\n]',lines[0])[0]) # Gets 'K' from the file
                # Splits up the DNA from the input file into an array then loops over it saving each strand as a list to the class variable DNA_LIST
                for dna in re.split('[\s\n]',lines[1]):
                    self.DNA_LIST.append(dna)
                # Initializes the best kmer distance as the largest possible distance
                self.BEST_KMER_D[0] = (self.K * len(self.DNA_LIST) * len(self.DNA_LIST[0]))
        except OSError:
            print("Could not open file " + myFile + ".")
            exit()
        # Initialize kmer list
        self.fillKmerList(self.K)


    def distance(self,kmer,dna):
        distance    = 0
        maxLength   = len(dna) - len(kmer) + 1
        temp        = [] # Temp array that will hold the distances between the kmer and dna strand
        for i in range(maxLength):
            for j in range(len(kmer)):
                if dna[i:i+len(kmer)][j] != kmer[j]:
                    distance+=1
            # Add the distance to the temp array and refresh the distance var for the next strand of dna
            temp.append(distance)
            distance = 0 
        return temp

    def median(self,kmer):
        kmerDis        = []
        totalDistance  = 0 
        for dna in self.DNA_LIST:
            kmerDis = self.distance(kmer,dna)
            # Sort the array to get its minimum value then add that to the total distance for this kmer
            kmerDis.sort()
            totalDistance += kmerDis[0]
        if totalDistance < self.BEST_KMER_D[0]:
            self.BEST_KMER      = kmer
            self.BEST_KMER_D[0] = totalDistance  

    def run(self):
        for file in self.INPUT_FILES:
            self.fillDNAList(file)
            for kmer in self.KMER_LIST:
                self.median(kmer)
            print(file + " produced a best-k-mer of: " + self.BEST_KMER)

if __name__ == "__main__":
    program = medianString()
    program.run()