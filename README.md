# Leakage-Resistant Rice Leaf Disease Classification

Research repository for the study **“Leakage-Resistant Rice Leaf Disease Classification Under Class Imbalance: An Empirical Study of Moderated Class Weighting and Cross-Split Generalization.”**

## Study summary
This study evaluates lightweight rice leaf disease classification under class imbalance using a frozen ImageNet-pretrained MobileNetV2. The RiceLeafDiseaseBD Version 2 dataset was audited for exact duplicate content and conflicting labels before a stratified 7,777/972/973 train/validation/held-out-test split. Three training strategies were compared: unweighted baseline, full inverse-frequency class weighting, and moderated weighting using the square root of the inverse-frequency weights.

## Main result
Moderated weighting was selected using validation Macro-F1. It achieved **64.61% validation accuracy, 58.41% validation Macro-F1, and 63.22% validation Weighted-F1**. On the locked held-out test set it achieved **60.12% accuracy and 53.14% Macro-F1**. Leaf Smut remained the weakest class (11.54% test F1), while Sheath Blight, Rice Tungro, and Healthy were substantially stronger.

## Dataset
RiceLeafDiseaseBD, Version 2 (Mendeley Data), DOI: **10.17632/86s4jzj2m4.2**.

The dataset is not redistributed in this repository. Obtain the exact Version 2 release from the dataset provider and follow its license/terms.

## Repository contents
- `paper/` — research manuscript PDF
- `figures/` — final figures extracted from the manuscript
- `results/` — final reported metrics and analysis tables
- `code/` — documented experiment/reproduction workflow
- `data/` — dataset and manifest documentation; no image dataset is redistributed
- `models/` — model artifact documentation; model weights are not redistributed here
- `docs/` — reproducibility notes

## Important reproducibility note
The original experiments were conducted in Google Colab and the authoritative outputs were saved during experimentation. The scripts in `code/` document the finalized protocol and provide a clean starting point for reproduction; they should not be interpreted as a claim that the original Colab notebook is reproduced byte-for-byte.

## Research integrity
The held-out test set was locked before final evaluation and was not used for model selection. The study is presented as an empirical reliability/generalization analysis, not as a state-of-the-art claim or production-ready diagnostic system.

## Citation
See `CITATION.cff`.
