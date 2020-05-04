import numpy as np
from datetime import datetime
from time import asctime
import keras.backend.tensorflow_backend as backend
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense, Dropout, Input, Activation, Flatten, Conv2D
from keras.optimizers import Adam
from keras.callbacks import TensorBoard
import tensorflow as tf
from collections import deque
import random
from Deep_Q_Learning.GC_Env import GC_Env

DISCOUNT = 0.9
REPLAY_MEMORY_SIZE = 500_000  # How many last steps to keep for model training
# Minimum number of steps in a memory to start training
MIN_REPLAY_MEMORY_SIZE = 200
MINIBATCH_SIZE = 64  # How many steps (samples) to use for training
HALF_MINIBATCH = int(MINIBATCH_SIZE / 2)
UPDATE_TARGET_EVERY = 5  # Terminal states (end of episodes)
LEARNING_RATE = 0.01
MODEL_NAME = f'lr={LEARNING_RATE}_gamma={DISCOUNT}'


# Own Tensorboard class


class ModifiedTensorBoard(TensorBoard):

    # Overriding init to set initial step and writer (we want one log file for all .fit() calls)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.step = 1
        self.writer = tf.summary.FileWriter(self.log_dir)

    # Overriding this method to stop creating default log writer
    def set_model(self, model):
        pass

    # Overrided, saves logs with our step number
    # (otherwise every .fit() will start writing from 0th step)
    def on_epoch_end(self, epoch, logs=None):
        self.update_stats(**logs)

    # Overrided
    # We train for one batch only, no need to save anything at epoch end
    def on_batch_end(self, batch, logs=None):
        pass

    # Overrided, so won't close writer
    def on_train_end(self, _):
        pass

    # Custom method for saving own metrics
    # Creates writer, writes custom metrics and closes writer
    def update_stats(self, **stats):
        self._write_logs(stats, self.step)


class DQNAgent:
    def __init__(self, env, model=None):

        self.env = env

        if model:
            self.model = model
            print("nanana")
            self.target_model = model
        else:
            # Main model
            self.model = self.create_model()

            # Target network
            self.target_model = self.create_model()
        self.target_model.set_weights(self.model.get_weights())

        # An array with last n steps for training
        self.replay_memory = deque(maxlen=REPLAY_MEMORY_SIZE)
        # self.negative_memory = deque(maxlen=REPLAY_MEMORY_SIZE)
        # self.positive_memory = deque(maxlen=REPLAY_MEMORY_SIZE)

        # Custom tensorboard object
        self.tensorboard = ModifiedTensorBoard(
            log_dir=f'logs/{datetime.now().strftime("%Y-%m-%d_%H-%M")}-{MODEL_NAME}')

        # Used to count when to update target network with main network's weights
        self.target_update_counter = 0

    def create_model(self):
        model = Sequential()

        model.add(
            Dense(40, input_shape=self.env.OBSERVATION_SPACE_VALUES, activation='tanh'))
        model.add(Dense(40, activation='tanh'))
        model.add(Dense(40, activation='tanh'))
        model.add(Dense(40, activation='tanh'))
        model.add(Dense(40, activation='tanh'))

        model.add(Dense(self.env.ACTION_SPACE_SIZE, activation='softmax'))
        model.compile(loss='huber_loss',
                      optimizer='SGD', metrics=['accuracy'])
        print(model.summary())
        return model

    # Adds step's data to a memory replay array
    # (observation space, action, reward, new observation space, done)
    def update_replay_memory(self, transition):
        self.replay_memory.append(transition)
        # if transition[2] > 0:
        #     self.positive_memory.append(transition)
        # else:
        #     self.negative_memory.append(transition)

    # Trains main network every step during episode
    def train(self, terminal_state, step):

        # Start training only if certain number of samples is already saved
        if len(self.replay_memory) < MIN_REPLAY_MEMORY_SIZE:
            return

        # Get a minibatch of random samples from memory replay table
        minibatch = random.sample(self.replay_memory, MINIBATCH_SIZE)

        # Get current states from minibatch, then query NN model for Q values
        current_states = np.array([transition[0]
                                   for transition in minibatch])
        current_qs_list = self.model.predict(current_states)

        # Get future states from minibatch, then query NN model for Q values
        # When using target network, query it, otherwise main network should be queried
        new_current_states = np.array(
            [transition[3] for transition in minibatch])
        future_qs_list = self.target_model.predict(new_current_states)

        X = []
        y = []

        # Now we need to enumerate our batches
        for index, (current_state, action, reward, new_current_state, old_state, done) in enumerate(minibatch):

            # If not a terminal state, get new q from future states, otherwise set it to 0
            # almost like with Q Learning, but we use just part of equation here
            if not done and not np.array_equal(current_state, new_current_state) and not np.array_equal(old_state, new_current_state):
                max_future_q = np.max(future_qs_list[index])
                new_q = reward + DISCOUNT * max_future_q
            else:
                new_q = reward

            # Update Q value for given state
            current_qs = current_qs_list[index]
            current_qs[action] = new_q

            # And append to our training data
            X.append(current_state)
            y.append(current_qs)

        # Fit on all samples as one batch, log only on terminal state
        self.model.fit(np.array(X), np.array(y), batch_size=MINIBATCH_SIZE, verbose=0,
                       shuffle=False, callbacks=[self.tensorboard] if terminal_state else None)

        # Update target network counter every episode
        if terminal_state:
            self.target_update_counter += 1

        # If counter reaches set value, update target network with weights of main network
        if self.target_update_counter > UPDATE_TARGET_EVERY:
            self.target_model.set_weights(self.model.get_weights())
            self.target_update_counter = 0

    # Queries main network for Q values given current observation space (environment state)
    def get_qs(self, state):
        return self.model.predict(np.array(state).reshape(-1, *state.shape))
