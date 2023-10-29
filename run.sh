#!/bin/bash

python3 fed_avg.py \
--batch_size=10 \
--frac=0.1 \
--lr=0.01 \
--n_client_epochs=20 \
--n_clients=10 \
--n_epochs=10 \
--n_shards=200 \
--non_iid=1 \
--sample_type 'federated' \
--wandb_project='UnifFedAvgDemoNonIID' \
--exp_name='non_iid' \
--wandb=True

#python fed_avg.py \
#--batch_size=10 \
#--frac=0.1 \
#--lr=0.01 \
#--n_client_epochs=20 \
#--n_clients=100 \
#--n_epochs=1000 \
#--n_shards=200 \
#--non_iid=1 \
#--sample_type group
#
#python fed_avg.py \
#--batch_size=10 \
#--frac=0.1 \
#--lr=0.01 \
#--n_client_epochs=20 \
#--n_clients=100 \
#--n_epochs=1000 \
#--n_shards=200 \
#--non_iid=1 \
#--sample_type responsiveness