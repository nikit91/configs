#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE.txt file in the root directory of this source tree.


def get_torchbiggraph_config():

    config = dict(  # noqa
        # I/O data
        entity_path="data/dbp2103_complex",
        edge_paths=["data/dbp2103_complex/train_partitioned"],
        checkpoint_path="model/dbp2103_complex",
        # Graph structure
        entities={"all": {"num_partitions": 1}},
        relations=[
            {
                "name": "all_edges",
                "lhs": "all",
                "rhs": "all",
                "operator": "complex_diagonal"
            }
        ],
        dynamic_relations=True,
        # Scoring model
        dimension=100,
        global_emb=False,
        comparator="dot",
        # Training
        #num_epochs=5,
        #num_uniform_negs=100,
        #loss_fn="softmax",
        #lr=0.1,
        num_epochs=4,
        num_edge_chunks=100,
        batch_size=1000,
        num_batch_negs=50,
        num_uniform_negs=50,
        loss_fn='softmax',
        lr=0.1,
        relation_lr=0.01,
        #regularization_coef=1e-3,
        # Evaluation during training
        eval_fraction=0,  # to reproduce results, we need to use all training data
        # Misc
        verbose=1,
    )

    return config
