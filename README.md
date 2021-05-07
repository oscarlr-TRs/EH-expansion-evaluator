# EH-expansion-evaluator
## Quick start
```
git clone https://github.com/oscarlr/EH-expansion-evaluator
cd EH-expansion-evaluator

### Generate Random Forest feature table from Expansion Hunter output VCFs
python ExtractFeatureFromEHvcf.py  \
       --vcf_list test/HG00123.hg38Catalog.EHv3.2.2.vcf test/HG00125.hg38Catalog.EHv3.2.2.vcf test/HG00129.hg38Catalog.EHv3.2.2.vcf test/HG04212.hg38Catalog.EHv3.2.2.vcf  test/HG04219.hg38Catalog.EHv3.2.2.vcf  test/NA20895.hg38Catalog.EHv3.2.2.vcf test/NA20901.hg38Catalog.EHv3.2.2.vcf test/NA20903.hg38Catalog.EHv3.2.2.vcf test/NA20904.hg38Catalog.EHv3.2.2.vcf test/NA20908.hg38Catalog.EHv3.2.2.vcf test/NA21090.hg38Catalog.EHv3.2.2.vcf \
       --out test/TestFeatureExtraction \
       --locus_file test/ExpansionTestList.txt

### Run classifer on test data using features generated above
python classify_expansions.py model/model.pkl test/TestFeatureExtraction.RF_Feature.tsv > test/Test.RF_Prediction_Output.tsv
```
## Requirements
1. python/3.6

## Inputs 
1. VCFs generated from Expansion Hunter
2. 2-column text file with sample ids and locus. See `test/ExpansionTestList.txt` for an example.
3. `<prefix>.RF_Feature.tsv` file generated from `ExtractFeatureFromEHvcf.py`
4. `model.pkl` file in model folder

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
