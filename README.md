# 🧠 learning-pytorch

A small repo containing programs I wrote while learning the basics of PyTorch. It includes demonstrations of tensor operations, creation methods, and reshaping techniques.

---

## 📂 Files

### `operation.py`

Performs basic tensor operations using PyTorch’s arithmetic and matrix functions.

**Operations include:**
- `add`: Element-wise addition
- `sub`: Element-wise subtraction
- `mul`: Element-wise multiplication
- `div`: Element-wise division
- `pow`: Element-wise exponentiation
- `dot`: Dot product (for 1D tensors)
- `mm`: Matrix multiplication (for 2D tensors)

Example usage:
```python
args = torch.ones(2, 2), torch.rand(2, 2)
torch.sub(*args)
```

---

### `BaseFuncs.py`

Demonstrates different tensor creation functions in PyTorch.

**Functions used:**
- `empty`: Uninitialized tensor
- `rand`: Random tensor
- `zeros`: Tensor of zeros
- `ones`: Tensor of ones
- `tensor`: Tensor from user-defined values

Example usage:
```python
torch.ones(3, 2)  # Creates a 3x2 tensor filled with 1s
```

---

### `AdvFuncs.py`

Shows advanced tensor functionalities such as slicing, reshaping, and value access.

**Included techniques:**
- Tensor slicing (e.g., `[:, 0]`, `[1, :]`, `[1, 1]`)
- Extracting scalar values using `.item()`
- Reshaping tensors using `.view()`

Example usage:
```python
x = torch.rand(5, 3)
x.view(1, 15)  # Reshape into 1 row and 15 columns
```

---

## 🚀 Running

Make sure you have PyTorch installed:

```bash
pip install torch
```

Then run any script:

```bash
python operation.py
python BaseFuncs.py
python AdvFuncs.py
```
