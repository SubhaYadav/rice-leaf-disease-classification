# Code

The study was executed in Google Colab. The authoritative experiment outputs are preserved in `results/`. This folder is a clean documentation/reproduction scaffold rather than a byte-for-byte export of the original interactive notebook.

Final protocol: TensorFlow/Keras, 224x224 RGB inputs, batch size 32, MobileNetV2 with ImageNet weights and frozen base, horizontal flip/rotation/zoom/contrast augmentation, Adam learning rate 1e-4, sparse categorical cross-entropy, maximum 12 epochs, validation-loss checkpointing, early stopping patience 3, and ReduceLROnPlateau patience 2.

Do not use the held-out test set for tuning.
