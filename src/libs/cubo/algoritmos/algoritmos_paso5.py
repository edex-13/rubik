from src.permutaciones import R, R_PRIMA, L, L_PRIMA, U, U_PRIMA, D, D_PRIMA, F, F_PRIMA, B, B_PRIMA


uno = [R_PRIMA, F, R_PRIMA, B, B, R, F_PRIMA, R_PRIMA, B, B, R, R]
dos = [R_PRIMA, B_PRIMA, R, U_PRIMA, R, D, R_PRIMA, U, R, D_PRIMA, R, R, B, R]
tres = [F, U_PRIMA, R, U_PRIMA, R, U, R_PRIMA, U, R, U, U,
        R_PRIMA, U, R_PRIMA, U_PRIMA, R, U, U, R_PRIMA, F_PRIMA]
cuatro = [R_PRIMA, U, R, U_PRIMA, R, R, F_PRIMA,
          U_PRIMA, F, U, R, F, R_PRIMA, F_PRIMA, R, R]
cinco = [R, R, U, R_PRIMA, U, R_PRIMA, U_PRIMA, R,
         U_PRIMA, R, R, U_PRIMA, D, R_PRIMA, U, R, D_PRIMA]
seis = [R_PRIMA, U_PRIMA, R, U, D_PRIMA, R, R, U,
        R_PRIMA, U, R, U_PRIMA, R, U_PRIMA, R, R, D]
siete = [R, R, U_PRIMA, R, U_PRIMA, R, U, R_PRIMA,
         U, R, R, D_PRIMA, U, R, U_PRIMA, R_PRIMA, D]
ocho = [R, U, R_PRIMA, U_PRIMA, D, R, R, U_PRIMA, R,
        U_PRIMA, R_PRIMA, U, R_PRIMA, U, R, R, D_PRIMA]
nueve = [R, R, U, U, R, U, U, R, R, U, U, R, R, U, U, R, U, U, R, R]
diez = [L_PRIMA, U_PRIMA, L, F, L_PRIMA, U_PRIMA, L, U, L, F_PRIMA, L, L, U, L]
once = [R, U, R_PRIMA, F_PRIMA, R, U, R_PRIMA,
        U_PRIMA, R_PRIMA, F, R, R, U_PRIMA, R_PRIMA]
doce = [R, F, U_PRIMA, R_PRIMA, U, R, U, F_PRIMA,
        R, R, F_PRIMA, R, U, R, U_PRIMA, R_PRIMA, F]
trece = [R_PRIMA, U, R, U_PRIMA, R_PRIMA, F_PRIMA, U_PRIMA,
         F, R, U, R_PRIMA, F, R_PRIMA, F_PRIMA, R, U_PRIMA, R]
catorce = [L, U, U, L_PRIMA, U, U, L, F_PRIMA,
           L_PRIMA, U_PRIMA, L, U, L, F, L, L]

quince = [R_PRIMA, U, U, R, U, U, R_PRIMA, F, R,
          U, R_PRIMA, U_PRIMA, R_PRIMA, F_PRIMA, R, R]

diesies = [R_PRIMA, U, R_PRIMA, U_PRIMA, R, D_PRIMA, R_PRIMA,
           D, R_PRIMA, U, D_PRIMA, R, R, U_PRIMA, R, R, D, R, R]

M_17 = [R, U, R_PRIMA, U_PRIMA, R_PRIMA, F, R, R,
        U_PRIMA, R_PRIMA, U, F_PRIMA, L_PRIMA, U, L]
M_18 = [R, R, U_PRIMA, R_PRIMA, U_PRIMA, R, U, R, U, R, U_PRIMA, R]
M_19 = [R_PRIMA, U, R_PRIMA, U_PRIMA, R_PRIMA, U_PRIMA, R_PRIMA, U, R, U, R, R]
M_20 = [F, R_PRIMA, F, R, R, U_PRIMA, R_PRIMA, U_PRIMA, R,
        U, R_PRIMA, F_PRIMA, R, U, R_PRIMA, U_PRIMA, F_PRIMA]
M_21 = [U, R_PRIMA, U_PRIMA, R, U_PRIMA, R, U, R,
        U_PRIMA, R_PRIMA, U, R, U, R, R, U_PRIMA, R_PRIMA]

algoritmos = [uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez,
              once, doce, trece, catorce, quince, diesies, M_17, M_18, M_19, M_20, M_21]

