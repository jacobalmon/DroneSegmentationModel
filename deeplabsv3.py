import torch
import torchvision.models.segmentation as models
import os

# Create the directory if it doesn't exist
os.makedirs('deeplabsv3', exist_ok=True)

# Load pre-trained DeepLabV3 model
model = models.deeplabv3_resnet101(pretrained=True)
model.eval()

# Save the model
torch.save(model.state_dict(), 'deeplabsv3/deeplabv3_resnet101.pth')