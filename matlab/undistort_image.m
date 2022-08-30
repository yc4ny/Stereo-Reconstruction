IntrinsicMatrix = [1769.60561310104 0 0; 0 1763.89532833387 0; 1927.08704019384 1064.40054933721 1 ];
radialDistortion = [-0.244052127306437,0.0597008096110524];


cameraParams = cameraParameters('IntrinsicMatrix',IntrinsicMatrix,'RadialDistortion',radialDistortion); 


files = dir("pose/C1/*.jpg");
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("pose/C1/"+filename);
    J = undistortImage(I,cameraParams);
    imwrite(J, sprintf('pose/C1_undistort/%d.jpg',i))

end
