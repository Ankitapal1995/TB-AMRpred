# WG-XGB_prediction
AMR prediction in Mycobacterium tuberculosis using whole genome sequences


# script run using whole genome fasta sequence
WG-XGB_prediction input.fasta
or
WG-XGB_prediction input.fna

# script run using whole genome fastq sequence
WG-XGB_prediction input_1.fastq.gz input_2.fastq.gz

# requirement
conda env create -f environment_amr.yml
or
# manually create environment
miniconda3=24.1.2
python=3.12.0
snippy=4.6.0
numpy==1.26.4
pandas==2.2.1
matplotlib==3.8.3
scikit-learn==1.4.1
xgboost==2.0.3
pip=24.0



