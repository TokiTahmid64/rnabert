
import os
import numpy as np
folder_path="dataset//all_sequences"
files=os.listdir(folder_path)

all_accession_ids=[]
all_sequences=[]
for file in files:
    file_path=os.path.join(folder_path,file)
    with open(file_path, "r") as file:
        # Read the contents of the file
        file_contents = file.read()
    splitted=file_contents.split("\n")
    all_accession_ids.append(splitted[0].replace(">",""))
    all_sequences.append(splitted[1])

all_accession_ids=all_accession_ids[:len(all_accession_ids)//2]
all_sequences=all_sequences[:len(all_sequences)//2]

train_id_file="dataset//TR_ids"
test1_id_file="dataset//TS1_ids"
test2_id_file="dataset//TS2_ids"
test3_id_file="dataset//TS3_ids"
valid_id_file="dataset//VL_ids"

train_ids=[]
test1_ids=[]
test2_ids=[]
test3_ids=[]
valid_ids=[]
with open(train_id_file, "r") as file:
    # Read the contents of the file
    file_contents = file.read()
splitted=file_contents.split("\n")
for i in splitted:
    if i!="":
        train_ids.append(i)

with open(test1_id_file, "r") as file:
    # Read the contents of the file
    file_contents = file.read()
splitted=file_contents.split("\n")
for i in splitted:
    if i!="":
        test1_ids.append(i)

with open(test2_id_file, "r") as file:
    # Read the contents of the file
    file_contents = file.read()
splitted=file_contents.split("\n")
for i in splitted:
    if i!="":
        test2_ids.append(i)

with open(test3_id_file, "r") as file:
    # Read the contents of the file
    file_contents = file.read()
splitted=file_contents.split("\n")
for i in splitted:
    if i!="":
        test3_ids.append(i)

with open(valid_id_file, "r") as file:
    # Read the contents of the file
    file_contents = file.read()
splitted=file_contents.split("\n")
for i in splitted:
    if i!="":
        valid_ids.append(i)


train_sequences=[]
test1_sequences=[]
test2_sequences=[]
test3_sequences=[]
valid_sequences=[]

for i in range(len(all_accession_ids)):
    if all_accession_ids[i] in train_ids:
        train_sequences.append(all_sequences[i])
    elif all_accession_ids[i] in test1_ids:
        test1_sequences.append(all_sequences[i])
    elif all_accession_ids[i] in test2_ids:
        test2_sequences.append(all_sequences[i])
    elif all_accession_ids[i] in test3_ids:
        test3_sequences.append(all_sequences[i])
    elif all_accession_ids[i] in valid_ids:
        valid_sequences.append(all_sequences[i])

print(len(train_sequences))
print(len(test1_sequences))
print(len(test2_sequences))
print(len(test3_sequences))
print(len(valid_sequences))



for i in range(len(train_sequences)):
    train_sequences[i]=' '.join(train_sequences[i])
for i in range(len(test1_sequences)):
    test1_sequences[i]=' '.join(test1_sequences[i])
for i in range(len(test2_sequences)):
    test2_sequences[i]=' '.join(test2_sequences[i])
for i in range(len(test3_sequences)):
    test3_sequences[i]=' '.join(test3_sequences[i])
for i in range(len(valid_sequences)):
    valid_sequences[i]=' '.join(valid_sequences[i])

#save the sequences as pickle files
import pickle
with open("dataset//train_sequences.pkl", "wb") as fp:   #Pickling
    pickle.dump(train_sequences, fp)
with open("dataset//test1_sequences.pkl", "wb") as fp:   #Pickling
    pickle.dump(test1_sequences, fp)
with open("dataset//test2_sequences.pkl", "wb") as fp:   #Pickling
    pickle.dump(test2_sequences, fp)
with open("dataset//test3_sequences.pkl", "wb") as fp:   #Pickling
    pickle.dump(test3_sequences, fp)
with open("dataset//valid_sequences.pkl", "wb") as fp:   #Pickling
    pickle.dump(valid_sequences, fp)

#load the sequences from pickle files
with open("dataset//train_sequences.pkl", "rb") as fp:   # Unpickling
    train_sequences = pickle.load(fp)
    print(len(train_sequences))
    print(train_sequences[0])