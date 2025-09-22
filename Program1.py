import torch
import numpy as np
# 1. Creating Tensors

a = torch.tensor([1, 2, 3])
b = torch.zeros(2, 3)
c = torch.ones(4)
d = torch.rand(2, 2)
e = torch.randn(2, 2)
f = torch.eye(3)
g = torch.arange(0, 10, 2)
h = torch.linspace(0, 1, 5)

print("Tensor a:", a)
print("Zeros (b):\n", b)
print("Ones (c):", c)
print("Random Uniform (d):\n", d)
print("Random Normal (e):\n", e)
print("Identity Matrix (f):\n", f)
print("Arange (g):", g)
print("Linspace (h):", h)

# 2. Reshaping and Viewing
x = torch.rand(2, 3)
print("Original x:\n", x)
print("Reshape (3, 2):\n", x.view(3, 2))
print("Transpose:\n", x.T)
print("Unsqueeze (add dim):\n", x.unsqueeze(0))
print("Squeeze (remove dim):\n", x.unsqueeze(0).squeeze())

# 3. Arithmetic Operations
a = torch.tensor([1.0, 2.0])
b = torch.tensor([3.0, 4.0])
print("Add:", a + b)
print("Multiply:", a * b)
print("Divide:", a / b)
print("Dot Product:", a @ b)
print("Mean of a:", a.mean())
print("Sum of a:", a.sum())
print("Max of a:", a.max())


# 4. Indexing and Slicing
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print("x[0] (first row):", x[0])
print("x[:,1] (second column):", x[:, 1])
print("x[1,2] (row 1, col 2):", x[1, 2])
print("x[0:2,1:] (slice):\n", x[0:2, 1:])

# 5. Tensor Info
print("Shape:", x.shape)
print("Dimensions:", x.ndim)
print("Data type:", x.dtype)
print("Size:", x.size())
print("Device:", x.device)

# 6. Move to GPU (if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.rand(2, 2).to(device)
print("Tensor on device:", x)


# 7. NumPy Conversion
a_np = np.array([1, 2, 3])
b_torch = torch.from_numpy(a_np)
c_np_back = b_torch.numpy()
print("NumPy to Tensor:", b_torch)
print("Tensor to NumPy:", c_np_back)


# 8. Random Seed
torch.manual_seed(42)
print("Random (with seed):", torch.rand(2, 2))


# 9. In-place Operation
x = torch.tensor([1.0, 2.0])
x.add_(1)
print("In-place addition:", x)

# 10. Autograd Example
x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1
print("Expression y = x^2 + 3x + 1, where x=2")
y.backward()
print("dy/dx:", x.grad)
