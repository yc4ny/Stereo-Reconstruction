files = dir("checkerboard/C2_undistort/*.jpg");
files = natsortfiles(files);
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("checkerboard/C2_undistort/"+filename);
    [imagePoints,boardSize] = detectCheckerboardPoints(I);
    disp(imagePoints)
    save( sprintf('checkerboard/C2_keypoints/%d.mat', i), 'imagePoints');

end

files = dir("checkerboard/C3_undistort/*.jpg");
files = natsortfiles(files);
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("checkerboard/C3_undistort/"+filename);
    [imagePoints,boardSize] = detectCheckerboardPoints(I);
    disp(imagePoints)
    save( sprintf('checkerboard/C3_keypoints/%d.mat', i), 'imagePoints');

end

