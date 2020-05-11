# from datetime import datetime
import os
import numpy as np
from numpy.random import random
from tqdm import tqdm
from keras.models import load_model
from Deep_Q_Learning.deep_q_learning import DQNAgent
from Deep_Q_Learning.__gc_env__ import GcEnv

MIN_REWARD = 0  # For model save
STEP_LIMIT = 500
CURRENT_RUN_COUNT = 60
DELTA = 40
MODEL_NAME = f'Limited-{CURRENT_RUN_COUNT + DELTA}k'

# Environment settings
EPISODES = DELTA * 1_000

# Exploration settings
EPSILON = 1  # not a constant, going to be decayed
EPSILON_DECAY = 0.99975
MIN_EPSILON = 0.01

#  Stats settings
AGGREGATE_STATS_EVERY = 50  # episodes

ENV = GcEnv()

# For stats
EP_REWARDS = []
STEPS = []

MODEL = load_model(os.path.join(
    'trained_models', f'limited-{CURRENT_RUN_COUNT}k'))

# MODEL = None

AGENT = DQNAgent(env=ENV, model=MODEL, model_name=MODEL_NAME)

for episode in tqdm(range(1, EPISODES + 1), ascii=True, unit='episodes'):

    # Update tensorboard step every episode
    AGENT.tensorboard.step = episode

    # Restarting episode - reset episode reward and step number
    episode_reward = 0
    step = 1

    # Reset environment and get initial state
    current_state = ENV.reset()
    old_state = np.zeros(1)

    # Reset flag and start iterating until episode ends
    done = False
    while not done and step <= STEP_LIMIT:

        # This part stays mostly the same, the change is to query a model for Q values
        if random() > EPSILON:
            # Get action from Q table
            action = np.argmax(AGENT.get_qs(current_state))
        else:
            # Get random action
            action = np.random.randint(0, ENV.ACTION_SPACE_SIZE)

        new_state, reward, done = ENV.step(action)

        # Transform new continous state to new discrete state and count reward
        episode_reward += reward

        # Every step we update replay memory and train main network
        AGENT.update_replay_memory(
            (current_state, action, reward, new_state, old_state, done))
        AGENT.train(done or step >= STEP_LIMIT)

        old_state = current_state
        current_state = new_state
        step += 1

    AGENT.tensorboard.update_stats(reward=episode_reward)

    # Append episode reward to a list and log stats (every given number of episodes)
    EP_REWARDS.append(episode_reward)
    STEPS.append(step)
    if not episode % AGGREGATE_STATS_EVERY or episode == 1:
        average_reward = sum(
            EP_REWARDS[-AGGREGATE_STATS_EVERY:]) / len(EP_REWARDS[-AGGREGATE_STATS_EVERY:])
        min_reward = min(EP_REWARDS[-AGGREGATE_STATS_EVERY:])
        max_reward = max(EP_REWARDS[-AGGREGATE_STATS_EVERY:])
        average_steps = sum(STEPS[-AGGREGATE_STATS_EVERY:]) / \
            len(STEPS[-AGGREGATE_STATS_EVERY:])
        AGENT.tensorboard.update_stats(
            reward_avg=average_reward, reward_min=min_reward,
            reward_max=max_reward, epsilon=EPSILON, average_steps=average_steps)

        # Save model, but only when min reward is greater or equal a set value
        # if min_reward >= MIN_REWARD:
        #     AGENT.model.save(
        #         f'trained_models/{MODEL_NAME}__{max_reward:_>7.2f}max_{average_reward:_>7.2f} \
        #             avg_{min_reward:_>7.2f}min__{datetime.now().strftime("%Y-%m-%d_%H-%M")}.model')

    if not episode % EPISODES:
        AGENT.model.save(f'trained_models/{MODEL_NAME}')

    # plot_model(agent.model, to_file='model.png')

    # Decay epsilon
    if EPSILON > MIN_EPSILON:
        EPSILON *= EPSILON_DECAY
        EPSILON = max(MIN_EPSILON, EPSILON)
