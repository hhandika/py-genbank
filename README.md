# py-genbank

This is a command line application to generate fasta input files for GenBank BankIt submission. It is designed for Sanger sequencing data. The original script was written by Dr. Jacob A. Esselstyn. I refactored it and expanded its capabilities. 

## State of Code
Work in progress. Currently, it is working as expected. It is only accept one nexus file as an input. I am working on expanding its the capability to accept multiple files in both fasta and nexus format as inputs. Hence, you should expect significant refactoring and re-structuring in this repo.

## Installation
Clone the repo

```
git clone https://github.com/hhandika/py-genbank
```
Go the the folder and install using pip

```
pip install --editable .
```

## Usage
pygb -i [filename]
```
pygb -i cytb.nex
```


