data = load('spcs_on_spx.txt');
X = data(:,1);
y = data(:,2);
m=length(y)

% plotData(X,y) you would save this in plotData.m
plot(X, y, 'rx', 'MarkerSize', 10);     % Plot the data
ylabel('S&P 500');           % Set the y-axis label
xlabel('Case Shiller 10 City Index') % set the x-axis label

X = [ones(m,1), data(:,1)];
theta = zeros(2, 1)


%function J = costFunction(X, y, theta)
J = 1/(2*m) * sum(((X*theta)-y).^2)

X (:,1) % first column (of ones in the matrix)
X (:,2) % second column (first variable in the model)