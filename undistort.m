IntrinsicMatrix = [1793.40866450411,0,0;0,1784.34883485341,0;1941.82280218514,1079.49235904473,1];
radialDistortion = [0.247779937548622,0.0637764128399176];
cameraParams = cameraParameters('IntrinsicMatrix',IntrinsicMatrix,'RadialDistortion',radialDistortion); 
%disp(C1)
files = dir("C2_frames/*.jpg");
for i = 1:numel(files)
    filename = files(i).name;
    I = imread("C2_frames/"+filename);
    J = undistortImage(I,C1_intrinsic);
    imwrite(J, sprintf('C2_undistorted/%d.jpg',i))

end