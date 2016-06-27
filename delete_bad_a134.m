%% read data and mask bad points with GUI

fin='varres.txt'

indata=importdata(fin,' ',2);

dat=indata.data;
header=indata.textdata;

figure(1),clf
plot(dat(:,2),dat(:,3),'b.'),hold on

pmask = PolyDraw

in=inpolygon(dat(:,2),dat(:,3),pmask(1,:),pmask(2,:));
plot(dat(in,2),dat(in,3),'rx')


dat(in,:)=[];
plot(dat(:,2),dat(:,3),'gs')

%fix index column
dat(:,1)=1:length(dat(:,1))

%% output results

fout='A134L_detrend_mm_resamp.txt'

fid = fopen(fout, 'w');
% Table Header
for i=1:length(header)
  fprintf(fid, [header{i} '\n']);
end
fclose(fid);
dlmwrite(fout, dat, 'delimiter',' ', '-append')

figure(2),clf
plot(dat(:,2),dat(:,3),'b.'),hold on
