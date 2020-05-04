import time
import numpy as np
from tqdm import tqdm
from Deep_Q_Learning.Deep_Q_Learning import DQNAgent, MODEL_NAME
from Deep_Q_Learning.GC_Env import GC_Env
from keras.utils import plot_model
from keras.models import load_model
from datetime import datetime

MIN_REWARD = 0  # For model save
STEP_LIMIT = 500

# Environment settings
EPISODES = 20_000

# Exploration settings
epsilon = 1  # not a constant, going to be decayed
EPSILON_DECAY = 0.99975
MIN_EPSILON = 0.01

#  Stats settings
AGGREGATE_STATS_EVERY = 20  # episodes

env = GC_Env()

# For stats
ep_rewards = []
steps = []

# model = load_model(
#     'trained_models\\lr=0.001_gamma=0.5___-35.90max_-1172.30avg_-4394.80min__2020-05-01_23-03.model')

model = None

agent = DQNAgent(env=env, model=model)

for episode in tqdm(range(1, EPISODES + 1), ascii=True, unit='episodes'):

    # Update tensorboard step every episode
    agent.tensorboard.step = episode

    # Restarting episode - reset episode reward and step number
    episode_reward = 0
    step = 1

    # Reset environment and get initial state
    current_state = env.reset()
    old_state = np.zeros(1)

    # Reset flag and start iterating until episode ends
    done = False
    while not done and step <= STEP_LIMIT:

        # This part stays mostly the same, the change is to query a model for Q values
        if np.random.random() > epsilon:
            # Get action from Q table
            action = np.argmax(agent.get_qs(current_state))
        else:
            # Get random action
            action = np.random.randint(0, env.ACTION_SPACE_SIZE)

        new_state, reward, done = env.step(action)

        # Transform new continous state to new discrete state and count reward
        episode_reward += reward

        # Every step we update replay memory and train main network
        agent.update_replay_memory(
            (current_state, action, reward, new_state, old_state, done))
        agent.train(done or step >= STEP_LIMIT, step)

        old_state = current_state
        current_state = new_state
        step += 1

    agent.tensorboard.update_stats(reward=episode_reward)

    # Append episode reward to a list and log stats (every given number of episodes)
    ep_rewards.append(episode_reward)
    steps.append(step)
    if not episode % AGGREGATE_STATS_EVERY or episode == 1:
        average_reward = sum(
            ep_rewards[-AGGREGATE_STATS_EVERY:]) / len(ep_rewards[-AGGREGATE_STATS_EVERY:])
        min_reward = min(ep_rewards[-AGGREGATE_STATS_EVERY:])
        max_reward = max(ep_rewards[-AGGREGATE_STATS_EVERY:])
        average_steps = sum(steps[-AGGREGATE_STATS_EVERY:]) / \
            len(steps[-AGGREGATE_STATS_EVERY:])
        agent.tensorboard.update_stats(
            reward_avg=average_reward, reward_min=min_reward, reward_max=max_reward, epsilon=epsilon, average_steps=average_steps)

        # Save model, but only when min reward is greater or equal a set value
        if min_reward >= MIN_REWARD:
            agent.model.save(
                f'trained_models/{MODEL_NAME}__{max_reward:_>7.2f}max_{average_reward:_>7.2f}avg_{min_reward:_>7.2f}min__{datetime.now().strftime("%Y-%m-%d_%H-%M")}.model')

    if not episode % EPISODES:
        agent.model.save(
            f'trained_models/{MODEL_NAME}__{max_reward:_>7.2f}max_{average_reward:_>7.2f}avg_{min_reward:_>7.2f}min__{datetime.now().strftime("%Y-%m-%d_%H-%M")}.model')

    # plot_model(agent.model, to_file='model.png')

    # Decay epsilon
    if epsilon > MIN_EPSILON:
        epsilon *= EPSILON_DECAY
        epsilon = max(MIN_EPSILON, epsilon)
