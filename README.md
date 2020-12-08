# EH-expansion-evaluator
## Quick start
```
git clone https://github.com/oscarlr/EH-expansion-evaluator
python classify_expansions.py model/raf_model.sav test/test_set.txt > test/out.txt
```
## Input
There are two inputs. The first input is the model (```model/raf_model.sav```) and the second input is a modified output from Expansion Hunter. The second input must be a tab delimited file with the following columns:
```
"chrom","start","end","Loc","RefUnit","RefCopy","Locus","SampleId","LongAllele","IRR_A1","IRR_A2","IRR_Total","IRR_A1/IRR_A2","SPR_A1","SPR_A2","SPR_Total","FR_A1","FR_A2","FR_A1/FR_A2","FR_Total","Total Reads"
```
