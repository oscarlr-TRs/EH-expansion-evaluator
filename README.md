# EH-expansion-evaluator
## Quick start
```
git clone https://github.com/oscarlr/EH-expansion-evaluator
python classify_expansions.py model/raf_model.sav test/test_set.txt > test/out.txt
```
## Requirements
1. python/3.6
## Input
There are two inputs. The first input is the model (```model/raf_model.sav```) and the second input is a modified output from Expansion Hunter. The second input must be a tab delimited file with the following columns:
```
     1	chrom
     2	start
     3	end
     4	Loc
     5	RefUnit
     6	RefCopy
     7	Locus
     8	SampleId
     9	LongAllele
    10	IRR_A1
    11	IRR_A2
    12	IRR_Total
    13	IRR_A1/IRR_A2
    14	SPR_A1
    15	SPR_A2
    16	SPR_Total
    17	FR_A1
    18	FR_A2
    19	FR_A1/FR_A2
    20	FR_Total
    21	Total Reads
```
## Output
The output is a tab delimited file. It contains 10 columns, the first 9 columsn from input and 10th column with the model's prediction of whether the expansion is true or false:
```
     1	chrom
     2	start
     3	end
     4	Loc
     5	RefUnit
     6	RefCopy
     7	Locus
     8	SampleId
     9	LongAllele
    10	T/F_Expansions
```
## Model
The model is a Random Forest classifier with 12 features trained on more than 3,400 manually curated IGV screenshots of read pileups overlapping predicted expansions from Expansion Hunter. The most predictive features are the flanking reads followed by spanning reads and in-repeat reads.

![alt text](https://github.com/oscarlr/EH-expansion-evaluator/blob/main/figs/feat_scores.png?raw=true)
## Contact
[Oscar Rodriguez](https://oscarlr.github.io/) (oscar.rodriguez@icahn.mssm.edu)
Andrew Sharp (andrew.sharp@mssm.edu)
