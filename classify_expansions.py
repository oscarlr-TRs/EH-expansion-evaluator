#!/bin/env python
import sys
import pickle
import numpy

modelfn = sys.argv[1]
expansionsfn = sys.argv[2]

columns = ["IRR_A1","IRR_A2","IRR_Total","IRR_A1/IRR_A2",
           "SPR_A1","SPR_A2","SPR_Total","FR_A1","FR_A2",
           "FR_A1/FR_A2","FR_Total","Total Reads"]

def format_data(data):
    columns = ["IRR_A1","IRR_A2","IRR_Total","IRR_A1/IRR_A2",
               "SPR_A1","SPR_A2","SPR_Total","FR_A1","FR_A2",
               "FR_A1/FR_A2","FR_Total","Total Reads"]
    features = []
    entries = []
    for entry in data:
        feature_line = []
        for column in columns:
            feature_line.append(data[entry][column])
        features.append(feature_line)
        entries.append(entry)
    features = numpy.array(features).astype(numpy.float)
    return entries,features
            
def read_in_dataset(fn):
    data = {}
    header_vals = None
    entry_name_vals = ["chrom","start","end","Loc","RefUnit","RefCopy","Locus","SampleId","LongAllele"]
    columns = ["IRR_A1","IRR_A2","IRR_Total","IRR_A1/IRR_A2",
               "SPR_A1","SPR_A2","SPR_Total","FR_A1","FR_A2",
               "FR_A1/FR_A2","FR_Total","Total Reads"]
    with open(fn,'r') as fh:
        for line in fh:
            if "VALUE" in line:
                continue
            if "DIV" in line:
                continue
            line = line.rstrip().split('\t')
            if line[0] == "chrom":
                header_vals = line
            else:
                entry = {}
                for val,header in zip(line,header_vals):
                    entry[header] = val
                skip = False
                for column in columns:
                    if entry[column] == ".":
                        skip = True
                if skip:
                    continue
                entry_name = []
                for entry_name_val in entry_name_vals:
                    entry_name.append(entry[entry_name_val])
                entry_name = "_".join(entry_name)
                data[entry_name] = {}
                for column in columns:                    
                    data[entry_name][column] = float(entry[column])
    return data

data = read_in_dataset(expansionsfn)
entries,features = format_data(data)
loaded_model = pickle.load(open(modelfn, 'rb'))
preds = loaded_model.predict(features)
header = ["chrom","start","end","Loc","RefUnit","RefCopy","Locus","SampleId","LongAllele","T/F_Expansions"]
print("\t".join(header))
for entry,pred in zip(entries,preds):
    output = entry.split("_")
    output.append(pred)
    print("\t".join(output))
