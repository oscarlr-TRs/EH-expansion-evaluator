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
## Output :
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

## Input : Classifer
There are two inputs. The first input is the model (```model/raf_model.sav```) and the second input is tab delimited feature table generated from Expansion Hunter output vcf using above script. 
## Output
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
The model is a Random Forest classifier with 12 features trained on more than 3,400 manually curated IGV screenshots of read pileups overlapping _**predicted expansions**_ from Expansion Hunter. The most predictive features are the flanking reads, specifically the flanking ratio between both alleles, followed by spanning reads and in-repeat reads.

![alt text](https://github.com/oscarlr/EH-expansion-evaluator/blob/main/figs/feat_scores.png?raw=true)

### Acknowledgments
Credit to Alejandro Martin Trujillo for datasets, providing features and contribution to concept and Scott Gies for manually curating the training data. 

## Contact
[Oscar Rodriguez](https://oscarlr.github.io/) (oscar.rodriguez@icahn.mssm.edu)
[Andrew Sharp](https://icahn.mssm.edu/profiles/andrew-j-sharp) (andrew.sharp@mssm.edu)
