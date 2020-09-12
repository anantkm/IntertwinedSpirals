# spiral.py
# COMP9444, CSE, UNSW
#Author: Anant Krishna Mahale | z5277610

import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.nn.functional as F
import math


class PolarNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(PolarNet, self).__init__()
        # INSERT CODE HERE
        self.fc_layer_1 = nn.Linear(2, num_hid)
        self.fc_layer_2 = nn.Linear(num_hid, 1)

    def forward(self, input):
        raw_x=input[:,0]
        raw_y=input[:,1]
        #convertion to polar co-ordinates from the inputs. 
        x_square = raw_x**2
        y_square = raw_y**2
        sqaure_sum = x_square + y_square
        sqrt_sqaure_sum=torch.sqrt(sqaure_sum)
        r=sqrt_sqaure_sum.reshape(-1,1) #final r
        
        temp_a=torch.atan2(raw_y,raw_x)
        a = temp_a.reshape(-1,1) # final a
        
        new_input = torch.cat( (r,a) ,1)

        hidden_s1 = self.fc_layer_1(new_input)
        self.layer_1_sum = torch.tanh(hidden_s1)
        hidden_s2 = self.fc_layer_2(self.layer_1_sum )
        self.output = torch.sigmoid(hidden_s2)
        return  self.output

class RawNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(RawNet, self).__init__()
        self.fc_layer_1 = nn.Linear(2, num_hid)
        self.fc_layer_2 = nn.Linear(num_hid,num_hid )
        self.fc_layer_3 = nn.Linear(num_hid,1 )        

    def forward(self, input):
        hidden_s1 = self.fc_layer_1(input)
        self.layer_1_sum = torch.tanh(hidden_s1)
        hidden_s2 = self.fc_layer_2(self.layer_1_sum)
        self.layer_2_sum  = torch.tanh(hidden_s2)
        hidden_s3 = self.fc_layer_3(self.layer_2_sum)
        self.output  = torch.sigmoid(hidden_s3)
        return(self.output)

class ShortNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(ShortNet, self).__init__()
        # INSERT CODE HERE
        self.layer_1 =nn.Linear(2,num_hid)
        self.layer_2=nn.Linear(num_hid+2,num_hid) 
        self.layer_3=nn.Linear(num_hid+num_hid+2,1) 

    def forward(self, input):
        
        hidden_s1 = self.layer_1(input)
        self.layer_1_sum = torch.tanh(hidden_s1)
        temp_1 = torch.cat( (self.layer_1_sum,input) , 1)
        
        hidden_s2 = self.layer_2(temp_1)
        self.layer_2_sum = torch.tanh(hidden_s2)
        temp_2 = torch.cat( (self.layer_2_sum,self.layer_1_sum,input) , 1)
        
        hidden_s3 = self.layer_3(temp_2)
        self.output = torch.sigmoid(hidden_s3)
        return self.output

def graph_hidden(net, layer, node):
    xrange = torch.arange(start=-7,end=7.1,step=0.01,dtype=torch.float32)
    yrange = torch.arange(start=-6.6,end=6.7,step=0.01,dtype=torch.float32)
    xcoord = xrange.repeat(yrange.size()[0])
    ycoord = torch.repeat_interleave(yrange, xrange.size()[0], dim=0)
    grid = torch.cat((xcoord.unsqueeze(1),ycoord.unsqueeze(1)),1)

    with torch.no_grad(): 
        net.eval()        
        output = net(grid)
        if layer == 1:
            pred = (net.layer_1_sum[:, node]>=0).float()
        elif layer == 2:
            pred = (net.layer_2_sum[:, node]>=0).float()

        # plot function computed by model
        plt.clf()
        plt.pcolormesh(xrange,yrange,pred.cpu().view(yrange.size()[0],xrange.size()[0]), cmap='Wistia')
