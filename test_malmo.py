#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import marlo
import cv2 as cv


def make_env(env_seed=0):
    join_tokens = marlo.make(
        "MarLo-FindTheGoal-v0",
        params=dict(
            allowContinuousMovement=["move", "turn"],
            kill_clients_after_num_rounds=500
        ))
    env = marlo.init(join_tokens[0])

    obs = env.reset()
    # env.render(mode="rgb_array")
    action = env.action_space.sample()
    obs, r, done, info = env.step(action)
    env.seed(int(env_seed))
    return env

env = make_env()
obs = env.reset()

for i in range(100):
    action = env.action_space.sample()
    obs, r, done, info = env.step(action)
    print(r, done, info)
