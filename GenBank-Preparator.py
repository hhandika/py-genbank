#!/usr/bin/python

# This script will format input files for use in GenBank's Sequin program.
# It takes a nexus file as input, and produces a non-interleaved fasta file.
# The first two elements of all taxon names should be Genus_species and VoucherNumber. They should be separated by a period.
# Whatever follows the voucher number (separated by a period) in the taxon labels will be ignored. 
# Here is an example of the output taxon labels:
#>FMNH222222 [organism=Hipposideros pygmaeus] [molecule=DNA] [moltype=genomic] [location=mitochondrion] [specimen-voucher=FMNH222222]

nexIn = open('cytb.nex', 'r') #the file with the trees
fasOut = open('cytb-genbankIn.fas', 'a')	#the output file with new taxon labels
metadata = '[organelle=mitochondrion] [molecule=DNA] [moltype=genomic DNA] [gene=CYTB] [product=cytochrome b]' #whatever variables are consistent across all sequences

def parse_name(taxLabel):
	taxLabel = taxLabel.split('.')
	taxon = taxLabel[0].split('_')
	taxon = str(taxon[0] + ' ' + taxon[1])
	voucher = taxLabel[1]
	return taxon, voucher
	
for line in nexIn:
	sequ = str(line)
	data = sequ.split()
	if len(data) == 2 and len(data[1]) > 200:
		data = sequ.split()
		taxon = parse_name(data[0])
		byline = '>' + taxon[1] + ' ' + '[organism=' + taxon[0] + '] '+ metadata + ' [specimen-voucher=' + taxon[1] + ']' + '\n'
		fasOut.write(byline)
		fasOut.write(data[1])
		fasOut.write(2*'\n')
