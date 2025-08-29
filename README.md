# 🛰️ Semantic Segmentation of Aerial Drone Imagery  

This project focuses on **semantic segmentation of aerial drone imagery** using both **CNN-Transformer hybrid models** and **pre-trained DeepLabV3 backbones**.  
The pipeline was designed to handle **high-resolution drone images**, achieving strong segmentation performance across multiple evaluation metrics.  

---

## 📖 Table of Contents  
- [✨ Key Highlights](#-key-highlights)  
- [🖼️ Example Outputs](#-example-outputs)  
- [⚙️ Methodology](#️-methodology)  
- [📊 Results](#-results)  
- [📦 Tech Stack](#-tech-stack)  
- [🔮 Future Improvements](#-future-improvements)  
- [👤 Author](#-author)  

---

## ✨ Key Highlights  
- 🧠 **Computer Vision Model**: Developed a semantic segmentation framework using a **DeepLabV3 backbone** integrated with a **CNN-Transformer hybrid**.  
- 📈 **Performance**: Achieved **84% pixel-wise accuracy**, **60% mIoU**, and an **F1-score of 74%** on a dataset of 400 labeled aerial images.  
- 🔄 **Pipeline Engineering**: Built a complete PyTorch pipeline for data preprocessing, training, and evaluation.  
- 🛠️ **Preprocessing**: Implemented **image tiling** and **mask remapping** for efficient training on high-resolution drone imagery.  
- 📊 **Evaluation Metrics**: Used **mIoU, pixel accuracy, and F1-score** for comprehensive model evaluation.  

---

## 🖼️ Example Outputs  

<img width="1138" height="367" alt="image" src="https://github.com/user-attachments/assets/e3c7f7aa-d681-4546-9dc3-f26698703bd6" />

<img width="836" height="230" alt="image" src="https://github.com/user-attachments/assets/5b84dc22-55f3-4e39-bc2f-3319d5fa2469" />

---

## ⚙️ Methodology  

### 1. Data Preprocessing  
- High-resolution aerial drone images split into **tiles** for GPU-efficient training.  
- Remapped segmentation masks into consistent class labels.  

### 2. Model Architectures  
- **DeepLabV3**: Used pre-trained backbones for semantic segmentation.  
- **Hybrid CNN-Transformer**: Designed a custom architecture combining convolutional layers for local feature extraction and Transformer blocks for global context.  

### 3. Evaluation  
- Metrics: **Mean Intersection over Union (mIoU)**, **Pixel Accuracy**, **F1-score**.  
- Evaluated on a public dataset of **400 labeled aerial drone images**.  

---

## 📊 Results  

| Model                    | Pixel Accuracy | mIoU | F1 Score |  
|---------------------------|----------------|------|----------|  
| DeepLabV3 (pre-trained)   | 81%            | 55%  | 70%      |  
| CNN-Transformer (Hybrid)  | **84%**        | **60%** | **74%** |  

✅ Hybrid CNN-Transformer outperformed baseline DeepLabV3 across all metrics.  

---

## 📦 Tech Stack  
- **Language**: Python 3  
- **Frameworks/Libraries**: PyTorch, Torchvision, NumPy, OpenCV, Matplotlib  
- **Deep Learning**: DeepLabV3, Transformer layers  
- **Tools**: Jupyter Notebook, CUDA-enabled GPU  

---

## 🔮 Future Improvements  
- ✅ Expand dataset with more diverse aerial imagery.  
- ✅ Add support for multi-class segmentation beyond current labels.  
- ✅ Deploy as a web-based visualization tool with FastAPI/Streamlit.  
- ✅ Experiment with Vision Transformers (ViT) and Swin Transformers.  

---

## 👤 Author  
**Jacob Almon**  
- [LinkedIn](https://www.linkedin.com/in/jacob-almon-93a089261/)  
- [GitHub](https://github.com/jacobalmon)  

**Svetya Koppisetty**
- [LinkedIn](https://www.linkedin.com/in/svetyak/)  
- [GitHub](https://github.com/svetya)  

**Connor MacDonald**
- [LinkedIn](https://www.linkedin.com/in/connor-macdonald12/)  
- [GitHub](https://github.com/ConnorM1205)  
---
