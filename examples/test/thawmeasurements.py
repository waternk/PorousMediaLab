import numpy as np

C1h = np.array([0.000000327, 0.000010505, 0.000000490, 0.000007643, 0.000000572, 0.000008502, 0.000000082, 0.000007889,
                0.000000, 0.000000,                     0.000000, 0.000000, 0.000000, 0.000000,
                0.000001, 0.000052, 0.000002, 0.000031, 0.000002, 0.000021, 0.000001, 0.000019,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000000, 0.000026, 0.000001, 0.000024, 0.000000, 0.000033, 0.000001, 0.000021,
                0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]) #nmol/cm^3

C1h_nz = np.array([0.000000327, 0.000010505, 0.000000490, 0.000007643, 0.000000572, 0.000008502, 0.000000082, 0.000007889,
                0.000001, 0.000052, 0.000002, 0.000031, 0.000002, 0.000021, 0.000001, 0.000019,
                0.000000, 0.000026, 0.000001, 0.000024, 0.000000, 0.000033, 0.000001, 0.000021])

Tm_nz = np.array([ 3, 21, 46, 94, 309,  328, 351, 401, 599, 623, 645, 691])

T1C1h = np.array([0.000000, 0.000011, 0.000000, 0.000008, 0.000001, 0.000009, 0.000000, 0.000008]) # nmol/cm^3

F1C1h = np.array([0.000000, 0.000000,                     0.000000, 0.000000, 0.000000, 0.000000]) # nmol/cm^3

T2C1h = np.array([0.000001, 0.000053, 0.000002, 0.000031, 0.000002, 0.000021, 0.000001, 0.000019]) # nmol/cm^3

F2C1h = np.array([0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]) # nmol/cm^3

T3C1h = np.array([0.000000, 0.000027, 0.000001, 0.000024, 0.000000, 0.000033, 0.000001, 0.000021]) # nmol/cm^3

F3C1h = np.array([0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]) # nmol/cm^3






C1D9 = np.array([0.000389, 0.000400, 0.001464, 0.000750, 0.000828, 0.000491, 0.000602, 0.001139,
                np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                0.001073, 0.000982, 0.001046, 0.001035, 0.001256, 0.000782, 0.001450, 0.002173,
                np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                0.001392, 0.000924, 0.001022, 0.001839, 0.002795, 0.004447, 0.004556, 0.004333,
                np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]) # nmol/cm^3


T1C1D9 = np.array([0.000389, 0.000400, 0.001464, 0.000750, 0.000828, 0.000491, 0.000602, 0.001139]) # nmol/cm^3

T2C1D9 = np.array([0.001073, 0.000982, 0.001046, 0.001035, 0.001256, 0.000782, 0.001450, 0.002173]) # nmol/cm^3

T3C1D9 = np.array([0.001392, 0.000924, 0.001022, 0.001839, 0.002795, 0.004447, 0.004556, 0.004333]) # nmol/cm^3




C1D21 = np.array([0.000265, 0.000199, 0.002026, 0.000789, 0.000512, 0.000170, 0.001078, 0.000844,
                  0.007275, 0.005526,                     0.003994, 0.011282, 0.001228, 0.002170,
                  0.001896, 0.000903, 0.001128, 0.001156, 0.001583, 0.001186, 0.001246, 0.000861,
                  0.003700, 0.002688, 0.001491, 0.002736, 0.003641, 0.002593, 0.003799, 0.000827,
                  0.001143, 0.001470, 0.001614, 0.002281, 0.005041, 0.014977, 0.004377, 0.004025,
                  0.014818, 0.045181, 0.040624, 0.050120, 0.031790, 0.036862, 0.034470, 0.043557]) # nmol/cm^3


T1C1D21 = np.array([0.000265, 0.000199, 0.002026, 0.000789, 0.000512, 0.000170, 0.001078, 0.000844]) # nmol/cm^3

F1C1D21 = np.array([0.007275, 0.005526,                     0.003994, 0.011282, 0.001228, 0.002170]) # nmol/cm^3

T2C1D21 = np.array([0.001896, 0.000903, 0.001128, 0.001156, 0.001583, 0.001186, 0.001246, 0.000861]) # nmol/cm^3

F2C1D21 = np.array([0.003700, 0.002688, 0.001491, 0.002736, 0.003641, 0.002593, 0.003799, 0.000827]) # nmol/cm^3

T3C1D21 = np.array([0.001143, 0.001470, 0.001614, 0.002281, 0.005041, 0.014977, 0.004377, 0.004025]) # nmol/cm^3

F3C1D21 = np.array([0.014818, 0.045181, 0.040624, 0.050120, 0.031790, 0.036862, 0.034470, 0.043557]) # nmol/cm^3




C1D33 = np.array([0.000006, 0.000016, 0.000053, 0.000100, 0.000044, 0.000027, 0.000017, 0.000017,
                  0.000121, 0.000067,                     0.000037, 0.000032, 0.000023, 0.000344,
                  0.000042, 0.000042, 0.000051, 0.000048, 0.000057, 0.000087, 0.000110, 0.000089,
                  0.000062, 0.000091, 0.000052, 0.000017, 0.000004, 0.000100, 0.000031, 0.000035,
                  0.000795, 0.000403, 0.000221, 0.000311, 0.000075, 0.000006, 0.000046, 0.000014,
                  0.000048, 0.000106, 0.000108, 0.000124, 0.000376, 0.000084, 0.000008, 0.000106]) #nmol/cm^3


T1C1D33 = np.array([0.000006, 0.000016, 0.000053, 0.000100, 0.000044, 0.000027, 0.000017, 0.000017]) # nmol/cm^3

F1C1D33 = np.array([0.000121, 0.000067,                     0.000037, 0.000032, 0.000023, 0.000344]) # nmol/cm^3

T2C1D33 = np.array([0.000042, 0.000042, 0.000051, 0.000048, 0.000057, 0.000087, 0.000110, 0.000089]) # nmol/cm^3

F2C1D33 = np.array([0.000062, 0.000091, 0.000052, 0.000017, 0.000004, 0.000100, 0.000031, 0.000035]) # nmol/cm^3

T3C1D33 = np.array([0.000795, 0.000403, 0.000221, 0.000311, 0.000075, 0.000006, 0.000046, 0.000014]) # nmol/cm^3

F3C1D33 = np.array([0.000048, 0.000106, 0.000108, 0.000124, 0.000376, 0.000084, 0.000008, 0.000106]) # nmol/cm^3


#################################################################################################################################


C2h = np.array([0.000000, 0.000003, 0.000000, 0.000003, 0.000000, 0.000002, 0.000000, 0.000002,
                0.000000, 0.000002,                     0.000002, 0.000003, 0.000009, 0.000004,
                0.000000, 0.000005, 0.000000, 0.000005, 0.000000, 0.000006, 0.000000, 0.000005,
                0.000002, 0.000011, 0.000047, 0.000026, 0.000075, 0.000030, 0.000217, 0.000033,
                0.000000, 0.000008, 0.000000, 0.000010, 0.000000, 0.000011, 0.000000, 0.000010,
                0.000003, 0.000010, 0.000026, 0.000013, 0.000026, 0.000014, 0.000101, 0.000109]) #nmol/cm^3


T1C2h = np.array([0.000000, 0.000003, 0.000000, 0.000003, 0.000000, 0.000002, 0.000000, 0.000002]) # nmol/cm^3

F1C2h = np.array([0.000000, 0.000002,                     0.000002, 0.000003, 0.000009, 0.000004]) # nmol/cm^3

T2C2h = np.array([0.000000, 0.000005, 0.000000, 0.000005, 0.000000, 0.000006, 0.000000, 0.000005]) # nmol/cm^3

F2C2h = np.array([0.000002, 0.000011, 0.000047, 0.000026, 0.000075, 0.000030, 0.000217, 0.000033]) # nmol/cm^3

T3C2h = np.array([0.000000, 0.000008, 0.000000, 0.000010, 0.000000, 0.000011, 0.000000, 0.000010]) # nmol/cm^3

F3C2h = np.array([0.000003, 0.000010, 0.000026, 0.000013, 0.000026, 0.000014, 0.000101, 0.000109]) # nmol/cm^3




C2D9 = np.array([0.000288, 0.000225, 0.002147, 0.000851, 0.001137, 0.001009, 0.000736, 0.002097,
                np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                 0.000684, 0.000809, 0.001253, 0.000978, 0.000669, 0.000884, 0.001049, 0.001322,
                 np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                 0.001594, 0.004063, 0.000598, 0.002282, 0.006599, 0.002642, 0.006560, 0.002105,
                 np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,])  #nmol/cm^3


T1C2D9 = np.array([0.000288, 0.000225, 0.002147, 0.000851, 0.001137, 0.001009, 0.000736, 0.002097]) # nmol/cm^3

T2C2D9 = np.array([0.000684, 0.000809, 0.001253, 0.000978, 0.000669, 0.000884, 0.001049, 0.001322]) # nmol/cm^3

T3C2D9 = np.array([0.001594, 0.004063, 0.000598, 0.002282, 0.006599, 0.002642, 0.006560, 0.002105]) # nmol/cm^3




C2D21 = np.array([0.000412, 0.000396, 0.003611, 0.000932, 0.001624, 0.001067, 0.001328, 0.002261,
                  0.004904, 0.011732,                     0.002676, 0.008648, 0.001041, 0.002630,
                  0.002391, 0.000758, 0.000803, 0.001327, 0.001006, 0.000639, 0.000584, 0.000825,
                  0.002786, 0.002127, 0.005483, 0.010118, 0.007575, 0.012586, 0.006638, 0.002185,
                  0.003891, 0.000921, 0.000845, 0.005012, 0.009455, 0.011048, 0.009578, 0.006092,
                  0.010271, 0.028884, 0.019777, 0.032388, 0.020136, 0.025858, 0.022837, 0.027749])  #nmol/cm^3


T1C2D21 = np.array([0.000412, 0.000396, 0.003611, 0.000932, 0.001624, 0.001067, 0.001328, 0.002261]) # nmol/cm^3

F1C2D21 = np.array([0.004904, 0.011732,                     0.002676, 0.008648, 0.001041, 0.002630]) # nmol/cm^3

T2C2D21 = np.array([0.002391, 0.000758, 0.000803, 0.001327, 0.001006, 0.000639, 0.000584, 0.000825]) # nmol/cm^3

F2C2D21 = np.array([0.002786, 0.002127, 0.005483, 0.010118, 0.007575, 0.012586, 0.006638, 0.002185]) # nmol/cm^3

T3C2D21 = np.array([0.003891, 0.000921, 0.000845, 0.005012, 0.009455, 0.011048, 0.009578, 0.006092]) # nmol/cm^3

F3C2D21 = np.array([0.010271, 0.028884, 0.019777, 0.032388, 0.020136, 0.025858, 0.022837, 0.027749]) # nmol/cm^3




C2D33 = np.array([0.000002, 0.000021, 0.000041, 0.000039, 0.000069, 0.000015, 0.000029, 0.000100,
                  0.000152, 0.000232,                     0.000001, 0.000073, 0.000008, 0.000615,
                  0.000161, 0.000044, 0.000070, 0.000069, 0.000076, 0.000136, 0.000133, 0.000135,
                  0.000125, 0.000205, 0.000138, 0.000269, 0.000177, 0.000109, 0.000096, 0.000641,
                  0.000169, 0.000000, 0.000102, 0.000472, 0.000007, 0.000012, 0.000001, 0.000003,
                  0.000007, 0.000028, 0.000026, 0.000014, 0.000019, 0.000021, 0.000004, 0.000029]) #nmol/cm^3


T1C2D33 = np.array([0.000002, 0.000021, 0.000041, 0.000039, 0.000069, 0.000015, 0.000029, 0.000100]) # nmol/cm^3

F1C2D33 = np.array([0.000152, 0.000232,                     0.000001, 0.000073, 0.000008, 0.000615]) # nmol/cm^3

T2C2D33 = np.array([0.000161, 0.000044, 0.000070, 0.000069, 0.000076, 0.000136, 0.000133, 0.000135]) # nmol/cm^3

F2C2D33 = np.array([0.000125, 0.000205, 0.000138, 0.000269, 0.000177, 0.000109, 0.000096, 0.000641]) # nmol/cm^3

T3C2D33 = np.array([0.000169, 0.000000, 0.000102, 0.000472, 0.000007, 0.000012, 0.000001, 0.000003]) # nmol/cm^3

F3C2D33 = np.array([0.000007, 0.000028, 0.000026, 0.000014, 0.000019, 0.000021, 0.000004, 0.000029]) # nmol/cm^3


#################################################################################################################################


C3h = np.array([0.000002493, 0.000037563, 0.000002371, 0.000022890, 0.000002657, 0.000025587, 0.000001185, 0.000023871,
                0.000039, 0.000040,                     0.000007, 0.000007, 0.000000, 0.000000,
                0.000003, 0.000078, 0.000000, 0.000054, 0.000000, 0.000041, 0.000000, 0.000032,
                0.000000, 0.000000, 0.000000, 0.000007, 0.000000, 0.000000, 0.000000, 0.000000,
                0.000002, 0.000071, 0.000000, 0.000044, 0.000001, 0.000038, 0.000000, 0.000029,
                0.000000, 0.000001, 0.000000, 0.000036, 0.000000, 0.000091, 0.000001, 0.000058]) #nmol/cm^3


T1C3h = np.array([0.000002, 0.000038, 0.000002, 0.000023, 0.000003, 0.000026, 0.000001, 0.000024])     #nmol/cm^3

F1C3h = np.array([0.000039, 0.000040,                     0.000007, 0.000007, 0.000000, 0.000000])
#nmol/cm^3

T2C3h = np.array([0.000003, 0.000078, 0.000000, 0.000054, 0.000000, 0.000041, 0.000000, 0.000032])     #nmol/cm^3

F2C3h = np.array([0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000])
#nmol/cm^3

T3C3h = np.array([0.000002, 0.000071, 0.000000, 0.000044, 0.000001, 0.000038, 0.000000, 0.000029])     #nmol/cm^3

F3C3h = np.array([0.000000, 0.000001, 0.000000, 0.0000, 0.000000, 0.0000, 0.00000, 0.0000])
#nmol/cm^3




C3D9 = np.array([0.000584, 0.000512, 0.007595, 0.003693, 0.001239, 0.003341, 0.001151, 0.004417,
                np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                 0.002433, 0.001562, 0.001139, 0.002307, 0.001285, 0.001645, 0.001359, 0.002123,
                 np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
                 0.003691, 0.001127, 0.004296, 0.003375, 0.003484, 0.004625, 0.011027, 0.008556,
                 np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,])  # nmol/cm^3


T1C3D9 = np.array([0.000584, 0.000512, 0.007595, 0.003693, 0.001239, 0.003341, 0.001151, 0.004417])     #nmol/cm^3

T2C3D9 = np.array([0.002433, 0.001562, 0.001139, 0.002307, 0.001285, 0.001645, 0.001359, 0.002123])     #nmol/cm^3

T3C3D9 = np.array([0.003691, 0.001127, 0.004296, 0.003375, 0.003484, 0.004625, 0.011027, 0.008556])     #nmol/cm^3




C3D21 = np.array([0.000407, 0.000311, 0.001336, 0.000159, 0.000991, 0.000825, 0.000193, 0.002083,
                  0.000602, 0.000933,                     0.003661, 0.000098, 0.001618, 0.001413,
                  0.001135, 0.001410, 0.000618, 0.001152, 0.000661, 0.000674, 0.000869, 0.000659,
                  0.001677, 0.001647, 0.002630, 0.001064, 0.001963, 0.013393, 0.002350, 0.001776,
                  0.022243, 0.000367, 0.000624, 0.005966, 0.005082, 0.012488, 0.008330, 0.006609,
                  0.012942, 0.024945, 0.020922, 0.040082, 0.008857, 0.014354, 0.013528, 0.033994])      # nmol/cm^3


T1C3D21 = np.array([0.000407, 0.000311, 0.001336, 0.000159, 0.000991, 0.000825, 0.000193, 0.002083]) # nmol/cm^3

F1C3D21 = np.array([0.000602, 0.000933,                     0.003661, 0.000098, 0.001618, 0.001413]) # nmol/cm^3

T2C3D21 = np.array([0.001135, 0.001410, 0.000618, 0.001152, 0.000661, 0.000674, 0.000869, 0.000659]) # nmol/cm^3

F2C3D21 = np.array([0.001677, 0.001647, 0.002630, 0.001064, 0.001963, 0.013393, 0.002350, 0.001776]) # nmol/cm^3

T3C3D21 = np.array([0.022243, 0.000367, 0.000624, 0.005966, 0.005082, 0.012488, 0.008330, 0.006609]) # nmol/cm^3

F3C3D21 = np.array([0.012942, 0.024945, 0.020922, 0.040082, 0.008857, 0.014354, 0.013528, 0.033994]) # nmol/cm^3


C3D33 = np.array([0.000005, 0.000009, 0.000027, 0.000052, 0.000062, 0.000114, 0.000007, 0.000025,
                  0.000131, 0.000211,                     0.000044, 0.000137, 0.000058, 0.000108,
                  0.000111, 0.000108, 0.000059, 0.000095, 0.000105, 0.000175, 0.000145, 0.000177,
                  0.000018, 0.000259, 0.000147, 0.000248, 0.000165, 0.000225, 0.000292, 0.000050,
                  0.000000, 0.000096, 0.000013, 0.000535, 0.000015, 0.000023, 0.000066, 0.000045,
                  0.000016, 0.000098, 0.000038, 0.000049, 0.000068, 0.000015, 0.000031, 0.000056])  # nmol/cm^3


T1C3D33 = np.array([0.000005, 0.000009, 0.000027, 0.000052, 0.000062, 0.000114, 0.000007, 0.000025]) # nmol/cm^3

F1C3D33 = np.array([0.000131, 0.000211,                     0.000044, 0.000137, 0.000058, 0.000108]) # nmol/cm^3

T2C3D33 = np.array([0.000111, 0.000108, 0.000059, 0.000095, 0.000105, 0.000175, 0.000145, 0.000177]) # nmol/cm^3

F2C3D33 = np.array([0.000018, 0.000259, 0.000147, 0.000248, 0.000165, 0.000225, 0.000292, 0.000050]) # nmol/cm^3

T3C3D33 = np.array([0.000000, 0.000096, 0.000013, 0.000535, 0.000015, 0.000023, 0.000066, 0.000045]) # nmol/cm^3

F3C3D33 = np.array([0.000016, 0.000098, 0.000038, 0.000049, 0.000068, 0.000015, 0.000031, 0.000056]) # nmol/cm^3


#################################################################################################################################


#Tm = np.array ([1, 1.083, 2, 2.083, 3, 3.083, 5, 5.083,
#                8, 8.083,          10, 10.803, 11, 11.083,
#
#                14, 14.083, 15, 15.083, 16, 16.083, 18, 18.083,
#                21, 21.083, 22, 22.083, 23, 23.083, 25, 25.083,
#
#                28, 28.083, 29, 29.083, 30, 30.083, 31, 31.083,
#                34, 34.083, 35, 35.083, 36, 36.083, 38, 38.083])    # days
#
#T1Tm = np.array([1, 1.083, 2, 2.083, 3, 3.083, 5, 5.083])       # days
#F1Tm = np.array([8, 8.083,          10, 10.803, 11, 11.083])     # days
#
#T2Tm = np.array([14, 14.083, 15, 15.083, 16, 16.083, 18, 18.083])   # days
#F2Tm = np.array([21, 21.083, 22, 22.083, 23, 23.083, 25, 25.083])   # days
#
#T3Tm = np.array([28, 28.083, 29, 29.083, 30, 30.083, 31, 31.083])   # days
#F3Tm = np.array([34, 34.083, 35, 35.083, 36, 36.083, 38, 38.083])   # days


#################################################################################################################################


#Tm = np.array([18, 20, 36, 38, 61, 63, 109, 111,
#               179, 181,       231, 233, 275, 277,
#
#               352, 354, 371, 373, 394, 396, 444, 446,
#               516, 518, 539, 541, 562, 564, 610, 612,
#
#               683, 685, 707, 709, 729, 731, 775, 777,
#               851, 853, 872, 874, 896, 898, 949, 951
#              ])   # h


#T1Tm = np.array([18, 20, 36, 38, 61, 63, 109, 111])      # h
#F1Tm = np.array([179, 181,       231, 233, 275, 277])    # h

#T2Tm = np.array([352, 354, 371, 373, 394, 396, 444, 446]) # subtract 322 from these values
#F2Tm = np.array([516, 518, 539, 541, 562, 564, 610, 612])  # h

#T3Tm = np.array([683, 685, 707, 709, 729, 731, 775, 777]) # subtract 612 from these values
#F3Tm = np.array([851, 853, 872, 874, 896, 898, 949, 951])  # h


#Tm = np.array([18, 20, 36, 38, 61, 63, 109, 111,
#               49, 51,         101, 103, 145, 147,
#
#               30, 32, 49, 51, 72, 74, 122, 124,
#               43, 45, 66, 68, 89, 91, 137, 139,
#
#              71, 73, 95, 97, 117, 119, 163, 165,
#               39, 41, 60, 62, 84, 86, 137, 139])   #hours (separating each freeze/thaw period and starts each period from time 0


#T1Tm = np.array([18, 20, 36, 38, 61, 63, 109, 111])      # h
#F1Tm = np.array([49, 51,         101, 103, 145, 147])    # h

#T2Tm = np.array([30, 32, 49, 51, 72, 74, 122, 124])      # h
#F2Tm = np.array([43, 45, 66, 68, 89, 91, 137, 139])      # h

#T3Tm = np.array([71, 73, 95, 97, 117, 119, 163, 165])    # h
#F3Tm = np.array([39, 41, 60, 62, 84, 86, 137, 139])      # h




Tm = np.array([18, 20, 36, 38, 61, 63, 109, 111,
               2, 4,         54, 56, 98, 100,

               2, 4, 21, 23, 44, 46, 94, 96,
               2, 4, 25, 27, 48, 50, 96, 98,

               2, 4, 26, 28, 48, 50, 94, 96,
               2, 4, 23, 25, 47, 49, 100, 102])   #hours (connecting freeze and thaw period head to tail)


T1Tm = np.array([18, 20, 36, 38, 61, 63, 109, 111])      # h
F1Tm = np.array([2, 4,         54, 56, 98, 100])    # h

T2Tm = np.array([2, 4, 21, 23, 44, 46, 94, 96])      # h
F2Tm = np.array([2, 4, 25, 27, 48, 50, 96, 98])      # h

T3Tm = np.array([2, 4, 26, 28, 48, 50, 94, 96])    # h
F3Tm = np.array([2, 4, 23, 25, 47, 49, 100, 102])      # h







#################################################################################################################################


#T_frz = np.array([7, 20, 33])       # days

#F1T_frz = np.array([7])             # days
#F2T_frz = np.array([20])            # days
#F3T_frz = np.array([33])            # days


#T_thw = np.array([13, 27, 40])      # days

#T1T_thw = np.array([13])            # days
#T2T_thw = np.array([27])            # days
#T3T_thw = np.array([40])            # days


#################################################################################################################################


T_frz = np.array([130, 473, 812])   # h

F1T_frz = np.array([130])
F2T_frz = np.array([473])
F3T_frz = np.array([812])

T_thw = np.array([322, 612, 960])   # h

T1T_thw = np.array([322])
T2T_thw = np.array([612])
T3T_thw = np.array([960])


#################################################################################################################################


zm = np.array([9, 21, 33])  # cm


phi_m = [0.970098486, 0.966776096, 0.94193848, 0.94398245, 0.939010254, 0.939921956, 0.94770194, 0.936546993]  # [-]
z_phi = [5.25, 10.5, 15.75, 21, 27, 33, 39, 45]  # [cm]


#################################################################################################################################

D_SF6w = 0.00000919703 * 60 * 60 # cm2/h
#D = A * exp (-Ea / R T)
#A = 0.029 cm^2/s;     Ea = 19.3 KJ/mol;     R = 8.314E-3 KJ/mol K;     T = 288.15K

D_SF6g = 0.093 * 60 * 60  # cm2/h; Boon et al., (2013)


Vh1 = 0.388772091 * 1000 # cm3
Vh2 = 0.335757715 * 1000 # cm3
Vh3 = 0.375518497 * 1000  # cm3
SA = 44.17864669  # cm2
D_column = 7.5  # cm


#################################################################################################################################


"""injections
The depth where the SF6 injection is happening is at 18-cm.
The injection times (hours) are -2, 270 and 542 for thaw period. The injections were happening 2-hours before the T0 of each thaw period.
The amount of SF6 are 72.586 umol/L, 111.645 umol/L and 164.735 umol/L accordingly.
All the injections are dissolved gas.
"""
Vi = 0.02 * 1000  # mL or cm3 injections

Ci = np.array([0.073809, 0.153813, 0.113706, 0.152248, 0.164735, 0.157096])  # nmol/cm3

T1Ci = np.array([0.073809])   # nmol/cm3
F1Ci = np.array([0.153813])   # nmol/cm3
T2Ci = np.array([0.113706])   # nmol/cm3
F2Ci = np.array([0.152248])   # nmol/cm3
T3Ci = np.array([0.164735])   # nmol/cm3
F3Ci = np.array([0.157096])   # nmol/cm3


#Ti = np.array([1, 8, 14, 21, 28, 34])  # time of injections in days

#T1Ti = np.array([0.917])   # days
#F1Ti = np.array([7.917])   # days
#T2Ti = np.array([13.917])  # days
#F2Ti = np.array([20.917])  # days
#T3Ti = np.array([27.917])  # days
#F3Ti = np.array([33.917])  # days




#Ti = np.array([16, 177, 350, 514, 681, 851])  # time of injections

#T1Ti = np.array([16])
#F1Ti = np.array([177])

#T2Ti = np.array([350]) # subtract 322 from 350
#F2Ti = np.array([514])

#T3Ti = np.array([681]) # subtract 612 from 681
#F3Ti = np.array([851])


#Ti = np.array([16, 47, 28, 41, 69, 851])  # time of injections in hours; starting each period from 0 hour.

#T1Ti = np.array([16])
#F1Ti = np.array([47])

#T2Ti = np.array([28])
#F2Ti = np.array([41])

#T3Ti = np.array([69])
#F3Ti = np.array([37])


Ti = np.array([16, 0, 0, 0, 0, 0])  # connecting freeze and thaw period head to tail

T1Ti = np.array([16])
F1Ti = np.array([0])

T2Ti = np.array([0])
F2Ti = np.array([0])

T3Ti = np.array([0])
F3Ti = np.array([0])





SF6_Hcc = 132  # Henry constant
Kh = 132       # Henry constant
