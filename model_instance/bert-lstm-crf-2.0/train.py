import logging

import tensorflow as tf
import tensorflow_addons as tf_ad

from args_helper import args
from utils import tokenize, load_tag, load_data
from model import LSTMCRFModel


print('load tag and annotation data')
tag_dict = load_tag(args.tag_file)
text_list, tags_list = load_data(args.train_path, tag_dict)
embeddings_list, token_len_list, label_sequences = tokenize(text_list, tags_list, tag_dict, args.max_token_len)

print('build training set')
train_dataset = tf.data.Dataset.from_tensor_slices((embeddings_list, token_len_list, label_sequences))
train_dataset = train_dataset.shuffle(len(embeddings_list)).batch(args.batch_size, drop_remainder=True)

print('build model')
model = LSTMCRFModel(hidden_num=args.hidden_num, label_size=len(tag_dict), lstm_layer='gru')
optimizer = tf.keras.optimizers.Adam(args.lr)

ckpt = tf.train.Checkpoint(optimizer=optimizer, model=model)
# ckpt.restore(tf.train.latest_checkpoint(args.output_dir))
ckpt_manager = tf.train.CheckpointManager(ckpt,
                                          args.output_dir,
                                          checkpoint_name='ner_model.ckpt',
                                          max_to_keep=3)


@tf.function
def train_one_step(embedding_batch, token_len_batch, labels_batch, crf_layer):
    """ calculate loss and update gradient """
    with tf.GradientTape() as tape:
        logits, log_likelihood = model(embedding_batch, labels=labels_batch, text_lens=token_len_batch, training=True)
        if crf_layer:
            loss = - tf.reduce_mean(log_likelihood)
        else:
            # loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=labels_batch)
            loss = tf.keras.losses.sparse_categorical_crossentropy(y_true=labels_batch, y_pred=logits, from_logits=True)
            mask = tf.sequence_mask(token_len_batch, 512)
            mask = tf.cast(mask, dtype=tf.float32)
            loss *= mask
            loss = tf.reduce_mean(loss)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    return loss, logits


def get_acc_one_step(logits, text_lens, labels_batch):
    """ calculate precision """
    paths = []
    accuracy = 0
    for logit, text_len, labels in zip(logits, text_lens, labels_batch):
        viterbi_path, _ = tf_ad.text.viterbi_decode(logit[:text_len], model.transition_params)
        paths.append(viterbi_path)
        correct_prediction = tf.equal(
            tf.convert_to_tensor(tf.keras.preprocessing.sequence.pad_sequences([viterbi_path], padding='post'),
                                 dtype=tf.int32),
            tf.convert_to_tensor(tf.keras.preprocessing.sequence.pad_sequences([labels[:text_len]], padding='post'),
                                 dtype=tf.int32)
        )
        accuracy = accuracy + tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        # print(tf.reduce_mean(tf.cast(correct_prediction, tf.float32)))
    accuracy = accuracy / len(paths)
    return accuracy


print('start training')
best_acc = 0
step = 0
for epoch in range(args.epoch):
    print('epoch', epoch)
    for _, (embedding_batch, token_len_batch, labels_batch) in enumerate(train_dataset):
        step = step + 1
        loss, logits = train_one_step(embedding_batch, token_len_batch, labels_batch, args.crf_layer)
        if step % 20 == 0:
            accuracy = get_acc_one_step(logits, token_len_batch, labels_batch)
            # logging.info('epoch %d, step %d, loss %.4f , accuracy %.4f' % (epoch, step, loss, accuracy))
            print('epoch %d, step %d, loss %.4f , accuracy %.4f' % (epoch, step, loss, accuracy))
            if accuracy > best_acc:
              best_acc = accuracy
              ckpt_manager.save()
              logging.info("model saved")

print('end training')
