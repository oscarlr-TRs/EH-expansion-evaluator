# EH-expansion-evaluator
## Quick start
```
git clone https://github.com/oscarlr/EH-expansion-evaluator
cd EH-expansion-evaluator

### Generate Random Forest feature table from Expansion Hunter output VCFs
python ExtractFeatureFromEHvcf.py  \
       --vcf_list test/HG00123.hg38Catalog.EHv3.2.2.vcf test/HG00125.hg38Catalog.EHv3.2.2.vcf test/HG00129.hg38Catalog.EHv3.2.2.vcf test/HG04212.hg38Catalog.EHv3.2.2.vcf  test/HG04219.hg38Catalog.EHv3.2.2.vcf  test/NA20895.hg38Catalog.EHv3.2.2.vcf test/NA20901.hg38Catalog.EHv3.2.2.vcf test/NA20903.hg38Catalog.EHv3.2.2.vcf test/NA20904.hg38Catalog.EHv3.2.2.vcf test/NA20908.hg38Catalog.EHv3.2.2.vcf test/NA21090.hg38Catalog.EHv3.2.2.vcf \
       --out test/TestFeatureExtraction \
       --locus_file test/ExpansionTestList.tsv

### Run classifer on test data using features generated above
python classify_expansions.py model/raf_model.sav test/TestFeatureExtraction.RF_Feature.tsv > test/Test.RF_Prediction_Output.tsv
```
## Requirements
1. python/3.6
## Input : Feature extraction from vcf
a. space separated list of Expansion Hunter generated vcf files
b. TSV file containing Sample and Locus List to test with classifier
     ```
     1	SampleId
     2    LocusId
     ```
### Output :
TSV file with following columns
```
     1	chrom
     2	start
     3	end
     4	RefUnit  
     5	LocusId
     6	SampleId
     7    A1
     8    A2
     9	IRR_A1
    10	IRR_A2
    11	SPR_A1
    12	SPR_A2
    13	FR_A1
    14	FR_A2
    15    LongAllele
    16	IRR_Total
    17	SPR_Total
    18	FR_Total
    19	IRR_Ratio    
    20	FR_Ratio
    21	Total Reads
```
## Classifer (classify_expansions.py)
### Input 
There are two inputs. The first input is the model (```model/model.pkl```) and the second input is a modified output from Expansion Hunter. The second input must be a tab delimited file with the following columns:
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
### Output
The output is a tab delimited file. It contains 8 columns, the first 7 columns from the input and 8th column with the model's prediction of whether the expansion is true or false:
```
     1	chrom
     2	start
     3	end
     4	RefUnit
     5	LocusId
     6	SampleId
     7	LongAllele
     8	ExpansionPredictedLabels
```
## Model
The model is a Random Forest classifier with 12 features trained on more than 1,400 manually curated IGV screenshots of read pileups overlapping _**predicted expansions**_ from Expansion Hunter and on 600 TR expansions predicted to be true based on long-read sequencing data. The most predictive features are the flanking reads, specifically the flanking ratio between both alleles, followed by spanning reads and in-repeat reads.

```
FR_A1/FR_A2	0.30
SPR_A2	0.14
IRR_A2	0.13
FR_A2	0.10
IRR_Total	0.07
SPR_A1	0.07
Total Reads	0.05
FR_Total	0.05
FR_A1	0.04
SPR_Total	0.04
IRR_A1/IRR_A2	0.004
IRR_A1	0.004
```

### Acknowledgments
Credit to Alejandro Martin Trujillo for datasets, providing features and contribution to concept and Scott Gies for manually curating the training data. 

## Contact
[Oscar Rodriguez](https://oscarlr.github.io/) (oscar.rodriguez@icahn.mssm.edu)
[Andrew Sharp](https://icahn.mssm.edu/profiles/andrew-j-sharp) (andrew.sharp@mssm.edu)
