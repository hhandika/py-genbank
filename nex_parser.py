"""
Automate sequence preparation for Genbank submission

Author: Heru Handika and Jacob A. Esselstyn
Creation Date: 26 September 2020

License MIT
"""

def parse_name(seq_name):
    seq_name = seq_name.split("_")
    taxon = seq_name[0] + ' ' + seq_name[1]
    voucher = seq_name[2]
    return taxon, voucher

def main():
    nexus_input = open('data/cytb.nex', 'r')
    fasta_output = open('data/cytb_genebankIn.fasta', 'a')
    metadata = '[organelle=mitochondrion] [molecule=DNA] [moltype=genomic DNA] [gene=CYTB] [product=cytochrome b]'

    for line in nexus_input:
        seq = str(line)
        data = seq.split()
        if len(data) == 2 and len(data[1]) > 200:
            data = seq.split()
            taxon = parse_name(data[0])
            byline = '>' + taxon[1] + ' ' + '[organism=' + taxon[0] + '] ' \
                + metadata + ' [specimen-voucher=' + taxon[1] + ']' + '\n'
            fasta_output.write(byline)
            fasta_output.write(data[1])
            fasta_output.write("\n\n")

    fasta_output.close()

if __name__ == "__main__":
    main()