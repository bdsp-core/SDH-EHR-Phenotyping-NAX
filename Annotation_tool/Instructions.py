#The following folder contains all the files necessary to manually annotate the +/- ICD groups for MGB and BIDMC. 
#1. You will need to obtain official approval to use the annotation tool. Please reach out via the email listed on the paper. 
#2. Once you have access, you will need to create a username and password. 
#3. Select the regexes.js file. This file will contain all the keywords that the annotation tool will highlight. 
    #Please feel free to replace the keywords highlighted as you see fit, however, these were the keywords used by the annotators. 
#4. Go to the READ_ME.py and change the file path at the bottom to the file path of your ICD+ Group for MGB. 
#5. Run the READ_ME file.
#6. Save all the files, and then open up the annotation tool "20240429_annotation tool_open source (1).html" on your computer.
#7. Type in your username and password. 
#8. Manually annotate all patient notes in the ICD+ group for MGB as positive or negative cases. 
#9. Repeat bullet points 4-8, changing the file path each round from ICD+ MGB to ICD- MGB, to ICD+ BIDMC, to ICD- BIDMC. 
#10. Once all of the ICD + and ICD- files for both hospitals have been manually annotated, 
    #click inspect, console, and type in "(download_csv_progress_json)".
#11. Once you have the csv containing all of your manual annotations for each patient, copy the file path of that file.
#12. Go to Step 2 and put in the file path for the manual annotations csv you made. 
#13. Run steps 1-25. 

