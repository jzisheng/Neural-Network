import numpy as np

class Neural_Network(object):
	# Set this value to true for print statements
	debug = True
	def __init__(self):
		# Sets up neural network layers
		self.inputLayerSize = 2 	# No. of inputs the neural network takes in
		self.hiddenLayerSize = 2 	# No. of node in hidden layers
		self.outputLayerSize = 1	# No. of outputs of NN
		self.learningRate = 0.5		# Learning rate

		# Initializes weights to random values
		self.W1 = np.random.randn(self.inputLayerSize+1,self.hiddenLayerSize)
		self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)

 	# Feedforward Function
	def forward(self, X):
		# Propogate inputs through network
		self.z2 = np.dot(X,self.W1)
		self.a2 = self.sigmoid(self.z2)
		self.z3 = np.dot(self.a2,self.W2)
		self.yHat = self.sigmoid(self.z3)
		return self.yHat

	# Activation Function
	def sigmoid(self,z):
		# Apply sigmoid activation function
		return 1/(1+np.exp(-z))

	# Derivative of sigmoid prime function
	def sigmoidPrime(self,z):
		return np.multiply((self.sigmoid(z)) , np.subtract(1,self.sigmoid(z)) )

	# Backpropgation Function
	def deltaTrain(self,X,y):
		# Backpropagates error from learned values
		self.yHat = self.forward(X)
		# Backpropagates error to weights from the hidden layer
		# to the output
		delta3 = np.multiply((y-self.yHat), self.sigmoidPrime(self.z3))
		djdW2 = np.dot(self.a2.T,delta3)
		NN.W2 += djdW2*self.learningRate
		# Backpropagates error to weights in the first layer to the hidden layer
		delta2 = np.multiply(np.dot(delta3,self.W2.T),self.sigmoidPrime(self.z2))
		djdW1 = np.dot(X.T,delta2)
		NN.W1 += djdW1*self.learningRate

	# Calculates the error of the neural network
	def errorFunction(self,X,y):
		self.yHat = self.forward(X)
		E = 0.5*sum(np.square(y-self.yHat))
		return E


	def costFunctionPrime(self,X,y):
		self.yHat = self.forward(X)
		delta = np.multiply((y-self.yHat),self.sigmoidPrime(self.z1))
		djdW1 = np.dot(np.transpose(X),delta)
		return djdW1


# Create neural network object class
NN = Neural_Network()
X = np.matrix("0 0 1; 0 1 1; 1 0 1; 1 1 1")
y = np.matrix("0; 1; 1; 0")
print("-- error before---- ")
print(NN.errorFunction(X,y))
for i in range(12000):
	NN.deltaTrain(X,y)
print("-- error after")
print(NN.errorFunction(X,y))
print("-- new weights")
print("-- NN W1")
print(NN.W1)
print("-- NN W2")
print(NN.W2)