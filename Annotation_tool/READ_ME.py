#This tool can be used to inspect the notes of your data. Just swap out the file paths with the paths you have to use. 
import os
import pandas as pd

def process_csv(group: bool, column1: str, column2: str, path: str = '.', file_name: str = ''):
    df = pd.read_csv(os.path.join(path, file_name), sep=',')

    if group:
        grouped = df.groupby('PatientID')
        df = grouped.agg(lambda x: x.tolist())
        df = df.reset_index()

    # Keep only the specified columns
    df = df[[column1, column2]]
    df = df.rename(columns={column1: 'EMPI', column2: 'Report_Text'})
    # Convert dataframe to JSON
    json_data = df.to_json(orient='records')

    # Write JSON to a JavaScript file with variable assignment and function call
    with open(os.path.join(path, 'data.js'), 'w') as f:
        f.write('var json=')
        f.write(json_data)
        #f.write(';\nreset_empi_loaded_file1();')

# True to group by PatientID, next is the
# path to your csv file


path = "/home/gregory178/Desktop/NAX project/NAX_SDH/Annotation_tool_training_error/"
file_name = "false_negatives_with_notes.csv"
# replace "note_id" with csv column with the unique id for each note and replace "note_txt" with the csv column containing the note text in the line below.
process_csv(False, "BDSPPatientID", "NoteContent", path, file_name)
#Unnamed: 0 usually