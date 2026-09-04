"""Final documented experimental protocol for the rice disease study.
This file records the finalized settings; it is not a replacement for the original Colab run history.
"""
IMG_SIZE=(224,224)
BATCH_SIZE=32
SEED=42
CLASS_NAMES=["Blast","Brown spot","Healthy","Leaf smut","Rice Tungro","Sheath blight"]
MAX_EPOCHS=12
LEARNING_RATE=1e-4
MODERATION_ALPHA=0.5
TRAIN_COUNT=7777
VALIDATION_COUNT=972
HELD_OUT_TEST_COUNT=973
