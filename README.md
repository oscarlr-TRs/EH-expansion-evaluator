# EH-expansion-evaluator
## Quick start
```
git clone https://github.com/oscarlr/EH-expansion-evaluator
python classify_expansions.py model/raf_model.sav test/test_set.txt > test/out.txt
```
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
