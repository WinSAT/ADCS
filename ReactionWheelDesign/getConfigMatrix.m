function [configMatrix] = getConfigMatrix(beta, maxRWTorques)
configMatrix = [];

configMatrix = [configMatrix maxRWTorques(1)*[cos(beta); 0; sin(beta)]];
configMatrix = [configMatrix maxRWTorques(2)*[0; cos(beta); sin(beta)]];
configMatrix = [configMatrix maxRWTorques(3)*[-cos(beta); 0; sin(beta)]];
configMatrix = [configMatrix maxRWTorques(4)*[0; -cos(beta); sin(beta)]];

end