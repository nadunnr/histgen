# HistGen: Histopathology Report Generation

>This repository is a re-implementation of the HistGen framework developed as part of a **Medical Image Processing** course project. This work is based on the original research and codebase by [dddavid4real](https://github.com/dddavid4real/HistGen). All credit for the architectural innovation, methodology, and primary development belongs to the original authors.

---

## Overview

**HistGen** is a Multiple Instance Learning (MIL)-empowered framework designed to automate the generation of clinical histopathology reports from gigapixel Whole Slide Images (WSIs). In clinical workflows, pathologists must manually compile findings into reports, a task that is labor-intensive, time-consuming, and prone to error. 

HistGen addresses these challenges by aligning WSIs and diagnostic reports at both local and global granularities, effectively bridging the gap between massive visual sequences and highly summarized clinical text.



### Key Components

* **Local-Global Hierarchical Encoder (LGH):** This module aggregates visual features from a region-to-slide perspective to capture both fine-grained details and overall diagnostic context.
* **Cross-Modal Context Module (CMC):** Facilitates explicit interaction between visual encoding and textual decoding stages. It serves as an external memory to store and refer to knowledge from previous iterations.
* **DINOv2 Backbone:** Employs a ViT-L model pre-trained on over 55,000 WSIs (approx. 200 million patches) to provide robust and informative patch embeddings for the MIL framework.

---

## Dataset Curation

As part of the framework, a benchmark WSI-report dataset was curated to evaluate performance:
* **Scale:** 7,753 WSI-report pairs encompassing various diseases and primary sites.
* **Source:** Diagnostic reports were downloaded from the TCGA platform.
* **Processing:** Raw text was cleaned and summarized using GPT-4 to remove noise and redundant information.

---

## Implementation Details

The model architecture and training hyperparameters are configured as follows:
* **Visual Encoder:** LGH module with a region size of 96.
* **Textual Decoder:** 3-layer Transformer decoder with 8 attention heads and 512-dimensional hidden states.
* **Context Module:** CMC module with a dimension of $512 \times 2048$.
* **Optimization:** Trained using Cross Entropy loss with the Adam optimizer ($LR = 1 \times 10^{-4}$).
* **Inference:** Beam search with a beam size of 3.

### Objective Function

The training objective is to maximize the conditional probability of the report $T$ given the WSI $I$:

$$\theta^{*} = \arg \max \sum_{i=1}^{t} \log P(y_{i} | y_{1}, y_{2}, \dots, y_{i-1}, I; \theta)$$

where $P(y_{i} | \dots)$ is the probability of generating the next word $y_i$ given the visual input $I$ and preceding tokens.

---

## Citation

If you use this work or refer to the HistGen architecture, please cite the original MICCAI paper:

```text
Guo, Z., Ma, J., Xu, Y., Wang, Y., Wang, L., & Chen, H. (2024). 
HistGen: Histopathology Report Generation via Local-Global Feature Encoding and Cross-modal Context Interaction. 
In International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI).