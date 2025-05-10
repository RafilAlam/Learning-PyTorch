import torch

args = torch.ones(2, 2), torch.rand(2, 2)
DesiredOperation = "sub"

ListofOperations = {
    "add": torch.add(*args),     # Addition of Tensors
    "sub": torch.sub(*args),     # Subtraction of Tensors
    "mul": torch.mul(*args),     # Multiplication of Tensors
    "div": torch.div(*args),     # Division of Tensors
    "pow": torch.pow(*args),     # Power of Tensors
    "dot": torch.dot(*args),     # Dot Product of Tensors
    "mm": torch.mm(*args),       # Matrix Multiplication of Tensors
}

print(f'{DesiredOperation} {args[0]} and {args[1]}: \n\n {ListofOperations[DesiredOperation]}')