"""
Automate sequence preparation for Genbank submission

Author: Heru Handika and Jacob A. Esselstyn
Creation Date: 26 September 2020

License MIT
"""
import os
from typing import Tuple

import click

def get_metadata(dna_type: str) -> str:
    metadata = '[molecule=DNA] [moltype=genomic DNA]'

    if dna_type == "mtdna":
        metadata =  metadata + '[gene=CYTB]'
        return metadata
    elif dna_type == "nucleus":
        return metadata
    else:
        print(f"\x1b[0;31mError: \x1b[0mInvalid dna type")

def get_input_files(infile: str, outfile: str, dna_type) -> Tuple[str, str, str]:
    nexus_input = open(infile, 'r')
    fasta_output = open(outfile, 'a')
    metadata = get_metadata(dna_type)

    return nexus_input, fasta_output, metadata

def parse_name(seq_name: str) -> str:
    seq_name = seq_name.split("_")
    taxon = seq_name[0] + ' ' + seq_name[1]
    voucher = seq_name[2]
    return taxon, voucher

def write_fasta_from_nexus(nexus_input: str, fasta_output: str, metadata: str) -> None:
    for line in nexus_input:
        seq = str(line)
        data = seq.split()
        if len(data) == 2 and len(data[1]) > 200:
            taxon = parse_name(data[0])
            byline = '>' + taxon[1] + ' ' + '[organism=' + taxon[0] + '] ' \
                + metadata + ' [specimen-voucher=' + taxon[1] + ']' + '\n'
                
            fasta_output.write(byline)
            fasta_output.write(data[1])
            fasta_output.write("\n\n")

    fasta_output.close()

def write_result(infile: str, outfile: str, dna_type: str) -> None:
    outfile = "result/" + outfile

    nex_in, fast_out, metadata = get_input_files(infile, outfile, dna_type)
    write_fasta_from_nexus(nex_in, fast_out, metadata)

    print(f"\x1b[0;33mFile is saved as \x1b[0m{outfile}")

@click.command()
@click.option('--infile', '-i', help='Add the input file')
@click.option('--outfile', '-o', default=None, help="Add output file name")
@click.option('--dna_type', '-dt', default='nucleus', help='Add the input file')
def main(infile: str, outfile: str, dna_type: str) -> None:
    """
    GenBank Submission Preparator

    Automate GenBank submission.

    Args:
        infile (nexus): a nexus formatted input file
        outfile (fasta): a fasta formatted output file
    """
    if outfile is None:
        outfile = infile.replace(".nex", "") + '_GenBankOut_2.fas'

    try: 
        write_result(infile, outfile, dna_type)
    except FileNotFoundError:
        os.mkdir("result")
        write_result(infile, outfile, dna_type)
    except FileExistsError:
        print(f"\x1b[0;31mFile exist!")

if __name__ == "__main__":
    main()