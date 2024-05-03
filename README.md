# TB-AMRpred  <br />
AMR prediction in Mycobacterium tuberculosis using whole genome sequences <br />

**install the code using git** <br />
``` git clone https://github.com/Ankitapal1995/TB-AMRpred.git``` <br />

**requirement**  <br />
```conda env create -f environment_amr.yml``` <br />

 or <br />


**manually create environment** <br />
```miniconda3=24.1.2```  <br />
```python=3.12.0```  <br />
```snippy=4.6.0```  <br />
```numpy==1.26.4```  <br />
```pandas==2.2.1```  <br />
```matplotlib==3.8.3```  <br />
```scikit-learn==1.4.2```  <br />
```xgboost==2.0.3 ```  <br />
```pip=24.0```  <br />

**activate conda environment** <br/>
```conda activate amr``` <br/>

**add path after installation** <br/>
open TB-AMRpred file and add your path <br/>
```path='your path to the TB-AMRpred'/scripts``` <br/>
go to ```scripts``` folder <br/>
```cd scripts```  <br/>
open ```paths_variable.py``` and add your path <br/>
```path='your path to the TB-AMRpred'/scripts``` <br/>

**script run using whole genome fasta sequence** <br />

```TB-AMRpred input.fasta``` <br />
or <br />

```TB-AMRpred input.fna ``` <br />

**script run using whole genome fastq sequence**  <br />
```TB-AMRpred input_1.fastq.gz input_2.fastq.gz``` <br />

 



