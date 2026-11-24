# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 15.0.1 for Mac OS X ARM (64-bit) (July 2, 2026)
# Date: Tue 27 Oct 2026 06:59:56


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.Y1, P.Xc__tilde__, P.Xc ],
             color = [ '1' ],
             lorentz = [ L.VSS1 ],
             couplings = {(0,0):C.GC_5})

V_2 = Vertex(name = 'V_2',
             particles = [ P.e__plus__, P.e__minus__, P.Y1 ],
             color = [ '1' ],
             lorentz = [ L.FFV1, L.FFV2 ],
             couplings = {(0,1):C.GC_1,(0,0):C.GC_4})

V_3 = Vertex(name = 'V_3',
             particles = [ P.Xd__tilde__, P.Xd, P.Y1 ],
             color = [ '1' ],
             lorentz = [ L.FFV1, L.FFV2 ],
             couplings = {(0,1):C.GC_2,(0,0):C.GC_6})

V_4 = Vertex(name = 'V_4',
             particles = [ P.Xm, P.Xm, P.Y1 ],
             color = [ '1' ],
             lorentz = [ L.FFV2 ],
             couplings = {(0,0):C.GC_3})

