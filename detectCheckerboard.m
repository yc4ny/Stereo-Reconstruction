files = dir("checkerboard/C1_undistort/*.jpg");
files = natsortfiles(files);
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("checkerboard/C1_undistort/"+filename);
    [imagePoints,boardSize] = detectCheckerboardPoints(I);
    disp(imagePoints)
    save( sprintf('checkerboard/C1_keypoints/%d.mat', i), 'imagePoints');

end

