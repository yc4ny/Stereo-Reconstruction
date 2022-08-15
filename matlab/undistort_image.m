IntrinsicMatrix = [1769.60561310104 0 0; 0 1763.89532833387 0; 1927.08704019384 1064.40054933721 1 ];
radialDistortion = [-0.244052127306437,0.0597008096110524];


cameraParams = cameraParameters('IntrinsicMatrix',IntrinsicMatrix,'RadialDistortion',radialDistortion); 


files = dir("checkerboard/C1/*.jpg");
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("checkerboard/C1/"+filename);
    J = undistortImage(I,cameraParams);
    imwrite(J, sprintf('checkerboard/%d.jpg',i))

end

files = dir("checkerboard/C2/*.jpg");
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("checkerboard/C2/"+filename);
    J = undistortImage(I,cameraParams);
    imwrite(J, sprintf('checkerboard/C2_undistort/%d.jpg',i))

end


files = dir("checkerboard/C3/*.jpg");
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("checkerboard/C3/"+filename);
    J = undistortImage(I,cameraParams);
    imwrite(J, sprintf('checkerboard/C3_undistort/%d.jpg',i))

end


files = dir("checkerboard/C4/*.jpg");
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("checkerboard/C4/"+filename);
    J = undistortImage(I,cameraParams);
    imwrite(J, sprintf('checkerboard/C4_undistort/%d.jpg',i))

end


files = dir("checkerboard/C5/*.jpg");
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("checkerboard/C5/"+filename);
    J = undistortImage(I,cameraParams);
    imwrite(J, sprintf('checkerboard/C5_undistort/%d.jpg',i))

end

