import torch

args = torch.rand(5, 3)
DesiredFunction = "view(1, 5)"

ListofTorches = {

    # Slice and return data like a cake

    "slice[:, 0]": args[:, 0],     # Slice and return column 0
    "slice[1, :]": args[1, :],     # Slice and return row 1
    "slice[1, 1]": args[1, 1],     # Slice and return element at row 1, column 1

    # Get actual value of 1 element in your tensor

    "item[1, 1].item()": args[1, 1].item(),

    # View tensor in different shape

    "view(1, 5)": args.view(5, 3), # Change shape of tensor to 1, 5 (Must be multiple eg. [total items/columns = integer] and [total items/row = integer])

    
}

print(f'Before {DesiredFunction}: {args} \n\n After: {ListofTorches[DesiredFunction]}')