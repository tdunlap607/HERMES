# HERMES
Auto Vulnernability Fix Commit Classification

The dataset is available at location: MSR/2019/experiment/full_data_set_with_all_features.txt

Watch our presentation at SANER 2022: https://www.youtube.com/watch?v=S4a3wpHbVTw

Slides for the presentation in file: HERMES-SANER-2022_slides.pptx

Also PDF version: HERMES-SANER-2022_slides.pdf

in json format

Data Object Classes are described in **entitites.py**

###### To replicate HERMES on full dataset please use this command
python3 experiment.py --min_df 5 --use_linked_commits_only False --use_issue_classifier True --use_stacking_ensemble True --use-patch-context-lines False --tf-idf-threshold 0.005 --dataset sub_enhanced_dataset_th_100.txt

###### To replicate HERMES on subset of explicitly linked commits please use this command
python3 experiment.py --min_df 5 --use_linked_commits_only True --use_issue_classifier True --use_stacking_ensemble True --use-patch-context-lines False --tf-idf-threshold 0.005 --dataset full_dataset_with_all_features.txt

##### To replicate HERMES on the explicitly linked data and on commits recovered links

Please extract zip files in MSR2019/experiment which contain dataset corresponding to different threshold (thresholds are written at postfix of file names).

After that, to run HERMES on different threshold, please use this command's template:

python3 experiment.py --min_df 5 --use_linked_commits_only True --use_issue_classifier True --use_stacking_ensemble True --use-patch-context-lines False --tf-idf-threshold 0.005 --dataset **file_name**

where file_name is name of file in list of files just extracted

Link to our issue corpus: https://zenodo.org/record/5602211#.YXjQg9ZBxO8

Descriptions for parameter in command:
- min_df [real]: Min document frequency to filter out infrequent terms
- use_linked_commits_only [boolean]: Option to use all commits in dataset for training and testing, or only use commits where each contain at least one issue linked to Github or Jira issue tracker
- use_issue_classifier [boolean]: Option to use or not use issue classifier in HERMES. If not, HERMES contain only message classifier and patch classifier
- use_stacking_ensemble [boolean]: Option to use stacking ensemble or simple voting to combine base classifier (i.e. message classsifier, patch classifier, issue classifier). If true, use stacking ensemble for combination. Otherwise, use simple voting
- tf-idf-threshold [real]: Option in issue classifier to filter out noises in issue classifier
- dataset [string]: Name of the dataset selected for experiment


# Steps on how to replicate:
Create a venv:
~~~~
python3 -m venv venv
source ./venv/bin/activate
~~~~

Rename the data_loader folder to loader: ````mv ./data_loader/ ./loader````

Install the necessary dependencies: ````pip3 install numpy pygithub scikit-learn nltk pandas````

Download stopword and punkt: places data in /home/USERNAME/nltk_data/
~~~~
python3 -m nltk.downloader stopwords
python3 -m nltk.downloader punkt
~~~~

Unzip the enchance dataset that you want to use:
~~~~
unzip ./MSR2019/experiments/sub_enhanced_dataset_th_100.txt.zip
~~~~

Create a directory to hold the classifier output: ````mkdir ./classifier_output````

Run from the command line:
~~~~
python3 experiment.py --min_df 5 --use_linked_commits_only False --use_issue_classifier True --use_stacking_ensemble True --use-patch-context-lines False --tf-idf-threshold 0.005 --dataset sub_enhanced_dataset_th_100.txt
~~~~


Temp results on DAA:
Message F1: 0.8
Issue F1: 1.0
Patch F1: 0.8
------------------------------------------------
Training result for positive weight: 0.5, negative weight: 0.5
Log message mean precision: 1.0
Log message mean recall: 0.6666666666666666
Log message mean f1: 0.8
Issue mean precision: 1.0
Issue mean recall: 1.0
Issue mean f1: 1.0
Patch mean precision: 1.0
Patch mean recall: 0.6666666666666666
Patch mean f1: 0.8
Joint-model mean precision: 1.0
Joint-model mean recall: 0.6666666666666666
Joint-model mean f1: 0.8
Joint-model mean AUC-ROC: 1.0
Joint-model mean AUC-PR: 1.0