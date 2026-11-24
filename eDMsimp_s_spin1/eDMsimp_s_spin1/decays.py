# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 15.0.1 for Mac OS X ARM (64-bit) (July 2, 2026)
# Date: Tue 27 Oct 2026 06:59:56


from object_library import all_decays, Decay
import particles as P


Decay_Y1 = Decay(name = 'Decay_Y1',
                 particle = P.Y1,
                 partial_widths = {(P.Xc__tilde__,P.Xc):'((-(gVXc**2*MXc**2) + (gVXc**2*MY1**2)/4.)*cmath.sqrt(-4*MXc**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.e__minus__,P.e__plus__):'((-16*gAe**2*Me**2 + 8*gVe**2*Me**2 + 4*gAe**2*MY1**2 + 4*gVe**2*MY1**2)*cmath.sqrt(-4*Me**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.Xd,P.Xd__tilde__):'((-16*gAXd**2*MXd**2 + 8*gVXd**2*MXd**2 + 4*gAXd**2*MY1**2 + 4*gVXd**2*MY1**2)*cmath.sqrt(-4*MXd**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.Xm,P.Xm):'((-16*gAXm**2*MXm**2 + 4*gAXm**2*MY1**2)*cmath.sqrt(-4*MXm**2*MY1**2 + MY1**4))/(96.*cmath.pi*abs(MY1)**3)'})

