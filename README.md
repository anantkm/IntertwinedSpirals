
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<HTML>
<HEAD>
</HEAD>
<BODY LANG="EN">
<h2 align=center>COMP9444 Neural Networks and Deep Learning</h2>
<h2 align=center>Twin Spirals Task</h2>
For Part 2 you will be training on the famous
Two Spirals Problem (Lang and Witbrock, 1988).
The supplied code
<code>spiral_main.py</code>
loads the training data from
<code>spirals.csv</code>,
applies the specified model and produces a graph of the resulting function,
along with the data.
For this task there is no test set as such,
but we instead judge the generalization
by plotting the function computed by the network
and making a visual assessment.
<ol>
<li> 
Provide code for a Pytorch Module called
<code>PolarNet</code>
which operates as follows:
First, the input <code>(x,y)</code> is converted
to polar co-ordinates <code>(r,a)</code> with
<code>r=sqrt(x*x + y*y)</code>, <code>a=atan2(y,x)</code>.
Next, <code>(r,a)</code> is fed into a 
fully connected neural network with one hidden layer using <code>tanh</code>
activation, followed by a single output using <code>sigmoid</code>
activation. The conversion to polar coordinates should be
included in your <code>forward()</code> method, so that the
Module performs the entire task of conversion followed by
network layers.
<p>
<li> [1 mark]
Run the code by typing
<pre>
python3 spiral_main.py --net polar --hid 10
</pre>
Try to find the minimum number of hidden nodes required
so that this PolarNet
learns to correctly classify all of the training data
within 20000 epochs, on almost all runs.
The <code>graph_output()</code> method will generate a picture of the function
computed by your PolarNet called <code>polar_out.png</code>,
which you should include in your report.
<p>
<li>
Provide code for a Pytorch Module called
<code>RawNet</code>
which operates on the raw input <code>(x,y)</code>
without converting to polar coordinates.
Your network should consist of two fully connected hidden layers
with tanh activation, plus the output layer, with sigmoid activation.
You should <b>not</b> use <code>Sequential</code> but should instead
build the network from individual components as shown
in the program <code>xor.py</code> from Exercises 5
(repeated in slide 4 of lecture slides 3b on PyTorch).
The number of neurons in both
hidden layers should be determined by the parameter <code>num_hid</code>.
<p>
<li> 
Run the code by typing
<pre>
python3 spiral_main.py --net raw
</pre>
Keeping the number of hidden nodes in each layer fixed at 10,
try to find a value for the size of the initial weights (--init)
such that this RawNet learns to correctly classify all of the training data
within 20000 epochs, on almost all runs.
Include in your report the number of hidden nodes,
and the values of any other metaparameters.
The <code>graph_output()</code> method will generate a picture of the function
computed by your RawNet called <code>raw_out.png</code>,
which you should include in your report.
<p>
<li> 
Provide code for a Pytorch Module called
<code>ShortNet</code>
which again operates on the raw input <code>(x,y)</code>
without converting to polar coordinates.
This network should again consist of two hidden layers (with tanh activation)
plus the output layer (with sigmoid activation),
but this time should include short-cut connections
between every pair of layers (<code>input, hid1, hid2</code> and <code>output</code>)
as depicted on slide 10 of lecture slides 3a on Hidden Unit Dynamics.
Note, however that this diagram shows only two hidden nodes in each
layer, which is not enough to learn the task;
in your code the number of neurons in both
hidden layers should be determined by the parameter <code>num_hid</code>.
<p>
<li> 
Run the code by typing
<pre>
python3 spiral_main.py --net short
</pre>
You should experiment to find a good value for the initial weight size,
and try to find the mininum number of hidden nodes per layer
so that this ShortNet
learns to correctly classify all of the training data
within 20000 epochs, on almost all runs.
Include in your report the number of hidden nodes per layer,
as well as the initial weight size and any other metaparameters.
The <code>graph_output()</code> method will generate a picture of the function
computed by your ShortNet called <code>short_out.png</code>,
which you should include in your report.
<p>
<li> 
Using <code>graph_output()</code> as a guide, write a method called
<code>graph_hidden(net, layer, node)</code>
which plots the activation
(after applying the <code>tanh</code> function) of
the hidden node with the specified number <code>(node)</code>
in the specified <code>layer</code> (1 or 2).
(Note: if <code>net</code> is of type <code>PolarNet</code>,
<code>graph_output()</code> only needs to behave correctly when layer is 1).
<p>
Hint: you might need to modify <code>forward()</code>
so that the hidden unit activations are retained, i.e.
replace <code>hid1 = torch.tanh(...)</code> with
<code>self.hid1 = torch.tanh(...)</code>
<p>
Use this code to generate plots of all the hidden nodes
in PolarNet, and all the hidden nodes in both layers of
RawNet and ShortNet,
and include them in your report.
</ol>

</ol>
</BODY>
</HTML>
