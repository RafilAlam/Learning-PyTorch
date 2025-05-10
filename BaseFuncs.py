import torch

args = 3, 2     # Blank groups of Blank (3, 2) = 3 groups of 2, (5) = 1 group of 5
DesiredFunction = "tensor"

ListofTorches = {
    "empty": torch.empty(*args),     # Uninitialised tensor of shape
    "rand": torch.rand(*args),       # Random tensor of shape
    "zeros": torch.zeros(*args),     # Zeros tensor of shape
    "ones": torch.ones(*args),       # Ones tensor of shape
    "tensor": torch.tensor(*args),   # Values tensor of shape
}

print(f'{DesiredFunction}:', ListofTorches[DesiredFunction])