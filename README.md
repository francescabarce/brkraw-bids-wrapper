# 🧠 brkraw-bids-wrapper

This repository contains a modified version of the [`brkraw`](https://github.com/CobraLab/brkraw) library along with a Python wrapper script that automates the conversion of Bruker MRI datasets into the BIDS format. It is specifically tailored for **preclinical rodent imaging** and includes a crucial modification that scales the voxel size by a factor of **10×**.

---

## 🚀 Purpose

Many widely-used neuroimaging tools such as **FSL** are optimized for human MRI data and make strong assumptions about image dimensions and voxel sizes. Since **rodent brains are significantly smaller**, using the original voxel sizes from Bruker data can cause problems during preprocessing and registration steps (e.g., erroneous skull stripping, segmentation failures, or misaligned transformations).

To address this, we modify `brkraw` to **artificially inflate voxel sizes by a factor of 10** during the conversion process. This allows rodent data to be processed by tools like FSL, while still maintaining relative spatial fidelity.

---

## 🛠️ Main Components

- `brkraw/`: Modified version of the original `brkraw` library, with changes to scale voxel sizes ×10.
- `run_brkraw_pipeline.py`: A Python script that:
  1. Removes subfolders containing fieldmaps (if present)
  2. Runs `brkraw tonii` to convert raw Bruker data to NIfTI
  3. Generates BIDS-compatible metadata files via `brkraw bids_helper`
  4. Converts the dataset to full BIDS format using `brkraw bids_convert`

---

## 📦 Why the voxel size ×10 modification?

### ❌ Problem

Rodent brain MRI datasets typically have voxel sizes in the range of ~0.1–0.3 mm. When passed into tools like FSL, these small dimensions lead to:
- Unexpected behavior in spatial filters and segmentation
- Alignment errors during registration
- Failures in BIDS compliance checks

### ✅ Solution

This modified version of `brkraw` multiplies voxel sizes by 10 during the conversion:
- A voxel of `0.2 mm` becomes `2 mm`
- The relative geometry is preserved
- Preprocessing tools behave as expected
- Allows downstream BIDS tools and neuroimaging pipelines to work out-of-the-box

---

## ▶️ How to Use

From a terminal:
install the library: pip install -e ./brkraw_fra

```bash
python run_brkraw_pipeline.py
