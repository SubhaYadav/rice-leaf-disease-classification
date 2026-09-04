# Reproducibility notes

## Audit
Exact-content hashing was applied to all 9,769 original images. The audit found 9,730 unique image contents, 39 duplicate hash groups, and 78 files involved in duplicate groups, including 8 conflicting-label groups. Conflicting duplicate groups were removed; redundant same-class copies were reduced to one representative.

## Split
The cleaned 9,722 images were stratified into 7,777 training and 1,945 temporary validation images. That 1,945-image validation pool was then stratified 50/50 into 972 final validation and 973 locked test images.

## Selection
Macro-F1 was the primary selection criterion. The test set was not used for selection.
