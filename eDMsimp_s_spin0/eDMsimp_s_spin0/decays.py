# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 15.0.1 for Mac OS X ARM (64-bit) (July 2, 2026)
# Date: Tue 27 Oct 2026 06:58:56


from object_library import all_decays, Decay
import particles as P


Decay_Y0 = Decay(name = 'Decay_Y0',
                 particle = P.Y0,
                 partial_widths = {(P.Xc__tilde__,P.Xc):'(gSXc**2*MXc**2*cmath.sqrt(-4*MXc**2*MY0**2 + MY0**4))/(16.*cmath.pi*abs(MY0)**3)',
                                   (P.Xr,P.Xr):'(gSXr**2*MXr**2*cmath.sqrt(-4*MXr**2*MY0**2 + MY0**4))/(32.*cmath.pi*abs(MY0)**3)',
                                   (P.e__minus__,P.e__plus__):'((-8*gSe**2*Me**2 + 2*gSe**2*MY0**2)*cmath.sqrt(-4*Me**2*MY0**2 + MY0**4))/(16.*cmath.pi*abs(MY0)**3)',
                                   (P.Xd,P.Xd__tilde__):'((-8*gSXd**2*MXd**2 + 2*gSXd**2*MY0**2)*cmath.sqrt(-4*MXd**2*MY0**2 + MY0**4))/(16.*cmath.pi*abs(MY0)**3)',
                                   (P.Xm,P.Xm):'((-8*gSXm**2*MXm**2 + 2*gSXm**2*MY0**2)*cmath.sqrt(-4*MXm**2*MY0**2 + MY0**4))/(32.*cmath.pi*abs(MY0)**3)'})

