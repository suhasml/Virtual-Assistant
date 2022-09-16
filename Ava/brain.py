import torch.nn as nn

class neuralnetwork(nn.Module):

    def __init__(self,input_size,hidden_size,num_classes):
        super(neuralnetwork,self).__init__()
        self.l1 = nn.Linear(input_size,hidden_size)  #Layer 1
        self.l2 = nn.Linear(hidden_size,hidden_size) #Layer 2 
        self.l3 = nn.Linear(hidden_size,num_classes) #Layer 3
        self.relu = nn.ReLU()

    
    def forward(self,x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        #forward propogation
        return out