import tensorflow as tf


class Agent:

    def __init__(self, num_actions, state_size):
        self.num_actions = num_actions
        self.discount_rate = 0.95

        initializer = tf.contrib.layers.xavier_initializer()

        self.input_layer = tf.placeholder(dtype=tf.float32, shape=[None, 1, state_size])

        hidden_layer_1 = tf.layers.dense(self.input_layer, 8, activation=tf.nn.relu, kernel_initializer=initializer)
        hidden_layer_2 = tf.layers.dense(hidden_layer_1, 8, activation=tf.nn.relu, kernel_initializer=initializer)

        out = tf.layers.dense(hidden_layer_2, self.num_actions, activation=None)

        self.outputs = tf.nn.softmax(out)
        self.choice = tf.argmax(self.outputs, axis=1)

        self.rewards = tf.placeholder(shape=[None, ], dtype=tf.float32)
        self.actions = tf.placeholder(shape=[None, ], dtype=tf.int64)

        one_hot_actions = tf.one_hot(self.actions, self.num_actions)

        cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=out, labels=one_hot_actions)

        self.loss = tf.reduce_mean(cross_entropy * self.rewards)

        self.gradients = tf.gradients(self.loss, tf.trainable_variables())

        self.gradients_to_apply = []
        for index, variable in enumerate(tf.trainable_variables()):
            gradient_placeholder = tf.placeholder(tf.float32)
            self.gradients_to_apply.append(gradient_placeholder)

        optimizer = tf.train.AdamOptimizer(learning_rate=1e-2)

        self.update_gradients = optimizer.apply_gradients(zip(self.gradients_to_apply, tf.trainable_variables()))
