from ast import Num
import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from neuron import bag_of_words,tokenize,stem
from brain import neuralnetwork

with open('intents.json','r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words += w
        xy.append((w,tag))

ignore_words = ['?','!','.',',','/']

all_words = [stem(w) for w in all_words if w not in ignore_words]

all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = []
y_train = []

for (pattern_sent,tag) in xy:
    bag = bag_of_words(pattern_sent,all_words)
    x_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)
    
x_train = np.array(x_train)
y_train = np.array(y_train)

num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(x_train[0])
hidden_size = 8
output_size = len(tags)



class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train
    
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
model = neuralnetwork(input_size,hidden_size,output_size).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for (words,labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        optimizer.zero_grad()
        outputs = model(words)
        loss = criterion(outputs,labels)
        loss.backward()
        optimizer.step()

    if (epoch+1)%100 == 0: #Loss and Accuracy after every 100 epochs
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

print('Final Loss: {:.4f}'.format(loss.item()))

data = {
    'model_state': model.state_dict(),
    'input_size' : input_size,
    'hidden_size' : hidden_size,
    'output_size' : output_size,
    'all_words' : all_words,
    'tags' : tags
}

FILE = 'model.pth'
torch.save(data, FILE)
print('Model Saved')