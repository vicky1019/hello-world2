import tensorflow as tf
import tensorflow_addons as tf_ad


class LSTMCRFModel(tf.keras.Model):
    def __init__(self, hidden_num, label_size, lstm_layer='gru', crf_layer=True):
        super(LSTMCRFModel, self).__init__()
        self.num_hidden = hidden_num
        self.label_size = label_size

        self.bilstm = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(hidden_num, return_sequences=True))
        self.bigru = tf.keras.layers.Bidirectional(tf.keras.layers.GRU(hidden_num, return_sequences=True))
        self.dense = tf.keras.layers.Dense(label_size)

        self.transition_params = tf.Variable(tf.random.uniform(shape=(label_size, label_size)))
        # self.dropout = tf.keras.layers.Dropout(0.5)

        self.lstm_layer = lstm_layer
        self.crf_layer = crf_layer

    # @tf.function
    def call(self, embeddings, labels=None, text_lens=None, training=None):
        # dropouts = self.dropout(embeddings, training)
        if self.lstm_layer == 'lstm':
            bilstms = self.bilstm(embeddings)
            logits = self.dense(bilstms)
        elif self.lstm_layer == 'gru':
            bigrus = self.bigru(embeddings)
            logits = self.dense(bigrus)
        else:
            logits = self.dense(embeddings)

        if labels is not None:
            if self.crf_layer:
                label_sequences = tf.convert_to_tensor(labels, dtype=tf.int32)
                log_likelihood, self.transition_params = tf_ad.text.crf_log_likelihood(logits,
                                                                                       label_sequences,
                                                                                       text_lens,
                                                                                       transition_params=self.transition_params)
                return logits, log_likelihood
            else:
                return logits, None
        else:
            return logits
