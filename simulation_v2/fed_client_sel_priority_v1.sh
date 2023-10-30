#!/bin/bash

#--------------------------
# MNIST CNN - IID
#--------------------------

# RUN 1: B = 10, E = 1
python3 fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID_Exp' \
    --exp_name='ex_iid' \
    --sample_type='weighted'

# RUN : B = 10, E = 5
python3 fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID_Exp' \
    --exp_name='ex_iid' \
    --sample_type='weighted'

# RUN : B = 10, E = 20
python3 fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=20 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID_Exp' \
    --exp_name='ex_iid' \
    --sample_type='weighted'

# RUN : B = 50, E = 1
python3 fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID_Exp' \
    --exp_name='ex_iid' \
    --sample_type='weighted'

# RUN : B = 50, E = 5
python3 fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID_Exp' \
    --exp_name='ex_iid' \
    --sample_type='weighted'

# RUN : B = 50, E = 20
python3 fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=20 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID_Exp' \
    --exp_name='ex_iid' \
    --sample_type='weighted'

# RUN : B = 600, E = 1
python3 fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID_Exp' \
    --exp_name='exp_iid' \
    --sample_type='weighted'

# RUN : B = 600, E = 5
python3 fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID_Exp' \
    --exp_name='ex_iid' \
    --sample_type='weighted'

# RUN : B = 600, E = 20
python3 fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=20 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True \
    --wandb_project='FedAvgIID_Exp' \
    --exp_name='ex_iid' \
    --sample_type='weighted'
