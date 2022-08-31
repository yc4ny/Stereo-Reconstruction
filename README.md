# Stereo Reconstruction - Reconstructing 3D Human Keypoints from 2D Images
This is my implementation of Stereo Camera Reconstruction using DLT (Direct Linear Transform), Triangulation with Linear/Non-Linear Optimization through Python. <br/> 

![Stereo Reconstruction Final Results](git_images/checkerboard_result.png)<br/>
> - Red points indicate the 2D reprojection of the reconstructed 3D points. <br/>
> - Green points indicate the 2D points found by MATLAB's Camera Calibrator.<br/> 
> - The "ON" sign in green indicates that the checkerboard points have been detected with MATLAB's calibrator. There must be at least 2 cameras with "ON" sign in order to reconstruct 3D points.<br/> 
> - The "Frame Error" indicates the average reprojection error (Euclidean distance) of points of the reconstructed 3D points. <br/>

![Stereo Reconstruction Final Results](git_images/openpose_result.png)<br/><br/> 
> - Green joints indicate the 2D reprojection of the reconstructed 3D joints. <br/>
> - Orange joints indicate the 2D joints found by openpose.<br/> 
> - The "Frame Reprojection Error" indicates the average reprojection error (Euclidean distance) of points of the reconstructed 3D joints. <br/>

## Environment Setup
> Note: This code was developed on Ubuntu 20.04/22.04 with Python 3.7. Later versions should work, but have not been tested.
Create and activate a virtual environment to work in, e.g. using Conda:

```
conda create -n venv_stereo python=3.7
conda activate venv_stereo
```
Install the remaining requirements with pip:
```
pip install -r requirements.txt
```

You must also have _ffmpeg_ installed on your system to save visualizations. <br/>
I have used 5 GOPRO10 cameras for this task. If you are using more or less cameras, you need to modify the DLT, optimization code. 

### OpenPose
[OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) is used to detect 2D joints from arbitrary RGB videos.<br/>
 Please install openpose and run it on your undistorted image frames to locate the 2D keypoints. <br/> 
 For the format of the output pose, this code is based on the "BODY_25" format, please add the ```--model_pose BODY_25 ``` flags in order to match the format of the output .json files used in this repo. <br/>
<img src="git_images/keypoints_pose_25.png" width="200">

