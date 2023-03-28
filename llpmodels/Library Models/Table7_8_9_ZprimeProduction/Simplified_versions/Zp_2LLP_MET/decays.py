# This file was automatically created by FeynRules 2.3.31
# Mathematica version: 11.2.0 for Mac OS X x86 (64-bit) (September 11, 2017)
# Date: Tue 10 Apr 2018 14:08:28


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.c):'(((3*CKM2x3*ee**2*MB**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MC**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MB**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MB**2*MC**2*complexconjugate(CKM2x3))/(MW**2*sw**2) + (3*CKM2x3*ee**2*MC**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MW**2*complexconjugate(CKM2x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MC**2 + MC**4 - 2*MB**2*MW**2 - 2*MC**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.u):'(((3*CKM1x3*ee**2*MB**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MU**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MB**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MB**2*MU**2*complexconjugate(CKM1x3))/(MW**2*sw**2) + (3*CKM1x3*ee**2*MU**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MW**2*complexconjugate(CKM1x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MU**2 + MU**4 - 2*MB**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_c = Decay(name = 'Decay_c',
                particle = P.c,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM2x3*ee**2*MB**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MC**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MB**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MB**2*MC**2*complexconjugate(CKM2x3))/(MW**2*sw**2) + (3*CKM2x3*ee**2*MC**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MW**2*complexconjugate(CKM2x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MC**2 + MC**4 - 2*MB**2*MW**2 - 2*MC**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)',
                                  (P.W__plus__,P.d):'(((3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MD**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MC**2*MD**2*complexconjugate(CKM2x1))/(MW**2*sw**2) + (3*CKM2x1*ee**2*MD**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MD**2 + MD**4 - 2*MC**2*MW**2 - 2*MD**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)',
                                  (P.W__plus__,P.s):'(((3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MS**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MC**2*MS**2*complexconjugate(CKM2x2))/(MW**2*sw**2) + (3*CKM2x2*ee**2*MS**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)'})

Decay_d = Decay(name = 'Decay_d',
                particle = P.d,
                partial_widths = {(P.W__minus__,P.c):'(((3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MD**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MC**2*MD**2*complexconjugate(CKM2x1))/(MW**2*sw**2) + (3*CKM2x1*ee**2*MD**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MD**2 + MD**4 - 2*MC**2*MW**2 - 2*MD**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)',
                                  (P.W__minus__,P.t):'(((3*CKM3x1*ee**2*MD**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MD**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MD**2*MT**2*complexconjugate(CKM3x1))/(MW**2*sw**2) + (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MT**2 + MT**4 - 2*MD**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)',
                                  (P.W__minus__,P.u):'(((3*CKM1x1*ee**2*MD**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MU**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MD**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MD**2*MU**2*complexconjugate(CKM1x1))/(MW**2*sw**2) + (3*CKM1x1*ee**2*MU**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MW**2*complexconjugate(CKM1x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)'})

Decay_e__minus__ = Decay(name = 'Decay_e__minus__',
                         particle = P.e__minus__,
                         partial_widths = {(P.W__minus__,P.ve):'((Me**2 - MW**2)*((ee**2*Me**2)/(2.*sw**2) + (ee**2*Me**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Me)**3)'})

Decay_h = Decay(name = 'Decay_h',
                particle = P.h,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.c,P.c__tilde__):'((-12*MC**2*yc**2 + 3*MH**2*yc**2)*cmath.sqrt(-4*MC**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.d,P.d__tilde__):'((-12*MD**2*ydo**2 + 3*MH**2*ydo**2)*cmath.sqrt(-4*MD**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.e__minus__,P.e__plus__):'((-4*Me**2*ye**2 + MH**2*ye**2)*cmath.sqrt(-4*Me**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((MH**2*ym**2 - 4*MMU**2*ym**2)*cmath.sqrt(MH**4 - 4*MH**2*MMU**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.s,P.s__tilde__):'((3*MH**2*ys**2 - 12*MS**2*ys**2)*cmath.sqrt(MH**4 - 4*MH**2*MS**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.u,P.u__tilde__):'((3*MH**2*yup**2 - 12*MU**2*yup**2)*cmath.sqrt(MH**4 - 4*MH**2*MU**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.W__minus__,P.vm):'((MMU**2 - MW**2)*((ee**2*MMU**2)/(2.*sw**2) + (ee**2*MMU**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MMU)**3)'})

Decay_s = Decay(name = 'Decay_s',
                particle = P.s,
                partial_widths = {(P.W__minus__,P.c):'(((3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MS**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MC**2*MS**2*complexconjugate(CKM2x2))/(MW**2*sw**2) + (3*CKM2x2*ee**2*MS**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)',
                                  (P.W__minus__,P.t):'(((3*CKM3x2*ee**2*MS**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MS**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MS**2*MT**2*complexconjugate(CKM3x2))/(MW**2*sw**2) + (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MT**2 + MT**4 - 2*MS**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)',
                                  (P.W__minus__,P.u):'(((3*CKM1x2*ee**2*MS**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MU**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MS**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MS**2*MU**2*complexconjugate(CKM1x2))/(MW**2*sw**2) + (3*CKM1x2*ee**2*MU**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MW**2*complexconjugate(CKM1x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MU**2 + MU**4 - 2*MS**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)'})

Decay_s1 = Decay(name = 'Decay_s1',
                 particle = P.s1,
                 partial_widths = {(P.x2,P.x3__tilde__):'((2*gS1X**2*MS1**2 - 2*gS1X**2*MX2**2 - 4*gS1X**2*MX2*MX3 - 2*gS1X**2*MX3**2)*cmath.sqrt(MS1**4 - 2*MS1**2*MX2**2 + MX2**4 - 2*MS1**2*MX3**2 - 2*MX2**2*MX3**2 + MX3**4))/(16.*cmath.pi*abs(MS1)**3)'})

Decay_s2 = Decay(name = 'Decay_s2',
                 particle = P.s2,
                 partial_widths = {(P.a,P.a):'MS2**6/(4.*cmath.pi*LambdaSgam**2*abs(MS2)**3)',
                                   (P.b,P.b__tilde__):'((-24*MB**2*ySd3x3**2 + 6*MS2**2*ySd3x3**2)*cmath.sqrt(-4*MB**2*MS2**2 + MS2**4))/(16.*cmath.pi*abs(MS2)**3)',
                                   (P.c,P.c__tilde__):'((-24*MC**2*ySu2x2**2 + 6*MS2**2*ySu2x2**2)*cmath.sqrt(-4*MC**2*MS2**2 + MS2**4))/(16.*cmath.pi*abs(MS2)**3)',
                                   (P.d,P.d__tilde__):'((-24*MD**2*ySd1x1**2 + 6*MS2**2*ySd1x1**2)*cmath.sqrt(-4*MD**2*MS2**2 + MS2**4))/(16.*cmath.pi*abs(MS2)**3)',
                                   (P.e__minus__,P.e__plus__):'((-8*Me**2*ySl1x1**2 + 2*MS2**2*ySl1x1**2)*cmath.sqrt(-4*Me**2*MS2**2 + MS2**4))/(16.*cmath.pi*abs(MS2)**3)',
                                   (P.mu__minus__,P.mu__plus__):'((-8*MMU**2*ySl2x2**2 + 2*MS2**2*ySl2x2**2)*cmath.sqrt(-4*MMU**2*MS2**2 + MS2**4))/(16.*cmath.pi*abs(MS2)**3)',
                                   (P.s,P.s__tilde__):'((-24*MS**2*ySd2x2**2 + 6*MS2**2*ySd2x2**2)*cmath.sqrt(-4*MS**2*MS2**2 + MS2**4))/(16.*cmath.pi*abs(MS2)**3)',
                                   (P.t,P.t__tilde__):'((6*MS2**2*ySu3x3**2 - 24*MT**2*ySu3x3**2)*cmath.sqrt(MS2**4 - 4*MS2**2*MT**2))/(16.*cmath.pi*abs(MS2)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((2*MS2**2*ySl3x3**2 - 8*MTA**2*ySl3x3**2)*cmath.sqrt(MS2**4 - 4*MS2**2*MTA**2))/(16.*cmath.pi*abs(MS2)**3)',
                                   (P.u,P.u__tilde__):'((6*MS2**2*ySu1x1**2 - 24*MU**2*ySu1x1**2)*cmath.sqrt(MS2**4 - 4*MS2**2*MU**2))/(16.*cmath.pi*abs(MS2)**3)',
                                   (P.x1,P.x3__tilde__):'((2*gS2X**2*MS2**2 - 2*gS2X**2*MX1**2 - 4*gS2X**2*MX1*MX3 - 2*gS2X**2*MX3**2)*cmath.sqrt(MS2**4 - 2*MS2**2*MX1**2 + MX1**4 - 2*MS2**2*MX3**2 - 2*MX1**2*MX3**2 + MX3**4))/(16.*cmath.pi*abs(MS2)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.d):'(((3*CKM3x1*ee**2*MD**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MD**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MD**2*MT**2*complexconjugate(CKM3x1))/(MW**2*sw**2) + (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MT**2 + MT**4 - 2*MD**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.s):'(((3*CKM3x2*ee**2*MS**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MS**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MS**2*MT**2*complexconjugate(CKM3x2))/(MW**2*sw**2) + (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MT**2 + MT**4 - 2*MS**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_u = Decay(name = 'Decay_u',
                particle = P.u,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM1x3*ee**2*MB**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MU**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MB**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MB**2*MU**2*complexconjugate(CKM1x3))/(MW**2*sw**2) + (3*CKM1x3*ee**2*MU**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MW**2*complexconjugate(CKM1x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MU**2 + MU**4 - 2*MB**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)',
                                  (P.W__plus__,P.d):'(((3*CKM1x1*ee**2*MD**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MU**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MD**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MD**2*MU**2*complexconjugate(CKM1x1))/(MW**2*sw**2) + (3*CKM1x1*ee**2*MU**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MW**2*complexconjugate(CKM1x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)',
                                  (P.W__plus__,P.s):'(((3*CKM1x2*ee**2*MS**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MU**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MS**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MS**2*MU**2*complexconjugate(CKM1x2))/(MW**2*sw**2) + (3*CKM1x2*ee**2*MU**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MW**2*complexconjugate(CKM1x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MU**2 + MU**4 - 2*MS**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.b__tilde__):'(((-3*CKM2x3*ee**2*MB**2*complexconjugate(CKM2x3))/(2.*sw**2) - (3*CKM2x3*ee**2*MC**2*complexconjugate(CKM2x3))/(2.*sw**2) - (3*CKM2x3*ee**2*MB**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) + (3*CKM2x3*ee**2*MB**2*MC**2*complexconjugate(CKM2x3))/(MW**2*sw**2) - (3*CKM2x3*ee**2*MC**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) + (3*CKM2x3*ee**2*MW**2*complexconjugate(CKM2x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MC**2 + MC**4 - 2*MB**2*MW**2 - 2*MC**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.c,P.d__tilde__):'(((-3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) - (3*CKM2x1*ee**2*MD**2*complexconjugate(CKM2x1))/(2.*sw**2) - (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) + (3*CKM2x1*ee**2*MC**2*MD**2*complexconjugate(CKM2x1))/(MW**2*sw**2) - (3*CKM2x1*ee**2*MD**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) + (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MD**2 + MD**4 - 2*MC**2*MW**2 - 2*MD**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(((-3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) - (3*CKM2x2*ee**2*MS**2*complexconjugate(CKM2x2))/(2.*sw**2) - (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) + (3*CKM2x2*ee**2*MC**2*MS**2*complexconjugate(CKM2x2))/(MW**2*sw**2) - (3*CKM2x2*ee**2*MS**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) + (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) - (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.d__tilde__):'(((-3*CKM3x1*ee**2*MD**2*complexconjugate(CKM3x1))/(2.*sw**2) - (3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) - (3*CKM3x1*ee**2*MD**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) + (3*CKM3x1*ee**2*MD**2*MT**2*complexconjugate(CKM3x1))/(MW**2*sw**2) - (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) + (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MT**2 + MT**4 - 2*MD**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.s__tilde__):'(((-3*CKM3x2*ee**2*MS**2*complexconjugate(CKM3x2))/(2.*sw**2) - (3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) - (3*CKM3x2*ee**2*MS**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) + (3*CKM3x2*ee**2*MS**2*MT**2*complexconjugate(CKM3x2))/(MW**2*sw**2) - (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) + (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MT**2 + MT**4 - 2*MS**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.b__tilde__):'(((-3*CKM1x3*ee**2*MB**2*complexconjugate(CKM1x3))/(2.*sw**2) - (3*CKM1x3*ee**2*MU**2*complexconjugate(CKM1x3))/(2.*sw**2) - (3*CKM1x3*ee**2*MB**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) + (3*CKM1x3*ee**2*MB**2*MU**2*complexconjugate(CKM1x3))/(MW**2*sw**2) - (3*CKM1x3*ee**2*MU**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) + (3*CKM1x3*ee**2*MW**2*complexconjugate(CKM1x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MU**2 + MU**4 - 2*MB**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(((-3*CKM1x1*ee**2*MD**2*complexconjugate(CKM1x1))/(2.*sw**2) - (3*CKM1x1*ee**2*MU**2*complexconjugate(CKM1x1))/(2.*sw**2) - (3*CKM1x1*ee**2*MD**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) + (3*CKM1x1*ee**2*MD**2*MU**2*complexconjugate(CKM1x1))/(MW**2*sw**2) - (3*CKM1x1*ee**2*MU**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) + (3*CKM1x1*ee**2*MW**2*complexconjugate(CKM1x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(((-3*CKM1x2*ee**2*MS**2*complexconjugate(CKM1x2))/(2.*sw**2) - (3*CKM1x2*ee**2*MU**2*complexconjugate(CKM1x2))/(2.*sw**2) - (3*CKM1x2*ee**2*MS**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) + (3*CKM1x2*ee**2*MS**2*MU**2*complexconjugate(CKM1x2))/(MW**2*sw**2) - (3*CKM1x2*ee**2*MU**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) + (3*CKM1x2*ee**2*MW**2*complexconjugate(CKM1x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MU**2 + MU**4 - 2*MS**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'((-Me**2 + MW**2)*(-(ee**2*Me**2)/(2.*sw**2) - (ee**2*Me**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'((-MMU**2 + MW**2)*(-(ee**2*MMU**2)/(2.*sw**2) - (ee**2*MMU**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_x1 = Decay(name = 'Decay_x1',
                 particle = P.x1,
                 partial_widths = {(P.s2,P.x3):'((-2*gS2X**2*MS2**2 + 2*gS2X**2*MX1**2 + 4*gS2X**2*MX1*MX3 + 2*gS2X**2*MX3**2)*cmath.sqrt(MS2**4 - 2*MS2**2*MX1**2 + MX1**4 - 2*MS2**2*MX3**2 - 2*MX1**2*MX3**2 + MX3**4))/(32.*cmath.pi*abs(MX1)**3)',
                                   (P.zp,P.x2):'((2*gX12Zp**2*MX1**2 - 12*gX12Zp**2*MX1*MX2 + 2*gX12Zp**2*MX2**2 + (2*gX12Zp**2*MX1**4)/MZp**2 - (4*gX12Zp**2*MX1**2*MX2**2)/MZp**2 + (2*gX12Zp**2*MX2**4)/MZp**2 - 4*gX12Zp**2*MZp**2)*cmath.sqrt(MX1**4 - 2*MX1**2*MX2**2 + MX2**4 - 2*MX1**2*MZp**2 - 2*MX2**2*MZp**2 + MZp**4))/(32.*cmath.pi*abs(MX1)**3)'})

Decay_x2 = Decay(name = 'Decay_x2',
                 particle = P.x2,
                 partial_widths = {(P.s1,P.x3):'((-2*gS1X**2*MS1**2 + 2*gS1X**2*MX2**2 + 4*gS1X**2*MX2*MX3 + 2*gS1X**2*MX3**2)*cmath.sqrt(MS1**4 - 2*MS1**2*MX2**2 + MX2**4 - 2*MS1**2*MX3**2 - 2*MX2**2*MX3**2 + MX3**4))/(32.*cmath.pi*abs(MX2)**3)',
                                   (P.zp,P.x1):'((2*gX12Zp**2*MX1**2 - 12*gX12Zp**2*MX1*MX2 + 2*gX12Zp**2*MX2**2 + (2*gX12Zp**2*MX1**4)/MZp**2 - (4*gX12Zp**2*MX1**2*MX2**2)/MZp**2 + (2*gX12Zp**2*MX2**4)/MZp**2 - 4*gX12Zp**2*MZp**2)*cmath.sqrt(MX1**4 - 2*MX1**2*MX2**2 + MX2**4 - 2*MX1**2*MZp**2 - 2*MX2**2*MZp**2 + MZp**4))/(32.*cmath.pi*abs(MX2)**3)'})

Decay_x3 = Decay(name = 'Decay_x3',
                 particle = P.x3,
                 partial_widths = {(P.S1__tilde__,P.x2):'((-2*gS1X**2*MS1**2 + 2*gS1X**2*MX2**2 + 4*gS1X**2*MX2*MX3 + 2*gS1X**2*MX3**2)*cmath.sqrt(MS1**4 - 2*MS1**2*MX2**2 + MX2**4 - 2*MS1**2*MX3**2 - 2*MX2**2*MX3**2 + MX3**4))/(32.*cmath.pi*abs(MX3)**3)',
                                   (P.S2__tilde__,P.x1):'((-2*gS2X**2*MS2**2 + 2*gS2X**2*MX1**2 + 4*gS2X**2*MX1*MX3 + 2*gS2X**2*MX3**2)*cmath.sqrt(MS2**4 - 2*MS2**2*MX1**2 + MX1**4 - 2*MS2**2*MX3**2 - 2*MX1**2*MX3**2 + MX3**4))/(32.*cmath.pi*abs(MX3)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'((-11*ee**2*MC**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MC**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MC**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MC**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'((-7*ee**2*MD**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MD**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MD**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MD**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'((-5*ee**2*Me**2 - ee**2*MZ**2 - (cw**2*ee**2*Me**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*Me**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*Me**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((-5*ee**2*MMU**2 - ee**2*MZ**2 - (cw**2*ee**2*MMU**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MMU**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MMU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'((-7*ee**2*MS**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MS**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MS**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MS**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'((-11*ee**2*MU**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MU**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MU**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

Decay_zp = Decay(name = 'Decay_zp',
                 particle = P.zp,
                 partial_widths = {(P.b,P.b__tilde__):'((24*gZpq**2*MB**2 + 12*gZpq**2*MZp**2)*cmath.sqrt(-4*MB**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.c,P.c__tilde__):'((24*gZpq**2*MC**2 + 12*gZpq**2*MZp**2)*cmath.sqrt(-4*MC**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.d,P.d__tilde__):'((24*gZpq**2*MD**2 + 12*gZpq**2*MZp**2)*cmath.sqrt(-4*MD**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.s,P.s__tilde__):'((24*gZpq**2*MS**2 + 12*gZpq**2*MZp**2)*cmath.sqrt(-4*MS**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.t,P.t__tilde__):'((24*gZpq**2*MT**2 + 12*gZpq**2*MZp**2)*cmath.sqrt(-4*MT**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.u,P.u__tilde__):'((24*gZpq**2*MU**2 + 12*gZpq**2*MZp**2)*cmath.sqrt(-4*MU**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.x1,P.x2__tilde__):'((-2*gX12Zp**2*MX1**2 + 12*gX12Zp**2*MX1*MX2 - 2*gX12Zp**2*MX2**2 - (2*gX12Zp**2*MX1**4)/MZp**2 + (4*gX12Zp**2*MX1**2*MX2**2)/MZp**2 - (2*gX12Zp**2*MX2**4)/MZp**2 + 4*gX12Zp**2*MZp**2)*cmath.sqrt(MX1**4 - 2*MX1**2*MX2**2 + MX2**4 - 2*MX1**2*MZp**2 - 2*MX2**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.x2,P.x1__tilde__):'((-2*gX12Zp**2*MX1**2 + 12*gX12Zp**2*MX1*MX2 - 2*gX12Zp**2*MX2**2 - (2*gX12Zp**2*MX1**4)/MZp**2 + (4*gX12Zp**2*MX1**2*MX2**2)/MZp**2 - (2*gX12Zp**2*MX2**4)/MZp**2 + 4*gX12Zp**2*MZp**2)*cmath.sqrt(MX1**4 - 2*MX1**2*MX2**2 + MX2**4 - 2*MX1**2*MZp**2 - 2*MX2**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.x3,P.x3__tilde__):'((8*gX3Zp**2*MX3**2 + 4*gX3Zp**2*MZp**2)*cmath.sqrt(-4*MX3**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)'})
