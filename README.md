# Median String finder
A program to find a k-mer pattern that has the smallest distance (d) over all k-mer patterns given a set of DNA sequences
## Inputs
- Searches current directory for files with the naming convention input_*.txt where * is a number
## Output
- Outputs the file name and a k-mer pattern that minimizes the distance among all possible choices of k-mers

## Notes
- Assumes file structure is correct
    * Structure Example
    1.  First line of the file should be a single interger (K)
    2.  Following lines are DNA sequences comprised of the letters A,C,G or T, seperated by spaces or newlines (\n)
    ```console
    6
    TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG
    ```
- Python file must be in the same directory as input files to run