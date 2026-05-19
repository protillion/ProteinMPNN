#!/bin/bash

path_to_PDB=$1

output_dir=$2
if [ ! -d $output_dir ]
then
    mkdir -p $output_dir
fi

python ../protein_mpnn_run.py \
        --pdb_path $path_to_PDB \
        --out_folder $output_dir \
        --sampling_temp "0.1" \
        --score_only 1 \
        --seed 123 \
        --batch_size 1