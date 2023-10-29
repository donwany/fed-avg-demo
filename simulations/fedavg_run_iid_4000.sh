#!/bin/bash

#--------------------------
# MNIST CNN - IID
#--------------------------

# RUN 1: B = 10, E = 1
python fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=4000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID4000_Exp' \
    --exp_name='ex_4000_iid'

# RUN : B = 10, E = 5
python fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=4000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID4000_Exp' \
    --exp_name='ex_4000_iid'

# RUN : B = 50, E = 1
python fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=4000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID4000_Exp' \
    --exp_name='ex_4000_iid'

# RUN : B = 50, E = 5
python fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=4000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID4000_Exp' \
    --exp_name='ex_4000_iid'

# RUN : B = 600, E = 1
python fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=4000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID4000_Exp' \
    --exp_name='ex_4000_iid'

# RUN : B = 600, E = 5
python fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=4000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID4000_Exp' \
    --exp_name='ex_4000_iid'

