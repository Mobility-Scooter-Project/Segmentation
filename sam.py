'''
Segment Anything Model (SAM) File
-A class that contains all SAM model data
'''
import torch

class SegmentAnything:
    def __init__(self):
        # Check if CUDA is available and use GPU if it is
        if torch.cuda.is_available():
            print("The following GPU will be used: ", torch.cuda.get_device_name(0), "\n")
            device=torch.device("cuda")
        else:
            device = torch.device("cpu")

        # The model weights and model type
        sam_checkpoint = "sam_vit_b_01ec64.pth"
        model_type = "vit_b"
        
        