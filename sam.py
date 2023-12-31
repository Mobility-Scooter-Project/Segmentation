'''
Segment Anything Model (SAM) File
-A class that contains all SAM model data
'''
import torch
import numpy as np
from segment_anything import sam_model_registry, SamPredictor

class SegmentAnything:
    # Initializes model
    def __init__(self):
        # Check if CUDA is available and use GPU if it is
        if torch.cuda.is_available():
            print("The following GPU will be used: ", torch.cuda.get_device_name(0), "\n")
            device=torch.device("cuda")
        else:
            device = torch.device("cpu")

        # The model weights and model type
        sam_checkpoint = "assets/sam_vit_b_01ec64.pth"
        model_type = "vit_b"
        
        # Define model and set it to device
        self.model = sam_model_registry[model_type](checkpoint=sam_checkpoint)
        self.model.to(device=device)
        self.predictor = SamPredictor(self.model)

    # Generate mask for a frame with a given input box and returns a mask in the format of a 2D numpy array
    def process(self, frame, input_box):
        self.predictor.set_image(frame)

        mask, _, _ = self.predictor.predict(
        point_coords=None,
        point_labels=None,
        box=input_box[None, :],
        multimask_output=False,
        )

        return np.squeeze(mask)