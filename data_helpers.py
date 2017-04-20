import numpy as np
import re
import itertools
from collections import Counter


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data_and_labels(fashion_data_file, finance_data_file, law_data_file, lifestyle_data_file):
    """
    Loads guardian data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    fashion_examples = list(open(fashion_data_file, "r").readlines())
    fashion_examples = [s.strip() for s in fashion_examples]
    finance_examples = list(open(finance_data_file, "r").readlines())
    finance_examples = [s.strip() for s in finance_examples]
    law_examples = list(open(law_data_file, "r").readlines())
    lifestyle_examples = list(open(lifestyle_data_file, "r").readlines())
    law_examples = [s.strip() for s in law_examples]
    lifestyle_examples = [s.strip() for s in lifestyle_examples]
    
	# Split by words
    x_text = fashion_examples + finance_examples + law_examples + lifestyle_examples
    x_text = [clean_str(sent) for sent in x_text]
    
	# Generate labels
    fashion_labels = [[1, 0, 0, 0] for _ in fashion_examples]
    finance_labels = [[0, 1, 0, 0] for _ in finance_examples]
    law_labels = [[0, 0, 1, 0] for _ in law_examples]
    lifestyle_labels = [[0, 0, 0, 1] for _ in lifestyle_examples]
    y = np.concatenate([fashion_labels, finance_labels, law_labels, lifestyle_labels], 0)
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int(len(data)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]
