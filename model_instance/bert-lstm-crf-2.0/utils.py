import numpy as np
from transformers import BertTokenizer, TFBertModel


def tokenize(text_list, tags_list, tag_dict, max_token_len):
    """ load tags to dict:
        Args:
            text list
            tag list
            tag dict - {tag: tag id}
        Returns:
            embeddings list - (data size, max token length, 768)
            token length list - (data size, 1)
            tags list - (batch size, max token length, tag size)
    """
    tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
    bert_model = TFBertModel.from_pretrained('bert-base-chinese')

    token_len_list = []
    embeddings_list = []

    for text, tags in zip(text_list, tags_list):
        inputs = tokenizer(text, max_length=max_token_len, padding="max_length", truncation=True, return_tensors="np")
        token_len = np.sum(inputs.data['attention_mask'])

        if token_len - 2 != len(tags):
            continue

        outputs = bert_model(inputs)

        embeddings = outputs.last_hidden_state.numpy()[0]
        embeddings_list.append(embeddings)

        token_len_list.append(token_len)

        tags.insert(0, tag_dict['O'])

        cur_len = len(tags)
        for i in range(cur_len, max_token_len):
            tags.append(tag_dict['O'])

    embeddings_list = np.array(embeddings_list)
    token_len_list = np.array(token_len_list)
    tags_list = np.array(tags_list, dtype=np.int32)

    return embeddings_list, token_len_list, tags_list


def load_tag(file_name):
    """ load tags to dict:
        Args:
            file_name - tags file
        Returns:
            tag dict - {tag: tag id}
    """
    tag_dict = {}
    tag_id = 0
    for line in open(file_name, "r", encoding='utf-8').readlines():
        tag = line.strip()
        tag_dict[tag] = tag_id
        tag_id += 1
    return tag_dict


def load_data(file_name, tag_dict):
    """ load tags to dict:
        Args:
            file_name - annotation file
            tag_dict - tag dict
        Returns:
            text list: numpy array
            tag list: in tag list every member is a tag id
    """
    text_list = []
    tags_list = []

    text = ''
    tags = []
    for line in open(file_name, "r", encoding='utf-8').readlines():
        line = line.strip()
        if line == "end":
            text_list.append(text)
            tags_list.append(tags)

            text = ''
            tags = []
        else:
            try:
                word, tag = line.split()
                text += word

                tag_id = tag_dict[tag]
                tags.append(tag_id)
            except Exception as e:
                print(line, e)

    return text_list, tags_list


if __name__ == "__main__":
    # text = '是一种简单可靠的编程语言。'
    # tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
    # bert_model = TFBertModel.from_pretrained('bert-base-chinese')
    #
    # inputs = tokenizer(text, max_length=512, padding="max_length", truncation=True, return_tensors="np")
    # token_len = np.sum(inputs.data['attention_mask'])
    #
    # outputs = bert_model(inputs)
    #
    # x = 0
    import tensorflow as tf
    tensor = np.array([[1, 2, -1], [1, -1, -1]])
    # mask = np.array([[True, True], [False, False], [True, False]])
    mask = tf.sequence_mask([2, 1], 3)
    print(mask)

    mask = tf.cast(mask, dtype=tf.float32)
    print(mask)

    a = tensor * mask
    print(a)

    y_true = [1, 2]
    y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
    loss = tf.keras.losses.sparse_categorical_crossentropy(y_true, y_pred, from_logits=True)
    print(loss)

    loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y_pred, labels=y_true)
    print(loss)
