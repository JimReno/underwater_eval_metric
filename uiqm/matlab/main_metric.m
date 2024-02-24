% Files = dir(strcat('../J/','*.jpg'));
% number=length(Files);
% for i=1:number
%     i
%     filename = Files(i).name;
%     img = imread(['../J/',filename]);
%     uiqm = UIQM(img);
%     uiqm =roundn(uiqm,-4);
%     score(i) = uiqm;
% 
% mean(score)

function uiqm_result=main_metric(file_path)
    % filename = 'm906_img_.png';
    img = imread(file_path);
    uiqm_result = UIQM(img);
end




