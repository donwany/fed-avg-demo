#!/bin/bash

# API_KEY = 9b5ce86c7c7d4e92dea493f54d181b97d058e0dc

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
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True

# RUN : B = 10, E = 5
python fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True

# RUN : B = 10, E = 20
python fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=20 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True

# RUN : B = 50, E = 1
python fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True

# RUN : B = 50, E = 5
python fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True

# RUN : B = 50, E = 20
python fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=20 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True

# RUN : B = 600, E = 1
python fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True

# RUN : B = 600, E = 5
python fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True

# RUN : B = 600, E = 20
python fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=20 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=0 \
    --wandb=True

#----------------------------------------------------------------
# MNIST CNN - NON_IID
#----------------------------------------------------------------
# RUN 1: B = 10, E = 1
python fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=1 \
    --wandb_project='FedAvgNonIID' \
    --exp_name='non_iid' \
    --wandb=True

# RUN : B = 10, E = 5
python fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=1 \
    --wandb_project='FedAvgNonIID' \
    --exp_name='non_iid' \
    --wandb=True

# RUN : B = 10, E = 20
python fed_avg.py \
    --batch_size=10 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=20 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=1 \
    --wandb_project='FedAvgNonIID' \
    --exp_name='non_iid' \
    --wandb=True

# RUN : B = 50, E = 1
python fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=1 \
    --wandb_project='FedAvgNonIID' \
    --exp_name='non_iid' \
    --wandb=True

# RUN : B = 50, E = 5
python fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=1 \
    --wandb_project='FedAvgNonIID' \
    --exp_name='non_iid' \
    --wandb=True

# RUN : B = 50, E = 20
python fed_avg.py \
    --batch_size=50 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=20 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=1 \
    --wandb_project='FedAvgNonIID' \
    --exp_name='non_iid' \
    --wandb=True

# RUN : B = 600, E = 1
python fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=1 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=1 \
    --wandb_project='FedAvgNonIID' \
    --exp_name='non_iid' \
    --wandb=True

# RUN : B = 600, E = 5
python fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=5 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=1 \
    --wandb_project='FedAvgNonIID' \
    --exp_name='non_iid' \
    --wandb=True

# RUN : B = 600, E = 20
python fed_avg.py \
    --batch_size=600 \
    --frac=0.1 \
    --lr=0.01 \
    --n_client_epochs=20 \
    --n_clients=100 \
    --n_epochs=1000 \
    --n_shards=200 \
    --non_iid=1 \
    --wandb_project='FedAvgNonIID' \
    --exp_name='non_iid' \
    --wandb=True
