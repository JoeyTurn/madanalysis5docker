# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Wed 11 Apr 2018 18:19:21



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

gZpuV = Parameter(name = 'gZpuV',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = 'g_{u Z\',V}',
                  lhablock = 'FRBlock',
                  lhacode = [ 1 ])

gZpuA = Parameter(name = 'gZpuA',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{u Z\',A}',
                  lhablock = 'FRBlock',
                  lhacode = [ 2 ])

gZpcV = Parameter(name = 'gZpcV',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = 'g_{c Z\',V}',
                  lhablock = 'FRBlock',
                  lhacode = [ 3 ])

gZpcA = Parameter(name = 'gZpcA',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{c Z\',A}',
                  lhablock = 'FRBlock',
                  lhacode = [ 4 ])

gZptV = Parameter(name = 'gZptV',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = 'g_{t Z\',V}',
                  lhablock = 'FRBlock',
                  lhacode = [ 5 ])

gZptA = Parameter(name = 'gZptA',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{t Z\',A}',
                  lhablock = 'FRBlock',
                  lhacode = [ 6 ])

gZpdV = Parameter(name = 'gZpdV',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = 'g_{d Z\',V}',
                  lhablock = 'FRBlock',
                  lhacode = [ 7 ])

gZpdA = Parameter(name = 'gZpdA',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{d Z\',A}',
                  lhablock = 'FRBlock',
                  lhacode = [ 8 ])

gZpsV = Parameter(name = 'gZpsV',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = 'g_{s Z\',V}',
                  lhablock = 'FRBlock',
                  lhacode = [ 9 ])

gZpsA = Parameter(name = 'gZpsA',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{s Z\',A}',
                  lhablock = 'FRBlock',
                  lhacode = [ 10 ])

gZpbV = Parameter(name = 'gZpbV',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = 'g_{b Z\',V}',
                  lhablock = 'FRBlock',
                  lhacode = [ 11 ])

gZpbA = Parameter(name = 'gZpbA',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{b Z\',A}',
                  lhablock = 'FRBlock',
                  lhacode = [ 12 ])

gS2 = Parameter(name = 'gS2',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = 'g_{S_2}',
                lhablock = 'FRBlock',
                lhacode = [ 13 ])

LambdaSgam = Parameter(name = 'LambdaSgam',
                       nature = 'external',
                       type = 'real',
                       value = 2000,
                       texname = '\\Lambda _{\\text{S$\\gamma $}}',
                       lhablock = 'FRBlock',
                       lhacode = [ 14 ])

gX2ZpV = Parameter(name = 'gX2ZpV',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = 'g_{X_2 Z\',V}',
                   lhablock = 'FRBlock',
                   lhacode = [ 15 ])

gX2ZpA = Parameter(name = 'gX2ZpA',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = 'g_{X_2 Z\',A}',
                   lhablock = 'FRBlock',
                   lhacode = [ 16 ])

gX3ZpV = Parameter(name = 'gX3ZpV',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = 'g_{X_3 Z\',V}',
                   lhablock = 'FRBlock',
                   lhacode = [ 17 ])

gX3ZpA = Parameter(name = 'gX3ZpA',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = 'g_{X_3 Z\',A}',
                   lhablock = 'FRBlock',
                   lhacode = [ 18 ])

LambdaXgam = Parameter(name = 'LambdaXgam',
                       nature = 'external',
                       type = 'real',
                       value = 2000,
                       texname = '\\Lambda _{\\text{X$\\gamma $}}',
                       lhablock = 'FRBlock',
                       lhacode = [ 19 ])

LambdaXe = Parameter(name = 'LambdaXe',
                     nature = 'external',
                     type = 'real',
                     value = 2000,
                     texname = '\\Lambda _{\\text{Xe}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 20 ])

LambdaXmu = Parameter(name = 'LambdaXmu',
                      nature = 'external',
                      type = 'real',
                      value = 1000000000,
                      texname = '\\Lambda _{\\text{X$\\mu $}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 21 ])

LambdaXta = Parameter(name = 'LambdaXta',
                      nature = 'external',
                      type = 'real',
                      value = 1000000000,
                      texname = '\\Lambda _{\\text{X$\\tau $}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 22 ])

gSu = Parameter(name = 'gSu',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = 'g_{\\text{Su}}',
                lhablock = 'FRBlock',
                lhacode = [ 23 ])

gSc = Parameter(name = 'gSc',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = 'g_{\\text{Sc}}',
                lhablock = 'FRBlock',
                lhacode = [ 24 ])

gSt = Parameter(name = 'gSt',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = 'g_{\\text{St}}',
                lhablock = 'FRBlock',
                lhacode = [ 25 ])

gSd = Parameter(name = 'gSd',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = 'g_{\\text{Sd}}',
                lhablock = 'FRBlock',
                lhacode = [ 26 ])

gSs = Parameter(name = 'gSs',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = 'g_{\\text{Ss}}',
                lhablock = 'FRBlock',
                lhacode = [ 27 ])

gSb = Parameter(name = 'gSb',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = 'g_{\\text{Sb}}',
                lhablock = 'FRBlock',
                lhacode = [ 28 ])

gSe = Parameter(name = 'gSe',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = 'g_{\\text{Se}}',
                lhablock = 'FRBlock',
                lhacode = [ 29 ])

gSmu = Parameter(name = 'gSmu',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = 'g_{\\text{S$\\mu $}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 30 ])

gSta = Parameter(name = 'gSta',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = 'g_{\\text{S$\\tau $}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 31 ])

gS1X = Parameter(name = 'gS1X',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = 'g_{S_1 X}',
                 lhablock = 'FRBlock',
                 lhacode = [ 32 ])

gS2X = Parameter(name = 'gS2X',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = 'g_{S_2 X}',
                 lhablock = 'FRBlock',
                 lhacode = [ 33 ])

gS12 = Parameter(name = 'gS12',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = 'g_{S_1 S_2 Z\'}',
                 lhablock = 'FRBlock',
                 lhacode = [ 34 ])

gX12ZpV = Parameter(name = 'gX12ZpV',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = 'g_{X_1 X_2 Z\',V}',
                    lhablock = 'FRBlock',
                    lhacode = [ 35 ])

gX12ZpA = Parameter(name = 'gX12ZpA',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = 'g_{X_1 X_2 Z\',A}',
                    lhablock = 'FRBlock',
                    lhacode = [ 36 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MX1 = Parameter(name = 'MX1',
                nature = 'external',
                type = 'real',
                value = 100.,
                texname = '\\text{MX1}',
                lhablock = 'MASS',
                lhacode = [ 52 ])

MX2 = Parameter(name = 'MX2',
                nature = 'external',
                type = 'real',
                value = 110.,
                texname = '\\text{MX2}',
                lhablock = 'MASS',
                lhacode = [ 53 ])

MX3 = Parameter(name = 'MX3',
                nature = 'external',
                type = 'real',
                value = 120.,
                texname = '\\text{MX3}',
                lhablock = 'MASS',
                lhacode = [ 54 ])

MZp = Parameter(name = 'MZp',
                nature = 'external',
                type = 'real',
                value = 500.,
                texname = '\\text{MZp}',
                lhablock = 'MASS',
                lhacode = [ 61 ])

MS1 = Parameter(name = 'MS1',
                nature = 'external',
                type = 'real',
                value = 100.,
                texname = '\\text{MS1}',
                lhablock = 'MASS',
                lhacode = [ 57 ])

MS2 = Parameter(name = 'MS2',
                nature = 'external',
                type = 'real',
                value = 110.,
                texname = '\\text{MS2}',
                lhablock = 'MASS',
                lhacode = [ 58 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WX1 = Parameter(name = 'WX1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{WX1}',
                lhablock = 'DECAY',
                lhacode = [ 52 ])

WX2 = Parameter(name = 'WX2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WX2}',
                lhablock = 'DECAY',
                lhacode = [ 53 ])

WX3 = Parameter(name = 'WX3',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WX3}',
                lhablock = 'DECAY',
                lhacode = [ 54 ])

WZp = Parameter(name = 'WZp',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{WZp}',
                lhablock = 'DECAY',
                lhacode = [ 61 ])

WS1 = Parameter(name = 'WS1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{WS1}',
                lhablock = 'DECAY',
                lhacode = [ 57 ])

WS2 = Parameter(name = 'WS2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WS2}',
                lhablock = 'DECAY',
                lhacode = [ 58 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

ySd1x1 = Parameter(name = 'ySd1x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'gSd*ydo',
                   texname = '\\text{ySd1x1}')

ySd2x2 = Parameter(name = 'ySd2x2',
                   nature = 'internal',
                   type = 'real',
                   value = 'gSs*ys',
                   texname = '\\text{ySd2x2}')

ySd3x3 = Parameter(name = 'ySd3x3',
                   nature = 'internal',
                   type = 'real',
                   value = 'gSb*yb',
                   texname = '\\text{ySd3x3}')

ySl1x1 = Parameter(name = 'ySl1x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'gSe*ye',
                   texname = '\\text{ySl1x1}')

ySl2x2 = Parameter(name = 'ySl2x2',
                   nature = 'internal',
                   type = 'real',
                   value = 'gSmu*ym',
                   texname = '\\text{ySl2x2}')

ySl3x3 = Parameter(name = 'ySl3x3',
                   nature = 'internal',
                   type = 'real',
                   value = 'gSta*ytau',
                   texname = '\\text{ySl3x3}')

ySu1x1 = Parameter(name = 'ySu1x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'gSu*yup',
                   texname = '\\text{ySu1x1}')

ySu2x2 = Parameter(name = 'ySu2x2',
                   nature = 'internal',
                   type = 'real',
                   value = 'gSc*yc',
                   texname = '\\text{ySu2x2}')

ySu3x3 = Parameter(name = 'ySu3x3',
                   nature = 'internal',
                   type = 'real',
                   value = 'gSt*yt',
                   texname = '\\text{ySu3x3}')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  texname = '\\text{I1a11}')

I1a12 = Parameter(name = 'I1a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  texname = '\\text{I1a12}')

I1a13 = Parameter(name = 'I1a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  texname = '\\text{I1a13}')

I1a21 = Parameter(name = 'I1a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM1x2)',
                  texname = '\\text{I1a21}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM2x2)',
                  texname = '\\text{I1a22}')

I1a23 = Parameter(name = 'I1a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM3x2)',
                  texname = '\\text{I1a23}')

I1a31 = Parameter(name = 'I1a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM1x3)',
                  texname = '\\text{I1a31}')

I1a32 = Parameter(name = 'I1a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM2x3)',
                  texname = '\\text{I1a32}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM3x3)',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x1)',
                  texname = '\\text{I2a11}')

I2a12 = Parameter(name = 'I2a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x1)',
                  texname = '\\text{I2a12}')

I2a13 = Parameter(name = 'I2a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x1)',
                  texname = '\\text{I2a13}')

I2a21 = Parameter(name = 'I2a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x2)',
                  texname = '\\text{I2a21}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x2)',
                  texname = '\\text{I2a22}')

I2a23 = Parameter(name = 'I2a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x2)',
                  texname = '\\text{I2a23}')

I2a31 = Parameter(name = 'I2a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x3)',
                  texname = '\\text{I2a31}')

I2a32 = Parameter(name = 'I2a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x3)',
                  texname = '\\text{I2a32}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x3)',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yup',
                  texname = '\\text{I3a11}')

I3a12 = Parameter(name = 'I3a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yup',
                  texname = '\\text{I3a12}')

I3a13 = Parameter(name = 'I3a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yup',
                  texname = '\\text{I3a13}')

I3a21 = Parameter(name = 'I3a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yc',
                  texname = '\\text{I3a21}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yc',
                  texname = '\\text{I3a22}')

I3a23 = Parameter(name = 'I3a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yc',
                  texname = '\\text{I3a23}')

I3a31 = Parameter(name = 'I3a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*yt',
                  texname = '\\text{I3a31}')

I3a32 = Parameter(name = 'I3a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*yt',
                  texname = '\\text{I3a32}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yt',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ydo',
                  texname = '\\text{I4a11}')

I4a12 = Parameter(name = 'I4a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ys',
                  texname = '\\text{I4a12}')

I4a13 = Parameter(name = 'I4a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yb',
                  texname = '\\text{I4a13}')

I4a21 = Parameter(name = 'I4a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ydo',
                  texname = '\\text{I4a21}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ys',
                  texname = '\\text{I4a22}')

I4a23 = Parameter(name = 'I4a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yb',
                  texname = '\\text{I4a23}')

I4a31 = Parameter(name = 'I4a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*ydo',
                  texname = '\\text{I4a31}')

I4a32 = Parameter(name = 'I4a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*ys',
                  texname = '\\text{I4a32}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yb',
                  texname = '\\text{I4a33}')

