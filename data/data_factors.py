import pandas as pd
#import tensorflow_hub as hub
import time
# this is to read all the datasets and creating embedding matrix etc

print("-----------STARTING---------")
start_time = time.time()

read_file_name = '../questions.csv'
#save_file_name = 'similar_questions.csv'
df = pd.read_csv(read_file_name)


#print(df.head())

#embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/2")
#embeddings = embed([
#"The quick brown fox jumps over the lazy dog.",
#"I am a sentence for which I would like to get its embedding"])

df = df[df['is_duplicate']==1]

#print (df.head())
train_input = df['question1'].tolist()
train_output = df['question2'].tolist()

total_len = 149306
print(len(train_input))

train_in = train_input[:104515]
train_out = train_output[:104515]

dev_in = train_input[104515:134376]
dev_out = train_output[104515:134376]

test_in = train_input[134376:]
test_out = train_output[134376:]

#all_data = train_input + train_output
#all_words = []
######
# creating vocab
######
#for t in all_data[:50]:
#	all_words = all_words + t.split()


#vocab = set(all_words)

#sp_char = ['<unk>', '<s>', '</s>']

#print(len(all_words))

#final_vocab = sp_char + all_words

#############################
# saving data
# f1 = open(train_input_file, 'w')
# f1.write(train_input)
# f1.close()
# f1 = open(train_output_file, 'w')
# f1.write(train_output)
# f1.close()
# f1 = open(vocab_file, 'w')
# f1.write(final_vocab)
# f1.close()

train_input_file = 'train.en'
train_output_file = 'train.vi'
dev_input_file = 'dev.en'
dev_output_file = 'dev.vi'
test_input_file = 'test.en'
test_output_file = 'test.vi'
#vocab_file = 'vocab.en'

with open(train_input_file, 'w') as f:
    for item in train_in:
        f.write("%s\n" % item)

with open(train_output_file, 'w') as f:
    for item in train_out:
        f.write("%s\n" % item)

with open(dev_input_file, 'w') as f:
    for item in dev_in:
        f.write("%s\n" % item)

with open(dev_output_file, 'w') as f:
    for item in dev_out:
        f.write("%s\n" % item)

with open(test_input_file, 'w') as f:
    for item in test_in:
        f.write("%s\n" % item)

with open(test_output_file, 'w') as f:
    for item in test_out:
        f.write("%s\n" % item)

print("----------FINISHED----------")
print("--- %s seconds ---" % (time.time() - start_time))


