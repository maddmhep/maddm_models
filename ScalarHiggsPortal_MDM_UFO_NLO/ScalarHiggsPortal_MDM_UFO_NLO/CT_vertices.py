# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 12.0.0 for Mac OS X x86 (64-bit) (April 7, 2019)
# Date: Fri 2 Feb 2024 17:50:13


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H, P.Z] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
               couplings = {(0,0,0):C.R2GC_295_285,(0,0,1):C.R2GC_295_286,(0,0,4):C.R2GC_295_287,(0,0,5):C.R2GC_295_288,(0,0,6):C.R2GC_295_289,(0,0,7):C.R2GC_295_290,(0,0,2):C.R2GC_295_292,(0,0,3):C.R2GC_295_291})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.W__plus__] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
               couplings = {(0,0,17):C.R2GC_379_537,(0,0,19):C.R2GC_406_761,(0,0,0):C.R2GC_406_762,(0,0,2):C.R2GC_285_239,(0,0,3):C.R2GC_406_763,(0,0,4):C.R2GC_379_534,(0,0,6):C.R2GC_406_768,(0,0,10):C.R2GC_406_766,(0,0,12):C.R2GC_406_767,(0,0,13):C.R2GC_406_764,(0,0,15):C.R2GC_406_765,(0,0,16):C.R2GC_379_536,(0,0,18):C.R2GC_406_769,(0,0,1):C.R2GC_400_698,(0,0,5):C.R2GC_406_773,(0,0,7):C.R2GC_406_770,(0,0,9):C.R2GC_406_771,(0,0,11):C.R2GC_406_774,(0,0,14):C.R2GC_406_772,(0,0,8):C.R2GC_406_775})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               loop_particles = [ [ [P.a] ], [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.Z] ], [ [P.a, P.Z] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.Z] ] ],
               couplings = {(0,0,0):C.R2GC_325_366,(0,0,9):C.R2GC_325_367,(0,0,10):C.R2GC_325_368,(0,0,1):C.R2GC_325_369,(0,0,3):C.R2GC_325_370,(0,0,4):C.R2GC_325_371,(0,0,5):C.R2GC_325_372,(0,0,6):C.R2GC_325_373,(0,0,7):C.R2GC_325_374,(0,0,8):C.R2GC_325_375,(0,0,2):C.R2GC_325_376})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.G0, P.G0, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0, P.H, P.Z] ], [ [P.G0, P.Z], [P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
               couplings = {(0,0,0):C.R2GC_379_533,(0,0,1):C.R2GC_379_534,(0,0,5):C.R2GC_379_535,(0,0,6):C.R2GC_379_536,(0,0,7):C.R2GC_379_537,(0,0,8):C.R2GC_379_538,(0,0,3):C.R2GC_379_539,(0,0,4):C.R2GC_325_373,(0,0,2):C.R2GC_379_540})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.W__plus__, P.Z] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
               couplings = {(0,0,17):C.R2GC_379_537,(0,0,19):C.R2GC_406_761,(0,0,0):C.R2GC_406_762,(0,0,2):C.R2GC_285_239,(0,0,3):C.R2GC_406_763,(0,0,4):C.R2GC_379_534,(0,0,8):C.R2GC_406_764,(0,0,10):C.R2GC_406_765,(0,0,12):C.R2GC_406_766,(0,0,14):C.R2GC_406_767,(0,0,15):C.R2GC_406_768,(0,0,16):C.R2GC_379_536,(0,0,18):C.R2GC_406_769,(0,0,1):C.R2GC_400_698,(0,0,5):C.R2GC_406_770,(0,0,7):C.R2GC_406_771,(0,0,9):C.R2GC_406_772,(0,0,11):C.R2GC_406_773,(0,0,13):C.R2GC_406_774,(0,0,6):C.R2GC_406_775})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
               couplings = {(0,0,0):C.R2GC_295_285,(0,0,1):C.R2GC_295_286,(0,0,4):C.R2GC_295_287,(0,0,5):C.R2GC_295_288,(0,0,6):C.R2GC_295_289,(0,0,7):C.R2GC_295_290,(0,0,2):C.R2GC_295_291,(0,0,3):C.R2GC_295_292})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.G0, P.G0, P.P__tilde__SDM, P.P__tilde__SDM ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               loop_particles = [ [ [P.G__plus__, P.W__plus__] ], [ [P.H, P.Z] ] ],
               couplings = {(0,0,0):C.R2GC_293_276,(0,0,1):C.R2GC_293_275})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.G__minus__, P.G__plus__, P.P__tilde__SDM, P.P__tilde__SDM ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ] ],
               couplings = {(0,0,0):C.R2GC_301_317,(0,0,1):C.R2GC_301_318,(0,0,2):C.R2GC_301_319})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.H, P.H, P.P__tilde__SDM, P.P__tilde__SDM ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               loop_particles = [ [ [P.G0, P.Z] ], [ [P.G__plus__, P.W__plus__] ] ],
               couplings = {(0,0,0):C.R2GC_293_275,(0,0,1):C.R2GC_293_276})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.G0, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H, P.Z] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_380_541,(0,0,1):C.R2GC_380_542,(0,0,5):C.R2GC_380_543,(0,0,6):C.R2GC_380_544,(0,0,7):C.R2GC_380_545,(0,0,8):C.R2GC_380_546,(0,0,3):C.R2GC_380_547,(0,0,4):C.R2GC_380_548,(0,0,2):C.R2GC_380_549})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.G__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                couplings = {(0,0,12):C.R2GC_380_545,(0,0,14):C.R2GC_388_615,(0,0,0):C.R2GC_388_616,(0,0,2):C.R2GC_287_251,(0,0,3):C.R2GC_388_617,(0,0,4):C.R2GC_380_542,(0,0,5):C.R2GC_388_618,(0,0,9):C.R2GC_388_619,(0,0,10):C.R2GC_388_620,(0,0,11):C.R2GC_380_544,(0,0,13):C.R2GC_388_621,(0,0,1):C.R2GC_387_614,(0,0,6):C.R2GC_388_622,(0,0,7):C.R2GC_388_623,(0,0,8):C.R2GC_388_624})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.H, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_296_293,(0,0,1):C.R2GC_296_294,(0,0,4):C.R2GC_296_295,(0,0,5):C.R2GC_296_296,(0,0,6):C.R2GC_296_297,(0,0,7):C.R2GC_296_298,(0,0,2):C.R2GC_296_299,(0,0,3):C.R2GC_296_300})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ] ],
                couplings = {(0,0,6):C.R2GC_285_239,(0,0,0):C.R2GC_300_311,(0,0,1):C.R2GC_300_312,(0,0,2):C.R2GC_300_313,(0,0,3):C.R2GC_300_314,(0,0,4):C.R2GC_300_315,(0,0,5):C.R2GC_300_316})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.a, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                couplings = {(0,0,0):C.R2GC_299_305,(0,0,1):C.R2GC_299_306,(0,0,2):C.R2GC_299_307,(0,0,3):C.R2GC_299_308,(0,0,4):C.R2GC_299_309,(0,0,5):C.R2GC_299_310})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV10, L.VVV2, L.VVV4, L.VVV6, L.VVV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
                couplings = {(0,0,0):C.R2GC_188_115,(0,0,1):C.R2GC_188_116,(0,2,0):C.R2GC_185_113,(0,2,1):C.R2GC_185_114,(0,3,0):C.R2GC_185_113,(0,3,1):C.R2GC_185_114,(0,4,0):C.R2GC_188_115,(0,4,1):C.R2GC_188_116,(0,5,0):C.R2GC_188_115,(0,5,1):C.R2GC_188_116,(0,1,0):C.R2GC_185_113,(0,1,1):C.R2GC_185_114})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
                couplings = {(2,0,0):C.R2GC_172_102,(2,0,1):C.R2GC_172_103,(0,0,0):C.R2GC_172_102,(0,0,1):C.R2GC_172_103,(6,0,0):C.R2GC_195_123,(6,0,1):C.R2GC_196_125,(4,0,0):C.R2GC_173_104,(4,0,1):C.R2GC_173_105,(3,0,0):C.R2GC_173_104,(3,0,1):C.R2GC_173_105,(8,0,0):C.R2GC_174_106,(8,0,1):C.R2GC_176_109,(7,0,0):C.R2GC_193_120,(7,0,1):C.R2GC_193_121,(5,0,0):C.R2GC_173_104,(5,0,1):C.R2GC_173_105,(1,0,0):C.R2GC_173_104,(1,0,1):C.R2GC_173_105,(11,0,0):C.R2GC_170_99,(11,0,1):C.R2GC_170_100,(10,0,0):C.R2GC_170_99,(10,0,1):C.R2GC_170_100,(9,0,1):C.R2GC_171_101,(2,1,0):C.R2GC_172_102,(2,1,1):C.R2GC_172_103,(0,1,0):C.R2GC_172_102,(0,1,1):C.R2GC_172_103,(4,1,0):C.R2GC_173_104,(4,1,1):C.R2GC_173_105,(3,1,0):C.R2GC_173_104,(3,1,1):C.R2GC_173_105,(8,1,0):C.R2GC_174_106,(8,1,1):C.R2GC_174_107,(6,1,0):C.R2GC_192_118,(6,1,1):C.R2GC_192_119,(7,1,0):C.R2GC_193_120,(7,1,1):C.R2GC_194_122,(5,1,0):C.R2GC_173_104,(5,1,1):C.R2GC_173_105,(1,1,0):C.R2GC_173_104,(1,1,1):C.R2GC_173_105,(11,1,0):C.R2GC_170_99,(11,1,1):C.R2GC_170_100,(10,1,0):C.R2GC_170_99,(10,1,1):C.R2GC_170_100,(9,1,1):C.R2GC_171_101,(2,2,0):C.R2GC_172_102,(2,2,1):C.R2GC_172_103,(0,2,0):C.R2GC_172_102,(0,2,1):C.R2GC_172_103,(4,2,0):C.R2GC_173_104,(4,2,1):C.R2GC_173_105,(3,2,0):C.R2GC_173_104,(3,2,1):C.R2GC_173_105,(8,2,0):C.R2GC_174_106,(8,2,1):C.R2GC_175_108,(6,2,0):C.R2GC_195_123,(6,2,1):C.R2GC_195_124,(7,2,0):C.R2GC_191_117,(7,2,1):C.R2GC_172_103,(5,2,0):C.R2GC_173_104,(5,2,1):C.R2GC_173_105,(1,2,0):C.R2GC_173_104,(1,2,1):C.R2GC_173_105,(11,2,0):C.R2GC_170_99,(11,2,1):C.R2GC_170_100,(10,2,0):C.R2GC_170_99,(10,2,1):C.R2GC_170_100,(9,2,1):C.R2GC_171_101})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.a, P.c, P.G__plus__] ], [ [P.a, P.c, P.s] ], [ [P.a, P.G__plus__, P.s] ], [ [P.c, P.G0, P.W__plus__], [P.c, P.H, P.W__plus__] ], [ [P.c, P.G__plus__, P.Z] ], [ [P.c, P.g, P.s] ], [ [P.c, P.s, P.Z] ], [ [P.G__plus__, P.s, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_343_406,(0,0,1):C.R2GC_343_407,(0,0,2):C.R2GC_343_408,(0,0,5):C.R2GC_343_409,(0,0,3):C.R2GC_343_410,(0,0,4):C.R2GC_343_411,(0,0,6):C.R2GC_343_412,(0,0,7):C.R2GC_343_413})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.a, P.b, P.G__plus__] ], [ [P.a, P.b, P.t] ], [ [P.a, P.G__plus__, P.t] ], [ [P.b, P.G0, P.t], [P.b, P.H, P.t] ], [ [P.b, P.G0, P.W__plus__], [P.b, P.H, P.W__plus__] ], [ [P.b, P.G__plus__, P.Z] ], [ [P.b, P.g, P.t] ], [ [P.b, P.t, P.Z] ], [ [P.G0, P.t, P.W__plus__], [P.H, P.t, P.W__plus__] ], [ [P.G__plus__, P.t, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_353_435,(0,0,1):C.R2GC_353_436,(0,0,2):C.R2GC_353_437,(0,0,6):C.R2GC_353_438,(0,0,3):C.R2GC_353_439,(0,0,4):C.R2GC_353_440,(0,0,5):C.R2GC_353_441,(0,0,7):C.R2GC_353_442,(0,0,9):C.R2GC_353_443,(0,1,0):C.R2GC_356_462,(0,1,1):C.R2GC_356_463,(0,1,2):C.R2GC_356_464,(0,1,6):C.R2GC_356_465,(0,1,3):C.R2GC_356_466,(0,1,5):C.R2GC_356_467,(0,1,7):C.R2GC_356_468,(0,1,8):C.R2GC_356_469,(0,1,9):C.R2GC_356_470})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0] ], [ [P.b, P.H] ], [ [P.b, P.H, P.Z] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.G__plus__, P.t, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_144_55,(0,0,1):C.R2GC_144_56,(0,0,2):C.R2GC_144_57,(0,0,3):C.R2GC_144_58,(0,0,5):C.R2GC_144_59,(0,0,6):C.R2GC_144_60,(0,0,4):C.R2GC_144_61,(0,0,7):C.R2GC_144_62})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0] ], [ [P.b, P.G0, P.Z] ], [ [P.b, P.H] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.G__plus__, P.t, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_145_63,(0,0,1):C.R2GC_145_64,(0,0,2):C.R2GC_145_65,(0,0,4):C.R2GC_145_66,(0,0,5):C.R2GC_145_67,(0,0,6):C.R2GC_145_68,(0,0,3):C.R2GC_145_69,(0,0,7):C.R2GC_145_70})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.vt__tilde__, P.ta__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.ta__minus__] ], [ [P.G0, P.ta__minus__, P.W__plus__], [P.H, P.ta__minus__, P.W__plus__] ], [ [P.G__plus__, P.ta__minus__, P.Z] ], [ [P.G__plus__, P.vt, P.Z] ], [ [P.ta__minus__, P.vt, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_369_483,(0,0,1):C.R2GC_369_484,(0,0,2):C.R2GC_369_485,(0,0,3):C.R2GC_369_486,(0,0,4):C.R2GC_369_487})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.ta__plus__, P.ta__minus__, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.G0, P.ta__minus__] ], [ [P.G__plus__, P.vt, P.W__plus__] ], [ [P.H, P.ta__minus__] ], [ [P.H, P.ta__minus__, P.Z] ], [ [P.ta__minus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_148_87,(0,0,1):C.R2GC_148_88,(0,0,3):C.R2GC_148_89,(0,0,5):C.R2GC_148_90,(0,0,2):C.R2GC_148_91,(0,0,4):C.R2GC_148_92})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.ta__plus__, P.ta__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.G0, P.ta__minus__] ], [ [P.G0, P.ta__minus__, P.Z] ], [ [P.G__plus__, P.vt, P.W__plus__] ], [ [P.H, P.ta__minus__] ], [ [P.ta__minus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_149_93,(0,0,1):C.R2GC_149_94,(0,0,4):C.R2GC_149_95,(0,0,5):C.R2GC_149_96,(0,0,2):C.R2GC_149_97,(0,0,3):C.R2GC_149_98})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.a, P.c, P.G__plus__] ], [ [P.a, P.c, P.s] ], [ [P.a, P.G__plus__, P.s] ], [ [P.c, P.G0, P.W__plus__], [P.c, P.H, P.W__plus__] ], [ [P.c, P.G__plus__, P.Z] ], [ [P.c, P.g, P.s] ], [ [P.c, P.s, P.Z] ], [ [P.G__plus__, P.s, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_344_414,(0,0,1):C.R2GC_344_415,(0,0,2):C.R2GC_344_416,(0,0,5):C.R2GC_344_417,(0,0,3):C.R2GC_344_418,(0,0,4):C.R2GC_344_419,(0,0,6):C.R2GC_344_420,(0,0,7):C.R2GC_344_421})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.a, P.b, P.G__plus__] ], [ [P.a, P.b, P.t] ], [ [P.a, P.G__plus__, P.t] ], [ [P.b, P.G0, P.t], [P.b, P.H, P.t] ], [ [P.b, P.G0, P.W__plus__], [P.b, P.H, P.W__plus__] ], [ [P.b, P.G__plus__, P.Z] ], [ [P.b, P.g, P.t] ], [ [P.b, P.t, P.Z] ], [ [P.G0, P.t, P.W__plus__], [P.H, P.t, P.W__plus__] ], [ [P.G__plus__, P.t, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_355_453,(0,0,1):C.R2GC_355_454,(0,0,2):C.R2GC_355_455,(0,0,6):C.R2GC_355_456,(0,0,3):C.R2GC_355_457,(0,0,5):C.R2GC_355_458,(0,0,7):C.R2GC_355_459,(0,0,8):C.R2GC_355_460,(0,0,9):C.R2GC_355_461,(0,1,0):C.R2GC_354_444,(0,1,1):C.R2GC_354_445,(0,1,2):C.R2GC_354_446,(0,1,6):C.R2GC_354_447,(0,1,3):C.R2GC_354_448,(0,1,4):C.R2GC_354_449,(0,1,5):C.R2GC_354_450,(0,1,7):C.R2GC_354_451,(0,1,9):C.R2GC_354_452})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0] ], [ [P.c, P.H] ], [ [P.c, P.H, P.Z] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_143_48,(0,0,1):C.R2GC_143_49,(0,0,2):C.R2GC_143_50,(0,0,3):C.R2GC_143_51,(0,0,5):C.R2GC_143_52,(0,0,4):C.R2GC_143_53,(0,0,6):C.R2GC_143_54})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.G__plus__, P.W__plus__] ], [ [P.G0, P.t] ], [ [P.g, P.t] ], [ [P.H, P.t] ], [ [P.H, P.t, P.Z] ], [ [P.t, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_147_79,(0,0,1):C.R2GC_147_80,(0,0,4):C.R2GC_147_81,(0,0,3):C.R2GC_147_82,(0,0,5):C.R2GC_147_83,(0,0,7):C.R2GC_147_84,(0,0,2):C.R2GC_147_85,(0,0,6):C.R2GC_147_86})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0] ], [ [P.c, P.G0, P.Z] ], [ [P.c, P.H] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_142_41,(0,0,1):C.R2GC_142_42,(0,0,2):C.R2GC_142_43,(0,0,4):C.R2GC_142_44,(0,0,5):C.R2GC_142_45,(0,0,3):C.R2GC_142_46,(0,0,6):C.R2GC_142_47})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.G__plus__, P.W__plus__] ], [ [P.G0, P.t] ], [ [P.G0, P.t, P.Z] ], [ [P.g, P.t] ], [ [P.H, P.t] ], [ [P.t, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_146_71,(0,0,1):C.R2GC_146_72,(0,0,5):C.R2GC_146_73,(0,0,3):C.R2GC_146_74,(0,0,6):C.R2GC_146_75,(0,0,7):C.R2GC_146_76,(0,0,2):C.R2GC_146_77,(0,0,4):C.R2GC_146_78})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.W__plus__] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_397_663,(0,0,2):C.R2GC_397_664,(0,0,3):C.R2GC_397_665,(0,0,5):C.R2GC_397_666,(0,0,8):C.R2GC_397_667,(0,0,11):C.R2GC_397_668,(0,0,12):C.R2GC_397_669,(0,0,0):C.R2GC_397_670,(0,0,4):C.R2GC_397_671,(0,0,6):C.R2GC_397_672,(0,0,7):C.R2GC_397_673,(0,0,9):C.R2GC_397_674,(0,0,10):C.R2GC_397_675})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_385_586,(0,0,2):C.R2GC_385_587,(0,0,3):C.R2GC_385_588,(0,0,8):C.R2GC_385_589,(0,0,10):C.R2GC_385_590,(0,0,11):C.R2GC_385_591,(0,0,12):C.R2GC_385_592,(0,0,0):C.R2GC_385_593,(0,0,4):C.R2GC_385_594,(0,0,5):C.R2GC_385_595,(0,0,6):C.R2GC_385_596,(0,0,7):C.R2GC_385_597,(0,0,9):C.R2GC_385_598})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.a, P.W__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_389_625,(0,0,2):C.R2GC_389_626,(0,0,3):C.R2GC_389_627,(0,0,5):C.R2GC_389_628,(0,0,6):C.R2GC_389_629,(0,0,0):C.R2GC_389_630,(0,0,4):C.R2GC_389_631})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.W__minus__, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                couplings = {(0,0,1):C.R2GC_395_656,(0,0,2):C.R2GC_395_657,(0,0,8):C.R2GC_395_658,(0,0,0):C.R2GC_395_659,(0,0,3):C.R2GC_393_652,(0,0,4):C.R2GC_393_651,(0,0,5):C.R2GC_395_660,(0,0,6):C.R2GC_395_661,(0,0,7):C.R2GC_395_662,(0,1,1):C.R2GC_393_647,(0,1,2):C.R2GC_393_648,(0,1,8):C.R2GC_393_649,(0,1,0):C.R2GC_393_650,(0,1,3):C.R2GC_393_651,(0,1,4):C.R2GC_393_652,(0,1,5):C.R2GC_393_653,(0,1,6):C.R2GC_393_654,(0,1,7):C.R2GC_393_655})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.W__minus__, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                couplings = {(0,0,1):C.R2GC_383_570,(0,0,2):C.R2GC_383_571,(0,0,8):C.R2GC_383_572,(0,0,0):C.R2GC_383_573,(0,0,3):C.R2GC_383_574,(0,0,4):C.R2GC_383_575,(0,0,5):C.R2GC_383_576,(0,0,6):C.R2GC_383_577,(0,0,7):C.R2GC_383_578,(0,1,1):C.R2GC_384_579,(0,1,2):C.R2GC_384_580,(0,1,8):C.R2GC_384_581,(0,1,0):C.R2GC_384_582,(0,1,3):C.R2GC_383_577,(0,1,4):C.R2GC_384_583,(0,1,5):C.R2GC_384_584,(0,1,6):C.R2GC_383_574,(0,1,7):C.R2GC_384_585})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.a, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVV1, L.VVV10, L.VVV2, L.VVV4, L.VVV6, L.VVV9 ],
                loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_314_335,(0,0,1):C.R2GC_314_336,(0,0,2):C.R2GC_314_337,(0,0,3):C.R2GC_314_338,(0,2,0):C.R2GC_313_333,(0,2,1):C.R2GC_268_224,(0,2,2):C.R2GC_234_190,(0,2,3):C.R2GC_313_334,(0,3,0):C.R2GC_313_333,(0,3,1):C.R2GC_268_224,(0,3,2):C.R2GC_234_190,(0,3,3):C.R2GC_313_334,(0,4,0):C.R2GC_314_335,(0,4,1):C.R2GC_314_336,(0,4,2):C.R2GC_314_337,(0,4,3):C.R2GC_314_338,(0,5,0):C.R2GC_314_335,(0,5,1):C.R2GC_314_336,(0,5,2):C.R2GC_314_337,(0,5,3):C.R2GC_314_338,(0,1,0):C.R2GC_313_333,(0,1,1):C.R2GC_268_224,(0,1,2):C.R2GC_234_190,(0,1,3):C.R2GC_313_334})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.W__plus__] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_397_663,(0,0,2):C.R2GC_397_664,(0,0,3):C.R2GC_397_665,(0,0,5):C.R2GC_397_666,(0,0,8):C.R2GC_397_667,(0,0,11):C.R2GC_397_668,(0,0,12):C.R2GC_397_669,(0,0,0):C.R2GC_397_670,(0,0,4):C.R2GC_397_671,(0,0,6):C.R2GC_397_672,(0,0,7):C.R2GC_397_673,(0,0,9):C.R2GC_397_674,(0,0,10):C.R2GC_397_675})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_385_592,(0,0,2):C.R2GC_386_599,(0,0,3):C.R2GC_386_600,(0,0,8):C.R2GC_385_590,(0,0,10):C.R2GC_385_589,(0,0,11):C.R2GC_386_601,(0,0,12):C.R2GC_385_586,(0,0,0):C.R2GC_386_602,(0,0,4):C.R2GC_385_597,(0,0,5):C.R2GC_386_603,(0,0,6):C.R2GC_386_604,(0,0,7):C.R2GC_385_594,(0,0,9):C.R2GC_386_605})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.a, P.W__plus__, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_389_629,(0,0,2):C.R2GC_390_632,(0,0,3):C.R2GC_390_633,(0,0,5):C.R2GC_390_634,(0,0,6):C.R2GC_389_625,(0,0,0):C.R2GC_390_635,(0,0,4):C.R2GC_390_636})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.W__plus__, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                couplings = {(0,0,1):C.R2GC_393_647,(0,0,2):C.R2GC_393_648,(0,0,8):C.R2GC_393_649,(0,0,0):C.R2GC_393_650,(0,0,3):C.R2GC_393_651,(0,0,4):C.R2GC_393_652,(0,0,5):C.R2GC_393_653,(0,0,6):C.R2GC_393_654,(0,0,7):C.R2GC_393_655,(0,1,1):C.R2GC_395_656,(0,1,2):C.R2GC_395_657,(0,1,8):C.R2GC_395_658,(0,1,0):C.R2GC_395_659,(0,1,3):C.R2GC_393_652,(0,1,4):C.R2GC_393_651,(0,1,5):C.R2GC_395_660,(0,1,6):C.R2GC_395_661,(0,1,7):C.R2GC_395_662})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.W__plus__, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                couplings = {(0,0,1):C.R2GC_383_570,(0,0,2):C.R2GC_383_571,(0,0,8):C.R2GC_383_572,(0,0,0):C.R2GC_383_573,(0,0,3):C.R2GC_383_574,(0,0,4):C.R2GC_383_575,(0,0,5):C.R2GC_383_576,(0,0,6):C.R2GC_383_577,(0,0,7):C.R2GC_383_578,(0,1,1):C.R2GC_384_579,(0,1,2):C.R2GC_384_580,(0,1,8):C.R2GC_384_581,(0,1,0):C.R2GC_384_582,(0,1,3):C.R2GC_383_577,(0,1,4):C.R2GC_384_583,(0,1,5):C.R2GC_384_584,(0,1,6):C.R2GC_383_574,(0,1,7):C.R2GC_384_585})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__], [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                couplings = {(0,0,11):C.R2GC_382_556,(0,0,13):C.R2GC_382_557,(0,0,1):C.R2GC_382_558,(0,0,2):C.R2GC_382_559,(0,0,3):C.R2GC_382_560,(0,0,6):C.R2GC_382_562,(0,0,9):C.R2GC_382_561,(0,0,10):C.R2GC_382_563,(0,0,12):C.R2GC_382_564,(0,0,0):C.R2GC_382_565,(0,0,4):C.R2GC_382_566,(0,0,5):C.R2GC_382_567,(0,0,7):C.R2GC_382_569,(0,0,8):C.R2GC_382_568})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a] ], [ [P.a, P.G0, P.G__plus__], [P.a, P.G__plus__, P.H] ], [ [P.a, P.G0, P.W__plus__], [P.a, P.H, P.W__plus__] ], [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.G__plus__, P.W__plus__, P.Z] ], [ [P.a, P.G__plus__, P.Z] ], [ [P.a, P.W__plus__] ], [ [P.a, P.W__plus__, P.Z] ], [ [P.a, P.Z] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__], [P.G__plus__, P.H, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z], [P.G__plus__, P.H, P.Z] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z], [P.H, P.W__plus__, P.Z] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_400_690,(0,0,19):C.R2GC_382_556,(0,0,21):C.R2GC_400_691,(0,0,3):C.R2GC_400_692,(0,0,7):C.R2GC_400_693,(0,0,9):C.R2GC_400_694,(0,0,10):C.R2GC_382_559,(0,0,11):C.R2GC_382_560,(0,0,14):C.R2GC_400_695,(0,0,17):C.R2GC_400_696,(0,0,18):C.R2GC_382_563,(0,0,20):C.R2GC_400_697,(0,0,1):C.R2GC_400_698,(0,0,2):C.R2GC_400_699,(0,0,4):C.R2GC_400_700,(0,0,6):C.R2GC_400_701,(0,0,8):C.R2GC_400_702,(0,0,12):C.R2GC_382_566,(0,0,13):C.R2GC_400_703,(0,0,15):C.R2GC_400_704,(0,0,16):C.R2GC_400_705,(0,0,5):C.R2GC_400_706})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__], [P.G__plus__, P.H, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                couplings = {(0,0,11):C.R2GC_382_556,(0,0,13):C.R2GC_382_557,(0,0,1):C.R2GC_382_558,(0,0,2):C.R2GC_382_559,(0,0,3):C.R2GC_382_560,(0,0,7):C.R2GC_382_561,(0,0,8):C.R2GC_382_562,(0,0,10):C.R2GC_382_563,(0,0,12):C.R2GC_382_564,(0,0,0):C.R2GC_382_565,(0,0,4):C.R2GC_382_566,(0,0,5):C.R2GC_382_567,(0,0,6):C.R2GC_382_568,(0,0,9):C.R2GC_382_569})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                couplings = {(0,0,6):C.R2GC_387_606,(0,0,8):C.R2GC_387_607,(0,0,1):C.R2GC_387_608,(0,0,2):C.R2GC_387_609,(0,0,3):C.R2GC_387_610,(0,0,5):C.R2GC_387_611,(0,0,7):C.R2GC_387_612,(0,0,0):C.R2GC_387_613,(0,0,4):C.R2GC_387_614})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,3):C.R2GC_321_339,(0,0,0):C.R2GC_321_340,(0,0,1):C.R2GC_321_341,(0,0,2):C.R2GC_321_342,(0,0,4):C.R2GC_321_343,(0,1,3):C.R2GC_321_339,(0,1,0):C.R2GC_321_340,(0,1,1):C.R2GC_321_341,(0,1,2):C.R2GC_321_342,(0,1,4):C.R2GC_321_343,(0,2,3):C.R2GC_322_344,(0,2,0):C.R2GC_322_345,(0,2,1):C.R2GC_322_346,(0,2,2):C.R2GC_322_347,(0,2,4):C.R2GC_322_348})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVV1, L.VVV10, L.VVV2, L.VVV4, L.VVV6, L.VVV9 ],
                loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_335_392,(0,0,1):C.R2GC_335_393,(0,0,2):C.R2GC_335_394,(0,0,3):C.R2GC_335_395,(0,2,0):C.R2GC_308_328,(0,2,1):C.R2GC_308_329,(0,2,2):C.R2GC_308_330,(0,2,3):C.R2GC_308_331,(0,3,0):C.R2GC_308_328,(0,3,1):C.R2GC_308_329,(0,3,2):C.R2GC_308_330,(0,3,3):C.R2GC_308_331,(0,4,0):C.R2GC_335_392,(0,4,1):C.R2GC_335_393,(0,4,2):C.R2GC_335_394,(0,4,3):C.R2GC_335_395,(0,5,0):C.R2GC_335_392,(0,5,1):C.R2GC_335_393,(0,5,2):C.R2GC_335_394,(0,5,3):C.R2GC_335_395,(0,1,0):C.R2GC_308_328,(0,1,1):C.R2GC_308_329,(0,1,2):C.R2GC_308_330,(0,1,3):C.R2GC_308_331})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.a] ], [ [P.a, P.W__plus__] ], [ [P.a, P.W__plus__, P.Z] ], [ [P.a, P.Z] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_401_707,(0,0,6):C.R2GC_401_708,(0,0,8):C.R2GC_401_709,(0,0,1):C.R2GC_401_710,(0,0,3):C.R2GC_401_711,(0,0,4):C.R2GC_401_712,(0,0,5):C.R2GC_401_713,(0,0,7):C.R2GC_401_714,(0,0,2):C.R2GC_401_715,(0,1,0):C.R2GC_401_707,(0,1,6):C.R2GC_401_708,(0,1,8):C.R2GC_401_709,(0,1,1):C.R2GC_401_710,(0,1,3):C.R2GC_401_711,(0,1,4):C.R2GC_401_712,(0,1,5):C.R2GC_401_713,(0,1,7):C.R2GC_401_714,(0,1,2):C.R2GC_401_715,(0,2,6):C.R2GC_402_716,(0,2,1):C.R2GC_402_717,(0,2,4):C.R2GC_402_718,(0,2,5):C.R2GC_402_719,(0,2,7):C.R2GC_402_720,(0,2,2):C.R2GC_402_721})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.ta__plus__, P.vt, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.ta__minus__] ], [ [P.G0, P.ta__minus__, P.W__plus__], [P.H, P.ta__minus__, P.W__plus__] ], [ [P.G__plus__, P.ta__minus__, P.Z] ], [ [P.G__plus__, P.vt, P.Z] ], [ [P.ta__minus__, P.vt, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_368_478,(0,0,1):C.R2GC_368_479,(0,0,2):C.R2GC_368_480,(0,0,3):C.R2GC_368_481,(0,0,4):C.R2GC_368_482})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ] ],
                couplings = {(0,0,6):C.R2GC_286_245,(0,0,0):C.R2GC_374_509,(0,0,1):C.R2GC_374_510,(0,0,2):C.R2GC_374_511,(0,0,3):C.R2GC_374_512,(0,0,4):C.R2GC_374_513,(0,0,5):C.R2GC_374_514})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.Z, P.G0, P.H ],
                color = [ '1' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ] ],
                couplings = {(0,0,0):C.R2GC_376_521,(0,0,1):C.R2GC_376_522,(0,0,4):C.R2GC_376_523,(0,0,5):C.R2GC_376_524,(0,0,3):C.R2GC_376_525,(0,0,2):C.R2GC_376_526,(0,1,0):C.R2GC_375_515,(0,1,1):C.R2GC_375_516,(0,1,4):C.R2GC_375_517,(0,1,5):C.R2GC_375_518,(0,1,3):C.R2GC_375_519,(0,1,2):C.R2GC_375_520})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.H, P.W__plus__] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                couplings = {(0,0,0):C.R2GC_373_502,(0,0,1):C.R2GC_373_503,(0,0,2):C.R2GC_373_504,(0,0,4):C.R2GC_373_505,(0,0,5):C.R2GC_373_506,(0,0,6):C.R2GC_373_507,(0,0,3):C.R2GC_373_508,(0,1,0):C.R2GC_372_495,(0,1,1):C.R2GC_372_496,(0,1,2):C.R2GC_372_497,(0,1,4):C.R2GC_372_498,(0,1,5):C.R2GC_372_499,(0,1,6):C.R2GC_372_500,(0,1,3):C.R2GC_372_501})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.H, P.Z] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_403_722,(0,0,2):C.R2GC_403_723,(0,0,3):C.R2GC_403_724,(0,0,6):C.R2GC_403_725,(0,0,10):C.R2GC_403_726,(0,0,13):C.R2GC_403_727,(0,0,14):C.R2GC_403_728,(0,0,0):C.R2GC_403_729,(0,0,5):C.R2GC_403_730,(0,0,7):C.R2GC_403_731,(0,0,8):C.R2GC_403_732,(0,0,9):C.R2GC_403_733,(0,0,11):C.R2GC_403_734,(0,0,12):C.R2GC_403_735,(0,0,4):C.R2GC_403_736})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.H, P.Z] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_404_743,(0,0,2):C.R2GC_405_752,(0,0,3):C.R2GC_405_753,(0,0,9):C.R2GC_404_741,(0,0,11):C.R2GC_404_740,(0,0,13):C.R2GC_405_754,(0,0,14):C.R2GC_404_737,(0,0,0):C.R2GC_405_755,(0,0,5):C.R2GC_404_748,(0,0,6):C.R2GC_405_756,(0,0,7):C.R2GC_405_757,(0,0,8):C.R2GC_404_745,(0,0,10):C.R2GC_405_758,(0,0,12):C.R2GC_405_759,(0,0,4):C.R2GC_405_760})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.W__minus__, P.Z, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_398_676,(0,0,2):C.R2GC_398_677,(0,0,3):C.R2GC_398_678,(0,0,5):C.R2GC_398_679,(0,0,7):C.R2GC_398_680,(0,0,0):C.R2GC_398_681,(0,0,4):C.R2GC_398_682,(0,0,6):C.R2GC_398_683})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.H, P.Z] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_403_722,(0,0,2):C.R2GC_403_723,(0,0,3):C.R2GC_403_724,(0,0,6):C.R2GC_403_725,(0,0,10):C.R2GC_403_726,(0,0,13):C.R2GC_403_727,(0,0,14):C.R2GC_403_728,(0,0,0):C.R2GC_403_729,(0,0,5):C.R2GC_403_730,(0,0,7):C.R2GC_403_731,(0,0,8):C.R2GC_403_732,(0,0,9):C.R2GC_403_733,(0,0,11):C.R2GC_403_734,(0,0,12):C.R2GC_403_735,(0,0,4):C.R2GC_403_736})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.H, P.Z] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_404_737,(0,0,2):C.R2GC_404_738,(0,0,3):C.R2GC_404_739,(0,0,9):C.R2GC_404_740,(0,0,11):C.R2GC_404_741,(0,0,13):C.R2GC_404_742,(0,0,14):C.R2GC_404_743,(0,0,0):C.R2GC_404_744,(0,0,5):C.R2GC_404_745,(0,0,6):C.R2GC_404_746,(0,0,7):C.R2GC_404_747,(0,0,8):C.R2GC_404_748,(0,0,10):C.R2GC_404_749,(0,0,12):C.R2GC_404_750,(0,0,4):C.R2GC_404_751})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.W__plus__, P.Z, P.G__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,1):C.R2GC_398_680,(0,0,2):C.R2GC_399_684,(0,0,3):C.R2GC_399_685,(0,0,5):C.R2GC_399_686,(0,0,7):C.R2GC_398_676,(0,0,0):C.R2GC_399_687,(0,0,4):C.R2GC_399_688,(0,0,6):C.R2GC_399_689})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,1,3):C.R2GC_338_396,(0,1,0):C.R2GC_338_397,(0,1,1):C.R2GC_338_398,(0,1,2):C.R2GC_338_399,(0,1,4):C.R2GC_338_400,(0,2,3):C.R2GC_339_401,(0,2,0):C.R2GC_339_402,(0,2,1):C.R2GC_339_403,(0,2,2):C.R2GC_339_404,(0,2,4):C.R2GC_339_405,(0,3,3):C.R2GC_339_401,(0,3,0):C.R2GC_339_402,(0,3,1):C.R2GC_339_403,(0,3,2):C.R2GC_339_404,(0,3,4):C.R2GC_339_405,(0,0,1):C.R2GC_141_39,(0,0,2):C.R2GC_141_40})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.Z, P.Z, P.G0, P.G0 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H, P.Z] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_377_527,(0,0,1):C.R2GC_377_528,(0,0,5):C.R2GC_377_529,(0,0,6):C.R2GC_377_530,(0,0,7):C.R2GC_371_488,(0,0,3):C.R2GC_377_532,(0,0,4):C.R2GC_377_531,(0,0,2):C.R2GC_218_175})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.H, P.W__plus__] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ] ],
                couplings = {(0,0,7):C.R2GC_371_488,(0,0,0):C.R2GC_300_315,(0,0,1):C.R2GC_371_489,(0,0,2):C.R2GC_371_490,(0,0,4):C.R2GC_371_491,(0,0,5):C.R2GC_371_492,(0,0,6):C.R2GC_371_493,(0,0,3):C.R2GC_371_494})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.Z, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0, P.H, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_377_527,(0,0,1):C.R2GC_377_528,(0,0,5):C.R2GC_377_529,(0,0,6):C.R2GC_377_530,(0,0,7):C.R2GC_371_488,(0,0,3):C.R2GC_377_531,(0,0,4):C.R2GC_377_532,(0,0,2):C.R2GC_218_175})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.Z, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_381_550,(0,0,1):C.R2GC_381_551,(0,0,3):C.R2GC_381_552,(0,0,4):C.R2GC_381_553,(0,0,5):C.R2GC_381_554,(0,0,2):C.R2GC_381_555})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                couplings = {(0,0,3):C.R2GC_330_384,(0,0,0):C.R2GC_321_343,(0,0,1):C.R2GC_330_385,(0,0,2):C.R2GC_330_386,(0,0,4):C.R2GC_330_387,(0,1,3):C.R2GC_330_384,(0,1,0):C.R2GC_321_343,(0,1,1):C.R2GC_330_385,(0,1,2):C.R2GC_330_386,(0,1,4):C.R2GC_330_387,(0,2,3):C.R2GC_331_388,(0,2,0):C.R2GC_322_348,(0,2,1):C.R2GC_331_389,(0,2,2):C.R2GC_331_390,(0,2,4):C.R2GC_331_391})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.e__plus__, P.e__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.e__minus__] ], [ [P.e__minus__, P.Z] ], [ [P.ve, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_118_5,(0,1,1):C.R2GC_268_223,(0,1,2):C.R2GC_268_224,(0,2,1):C.R2GC_212_163})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.mu__plus__, P.mu__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.mu__minus__] ], [ [P.mu__minus__, P.Z] ], [ [P.vm, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_118_5,(0,1,1):C.R2GC_268_223,(0,1,2):C.R2GC_268_224,(0,2,1):C.R2GC_212_163})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.ta__plus__, P.ta__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.G0, P.ta__minus__], [P.H, P.ta__minus__] ], [ [P.ta__minus__, P.Z] ], [ [P.vt, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_118_5,(0,0,1):C.R2GC_278_231,(0,0,2):C.R2GC_268_223,(0,0,3):C.R2GC_268_224,(0,1,0):C.R2GC_118_5,(0,1,1):C.R2GC_278_231,(0,1,2):C.R2GC_212_163})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.u] ], [ [P.d, P.W__plus__] ], [ [P.g, P.u] ], [ [P.u, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_139_37,(0,0,2):C.R2GC_139_38,(0,1,1):C.R2GC_229_185,(0,1,3):C.R2GC_229_184,(0,2,3):C.R2GC_226_178})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0], [P.c, P.H] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s] ], [ [P.s, P.W__plus__] ] ],
                couplings = {(0,0,2):C.R2GC_132_27,(0,1,0):C.R2GC_139_37,(0,1,1):C.R2GC_139_38,(0,1,3):C.R2GC_229_184,(0,1,5):C.R2GC_229_185,(0,2,0):C.R2GC_139_37,(0,2,1):C.R2GC_139_38,(0,2,3):C.R2GC_226_178,(0,2,4):C.R2GC_226_179})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.W__plus__] ], [ [P.G0, P.t], [P.H, P.t] ], [ [P.g, P.t] ], [ [P.t, P.Z] ] ],
                couplings = {(0,0,3):C.R2GC_135_32,(0,1,0):C.R2GC_139_37,(0,1,1):C.R2GC_248_207,(0,1,2):C.R2GC_229_185,(0,1,4):C.R2GC_139_38,(0,1,5):C.R2GC_229_184,(0,2,0):C.R2GC_139_37,(0,2,1):C.R2GC_249_208,(0,2,4):C.R2GC_139_38,(0,2,5):C.R2GC_226_178})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.d] ], [ [P.d, P.g] ], [ [P.d, P.Z] ], [ [P.u, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_115_2,(0,1,1):C.R2GC_208_156,(0,1,2):C.R2GC_234_191,(0,1,3):C.R2GC_234_190,(0,2,1):C.R2GC_208_156,(0,2,2):C.R2GC_208_157})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.s] ], [ [P.c, P.G__plus__] ], [ [P.c, P.W__plus__] ], [ [P.g, P.s] ], [ [P.s, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_115_2,(0,0,1):C.R2GC_234_189,(0,0,2):C.R2GC_234_190,(0,0,3):C.R2GC_208_156,(0,0,4):C.R2GC_234_191,(0,1,0):C.R2GC_115_2,(0,1,3):C.R2GC_208_156,(0,1,4):C.R2GC_208_157})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0], [P.b, P.H] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.t, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_115_2,(0,0,1):C.R2GC_208_156,(0,0,2):C.R2GC_240_198,(0,0,3):C.R2GC_234_191,(0,0,4):C.R2GC_244_205,(0,0,5):C.R2GC_234_190,(0,1,0):C.R2GC_115_2,(0,1,1):C.R2GC_208_156,(0,1,2):C.R2GC_240_198,(0,1,3):C.R2GC_208_157,(0,1,4):C.R2GC_240_199})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.u] ], [ [P.d, P.W__plus__] ], [ [P.g, P.u] ], [ [P.u, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_133_28,(0,0,2):C.R2GC_133_29,(0,1,1):C.R2GC_230_187,(0,1,3):C.R2GC_230_186,(0,2,3):C.R2GC_227_180})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0], [P.c, P.H] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s] ], [ [P.s, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_133_28,(0,0,1):C.R2GC_133_29,(0,0,2):C.R2GC_133_30,(0,1,3):C.R2GC_230_186,(0,1,5):C.R2GC_230_187,(0,2,3):C.R2GC_227_180,(0,2,4):C.R2GC_227_181})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.W__plus__] ], [ [P.G0, P.t], [P.H, P.t] ], [ [P.g, P.t] ], [ [P.t, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_133_28,(0,0,4):C.R2GC_133_29,(0,0,3):C.R2GC_136_33,(0,1,1):C.R2GC_241_201,(0,1,2):C.R2GC_230_187,(0,1,5):C.R2GC_230_186,(0,2,1):C.R2GC_245_206,(0,2,5):C.R2GC_227_180})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.d] ], [ [P.d, P.g] ], [ [P.d, P.Z] ], [ [P.u, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_116_3,(0,1,1):C.R2GC_133_29,(0,1,2):C.R2GC_235_192,(0,1,3):C.R2GC_230_187,(0,2,1):C.R2GC_133_29,(0,2,2):C.R2GC_209_158})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.s] ], [ [P.c, P.G__plus__] ], [ [P.c, P.W__plus__] ], [ [P.g, P.s] ], [ [P.s, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_116_3,(0,0,1):C.R2GC_227_181,(0,0,2):C.R2GC_230_187,(0,0,3):C.R2GC_133_29,(0,0,4):C.R2GC_235_192,(0,1,0):C.R2GC_116_3,(0,1,3):C.R2GC_133_29,(0,1,4):C.R2GC_209_158})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0], [P.b, P.H] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.t, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_116_3,(0,0,1):C.R2GC_133_29,(0,0,2):C.R2GC_241_200,(0,0,3):C.R2GC_235_192,(0,0,4):C.R2GC_245_206,(0,0,5):C.R2GC_230_187,(0,1,0):C.R2GC_116_3,(0,1,1):C.R2GC_133_29,(0,1,2):C.R2GC_241_200,(0,1,3):C.R2GC_209_158,(0,1,4):C.R2GC_241_201})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.d, P.u] ], [ [P.a, P.d, P.W__plus__] ], [ [P.a, P.u, P.W__plus__] ], [ [P.d, P.g, P.u] ], [ [P.d, P.u, P.Z] ], [ [P.d, P.W__plus__, P.Z] ], [ [P.u, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_345_422,(0,0,1):C.R2GC_345_424,(0,0,2):C.R2GC_345_423,(0,0,3):C.R2GC_345_425,(0,0,4):C.R2GC_345_426,(0,0,5):C.R2GC_345_428,(0,0,6):C.R2GC_345_427})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.c, P.s] ], [ [P.a, P.c, P.W__plus__] ], [ [P.a, P.s, P.W__plus__] ], [ [P.c, P.g, P.s] ], [ [P.c, P.s, P.Z] ], [ [P.c, P.W__plus__, P.Z] ], [ [P.s, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_345_422,(0,0,1):C.R2GC_345_423,(0,0,2):C.R2GC_345_424,(0,0,3):C.R2GC_345_425,(0,0,4):C.R2GC_345_426,(0,0,5):C.R2GC_345_427,(0,0,6):C.R2GC_345_428})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.b, P.t] ], [ [P.a, P.b, P.W__plus__] ], [ [P.a, P.t, P.W__plus__] ], [ [P.b, P.G0, P.t] ], [ [P.b, P.g, P.t] ], [ [P.b, P.H, P.t] ], [ [P.b, P.t, P.Z] ], [ [P.b, P.W__plus__, P.Z] ], [ [P.t, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_345_422,(0,0,1):C.R2GC_345_424,(0,0,2):C.R2GC_345_423,(0,0,4):C.R2GC_345_425,(0,0,6):C.R2GC_345_426,(0,0,7):C.R2GC_345_428,(0,0,8):C.R2GC_345_427,(0,1,3):C.R2GC_348_433,(0,1,5):C.R2GC_348_434})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.d, P.u] ], [ [P.a, P.d, P.W__plus__] ], [ [P.a, P.u, P.W__plus__] ], [ [P.d, P.g, P.u] ], [ [P.d, P.u, P.Z] ], [ [P.d, P.W__plus__, P.Z] ], [ [P.u, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_345_422,(0,0,1):C.R2GC_345_424,(0,0,2):C.R2GC_345_423,(0,0,3):C.R2GC_345_425,(0,0,4):C.R2GC_345_426,(0,0,5):C.R2GC_345_428,(0,0,6):C.R2GC_345_427})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.c, P.s] ], [ [P.a, P.c, P.W__plus__] ], [ [P.a, P.s, P.W__plus__] ], [ [P.c, P.g, P.s] ], [ [P.c, P.s, P.Z] ], [ [P.c, P.W__plus__, P.Z] ], [ [P.s, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_345_422,(0,0,1):C.R2GC_345_423,(0,0,2):C.R2GC_345_424,(0,0,3):C.R2GC_345_425,(0,0,4):C.R2GC_345_426,(0,0,5):C.R2GC_345_427,(0,0,6):C.R2GC_345_428})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.b, P.t] ], [ [P.a, P.b, P.W__plus__] ], [ [P.a, P.t, P.W__plus__] ], [ [P.b, P.G0, P.t] ], [ [P.b, P.g, P.t] ], [ [P.b, P.H, P.t] ], [ [P.b, P.t, P.Z] ], [ [P.b, P.W__plus__, P.Z] ], [ [P.t, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_345_422,(0,0,1):C.R2GC_345_424,(0,0,2):C.R2GC_345_423,(0,0,4):C.R2GC_345_425,(0,0,6):C.R2GC_345_426,(0,0,7):C.R2GC_345_428,(0,0,8):C.R2GC_345_427,(0,1,3):C.R2GC_348_433,(0,1,5):C.R2GC_348_434})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.e__plus__, P.ve, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.e__minus__, P.W__plus__] ], [ [P.e__minus__, P.ve, P.Z] ], [ [P.e__minus__, P.W__plus__, P.Z] ], [ [P.ve, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_363_474,(0,0,1):C.R2GC_363_475,(0,0,2):C.R2GC_363_476,(0,0,3):C.R2GC_363_477})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.mu__minus__, P.W__plus__] ], [ [P.mu__minus__, P.vm, P.Z] ], [ [P.mu__minus__, P.W__plus__, P.Z] ], [ [P.vm, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_363_474,(0,0,1):C.R2GC_363_475,(0,0,2):C.R2GC_363_476,(0,0,3):C.R2GC_363_477})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.ta__minus__, P.W__plus__] ], [ [P.ta__minus__, P.vt, P.Z] ], [ [P.ta__minus__, P.W__plus__, P.Z] ], [ [P.vt, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_363_474,(0,0,1):C.R2GC_363_475,(0,0,2):C.R2GC_363_476,(0,0,3):C.R2GC_363_477})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.e__minus__, P.W__plus__] ], [ [P.e__minus__, P.ve, P.Z] ], [ [P.e__minus__, P.W__plus__, P.Z] ], [ [P.ve, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_363_474,(0,0,1):C.R2GC_363_475,(0,0,2):C.R2GC_363_476,(0,0,3):C.R2GC_363_477})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.mu__minus__, P.W__plus__] ], [ [P.mu__minus__, P.vm, P.Z] ], [ [P.mu__minus__, P.W__plus__, P.Z] ], [ [P.vm, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_363_474,(0,0,1):C.R2GC_363_475,(0,0,2):C.R2GC_363_476,(0,0,3):C.R2GC_363_477})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.a, P.ta__minus__, P.W__plus__] ], [ [P.ta__minus__, P.vt, P.Z] ], [ [P.ta__minus__, P.W__plus__, P.Z] ], [ [P.vt, P.W__plus__, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_363_474,(0,0,1):C.R2GC_363_475,(0,0,2):C.R2GC_363_476,(0,0,3):C.R2GC_363_477})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.u] ], [ [P.d, P.W__plus__] ], [ [P.g, P.u] ], [ [P.u, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_266_218,(0,0,1):C.R2GC_266_219,(0,0,2):C.R2GC_266_220,(0,0,3):C.R2GC_266_221,(0,1,0):C.R2GC_265_215,(0,1,2):C.R2GC_265_216,(0,1,3):C.R2GC_265_217})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0], [P.c, P.H] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s] ], [ [P.s, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_266_218,(0,0,1):C.R2GC_266_220,(0,0,2):C.R2GC_329_383,(0,0,3):C.R2GC_266_221,(0,0,5):C.R2GC_266_219,(0,1,0):C.R2GC_265_215,(0,1,1):C.R2GC_265_216,(0,1,2):C.R2GC_328_381,(0,1,3):C.R2GC_265_217,(0,1,4):C.R2GC_328_382})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.W__plus__] ], [ [P.G0, P.t], [P.H, P.t] ], [ [P.g, P.t] ], [ [P.t, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_266_218,(0,0,1):C.R2GC_347_431,(0,0,2):C.R2GC_266_219,(0,0,4):C.R2GC_266_220,(0,0,3):C.R2GC_347_432,(0,0,5):C.R2GC_266_221,(0,1,0):C.R2GC_265_215,(0,1,1):C.R2GC_346_429,(0,1,4):C.R2GC_265_216,(0,1,3):C.R2GC_346_430,(0,1,5):C.R2GC_265_217})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.d] ], [ [P.d, P.g] ], [ [P.d, P.Z] ], [ [P.u, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_237_193,(0,0,1):C.R2GC_237_196,(0,0,2):C.R2GC_237_197,(0,0,3):C.R2GC_237_195,(0,1,0):C.R2GC_210_159,(0,1,1):C.R2GC_210_160,(0,1,2):C.R2GC_210_161})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.s] ], [ [P.c, P.G__plus__] ], [ [P.c, P.W__plus__] ], [ [P.g, P.s] ], [ [P.s, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_237_193,(0,0,1):C.R2GC_237_194,(0,0,2):C.R2GC_237_195,(0,0,3):C.R2GC_237_196,(0,0,4):C.R2GC_237_197,(0,1,0):C.R2GC_210_159,(0,1,3):C.R2GC_210_160,(0,1,4):C.R2GC_210_161})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0], [P.b, P.H] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.t, P.W__plus__] ] ],
                couplings = {(0,0,0):C.R2GC_237_193,(0,0,1):C.R2GC_237_196,(0,0,2):C.R2GC_326_377,(0,0,3):C.R2GC_237_197,(0,0,4):C.R2GC_326_378,(0,0,5):C.R2GC_237_195,(0,1,0):C.R2GC_210_159,(0,1,1):C.R2GC_210_160,(0,1,2):C.R2GC_327_379,(0,1,3):C.R2GC_210_161,(0,1,4):C.R2GC_327_380})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.ve__tilde__, P.ve, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.e__minus__, P.W__plus__] ], [ [P.ve, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_271_229,(0,0,1):C.R2GC_271_230})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.vm__tilde__, P.vm, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.mu__minus__, P.W__plus__] ], [ [P.vm, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_271_229,(0,0,1):C.R2GC_271_230})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.vt__tilde__, P.vt, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.G__plus__, P.ta__minus__] ], [ [P.ta__minus__, P.W__plus__] ], [ [P.vt, P.Z] ] ],
                couplings = {(0,0,0):C.R2GC_282_232,(0,0,1):C.R2GC_271_229,(0,0,2):C.R2GC_271_230})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.e__plus__, P.e__minus__, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.e__minus__] ], [ [P.e__minus__, P.Z] ], [ [P.ve, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_269_225,(0,0,1):C.R2GC_269_226,(0,0,2):C.R2GC_269_227,(0,1,0):C.R2GC_213_164,(0,1,1):C.R2GC_213_165})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.mu__minus__] ], [ [P.mu__minus__, P.Z] ], [ [P.vm, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_269_225,(0,0,1):C.R2GC_269_226,(0,0,2):C.R2GC_269_227,(0,1,0):C.R2GC_213_164,(0,1,1):C.R2GC_213_165})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.G0, P.ta__minus__], [P.H, P.ta__minus__] ], [ [P.G__plus__, P.vt] ], [ [P.ta__minus__, P.Z] ], [ [P.vt, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_269_225,(0,0,1):C.R2GC_360_471,(0,0,3):C.R2GC_269_226,(0,0,4):C.R2GC_269_227,(0,1,0):C.R2GC_213_164,(0,1,1):C.R2GC_361_472,(0,1,2):C.R2GC_361_473,(0,1,3):C.R2GC_213_165})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.H ],
                 color = [ '1' ],
                 lorentz = [ L.S1 ],
                 loop_particles = [ [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.R2GC_205_150,(0,0,1):C.R2GC_205_151})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.ve__tilde__, P.ve ],
                 color = [ '1' ],
                 lorentz = [ L.FF3 ],
                 loop_particles = [ [ [P.e__minus__, P.W__plus__] ], [ [P.ve, P.Z] ] ],
                 couplings = {(0,0,0):C.R2GC_228_183,(0,0,1):C.R2GC_270_228})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.e__plus__, P.e__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.e__minus__] ], [ [P.e__minus__, P.Z] ], [ [P.ve, P.W__plus__] ] ],
                 couplings = {(0,1,1):C.R2GC_267_222,(0,1,2):C.R2GC_228_183,(0,2,1):C.R2GC_211_162,(0,0,0):C.R2GC_117_4})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.vm__tilde__, P.vm ],
                 color = [ '1' ],
                 lorentz = [ L.FF3 ],
                 loop_particles = [ [ [P.mu__minus__, P.W__plus__] ], [ [P.vm, P.Z] ] ],
                 couplings = {(0,0,0):C.R2GC_228_183,(0,0,1):C.R2GC_270_228})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.mu__plus__, P.mu__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.mu__minus__] ], [ [P.mu__minus__, P.Z] ], [ [P.vm, P.W__plus__] ] ],
                 couplings = {(0,1,1):C.R2GC_267_222,(0,1,2):C.R2GC_228_183,(0,2,1):C.R2GC_211_162,(0,0,0):C.R2GC_117_4})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.ta__plus__, P.ta__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.ta__minus__, P.Z] ], [ [P.vt, P.W__plus__] ] ],
                 couplings = {(0,1,0):C.R2GC_254_213,(0,1,1):C.R2GC_254_214,(0,3,0):C.R2GC_254_213,(0,3,1):C.R2GC_254_214,(0,2,1):C.R2GC_267_222,(0,2,2):C.R2GC_228_183,(0,4,1):C.R2GC_211_162,(0,0,0):C.R2GC_117_4})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.vt__tilde__, P.vt ],
                 color = [ '1' ],
                 lorentz = [ L.FF3 ],
                 loop_particles = [ [ [P.ta__minus__, P.W__plus__] ], [ [P.vt, P.Z] ] ],
                 couplings = {(0,0,0):C.R2GC_228_183,(0,0,1):C.R2GC_270_228})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.u] ], [ [P.d, P.W__plus__] ], [ [P.g, P.u] ], [ [P.u, P.Z] ] ],
                 couplings = {(0,1,1):C.R2GC_228_183,(0,1,3):C.R2GC_228_182,(0,2,3):C.R2GC_225_177,(0,0,0):C.R2GC_138_35,(0,0,2):C.R2GC_138_36})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.d] ], [ [P.d, P.g] ], [ [P.d, P.Z] ], [ [P.u, P.W__plus__] ] ],
                 couplings = {(0,1,1):C.R2GC_138_36,(0,1,2):C.R2GC_232_188,(0,1,3):C.R2GC_228_183,(0,2,1):C.R2GC_138_36,(0,2,2):C.R2GC_207_155,(0,0,0):C.R2GC_113_1})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.Z] ], [ [P.s, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_206_152,(0,0,1):C.R2GC_206_153,(0,0,2):C.R2GC_206_154,(0,2,0):C.R2GC_206_152,(0,2,1):C.R2GC_206_153,(0,2,2):C.R2GC_206_154,(0,1,0):C.R2GC_138_35,(0,1,1):C.R2GC_138_36,(0,1,2):C.R2GC_228_182,(0,1,3):C.R2GC_228_183,(0,3,0):C.R2GC_138_35,(0,3,1):C.R2GC_138_36,(0,3,2):C.R2GC_225_177})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.s] ], [ [P.c, P.W__plus__] ], [ [P.g, P.s] ], [ [P.s, P.Z] ] ],
                 couplings = {(0,1,1):C.R2GC_228_183,(0,1,2):C.R2GC_138_36,(0,1,3):C.R2GC_232_188,(0,2,2):C.R2GC_138_36,(0,2,3):C.R2GC_207_155,(0,0,0):C.R2GC_113_1})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.W__plus__] ], [ [P.g, P.t] ], [ [P.t, P.Z] ] ],
                 couplings = {(0,0,0):C.R2GC_252_209,(0,0,2):C.R2GC_252_210,(0,0,3):C.R2GC_252_211,(0,2,0):C.R2GC_252_209,(0,2,2):C.R2GC_252_210,(0,2,3):C.R2GC_252_211,(0,1,0):C.R2GC_138_35,(0,1,1):C.R2GC_228_183,(0,1,2):C.R2GC_138_36,(0,1,3):C.R2GC_228_182,(0,3,0):C.R2GC_138_35,(0,3,2):C.R2GC_138_36,(0,3,3):C.R2GC_225_177})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.Z] ], [ [P.t, P.W__plus__] ] ],
                 couplings = {(0,1,0):C.R2GC_242_202,(0,1,1):C.R2GC_242_203,(0,1,2):C.R2GC_242_204,(0,3,0):C.R2GC_242_202,(0,3,1):C.R2GC_242_203,(0,3,2):C.R2GC_242_204,(0,2,1):C.R2GC_138_36,(0,2,2):C.R2GC_232_188,(0,2,3):C.R2GC_228_183,(0,4,1):C.R2GC_138_36,(0,4,2):C.R2GC_207_155,(0,0,0):C.R2GC_113_1})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.SS1, L.SS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.R2GC_294_277,(0,0,1):C.R2GC_294_278,(0,0,4):C.R2GC_294_279,(0,0,5):C.R2GC_294_280,(0,0,6):C.R2GC_294_281,(0,0,7):C.R2GC_294_282,(0,0,2):C.R2GC_294_283,(0,0,3):C.R2GC_294_284,(0,1,0):C.R2GC_291_269,(0,1,1):C.R2GC_291_270,(0,1,4):C.R2GC_291_271,(0,1,5):C.R2GC_291_272,(0,1,2):C.R2GC_291_273,(0,1,3):C.R2GC_291_274})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.SS1, L.SS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H, P.Z] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.R2GC_294_277,(0,0,1):C.R2GC_294_278,(0,0,4):C.R2GC_294_279,(0,0,5):C.R2GC_294_280,(0,0,6):C.R2GC_305_320,(0,0,7):C.R2GC_305_321,(0,0,2):C.R2GC_294_284,(0,0,3):C.R2GC_305_322,(0,1,0):C.R2GC_291_269,(0,1,1):C.R2GC_291_270,(0,1,4):C.R2GC_291_271,(0,1,5):C.R2GC_291_272,(0,1,2):C.R2GC_291_274,(0,1,3):C.R2GC_291_273})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,9):C.R2GC_305_320,(0,0,11):C.R2GC_324_356,(0,0,0):C.R2GC_324_357,(0,0,1):C.R2GC_324_358,(0,0,2):C.R2GC_324_359,(0,0,3):C.R2GC_324_360,(0,0,4):C.R2GC_324_361,(0,0,6):C.R2GC_324_362,(0,0,7):C.R2GC_324_363,(0,0,8):C.R2GC_324_364,(0,0,10):C.R2GC_324_365,(0,1,0):C.R2GC_297_301,(0,1,2):C.R2GC_297_302,(0,1,3):C.R2GC_291_270,(0,1,5):C.R2GC_297_303,(0,1,6):C.R2GC_297_304,(0,1,8):C.R2GC_291_272})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.a, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.VV1, L.VV2, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.d], [P.s] ], [ [P.c] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,7):C.R2GC_197_128,(0,1,0):C.R2GC_289_259,(0,1,2):C.R2GC_289_260,(0,1,5):C.R2GC_289_261,(0,1,6):C.R2GC_289_262,(0,1,7):C.R2GC_289_263,(0,2,1):C.R2GC_197_126,(0,2,3):C.R2GC_197_127,(0,2,4):C.R2GC_197_128,(0,2,7):C.R2GC_117_4})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.a, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VV1, L.VV2, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.d], [P.s] ], [ [P.c] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,7):C.R2GC_203_145,(0,1,0):C.R2GC_290_264,(0,1,2):C.R2GC_290_265,(0,1,5):C.R2GC_290_266,(0,1,6):C.R2GC_290_267,(0,1,7):C.R2GC_290_268,(0,2,1):C.R2GC_202_141,(0,2,3):C.R2GC_202_142,(0,2,4):C.R2GC_202_143,(0,2,7):C.R2GC_202_144})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VV1, L.VV2, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.d], [P.s] ], [ [P.c] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.ve], [P.vm], [P.vt] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,8):C.R2GC_216_171,(0,1,0):C.R2GC_307_323,(0,1,2):C.R2GC_307_324,(0,1,5):C.R2GC_307_325,(0,1,6):C.R2GC_307_326,(0,1,8):C.R2GC_307_327,(0,2,1):C.R2GC_215_166,(0,2,3):C.R2GC_215_167,(0,2,4):C.R2GC_215_168,(0,2,7):C.R2GC_215_169,(0,2,8):C.R2GC_215_170})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.c, P.s] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.R2GC_197_128,(0,0,7):C.R2GC_216_171,(0,1,6):C.R2GC_323_349,(0,1,8):C.R2GC_323_350,(0,1,0):C.R2GC_323_351,(0,1,1):C.R2GC_323_352,(0,1,3):C.R2GC_323_353,(0,1,5):C.R2GC_323_354,(0,1,7):C.R2GC_323_355,(0,2,0):C.R2GC_117_4,(0,2,2):C.R2GC_228_183,(0,2,4):C.R2GC_311_332,(0,2,7):C.R2GC_215_170})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.g] ], [ [P.t] ] ],
                 couplings = {(0,0,3):C.R2GC_183_110,(0,1,0):C.R2GC_123_6,(0,1,2):C.R2GC_123_7,(0,1,4):C.R2GC_123_8,(0,2,1):C.R2GC_184_111,(0,2,3):C.R2GC_184_112})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.vt__tilde__, P.vt, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.G__plus__, P.ta__minus__] ] ],
                 couplings = {(0,0,0):C.R2GC_253_212})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.a, P.a, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_287_247,(0,0,1):C.R2GC_287_248,(0,0,3):C.R2GC_287_249,(0,0,4):C.R2GC_287_250,(0,0,5):C.R2GC_287_251,(0,0,2):C.R2GC_287_252})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_288_253,(0,0,1):C.R2GC_288_254,(0,0,3):C.R2GC_288_255,(0,0,4):C.R2GC_288_256,(0,0,5):C.R2GC_288_257,(0,0,2):C.R2GC_288_258})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_124_9,(0,0,1):C.R2GC_124_10,(0,0,2):C.R2GC_124_11})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.a, P.G0, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.G__plus__, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_284_234,(0,1,0):C.R2GC_283_233})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.a, P.a, P.a, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_199_129,(0,0,1):C.R2GC_199_130,(0,0,2):C.R2GC_199_131,(0,0,3):C.R2GC_199_132,(0,1,0):C.R2GC_199_129,(0,1,1):C.R2GC_199_130,(0,1,2):C.R2GC_199_131,(0,1,3):C.R2GC_199_132,(0,2,0):C.R2GC_199_129,(0,2,1):C.R2GC_199_130,(0,2,2):C.R2GC_199_131,(0,2,3):C.R2GC_199_132})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.a, P.a, P.a, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_204_146,(0,0,1):C.R2GC_204_147,(0,0,2):C.R2GC_204_148,(0,0,3):C.R2GC_204_149,(0,1,0):C.R2GC_204_146,(0,1,1):C.R2GC_204_147,(0,1,2):C.R2GC_204_148,(0,1,3):C.R2GC_204_149,(0,2,0):C.R2GC_204_146,(0,2,1):C.R2GC_204_147,(0,2,2):C.R2GC_204_148,(0,2,3):C.R2GC_204_149})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.a, P.a, P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_201_137,(0,0,1):C.R2GC_201_138,(0,0,2):C.R2GC_201_139,(0,0,3):C.R2GC_201_140,(0,1,0):C.R2GC_201_137,(0,1,1):C.R2GC_201_138,(0,1,2):C.R2GC_201_139,(0,1,3):C.R2GC_201_140,(0,2,0):C.R2GC_201_137,(0,2,1):C.R2GC_201_138,(0,2,2):C.R2GC_201_139,(0,2,3):C.R2GC_201_140})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_200_133,(0,0,1):C.R2GC_200_134,(0,0,2):C.R2GC_200_135,(0,0,3):C.R2GC_200_136,(0,1,0):C.R2GC_200_133,(0,1,1):C.R2GC_200_134,(0,1,2):C.R2GC_200_135,(0,1,3):C.R2GC_200_136,(0,2,0):C.R2GC_200_133,(0,2,1):C.R2GC_200_134,(0,2,2):C.R2GC_200_135,(0,2,3):C.R2GC_200_136})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.ve], [P.vm], [P.vt] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_218_172,(0,0,1):C.R2GC_218_173,(0,0,2):C.R2GC_218_174,(0,0,3):C.R2GC_218_175,(0,0,4):C.R2GC_218_176,(0,1,0):C.R2GC_218_172,(0,1,1):C.R2GC_218_173,(0,1,2):C.R2GC_218_174,(0,1,3):C.R2GC_218_175,(0,1,4):C.R2GC_218_176,(0,2,0):C.R2GC_218_172,(0,2,1):C.R2GC_218_173,(0,2,2):C.R2GC_218_174,(0,2,3):C.R2GC_218_175,(0,2,4):C.R2GC_218_176})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_126_15,(0,0,1):C.R2GC_126_16,(0,1,0):C.R2GC_126_15,(0,1,1):C.R2GC_126_16,(0,2,0):C.R2GC_126_15,(0,2,1):C.R2GC_126_16})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_137_34,(0,1,0):C.R2GC_137_34,(0,2,0):C.R2GC_137_34})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_128_19,(0,0,1):C.R2GC_128_20,(0,1,0):C.R2GC_128_19,(0,1,1):C.R2GC_128_20,(0,2,0):C.R2GC_128_19,(0,2,1):C.R2GC_128_20})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_131_25,(0,0,1):C.R2GC_131_26,(0,1,0):C.R2GC_131_25,(0,1,1):C.R2GC_131_26,(0,2,0):C.R2GC_131_25,(0,2,1):C.R2GC_131_26})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_127_17,(0,0,1):C.R2GC_127_18,(0,1,0):C.R2GC_127_17,(0,1,1):C.R2GC_127_18,(0,2,0):C.R2GC_127_17,(0,2,1):C.R2GC_127_18})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(1,0,0):C.R2GC_130_23,(1,0,1):C.R2GC_130_24,(0,1,0):C.R2GC_129_21,(0,1,1):C.R2GC_129_22,(0,2,0):C.R2GC_129_21,(0,2,1):C.R2GC_129_22,(0,3,0):C.R2GC_129_21,(0,3,1):C.R2GC_129_22})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.a, P.a, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_285_235,(0,0,1):C.R2GC_285_236,(0,0,3):C.R2GC_285_237,(0,0,4):C.R2GC_285_238,(0,0,5):C.R2GC_285_239,(0,0,2):C.R2GC_285_240})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_286_241,(0,0,1):C.R2GC_286_242,(0,0,3):C.R2GC_286_243,(0,0,4):C.R2GC_286_244,(0,0,5):C.R2GC_286_245,(0,0,2):C.R2GC_286_246})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_125_12,(0,0,1):C.R2GC_125_13,(0,0,2):C.R2GC_125_14})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.a, P.a, P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_285_235,(0,0,1):C.R2GC_285_236,(0,0,3):C.R2GC_285_237,(0,0,4):C.R2GC_285_238,(0,0,5):C.R2GC_285_239,(0,0,2):C.R2GC_285_240})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G__plus__, P.W__plus__] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.R2GC_286_241,(0,0,1):C.R2GC_286_242,(0,0,3):C.R2GC_286_243,(0,0,4):C.R2GC_286_244,(0,0,5):C.R2GC_286_245,(0,0,2):C.R2GC_286_246})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_125_12,(0,0,1):C.R2GC_125_13,(0,0,2):C.R2GC_125_14})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G0, P.G__plus__] ], [ [P.a, P.G0, P.W__plus__] ], [ [P.a, P.G__plus__, P.H] ], [ [P.a, P.H, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,5):C.R2GC_391_637,(0,0,8):C.R2GC_391_638,(0,0,0):C.R2GC_391_639,(0,0,1):C.R2GC_391_640,(0,0,2):C.R2GC_391_641,(0,0,3):C.R2GC_391_642,(0,0,4):C.R2GC_391_643,(0,0,6):C.R2GC_391_644,(0,0,7):C.R2GC_391_645,(0,0,9):C.R2GC_391_646})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_134_31,(0,0,1):C.R2GC_125_13})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G0, P.G__plus__] ], [ [P.a, P.G0, P.W__plus__] ], [ [P.a, P.G__plus__, P.H] ], [ [P.a, P.H, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,5):C.R2GC_391_637,(0,0,8):C.R2GC_391_638,(0,0,0):C.R2GC_391_639,(0,0,1):C.R2GC_391_640,(0,0,2):C.R2GC_391_641,(0,0,3):C.R2GC_391_642,(0,0,4):C.R2GC_391_643,(0,0,6):C.R2GC_391_644,(0,0,7):C.R2GC_391_645,(0,0,9):C.R2GC_391_646})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.H, P.Z] ], [ [P.P__tilde__SDM] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_295_280,(0,0,1):C.UVGC_295_281,(0,0,2):C.UVGC_295_284,(0,0,3):C.UVGC_295_283,(0,0,5):C.UVGC_295_282,(0,0,7):C.UVGC_182_38,(0,0,8):C.UVGC_295_285,(0,0,9):C.UVGC_295_286,(0,0,10):C.UVGC_295_287,(0,0,11):C.UVGC_295_288,(0,0,4):C.UVGC_295_290,(0,0,6):C.UVGC_295_289})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.W__plus__] ], [ [P.G__plus__], [P.G0, P.G__plus__] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.P__tilde__SDM] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,5):C.UVGC_295_282,(0,0,8):C.UVGC_379_739,(0,0,15):C.UVGC_406_1069,(0,0,19):C.UVGC_379_734,(0,0,21):C.UVGC_379_737,(0,0,23):C.UVGC_406_1070,(0,0,0):C.UVGC_406_1071,(0,0,2):C.UVGC_406_1072,(0,0,3):C.UVGC_406_1073,(0,0,4):C.UVGC_379_733,(0,0,7):C.UVGC_406_1077,(0,0,12):C.UVGC_325_440,(0,0,14):C.UVGC_406_1076,(0,0,16):C.UVGC_406_1074,(0,0,18):C.UVGC_406_1075,(0,0,20):C.UVGC_379_736,(0,0,22):C.UVGC_406_1078,(0,0,1):C.UVGC_382_771,(0,0,6):C.UVGC_406_1081,(0,0,9):C.UVGC_382_787,(0,0,11):C.UVGC_406_1079,(0,0,13):C.UVGC_406_1082,(0,0,17):C.UVGC_406_1080,(0,0,10):C.UVGC_371_688})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a] ], [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.Z] ], [ [P.a, P.Z] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0], [P.H] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.P__tilde__SDM] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_325_430,(0,0,6):C.UVGC_325_431,(0,0,8):C.UVGC_325_432,(0,0,10):C.UVGC_325_433,(0,0,12):C.UVGC_325_434,(0,0,13):C.UVGC_325_435,(0,0,1):C.UVGC_325_436,(0,0,3):C.UVGC_325_437,(0,0,4):C.UVGC_325_438,(0,0,5):C.UVGC_325_439,(0,0,7):C.UVGC_325_440,(0,0,9):C.UVGC_325_441,(0,0,11):C.UVGC_325_442,(0,0,2):C.UVGC_325_443})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0], [P.H] ], [ [P.G0, P.H] ], [ [P.G0, P.H, P.Z] ], [ [P.G0, P.Z], [P.H, P.Z] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.P__tilde__SDM] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_379_732,(0,0,1):C.UVGC_379_733,(0,0,2):C.UVGC_295_282,(0,0,6):C.UVGC_325_431,(0,0,8):C.UVGC_379_734,(0,0,9):C.UVGC_379_735,(0,0,10):C.UVGC_379_736,(0,0,11):C.UVGC_379_737,(0,0,12):C.UVGC_379_738,(0,0,3):C.UVGC_379_739,(0,0,5):C.UVGC_379_740,(0,0,7):C.UVGC_325_440,(0,0,4):C.UVGC_379_741})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.W__plus__, P.Z] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__], [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H] ], [ [P.H, P.W__plus__] ], [ [P.P__tilde__SDM] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,5):C.UVGC_406_1069,(0,0,12):C.UVGC_379_739,(0,0,17):C.UVGC_295_282,(0,0,19):C.UVGC_379_734,(0,0,21):C.UVGC_379_737,(0,0,23):C.UVGC_406_1070,(0,0,0):C.UVGC_406_1071,(0,0,2):C.UVGC_406_1072,(0,0,3):C.UVGC_406_1073,(0,0,4):C.UVGC_379_733,(0,0,9):C.UVGC_406_1074,(0,0,11):C.UVGC_406_1075,(0,0,14):C.UVGC_325_440,(0,0,16):C.UVGC_406_1076,(0,0,18):C.UVGC_406_1077,(0,0,20):C.UVGC_379_736,(0,0,22):C.UVGC_406_1078,(0,0,1):C.UVGC_382_771,(0,0,6):C.UVGC_382_787,(0,0,8):C.UVGC_406_1079,(0,0,10):C.UVGC_406_1080,(0,0,13):C.UVGC_406_1081,(0,0,15):C.UVGC_406_1082,(0,0,7):C.UVGC_371_688})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.H, P.H, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0] ], [ [P.G0, P.Z] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.P__tilde__SDM] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_295_280,(0,0,1):C.UVGC_295_281,(0,0,2):C.UVGC_295_282,(0,0,4):C.UVGC_295_283,(0,0,6):C.UVGC_295_284,(0,0,7):C.UVGC_182_38,(0,0,8):C.UVGC_295_285,(0,0,9):C.UVGC_295_286,(0,0,10):C.UVGC_295_287,(0,0,11):C.UVGC_295_288,(0,0,3):C.UVGC_295_289,(0,0,5):C.UVGC_295_290})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.P__tilde__SDM, P.P__tilde__SDM ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.G0] ], [ [P.G0, P.P__tilde__SDM] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.H, P.Z] ], [ [P.P__tilde__SDM] ] ],
                 couplings = {(0,0,0):C.UVGC_293_263,(0,0,2):C.UVGC_293_262,(0,0,4):C.UVGC_293_261,(0,0,6):C.UVGC_293_264,(0,0,1):C.UVGC_293_265,(0,0,3):C.UVGC_219_144,(0,0,5):C.UVGC_217_137})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.P__tilde__SDM, P.P__tilde__SDM ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.G0], [P.H] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__] ], [ [P.G__plus__, P.P__tilde__SDM] ], [ [P.G__plus__, P.Z] ], [ [P.P__tilde__SDM] ] ],
                 couplings = {(0,0,1):C.UVGC_293_261,(0,0,3):C.UVGC_301_321,(0,0,6):C.UVGC_293_264,(0,0,0):C.UVGC_301_322,(0,0,2):C.UVGC_219_143,(0,0,4):C.UVGC_293_265,(0,0,5):C.UVGC_301_323})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.H, P.H, P.P__tilde__SDM, P.P__tilde__SDM ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.G0] ], [ [P.G0, P.Z] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.H, P.P__tilde__SDM] ], [ [P.P__tilde__SDM] ] ],
                 couplings = {(0,0,0):C.UVGC_293_261,(0,0,2):C.UVGC_293_262,(0,0,4):C.UVGC_293_263,(0,0,6):C.UVGC_293_264,(0,0,1):C.UVGC_217_137,(0,0,3):C.UVGC_219_144,(0,0,5):C.UVGC_293_265})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.P__tilde__SDM, P.P__tilde__SDM, P.P__tilde__SDM, P.P__tilde__SDM ],
                 color = [ '1' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.G0], [P.H] ], [ [P.G__plus__] ], [ [P.P__tilde__SDM] ] ],
                 couplings = {(0,0,0):C.UVGC_182_38,(0,0,1):C.UVGC_182_39,(0,0,2):C.UVGC_182_40})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.G0, P.G0, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0], [P.H] ], [ [P.G0, P.H] ], [ [P.G0, P.H, P.Z] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H, P.Z] ], [ [P.P__tilde__SDM] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_380_742,(0,0,1):C.UVGC_380_743,(0,0,2):C.UVGC_296_293,(0,0,5):C.UVGC_380_744,(0,0,8):C.UVGC_380_745,(0,0,9):C.UVGC_380_746,(0,0,10):C.UVGC_380_747,(0,0,11):C.UVGC_380_748,(0,0,12):C.UVGC_380_749,(0,0,3):C.UVGC_380_750,(0,0,6):C.UVGC_380_751,(0,0,7):C.UVGC_380_752,(0,0,4):C.UVGC_380_753})

V_160 = CTVertex(name = 'V_160',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__], [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H] ], [ [P.H, P.W__plus__] ], [ [P.P__tilde__SDM] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,5):C.UVGC_388_852,(0,0,8):C.UVGC_380_750,(0,0,12):C.UVGC_296_293,(0,0,14):C.UVGC_380_745,(0,0,16):C.UVGC_380_748,(0,0,18):C.UVGC_388_853,(0,0,0):C.UVGC_388_854,(0,0,2):C.UVGC_388_855,(0,0,3):C.UVGC_388_856,(0,0,4):C.UVGC_380_743,(0,0,6):C.UVGC_388_857,(0,0,11):C.UVGC_388_858,(0,0,13):C.UVGC_388_859,(0,0,15):C.UVGC_380_747,(0,0,17):C.UVGC_388_860,(0,0,1):C.UVGC_387_836,(0,0,7):C.UVGC_388_861,(0,0,9):C.UVGC_387_840,(0,0,10):C.UVGC_388_862})

V_161 = CTVertex(name = 'V_161',
                 type = 'UV',
                 particles = [ P.H, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0] ], [ [P.G0, P.Z] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.P__tilde__SDM] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_296_291,(0,0,1):C.UVGC_296_292,(0,0,2):C.UVGC_296_293,(0,0,4):C.UVGC_296_294,(0,0,6):C.UVGC_296_295,(0,0,7):C.UVGC_296_296,(0,0,8):C.UVGC_296_297,(0,0,9):C.UVGC_296_298,(0,0,10):C.UVGC_296_299,(0,0,11):C.UVGC_296_300,(0,0,3):C.UVGC_296_301,(0,0,5):C.UVGC_296_302})

V_162 = CTVertex(name = 'V_162',
                 type = 'UV',
                 particles = [ P.H, P.P__tilde__SDM, P.P__tilde__SDM ],
                 color = [ '1' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.G0] ], [ [P.G__plus__] ], [ [P.H] ], [ [P.H, P.P__tilde__SDM] ], [ [P.P__tilde__SDM] ] ],
                 couplings = {(0,0,0):C.UVGC_220_146,(0,0,1):C.UVGC_220_147,(0,0,2):C.UVGC_220_148,(0,0,4):C.UVGC_220_149,(0,0,3):C.UVGC_220_150})

V_163 = CTVertex(name = 'V_163',
                 type = 'UV',
                 particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,6):C.UVGC_285_237,(0,0,0):C.UVGC_300_315,(0,0,1):C.UVGC_300_316,(0,0,2):C.UVGC_300_317,(0,0,3):C.UVGC_300_318,(0,0,4):C.UVGC_300_319,(0,0,5):C.UVGC_300_320})

V_164 = CTVertex(name = 'V_164',
                 type = 'UV',
                 particles = [ P.a, P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                 couplings = {(0,0,0):C.UVGC_299_310,(0,0,1):C.UVGC_299_311,(0,0,2):C.UVGC_299_312,(0,0,3):C.UVGC_299_313,(0,0,4):C.UVGC_299_314})

V_165 = CTVertex(name = 'V_165',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV10, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV9 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.ghG] ] ],
                 couplings = {(0,0,0):C.UVGC_188_50,(0,0,1):C.UVGC_190_53,(0,0,2):C.UVGC_190_54,(0,2,0):C.UVGC_185_45,(0,2,1):C.UVGC_185_46,(0,4,0):C.UVGC_185_45,(0,4,1):C.UVGC_187_48,(0,4,2):C.UVGC_187_49,(0,6,0):C.UVGC_188_50,(0,6,1):C.UVGC_188_51,(0,7,0):C.UVGC_188_50,(0,7,1):C.UVGC_189_52,(0,7,2):C.UVGC_168_15,(0,1,0):C.UVGC_185_45,(0,1,1):C.UVGC_186_47,(0,1,2):C.UVGC_169_17,(0,3,1):C.UVGC_168_14,(0,3,2):C.UVGC_168_15,(0,5,1):C.UVGC_169_16,(0,5,2):C.UVGC_169_17})

V_166 = CTVertex(name = 'V_166',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.ghG] ] ],
                 couplings = {(2,0,1):C.UVGC_172_22,(2,0,2):C.UVGC_172_23,(0,0,1):C.UVGC_172_22,(0,0,2):C.UVGC_172_23,(6,0,0):C.UVGC_193_59,(6,0,1):C.UVGC_196_63,(6,0,2):C.UVGC_171_20,(4,0,1):C.UVGC_173_24,(4,0,2):C.UVGC_173_25,(3,0,1):C.UVGC_173_24,(3,0,2):C.UVGC_173_25,(8,0,1):C.UVGC_172_23,(8,0,2):C.UVGC_172_22,(7,0,0):C.UVGC_193_59,(7,0,1):C.UVGC_193_60,(7,0,2):C.UVGC_191_57,(5,0,1):C.UVGC_173_24,(5,0,2):C.UVGC_173_25,(1,0,1):C.UVGC_173_24,(1,0,2):C.UVGC_173_25,(11,0,1):C.UVGC_170_18,(11,0,2):C.UVGC_170_19,(10,0,1):C.UVGC_170_18,(10,0,2):C.UVGC_170_19,(9,0,1):C.UVGC_171_20,(9,0,2):C.UVGC_171_21,(2,1,1):C.UVGC_172_22,(2,1,2):C.UVGC_172_23,(0,1,1):C.UVGC_172_22,(0,1,2):C.UVGC_172_23,(4,1,1):C.UVGC_173_24,(4,1,2):C.UVGC_173_25,(3,1,1):C.UVGC_173_24,(3,1,2):C.UVGC_173_25,(8,1,1):C.UVGC_174_26,(8,1,2):C.UVGC_172_22,(6,1,0):C.UVGC_191_55,(6,1,1):C.UVGC_192_58,(6,1,2):C.UVGC_171_20,(7,1,0):C.UVGC_193_59,(7,1,1):C.UVGC_194_61,(7,1,2):C.UVGC_191_57,(5,1,1):C.UVGC_173_24,(5,1,2):C.UVGC_173_25,(1,1,1):C.UVGC_173_24,(1,1,2):C.UVGC_173_25,(11,1,1):C.UVGC_170_18,(11,1,2):C.UVGC_170_19,(10,1,1):C.UVGC_170_18,(10,1,2):C.UVGC_170_19,(9,1,1):C.UVGC_171_20,(9,1,2):C.UVGC_171_21,(2,2,1):C.UVGC_172_22,(2,2,2):C.UVGC_172_23,(0,2,1):C.UVGC_172_22,(0,2,2):C.UVGC_172_23,(4,2,1):C.UVGC_173_24,(4,2,2):C.UVGC_173_25,(3,2,1):C.UVGC_173_24,(3,2,2):C.UVGC_173_25,(8,2,1):C.UVGC_175_27,(8,2,2):C.UVGC_172_22,(6,2,0):C.UVGC_193_59,(6,2,1):C.UVGC_195_62,(6,2,2):C.UVGC_171_20,(7,2,0):C.UVGC_191_55,(7,2,1):C.UVGC_191_56,(7,2,2):C.UVGC_191_57,(5,2,1):C.UVGC_173_24,(5,2,2):C.UVGC_173_25,(1,2,1):C.UVGC_173_24,(1,2,2):C.UVGC_173_25,(11,2,1):C.UVGC_170_18,(11,2,2):C.UVGC_170_19,(10,2,1):C.UVGC_170_18,(10,2,2):C.UVGC_170_19,(9,2,1):C.UVGC_171_20,(9,2,2):C.UVGC_171_21})

V_167 = CTVertex(name = 'V_167',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.a, P.c, P.G__plus__] ], [ [P.a, P.c, P.s] ], [ [P.a, P.G__plus__, P.s] ], [ [P.c, P.G0, P.W__plus__], [P.c, P.H, P.W__plus__] ], [ [P.c, P.G__plus__, P.Z] ], [ [P.c, P.g, P.s] ], [ [P.c, P.s, P.Z] ], [ [P.G__plus__, P.s, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_343_531,(0,0,1):C.UVGC_343_532,(0,0,2):C.UVGC_343_533,(0,0,5):C.UVGC_343_534,(0,0,3):C.UVGC_343_535,(0,0,4):C.UVGC_343_536,(0,0,6):C.UVGC_343_537,(0,0,7):C.UVGC_343_538})

V_168 = CTVertex(name = 'V_168',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.b, P.G__plus__] ], [ [P.a, P.b, P.t] ], [ [P.a, P.G__plus__, P.t] ], [ [P.b, P.G0, P.t], [P.b, P.H, P.t] ], [ [P.b, P.G0, P.W__plus__], [P.b, P.H, P.W__plus__] ], [ [P.b, P.G__plus__, P.Z] ], [ [P.b, P.g, P.t] ], [ [P.b, P.t, P.Z] ], [ [P.G0, P.t, P.W__plus__], [P.H, P.t, P.W__plus__] ], [ [P.G__plus__, P.t, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_353_593,(0,0,1):C.UVGC_353_594,(0,0,2):C.UVGC_353_595,(0,0,6):C.UVGC_353_596,(0,0,3):C.UVGC_353_597,(0,0,4):C.UVGC_353_598,(0,0,5):C.UVGC_353_599,(0,0,7):C.UVGC_353_600,(0,0,9):C.UVGC_353_601,(0,1,0):C.UVGC_356_620,(0,1,1):C.UVGC_356_621,(0,1,2):C.UVGC_356_622,(0,1,6):C.UVGC_356_623,(0,1,3):C.UVGC_356_624,(0,1,5):C.UVGC_356_625,(0,1,7):C.UVGC_356_626,(0,1,8):C.UVGC_356_627,(0,1,9):C.UVGC_356_628})

V_169 = CTVertex(name = 'V_169',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0] ], [ [P.b, P.H] ], [ [P.b, P.H, P.Z] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.G__plus__, P.t, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_351_579,(0,0,1):C.UVGC_351_580,(0,0,2):C.UVGC_350_574,(0,0,3):C.UVGC_350_573,(0,0,5):C.UVGC_351_581,(0,0,6):C.UVGC_351_582,(0,0,4):C.UVGC_351_583,(0,0,7):C.UVGC_351_584,(0,1,0):C.UVGC_350_571,(0,1,1):C.UVGC_350_572,(0,1,2):C.UVGC_350_573,(0,1,3):C.UVGC_350_574,(0,1,5):C.UVGC_350_575,(0,1,6):C.UVGC_350_576,(0,1,4):C.UVGC_350_577,(0,1,7):C.UVGC_350_578})

V_170 = CTVertex(name = 'V_170',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0] ], [ [P.b, P.G0, P.Z] ], [ [P.b, P.H] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.G__plus__, P.t, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_349_563,(0,0,1):C.UVGC_349_564,(0,0,2):C.UVGC_349_565,(0,0,4):C.UVGC_349_566,(0,0,5):C.UVGC_349_567,(0,0,6):C.UVGC_349_568,(0,0,3):C.UVGC_349_569,(0,0,7):C.UVGC_349_570,(0,1,0):C.UVGC_349_563,(0,1,1):C.UVGC_349_564,(0,1,2):C.UVGC_349_565,(0,1,4):C.UVGC_349_566,(0,1,5):C.UVGC_349_567,(0,1,6):C.UVGC_349_568,(0,1,3):C.UVGC_349_569,(0,1,7):C.UVGC_349_570})

V_171 = CTVertex(name = 'V_171',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.ta__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.a, P.G__plus__, P.ta__minus__] ], [ [P.G0, P.ta__minus__, P.W__plus__], [P.H, P.ta__minus__, P.W__plus__] ], [ [P.G__plus__, P.ta__minus__, P.Z] ], [ [P.G__plus__, P.vt, P.Z] ], [ [P.ta__minus__, P.vt, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_369_674,(0,0,1):C.UVGC_369_675,(0,0,2):C.UVGC_369_676,(0,0,3):C.UVGC_369_677,(0,0,4):C.UVGC_369_678})

V_172 = CTVertex(name = 'V_172',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.ta__minus__, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.G0, P.ta__minus__] ], [ [P.G__plus__, P.vt, P.W__plus__] ], [ [P.H, P.ta__minus__] ], [ [P.H, P.ta__minus__, P.Z] ], [ [P.ta__minus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_367_665,(0,0,1):C.UVGC_366_661,(0,0,3):C.UVGC_366_660,(0,0,5):C.UVGC_367_666,(0,0,2):C.UVGC_367_667,(0,0,4):C.UVGC_367_668,(0,1,0):C.UVGC_366_659,(0,1,1):C.UVGC_366_660,(0,1,3):C.UVGC_366_661,(0,1,5):C.UVGC_366_662,(0,1,2):C.UVGC_366_663,(0,1,4):C.UVGC_366_664})

V_173 = CTVertex(name = 'V_173',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.ta__minus__, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.G0, P.ta__minus__] ], [ [P.G0, P.ta__minus__, P.Z] ], [ [P.G__plus__, P.vt, P.W__plus__] ], [ [P.H, P.ta__minus__] ], [ [P.ta__minus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_365_653,(0,0,1):C.UVGC_365_654,(0,0,4):C.UVGC_365_655,(0,0,5):C.UVGC_365_656,(0,0,2):C.UVGC_365_657,(0,0,3):C.UVGC_365_658,(0,1,0):C.UVGC_365_653,(0,1,1):C.UVGC_365_654,(0,1,4):C.UVGC_365_655,(0,1,5):C.UVGC_365_656,(0,1,2):C.UVGC_365_657,(0,1,3):C.UVGC_365_658})

V_174 = CTVertex(name = 'V_174',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.a, P.c, P.G__plus__] ], [ [P.a, P.c, P.s] ], [ [P.a, P.G__plus__, P.s] ], [ [P.c, P.G0, P.W__plus__], [P.c, P.H, P.W__plus__] ], [ [P.c, P.G__plus__, P.Z] ], [ [P.c, P.g, P.s] ], [ [P.c, P.s, P.Z] ], [ [P.G__plus__, P.s, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_344_539,(0,0,1):C.UVGC_344_540,(0,0,2):C.UVGC_344_541,(0,0,5):C.UVGC_344_542,(0,0,3):C.UVGC_344_543,(0,0,4):C.UVGC_344_544,(0,0,6):C.UVGC_344_545,(0,0,7):C.UVGC_344_546})

V_175 = CTVertex(name = 'V_175',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.b, P.G__plus__] ], [ [P.a, P.b, P.t] ], [ [P.a, P.G__plus__, P.t] ], [ [P.b, P.G0, P.t], [P.b, P.H, P.t] ], [ [P.b, P.G0, P.W__plus__], [P.b, P.H, P.W__plus__] ], [ [P.b, P.G__plus__, P.Z] ], [ [P.b, P.g, P.t] ], [ [P.b, P.t, P.Z] ], [ [P.G0, P.t, P.W__plus__], [P.H, P.t, P.W__plus__] ], [ [P.G__plus__, P.t, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_355_611,(0,0,1):C.UVGC_355_612,(0,0,2):C.UVGC_355_613,(0,0,6):C.UVGC_355_614,(0,0,3):C.UVGC_355_615,(0,0,5):C.UVGC_355_616,(0,0,7):C.UVGC_355_617,(0,0,8):C.UVGC_355_618,(0,0,9):C.UVGC_355_619,(0,1,0):C.UVGC_354_602,(0,1,1):C.UVGC_354_603,(0,1,2):C.UVGC_354_604,(0,1,6):C.UVGC_354_605,(0,1,3):C.UVGC_354_606,(0,1,4):C.UVGC_354_607,(0,1,5):C.UVGC_354_608,(0,1,7):C.UVGC_354_609,(0,1,9):C.UVGC_354_610})

V_176 = CTVertex(name = 'V_176',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0] ], [ [P.c, P.H] ], [ [P.c, P.H, P.Z] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_341_519,(0,0,1):C.UVGC_341_520,(0,0,2):C.UVGC_341_521,(0,0,3):C.UVGC_341_522,(0,0,5):C.UVGC_341_523,(0,0,4):C.UVGC_341_524,(0,0,6):C.UVGC_341_525,(0,1,0):C.UVGC_342_526,(0,1,1):C.UVGC_342_527,(0,1,2):C.UVGC_341_522,(0,1,3):C.UVGC_341_521,(0,1,5):C.UVGC_342_528,(0,1,4):C.UVGC_342_529,(0,1,6):C.UVGC_342_530})

V_177 = CTVertex(name = 'V_177',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.G__plus__, P.W__plus__] ], [ [P.G0, P.t] ], [ [P.g, P.t] ], [ [P.H, P.t] ], [ [P.H, P.t, P.Z] ], [ [P.t, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_357_629,(0,0,1):C.UVGC_357_630,(0,0,4):C.UVGC_357_631,(0,0,3):C.UVGC_357_632,(0,0,5):C.UVGC_357_633,(0,0,7):C.UVGC_357_634,(0,0,2):C.UVGC_357_635,(0,0,6):C.UVGC_357_636,(0,1,0):C.UVGC_358_637,(0,1,1):C.UVGC_358_638,(0,1,4):C.UVGC_358_639,(0,1,3):C.UVGC_357_633,(0,1,5):C.UVGC_357_632,(0,1,7):C.UVGC_358_640,(0,1,2):C.UVGC_358_641,(0,1,6):C.UVGC_358_642})

V_178 = CTVertex(name = 'V_178',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0] ], [ [P.c, P.G0, P.Z] ], [ [P.c, P.H] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_340_512,(0,0,1):C.UVGC_340_513,(0,0,2):C.UVGC_340_514,(0,0,4):C.UVGC_340_515,(0,0,5):C.UVGC_340_516,(0,0,3):C.UVGC_340_517,(0,0,6):C.UVGC_340_518,(0,1,0):C.UVGC_340_512,(0,1,1):C.UVGC_340_513,(0,1,2):C.UVGC_340_514,(0,1,4):C.UVGC_340_515,(0,1,5):C.UVGC_340_516,(0,1,3):C.UVGC_340_517,(0,1,6):C.UVGC_340_518})

V_179 = CTVertex(name = 'V_179',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.G__plus__, P.W__plus__] ], [ [P.G0, P.t] ], [ [P.G0, P.t, P.Z] ], [ [P.g, P.t] ], [ [P.H, P.t] ], [ [P.t, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_352_585,(0,0,1):C.UVGC_352_586,(0,0,5):C.UVGC_352_587,(0,0,3):C.UVGC_352_588,(0,0,6):C.UVGC_352_589,(0,0,7):C.UVGC_352_590,(0,0,2):C.UVGC_352_591,(0,0,4):C.UVGC_352_592,(0,1,0):C.UVGC_352_585,(0,1,1):C.UVGC_352_586,(0,1,5):C.UVGC_352_587,(0,1,3):C.UVGC_352_588,(0,1,6):C.UVGC_352_589,(0,1,7):C.UVGC_352_590,(0,1,2):C.UVGC_352_591,(0,1,4):C.UVGC_352_592})

V_180 = CTVertex(name = 'V_180',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__], [P.a, P.W__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_397_919,(0,0,2):C.UVGC_397_920,(0,0,3):C.UVGC_397_921,(0,0,4):C.UVGC_397_922,(0,0,6):C.UVGC_397_923,(0,0,8):C.UVGC_397_924,(0,0,10):C.UVGC_397_925,(0,0,11):C.UVGC_397_926,(0,0,1):C.UVGC_397_927,(0,0,5):C.UVGC_397_928,(0,0,7):C.UVGC_397_929,(0,0,9):C.UVGC_397_930})

V_181 = CTVertex(name = 'V_181',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__], [P.a, P.W__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_385_809,(0,0,2):C.UVGC_385_810,(0,0,3):C.UVGC_385_811,(0,0,6):C.UVGC_385_812,(0,0,8):C.UVGC_385_813,(0,0,9):C.UVGC_385_814,(0,0,10):C.UVGC_385_815,(0,0,11):C.UVGC_385_816,(0,0,1):C.UVGC_385_817,(0,0,4):C.UVGC_385_818,(0,0,5):C.UVGC_385_819,(0,0,7):C.UVGC_385_820})

V_182 = CTVertex(name = 'V_182',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__], [P.a, P.W__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.ghA, P.ghWm] ], [ [P.ghWm, P.ghZ] ], [ [P.ghWp, P.ghZ] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__], [P.G__plus__, P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_389_863,(0,0,2):C.UVGC_389_864,(0,0,3):C.UVGC_389_865,(0,0,5):C.UVGC_389_866,(0,0,6):C.UVGC_389_867,(0,0,7):C.UVGC_389_868,(0,0,8):C.UVGC_389_869,(0,0,10):C.UVGC_389_870,(0,0,11):C.UVGC_389_871,(0,0,12):C.UVGC_389_872,(0,0,13):C.UVGC_389_873,(0,0,1):C.UVGC_389_874,(0,0,4):C.UVGC_389_875,(0,0,9):C.UVGC_389_876})

V_183 = CTVertex(name = 'V_183',
                 type = 'UV',
                 particles = [ P.W__minus__, P.G0, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.W__plus__] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                 couplings = {(0,0,2):C.UVGC_395_910,(0,0,3):C.UVGC_395_911,(0,0,8):C.UVGC_395_912,(0,0,12):C.UVGC_396_918,(0,0,13):C.UVGC_395_914,(0,0,1):C.UVGC_393_897,(0,0,4):C.UVGC_393_905,(0,0,6):C.UVGC_393_904,(0,0,7):C.UVGC_395_915,(0,0,9):C.UVGC_395_916,(0,0,11):C.UVGC_395_917,(0,1,0):C.UVGC_393_897,(0,1,2):C.UVGC_393_898,(0,1,3):C.UVGC_393_899,(0,1,5):C.UVGC_393_900,(0,1,10):C.UVGC_393_901,(0,1,13):C.UVGC_393_902,(0,1,1):C.UVGC_393_903,(0,1,4):C.UVGC_393_904,(0,1,6):C.UVGC_393_905,(0,1,7):C.UVGC_393_906,(0,1,9):C.UVGC_393_907,(0,1,11):C.UVGC_393_908})

V_184 = CTVertex(name = 'V_184',
                 type = 'UV',
                 particles = [ P.W__minus__, P.G__plus__, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ] ],
                 couplings = {(0,0,0):C.UVGC_383_789,(0,0,2):C.UVGC_383_790,(0,0,3):C.UVGC_383_791,(0,0,11):C.UVGC_383_792,(0,0,12):C.UVGC_383_793,(0,0,13):C.UVGC_383_794,(0,0,1):C.UVGC_383_795,(0,0,4):C.UVGC_383_796,(0,0,5):C.UVGC_383_797,(0,0,6):C.UVGC_383_798,(0,0,8):C.UVGC_383_799,(0,0,10):C.UVGC_383_800,(0,1,2):C.UVGC_384_801,(0,1,3):C.UVGC_384_802,(0,1,7):C.UVGC_384_803,(0,1,9):C.UVGC_384_804,(0,1,13):C.UVGC_384_805,(0,1,1):C.UVGC_383_789,(0,1,4):C.UVGC_383_799,(0,1,5):C.UVGC_384_806,(0,1,6):C.UVGC_384_807,(0,1,8):C.UVGC_383_796,(0,1,10):C.UVGC_384_808})

V_185 = CTVertex(name = 'V_185',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.W__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVV1, L.VVV10, L.VVV2, L.VVV4, L.VVV5, L.VVV6, L.VVV8, L.VVV9 ],
                 loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.G0, P.G__plus__], [P.G__plus__, P.H] ], [ [P.ghA, P.ghWm] ], [ [P.ghA, P.ghWm], [P.ghA, P.ghWp] ], [ [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ] ], [ [P.ghWm, P.ghZ], [P.ghWp, P.ghZ] ], [ [P.ghWp, P.ghZ] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,10):C.UVGC_320_385,(0,0,0):C.UVGC_320_386,(0,0,1):C.UVGC_166_13,(0,0,2):C.UVGC_314_368,(0,0,3):C.UVGC_315_373,(0,0,4):C.UVGC_315_374,(0,0,6):C.UVGC_313_364,(0,0,7):C.UVGC_315_375,(0,0,9):C.UVGC_313_365,(0,0,11):C.UVGC_320_387,(0,2,0):C.UVGC_319_383,(0,2,1):C.UVGC_313_361,(0,2,2):C.UVGC_313_362,(0,2,3):C.UVGC_313_363,(0,2,4):C.UVGC_314_370,(0,2,6):C.UVGC_318_381,(0,2,7):C.UVGC_314_371,(0,2,9):C.UVGC_318_382,(0,2,11):C.UVGC_319_384,(0,3,10):C.UVGC_313_359,(0,3,0):C.UVGC_313_360,(0,3,1):C.UVGC_313_361,(0,3,2):C.UVGC_313_362,(0,3,3):C.UVGC_313_363,(0,3,5):C.UVGC_313_364,(0,3,8):C.UVGC_313_365,(0,3,11):C.UVGC_313_366,(0,5,0):C.UVGC_316_377,(0,5,1):C.UVGC_166_13,(0,5,2):C.UVGC_314_368,(0,5,3):C.UVGC_315_373,(0,5,11):C.UVGC_316_378,(0,7,0):C.UVGC_314_367,(0,7,1):C.UVGC_166_13,(0,7,2):C.UVGC_314_368,(0,7,3):C.UVGC_314_369,(0,7,5):C.UVGC_314_370,(0,7,8):C.UVGC_314_371,(0,7,11):C.UVGC_314_372,(0,1,0):C.UVGC_317_379,(0,1,1):C.UVGC_313_361,(0,1,2):C.UVGC_313_362,(0,1,11):C.UVGC_317_380,(0,4,0):C.UVGC_160_7,(0,4,4):C.UVGC_318_381,(0,4,6):C.UVGC_314_370,(0,4,7):C.UVGC_318_382,(0,4,9):C.UVGC_314_371,(0,4,11):C.UVGC_163_10,(0,6,0):C.UVGC_212_119,(0,6,3):C.UVGC_315_373,(0,6,4):C.UVGC_313_364,(0,6,6):C.UVGC_315_374,(0,6,7):C.UVGC_313_365,(0,6,9):C.UVGC_315_375,(0,6,11):C.UVGC_315_376})

V_186 = CTVertex(name = 'V_186',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__], [P.a, P.W__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_397_919,(0,0,2):C.UVGC_397_920,(0,0,3):C.UVGC_397_921,(0,0,4):C.UVGC_397_922,(0,0,6):C.UVGC_397_923,(0,0,8):C.UVGC_397_924,(0,0,10):C.UVGC_397_925,(0,0,11):C.UVGC_397_926,(0,0,1):C.UVGC_397_927,(0,0,5):C.UVGC_397_928,(0,0,7):C.UVGC_397_929,(0,0,9):C.UVGC_397_930})

V_187 = CTVertex(name = 'V_187',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__], [P.a, P.W__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_385_816,(0,0,2):C.UVGC_386_821,(0,0,3):C.UVGC_386_822,(0,0,6):C.UVGC_386_823,(0,0,8):C.UVGC_386_824,(0,0,9):C.UVGC_386_825,(0,0,10):C.UVGC_386_826,(0,0,11):C.UVGC_385_809,(0,0,1):C.UVGC_386_827,(0,0,4):C.UVGC_386_828,(0,0,5):C.UVGC_386_829,(0,0,7):C.UVGC_386_830})

V_188 = CTVertex(name = 'V_188',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.G__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__], [P.a, P.W__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ] ], [ [P.ghWp, P.ghZ] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__], [P.G__plus__, P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_389_873,(0,0,2):C.UVGC_390_877,(0,0,3):C.UVGC_390_878,(0,0,5):C.UVGC_390_879,(0,0,6):C.UVGC_390_880,(0,0,7):C.UVGC_390_881,(0,0,8):C.UVGC_390_882,(0,0,10):C.UVGC_390_883,(0,0,11):C.UVGC_389_875,(0,0,12):C.UVGC_390_884,(0,0,13):C.UVGC_389_863,(0,0,1):C.UVGC_390_885,(0,0,4):C.UVGC_389_871,(0,0,9):C.UVGC_390_886})

V_189 = CTVertex(name = 'V_189',
                 type = 'UV',
                 particles = [ P.W__plus__, P.G0, P.G__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.W__plus__] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                 couplings = {(0,0,2):C.UVGC_393_898,(0,0,3):C.UVGC_393_899,(0,0,8):C.UVGC_393_900,(0,0,12):C.UVGC_394_909,(0,0,13):C.UVGC_393_902,(0,0,1):C.UVGC_393_903,(0,0,4):C.UVGC_393_904,(0,0,6):C.UVGC_393_905,(0,0,7):C.UVGC_393_906,(0,0,9):C.UVGC_393_907,(0,0,11):C.UVGC_393_908,(0,1,0):C.UVGC_393_903,(0,1,2):C.UVGC_395_910,(0,1,3):C.UVGC_395_911,(0,1,5):C.UVGC_395_912,(0,1,10):C.UVGC_395_913,(0,1,13):C.UVGC_395_914,(0,1,1):C.UVGC_393_897,(0,1,4):C.UVGC_393_905,(0,1,6):C.UVGC_393_904,(0,1,7):C.UVGC_395_915,(0,1,9):C.UVGC_395_916,(0,1,11):C.UVGC_395_917})

V_190 = CTVertex(name = 'V_190',
                 type = 'UV',
                 particles = [ P.W__plus__, P.G__minus__, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ] ],
                 couplings = {(0,0,0):C.UVGC_383_789,(0,0,2):C.UVGC_383_790,(0,0,3):C.UVGC_383_791,(0,0,11):C.UVGC_383_792,(0,0,12):C.UVGC_383_793,(0,0,13):C.UVGC_383_794,(0,0,1):C.UVGC_383_795,(0,0,4):C.UVGC_383_796,(0,0,5):C.UVGC_383_797,(0,0,6):C.UVGC_383_798,(0,0,8):C.UVGC_383_799,(0,0,10):C.UVGC_383_800,(0,1,2):C.UVGC_384_801,(0,1,3):C.UVGC_384_802,(0,1,7):C.UVGC_384_803,(0,1,9):C.UVGC_384_804,(0,1,13):C.UVGC_384_805,(0,1,1):C.UVGC_383_789,(0,1,4):C.UVGC_383_799,(0,1,5):C.UVGC_384_806,(0,1,6):C.UVGC_384_807,(0,1,8):C.UVGC_383_796,(0,1,10):C.UVGC_384_808})

V_191 = CTVertex(name = 'V_191',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0] ], [ [P.G0, P.G__plus__] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.W__plus__] ], [ [P.G__plus__] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,5):C.UVGC_382_768,(0,0,9):C.UVGC_382_767,(0,0,16):C.UVGC_382_766,(0,0,20):C.UVGC_382_769,(0,0,22):C.UVGC_382_770,(0,0,0):C.UVGC_382_771,(0,0,2):C.UVGC_382_772,(0,0,3):C.UVGC_382_773,(0,0,4):C.UVGC_382_774,(0,0,6):C.UVGC_382_777,(0,0,8):C.UVGC_382_780,(0,0,10):C.UVGC_382_775,(0,0,13):C.UVGC_382_778,(0,0,15):C.UVGC_382_779,(0,0,18):C.UVGC_382_776,(0,0,19):C.UVGC_382_781,(0,0,21):C.UVGC_382_782,(0,0,1):C.UVGC_382_783,(0,0,7):C.UVGC_382_787,(0,0,11):C.UVGC_382_784,(0,0,12):C.UVGC_382_785,(0,0,14):C.UVGC_382_788,(0,0,17):C.UVGC_382_786})

V_192 = CTVertex(name = 'V_192',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a] ], [ [P.a, P.G0], [P.a, P.H] ], [ [P.a, P.G0, P.W__plus__], [P.a, P.H, P.W__plus__] ], [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.G__plus__, P.W__plus__, P.Z] ], [ [P.a, P.G__plus__, P.Z] ], [ [P.a, P.W__plus__] ], [ [P.a, P.W__plus__, P.Z] ], [ [P.a, P.Z] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__], [P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.Z], [P.G__plus__, P.H, P.Z] ], [ [P.G0], [P.H] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z], [P.H, P.W__plus__, P.Z] ], [ [P.G0, P.Z], [P.H, P.Z] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_400_969,(0,0,14):C.UVGC_382_766,(0,0,18):C.UVGC_400_970,(0,0,23):C.UVGC_382_769,(0,0,25):C.UVGC_400_971,(0,0,1):C.UVGC_400_972,(0,0,3):C.UVGC_400_973,(0,0,7):C.UVGC_400_974,(0,0,9):C.UVGC_400_975,(0,0,10):C.UVGC_382_773,(0,0,11):C.UVGC_382_774,(0,0,12):C.UVGC_400_976,(0,0,15):C.UVGC_400_977,(0,0,17):C.UVGC_400_978,(0,0,19):C.UVGC_382_780,(0,0,21):C.UVGC_400_979,(0,0,22):C.UVGC_382_781,(0,0,24):C.UVGC_400_980,(0,0,2):C.UVGC_400_981,(0,0,4):C.UVGC_400_982,(0,0,6):C.UVGC_400_983,(0,0,8):C.UVGC_400_984,(0,0,13):C.UVGC_400_985,(0,0,16):C.UVGC_400_986,(0,0,20):C.UVGC_400_987,(0,0,5):C.UVGC_400_988})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0] ], [ [P.G0, P.G__plus__] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,5):C.UVGC_382_766,(0,0,11):C.UVGC_382_767,(0,0,17):C.UVGC_382_768,(0,0,20):C.UVGC_382_769,(0,0,22):C.UVGC_382_770,(0,0,0):C.UVGC_382_771,(0,0,2):C.UVGC_382_772,(0,0,3):C.UVGC_382_773,(0,0,4):C.UVGC_382_774,(0,0,6):C.UVGC_382_775,(0,0,10):C.UVGC_382_776,(0,0,12):C.UVGC_382_777,(0,0,14):C.UVGC_382_778,(0,0,16):C.UVGC_382_779,(0,0,18):C.UVGC_382_780,(0,0,19):C.UVGC_382_781,(0,0,21):C.UVGC_382_782,(0,0,1):C.UVGC_382_783,(0,0,7):C.UVGC_382_784,(0,0,8):C.UVGC_382_785,(0,0,9):C.UVGC_382_786,(0,0,13):C.UVGC_382_787,(0,0,15):C.UVGC_382_788})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0] ], [ [P.G0, P.G__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.ghA, P.ghWm], [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ], [P.ghWp, P.ghZ] ], [ [P.G__plus__] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,5):C.UVGC_387_831,(0,0,10):C.UVGC_387_832,(0,0,15):C.UVGC_387_833,(0,0,18):C.UVGC_387_834,(0,0,20):C.UVGC_387_835,(0,0,0):C.UVGC_387_836,(0,0,2):C.UVGC_387_837,(0,0,3):C.UVGC_387_838,(0,0,4):C.UVGC_387_839,(0,0,6):C.UVGC_387_840,(0,0,8):C.UVGC_387_841,(0,0,9):C.UVGC_387_842,(0,0,11):C.UVGC_387_843,(0,0,14):C.UVGC_387_844,(0,0,16):C.UVGC_387_845,(0,0,17):C.UVGC_387_846,(0,0,19):C.UVGC_387_847,(0,0,1):C.UVGC_387_848,(0,0,7):C.UVGC_387_849,(0,0,12):C.UVGC_387_850,(0,0,13):C.UVGC_387_851})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.G0, P.G__plus__], [P.G__plus__, P.H] ], [ [P.ghA, P.ghWm], [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ], [P.ghWp, P.ghZ] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,6):C.UVGC_321_388,(0,0,0):C.UVGC_321_389,(0,0,1):C.UVGC_321_390,(0,0,2):C.UVGC_321_391,(0,0,3):C.UVGC_321_392,(0,0,4):C.UVGC_321_393,(0,0,5):C.UVGC_321_394,(0,0,7):C.UVGC_321_395,(0,1,6):C.UVGC_321_388,(0,1,0):C.UVGC_321_389,(0,1,1):C.UVGC_321_390,(0,1,2):C.UVGC_321_391,(0,1,3):C.UVGC_321_392,(0,1,4):C.UVGC_321_393,(0,1,5):C.UVGC_321_394,(0,1,7):C.UVGC_321_395,(0,2,6):C.UVGC_322_396,(0,2,0):C.UVGC_322_397,(0,2,1):C.UVGC_322_398,(0,2,2):C.UVGC_322_399,(0,2,3):C.UVGC_322_400,(0,2,4):C.UVGC_321_393,(0,2,5):C.UVGC_321_394,(0,2,7):C.UVGC_322_401})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVV1, L.VVV10, L.VVV2, L.VVV3, L.VVV4, L.VVV6, L.VVV8, L.VVV9 ],
                 loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.G0, P.G__plus__], [P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.H] ], [ [P.ghA, P.ghWm] ], [ [P.ghA, P.ghWm], [P.ghA, P.ghWp] ], [ [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ] ], [ [P.ghWm, P.ghZ], [P.ghWp, P.ghZ] ], [ [P.ghWp, P.ghZ] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_337_492,(0,0,1):C.UVGC_335_486,(0,0,2):C.UVGC_335_487,(0,0,3):C.UVGC_337_493,(0,0,6):C.UVGC_309_353,(0,0,9):C.UVGC_309_355,(0,0,12):C.UVGC_337_494,(0,0,4):C.UVGC_337_495,(0,2,0):C.UVGC_308_348,(0,2,1):C.UVGC_308_349,(0,2,2):C.UVGC_308_350,(0,2,12):C.UVGC_308_351,(0,4,0):C.UVGC_333_477,(0,4,1):C.UVGC_308_349,(0,4,2):C.UVGC_308_350,(0,4,3):C.UVGC_332_472,(0,4,5):C.UVGC_309_353,(0,4,7):C.UVGC_309_352,(0,4,8):C.UVGC_309_355,(0,4,10):C.UVGC_309_354,(0,4,12):C.UVGC_333_478,(0,4,4):C.UVGC_332_476,(0,5,11):C.UVGC_336_489,(0,5,0):C.UVGC_336_490,(0,5,1):C.UVGC_335_486,(0,5,2):C.UVGC_335_487,(0,5,3):C.UVGC_334_480,(0,5,5):C.UVGC_334_481,(0,5,7):C.UVGC_332_473,(0,5,8):C.UVGC_334_482,(0,5,10):C.UVGC_332_474,(0,5,12):C.UVGC_336_491,(0,5,4):C.UVGC_334_484,(0,7,0):C.UVGC_335_485,(0,7,1):C.UVGC_335_486,(0,7,2):C.UVGC_335_487,(0,7,3):C.UVGC_334_480,(0,7,12):C.UVGC_335_488,(0,7,4):C.UVGC_334_484,(0,1,11):C.UVGC_332_470,(0,1,0):C.UVGC_332_471,(0,1,1):C.UVGC_308_349,(0,1,2):C.UVGC_308_350,(0,1,3):C.UVGC_332_472,(0,1,6):C.UVGC_332_473,(0,1,9):C.UVGC_332_474,(0,1,12):C.UVGC_332_475,(0,1,4):C.UVGC_332_476,(0,3,0):C.UVGC_334_479,(0,3,3):C.UVGC_334_480,(0,3,5):C.UVGC_332_473,(0,3,7):C.UVGC_334_481,(0,3,8):C.UVGC_332_474,(0,3,10):C.UVGC_334_482,(0,3,12):C.UVGC_334_483,(0,3,4):C.UVGC_334_484,(0,6,0):C.UVGC_165_12,(0,6,5):C.UVGC_309_352,(0,6,7):C.UVGC_309_353,(0,6,8):C.UVGC_309_354,(0,6,10):C.UVGC_309_355,(0,6,12):C.UVGC_161_8})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.a] ], [ [P.a, P.W__plus__] ], [ [P.a, P.W__plus__, P.Z] ], [ [P.a, P.Z] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.G0, P.G__plus__], [P.G__plus__, P.H], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.G0, P.G__plus__], [P.G__plus__, P.H] ], [ [P.G0], [P.H] ], [ [P.ghA, P.ghWm], [P.ghA, P.ghWp] ], [ [P.ghA, P.ghWm, P.ghWp] ], [ [P.ghA, P.ghWm, P.ghWp, P.ghZ] ], [ [P.ghA, P.ghWm, P.ghZ], [P.ghA, P.ghWp, P.ghZ] ], [ [P.ghWm, P.ghWp, P.ghZ] ], [ [P.ghWm, P.ghZ], [P.ghWp, P.ghZ] ], [ [P.G__plus__] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_401_989,(0,0,8):C.UVGC_382_787,(0,0,15):C.UVGC_391_894,(0,0,16):C.UVGC_401_990,(0,0,18):C.UVGC_401_991,(0,0,1):C.UVGC_401_992,(0,0,3):C.UVGC_401_993,(0,0,4):C.UVGC_401_994,(0,0,5):C.UVGC_401_995,(0,0,9):C.UVGC_321_393,(0,0,14):C.UVGC_330_459,(0,0,17):C.UVGC_401_996,(0,0,2):C.UVGC_401_997,(0,0,10):C.UVGC_401_998,(0,0,12):C.UVGC_401_999,(0,0,13):C.UVGC_401_1000,(0,0,11):C.UVGC_401_1001,(0,1,0):C.UVGC_401_989,(0,1,8):C.UVGC_382_787,(0,1,15):C.UVGC_391_894,(0,1,16):C.UVGC_401_990,(0,1,18):C.UVGC_401_991,(0,1,1):C.UVGC_401_992,(0,1,3):C.UVGC_401_993,(0,1,4):C.UVGC_401_994,(0,1,5):C.UVGC_401_995,(0,1,9):C.UVGC_321_393,(0,1,14):C.UVGC_330_459,(0,1,17):C.UVGC_401_996,(0,1,2):C.UVGC_401_997,(0,1,10):C.UVGC_401_998,(0,1,12):C.UVGC_401_999,(0,1,13):C.UVGC_401_1000,(0,1,11):C.UVGC_401_1001,(0,2,0):C.UVGC_402_1002,(0,2,16):C.UVGC_402_1003,(0,2,18):C.UVGC_402_1004,(0,2,1):C.UVGC_402_1005,(0,2,3):C.UVGC_402_1006,(0,2,4):C.UVGC_325_434,(0,2,6):C.UVGC_402_1007,(0,2,7):C.UVGC_402_1008,(0,2,9):C.UVGC_321_393,(0,2,14):C.UVGC_330_459,(0,2,17):C.UVGC_402_1009,(0,2,2):C.UVGC_402_1010,(0,2,10):C.UVGC_401_998,(0,2,12):C.UVGC_401_999,(0,2,13):C.UVGC_401_1000,(0,2,11):C.UVGC_401_1001})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.vt, P.G__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.a, P.G__plus__, P.ta__minus__] ], [ [P.G0, P.ta__minus__, P.W__plus__], [P.H, P.ta__minus__, P.W__plus__] ], [ [P.G__plus__, P.ta__minus__, P.Z] ], [ [P.G__plus__, P.vt, P.Z] ], [ [P.ta__minus__, P.vt, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_368_669,(0,0,1):C.UVGC_368_670,(0,0,2):C.UVGC_368_671,(0,0,3):C.UVGC_368_672,(0,0,4):C.UVGC_368_673})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.H, P.W__plus__] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,7):C.UVGC_286_239,(0,0,0):C.UVGC_374_703,(0,0,1):C.UVGC_374_704,(0,0,2):C.UVGC_374_705,(0,0,4):C.UVGC_374_706,(0,0,5):C.UVGC_374_707,(0,0,6):C.UVGC_374_708,(0,0,3):C.UVGC_374_709})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.Z, P.G0, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0, P.H, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H, P.Z] ], [ [P.t] ], [ [P.ta__minus__] ] ],
                 couplings = {(0,0,0):C.UVGC_376_717,(0,0,1):C.UVGC_376_718,(0,0,6):C.UVGC_376_719,(0,0,7):C.UVGC_376_720,(0,0,4):C.UVGC_376_721,(0,0,5):C.UVGC_376_722,(0,0,2):C.UVGC_376_723,(0,1,0):C.UVGC_375_710,(0,1,1):C.UVGC_375_711,(0,1,6):C.UVGC_375_712,(0,1,7):C.UVGC_375_713,(0,1,3):C.UVGC_375_714,(0,1,4):C.UVGC_375_715,(0,1,2):C.UVGC_375_716})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.Z, P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.H, P.W__plus__] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ] ],
                 couplings = {(0,0,0):C.UVGC_373_696,(0,0,1):C.UVGC_373_697,(0,0,2):C.UVGC_373_698,(0,0,4):C.UVGC_373_699,(0,0,5):C.UVGC_373_700,(0,0,6):C.UVGC_373_701,(0,0,3):C.UVGC_373_702,(0,1,0):C.UVGC_372_689,(0,1,1):C.UVGC_372_690,(0,1,2):C.UVGC_372_691,(0,1,4):C.UVGC_372_692,(0,1,5):C.UVGC_372_693,(0,1,6):C.UVGC_372_694,(0,1,3):C.UVGC_372_695})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__] ], [ [P.G0, P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.H, P.Z] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.H, P.W__plus__], [P.G__plus__, P.H, P.W__plus__] ], [ [P.G0, P.H, P.Z] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_403_1011,(0,0,2):C.UVGC_403_1012,(0,0,3):C.UVGC_403_1013,(0,0,4):C.UVGC_403_1014,(0,0,5):C.UVGC_403_1015,(0,0,12):C.UVGC_403_1016,(0,0,14):C.UVGC_403_1017,(0,0,16):C.UVGC_403_1018,(0,0,18):C.UVGC_403_1019,(0,0,20):C.UVGC_403_1020,(0,0,21):C.UVGC_403_1021,(0,0,1):C.UVGC_403_1022,(0,0,6):C.UVGC_403_1023,(0,0,8):C.UVGC_403_1024,(0,0,9):C.UVGC_403_1025,(0,0,10):C.UVGC_403_1026,(0,0,11):C.UVGC_403_1027,(0,0,13):C.UVGC_403_1028,(0,0,15):C.UVGC_403_1029,(0,0,17):C.UVGC_403_1030,(0,0,19):C.UVGC_403_1031,(0,0,7):C.UVGC_403_1032})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.H, P.Z] ], [ [P.G0, P.G__plus__, P.W__plus__], [P.G0, P.H, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.H, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_405_1055,(0,0,2):C.UVGC_404_1043,(0,0,3):C.UVGC_405_1056,(0,0,4):C.UVGC_405_1057,(0,0,11):C.UVGC_404_1045,(0,0,14):C.UVGC_405_1058,(0,0,16):C.UVGC_405_1059,(0,0,17):C.UVGC_405_1060,(0,0,19):C.UVGC_405_1061,(0,0,20):C.UVGC_405_1062,(0,0,21):C.UVGC_404_1034,(0,0,1):C.UVGC_405_1063,(0,0,5):C.UVGC_404_1037,(0,0,7):C.UVGC_404_1050,(0,0,8):C.UVGC_405_1064,(0,0,9):C.UVGC_405_1065,(0,0,10):C.UVGC_405_1066,(0,0,12):C.UVGC_404_1046,(0,0,13):C.UVGC_404_1054,(0,0,15):C.UVGC_405_1067,(0,0,18):C.UVGC_405_1068,(0,0,6):C.UVGC_404_1051})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.H, P.W__plus__] ], [ [P.ghA, P.ghWm] ], [ [P.ghWm, P.ghZ] ], [ [P.ghWp, P.ghZ] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_398_931,(0,0,2):C.UVGC_398_932,(0,0,3):C.UVGC_398_933,(0,0,4):C.UVGC_398_934,(0,0,8):C.UVGC_398_935,(0,0,9):C.UVGC_398_936,(0,0,10):C.UVGC_398_937,(0,0,11):C.UVGC_398_938,(0,0,14):C.UVGC_398_939,(0,0,16):C.UVGC_398_940,(0,0,17):C.UVGC_398_941,(0,0,19):C.UVGC_398_942,(0,0,20):C.UVGC_398_943,(0,0,21):C.UVGC_398_944,(0,0,1):C.UVGC_398_945,(0,0,5):C.UVGC_398_946,(0,0,6):C.UVGC_398_947,(0,0,7):C.UVGC_398_948,(0,0,12):C.UVGC_398_949,(0,0,13):C.UVGC_398_950,(0,0,15):C.UVGC_398_951,(0,0,18):C.UVGC_398_952})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__] ], [ [P.G0, P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.H, P.Z] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.H, P.W__plus__], [P.G__plus__, P.H, P.W__plus__] ], [ [P.G0, P.H, P.Z] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_403_1011,(0,0,2):C.UVGC_403_1012,(0,0,3):C.UVGC_403_1013,(0,0,4):C.UVGC_403_1014,(0,0,5):C.UVGC_403_1015,(0,0,12):C.UVGC_403_1016,(0,0,14):C.UVGC_403_1017,(0,0,16):C.UVGC_403_1018,(0,0,18):C.UVGC_403_1019,(0,0,20):C.UVGC_403_1020,(0,0,21):C.UVGC_403_1021,(0,0,1):C.UVGC_403_1022,(0,0,6):C.UVGC_403_1023,(0,0,8):C.UVGC_403_1024,(0,0,9):C.UVGC_403_1025,(0,0,10):C.UVGC_403_1026,(0,0,11):C.UVGC_403_1027,(0,0,13):C.UVGC_403_1028,(0,0,15):C.UVGC_403_1029,(0,0,17):C.UVGC_403_1030,(0,0,19):C.UVGC_403_1031,(0,0,7):C.UVGC_403_1032})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.H, P.Z] ], [ [P.G0, P.G__plus__, P.W__plus__], [P.G0, P.H, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.H, P.Z] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_404_1033,(0,0,2):C.UVGC_404_1034,(0,0,3):C.UVGC_404_1035,(0,0,4):C.UVGC_404_1036,(0,0,11):C.UVGC_404_1037,(0,0,14):C.UVGC_404_1038,(0,0,16):C.UVGC_404_1039,(0,0,17):C.UVGC_404_1040,(0,0,19):C.UVGC_404_1041,(0,0,20):C.UVGC_404_1042,(0,0,21):C.UVGC_404_1043,(0,0,1):C.UVGC_404_1044,(0,0,5):C.UVGC_404_1045,(0,0,7):C.UVGC_404_1046,(0,0,8):C.UVGC_404_1047,(0,0,9):C.UVGC_404_1048,(0,0,10):C.UVGC_404_1049,(0,0,12):C.UVGC_404_1050,(0,0,13):C.UVGC_404_1051,(0,0,15):C.UVGC_404_1052,(0,0,18):C.UVGC_404_1053,(0,0,6):C.UVGC_404_1054})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.G__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.G__plus__, P.W__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0, P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.H, P.W__plus__] ], [ [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ] ], [ [P.ghWp, P.ghZ] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.G__plus__, P.W__plus__, P.Z] ], [ [P.G__plus__, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_399_953,(0,0,2):C.UVGC_398_944,(0,0,3):C.UVGC_399_954,(0,0,4):C.UVGC_399_955,(0,0,8):C.UVGC_399_956,(0,0,9):C.UVGC_399_957,(0,0,10):C.UVGC_399_958,(0,0,11):C.UVGC_398_946,(0,0,14):C.UVGC_399_959,(0,0,16):C.UVGC_399_960,(0,0,17):C.UVGC_399_961,(0,0,19):C.UVGC_399_962,(0,0,20):C.UVGC_399_963,(0,0,21):C.UVGC_398_932,(0,0,1):C.UVGC_399_964,(0,0,5):C.UVGC_398_938,(0,0,6):C.UVGC_398_949,(0,0,7):C.UVGC_399_965,(0,0,12):C.UVGC_398_947,(0,0,13):C.UVGC_399_966,(0,0,15):C.UVGC_399_967,(0,0,18):C.UVGC_399_968})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.G0, P.G__plus__], [P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.H] ], [ [P.ghA, P.ghWm], [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ], [P.ghWp, P.ghZ] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,7):C.UVGC_338_496,(0,0,0):C.UVGC_338_497,(0,0,1):C.UVGC_338_498,(0,0,2):C.UVGC_338_499,(0,0,3):C.UVGC_338_500,(0,0,5):C.UVGC_338_501,(0,0,6):C.UVGC_338_502,(0,0,8):C.UVGC_338_503,(0,0,4):C.UVGC_338_504,(0,1,7):C.UVGC_339_505,(0,1,0):C.UVGC_339_506,(0,1,1):C.UVGC_339_507,(0,1,2):C.UVGC_339_508,(0,1,3):C.UVGC_339_509,(0,1,5):C.UVGC_338_501,(0,1,6):C.UVGC_338_502,(0,1,8):C.UVGC_339_510,(0,1,4):C.UVGC_339_511,(0,2,7):C.UVGC_339_505,(0,2,0):C.UVGC_339_506,(0,2,1):C.UVGC_339_507,(0,2,2):C.UVGC_339_508,(0,2,3):C.UVGC_339_509,(0,2,5):C.UVGC_338_501,(0,2,6):C.UVGC_338_502,(0,2,8):C.UVGC_339_510,(0,2,4):C.UVGC_339_511})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0] ], [ [P.G0, P.H] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.H, P.Z], [P.G0, P.H, P.Z] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_377_724,(0,0,1):C.UVGC_377_725,(0,0,2):C.UVGC_377_726,(0,0,6):C.UVGC_371_680,(0,0,8):C.UVGC_377_727,(0,0,9):C.UVGC_377_728,(0,0,10):C.UVGC_371_681,(0,0,3):C.UVGC_377_729,(0,0,4):C.UVGC_377_731,(0,0,5):C.UVGC_377_730,(0,0,7):C.UVGC_218_139})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0], [P.H] ], [ [P.G0, P.H] ], [ [P.G0, P.H, P.W__plus__] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.G__plus__, P.Z] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,3):C.UVGC_371_680,(0,0,9):C.UVGC_371_681,(0,0,0):C.UVGC_300_319,(0,0,1):C.UVGC_371_682,(0,0,2):C.UVGC_371_683,(0,0,4):C.UVGC_371_684,(0,0,6):C.UVGC_371_685,(0,0,7):C.UVGC_371_686,(0,0,8):C.UVGC_371_687,(0,0,5):C.UVGC_371_688})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0] ], [ [P.G0, P.H] ], [ [P.G0, P.Z], [P.G0, P.H, P.Z] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.H, P.Z] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_377_724,(0,0,1):C.UVGC_377_725,(0,0,2):C.UVGC_371_680,(0,0,6):C.UVGC_377_726,(0,0,8):C.UVGC_377_727,(0,0,9):C.UVGC_377_728,(0,0,10):C.UVGC_371_681,(0,0,3):C.UVGC_377_729,(0,0,4):C.UVGC_218_139,(0,0,5):C.UVGC_377_730,(0,0,7):C.UVGC_377_731})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0] ], [ [P.G0, P.H] ], [ [P.G0, P.H, P.Z] ], [ [P.ghWm], [P.ghWp] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.H, P.Z] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_381_754,(0,0,1):C.UVGC_381_755,(0,0,2):C.UVGC_381_756,(0,0,5):C.UVGC_381_757,(0,0,7):C.UVGC_381_758,(0,0,9):C.UVGC_381_759,(0,0,10):C.UVGC_381_760,(0,0,11):C.UVGC_381_761,(0,0,3):C.UVGC_381_762,(0,0,6):C.UVGC_381_763,(0,0,8):C.UVGC_381_764,(0,0,4):C.UVGC_381_765})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.a, P.W__plus__] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.G0, P.G__plus__], [P.G__plus__, P.H] ], [ [P.G0, P.G__plus__, P.H] ], [ [P.G0], [P.H] ], [ [P.G0, P.H] ], [ [P.ghA, P.ghWm], [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ], [P.ghWp, P.ghZ] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,9):C.UVGC_330_455,(0,0,0):C.UVGC_321_395,(0,0,1):C.UVGC_330_456,(0,0,2):C.UVGC_330_457,(0,0,3):C.UVGC_330_458,(0,0,7):C.UVGC_321_394,(0,0,8):C.UVGC_330_459,(0,0,10):C.UVGC_330_460,(0,0,4):C.UVGC_330_461,(0,1,9):C.UVGC_330_455,(0,1,0):C.UVGC_321_395,(0,1,1):C.UVGC_330_456,(0,1,2):C.UVGC_330_457,(0,1,3):C.UVGC_330_458,(0,1,7):C.UVGC_321_394,(0,1,8):C.UVGC_330_459,(0,1,10):C.UVGC_330_460,(0,1,4):C.UVGC_330_461,(0,2,5):C.UVGC_331_462,(0,2,9):C.UVGC_331_463,(0,2,0):C.UVGC_322_401,(0,2,1):C.UVGC_331_464,(0,2,2):C.UVGC_331_465,(0,2,3):C.UVGC_331_466,(0,2,6):C.UVGC_331_467,(0,2,7):C.UVGC_321_394,(0,2,8):C.UVGC_330_459,(0,2,10):C.UVGC_331_468,(0,2,4):C.UVGC_331_469})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.e__plus__, P.e__minus__, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.e__minus__] ], [ [P.e__minus__, P.Z] ], [ [P.ve, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_212_119,(0,0,1):C.UVGC_268_222,(0,0,2):C.UVGC_268_223,(0,1,0):C.UVGC_212_119,(0,1,1):C.UVGC_212_120})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.mu__plus__, P.mu__minus__, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.mu__minus__] ], [ [P.mu__minus__, P.Z] ], [ [P.vm, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_212_119,(0,0,1):C.UVGC_268_222,(0,0,2):C.UVGC_268_223,(0,1,0):C.UVGC_212_119,(0,1,1):C.UVGC_212_120})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.ta__minus__, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.G0, P.ta__minus__], [P.H, P.ta__minus__] ], [ [P.G__plus__, P.vt] ], [ [P.ta__minus__, P.Z] ], [ [P.vt, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_212_119,(0,0,1):C.UVGC_278_232,(0,0,3):C.UVGC_268_222,(0,0,4):C.UVGC_268_223,(0,1,0):C.UVGC_212_119,(0,1,1):C.UVGC_278_232,(0,1,2):C.UVGC_278_233,(0,1,3):C.UVGC_212_120})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.u] ], [ [P.d, P.W__plus__] ], [ [P.g, P.u] ], [ [P.u, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_226_159,(0,0,1):C.UVGC_229_171,(0,0,2):C.UVGC_226_160,(0,0,3):C.UVGC_229_170,(0,1,0):C.UVGC_226_159,(0,1,2):C.UVGC_226_160,(0,1,3):C.UVGC_226_162})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0], [P.c, P.H] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s] ], [ [P.s, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_226_159,(0,0,1):C.UVGC_226_160,(0,0,2):C.UVGC_226_161,(0,0,3):C.UVGC_229_170,(0,0,5):C.UVGC_229_171,(0,1,0):C.UVGC_226_159,(0,1,1):C.UVGC_226_160,(0,1,2):C.UVGC_226_161,(0,1,3):C.UVGC_226_162,(0,1,4):C.UVGC_226_163})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.W__plus__] ], [ [P.G0, P.t], [P.H, P.t] ], [ [P.g, P.t] ], [ [P.t, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_226_159,(0,0,1):C.UVGC_248_200,(0,0,2):C.UVGC_229_171,(0,0,4):C.UVGC_226_160,(0,0,3):C.UVGC_248_201,(0,0,5):C.UVGC_229_170,(0,1,0):C.UVGC_226_159,(0,1,1):C.UVGC_249_202,(0,1,4):C.UVGC_226_160,(0,1,3):C.UVGC_248_201,(0,1,5):C.UVGC_226_162})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.d] ], [ [P.d, P.g] ], [ [P.d, P.Z] ], [ [P.u, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_208_108,(0,0,1):C.UVGC_208_109,(0,0,2):C.UVGC_234_177,(0,0,3):C.UVGC_234_176,(0,1,0):C.UVGC_208_108,(0,1,1):C.UVGC_208_109,(0,1,2):C.UVGC_208_110})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.s] ], [ [P.c, P.G__plus__] ], [ [P.c, P.W__plus__] ], [ [P.g, P.s] ], [ [P.s, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_208_108,(0,0,1):C.UVGC_234_175,(0,0,2):C.UVGC_234_176,(0,0,3):C.UVGC_208_109,(0,0,4):C.UVGC_234_177,(0,1,0):C.UVGC_208_108,(0,1,3):C.UVGC_208_109,(0,1,4):C.UVGC_208_110})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0], [P.b, P.H] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.t, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_208_108,(0,0,1):C.UVGC_208_109,(0,0,2):C.UVGC_240_186,(0,0,3):C.UVGC_234_177,(0,0,4):C.UVGC_244_197,(0,0,5):C.UVGC_234_176,(0,1,0):C.UVGC_208_108,(0,1,1):C.UVGC_208_109,(0,1,2):C.UVGC_240_186,(0,1,3):C.UVGC_208_110,(0,1,4):C.UVGC_240_187})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.u] ], [ [P.d, P.W__plus__] ], [ [P.g, P.u] ], [ [P.u, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_227_164,(0,0,1):C.UVGC_230_173,(0,0,2):C.UVGC_209_112,(0,0,3):C.UVGC_230_172,(0,1,0):C.UVGC_227_164,(0,1,2):C.UVGC_209_112,(0,1,3):C.UVGC_227_166})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0], [P.c, P.H] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s] ], [ [P.s, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_227_164,(0,0,1):C.UVGC_209_112,(0,0,2):C.UVGC_227_165,(0,0,3):C.UVGC_230_172,(0,0,5):C.UVGC_230_173,(0,1,0):C.UVGC_227_164,(0,1,1):C.UVGC_209_112,(0,1,2):C.UVGC_227_165,(0,1,3):C.UVGC_227_166,(0,1,4):C.UVGC_227_167})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.W__plus__] ], [ [P.G0, P.t], [P.H, P.t] ], [ [P.g, P.t] ], [ [P.t, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_227_164,(0,0,1):C.UVGC_241_189,(0,0,2):C.UVGC_230_173,(0,0,4):C.UVGC_209_112,(0,0,3):C.UVGC_250_203,(0,0,5):C.UVGC_230_172,(0,1,0):C.UVGC_227_164,(0,1,1):C.UVGC_245_198,(0,1,4):C.UVGC_209_112,(0,1,3):C.UVGC_250_203,(0,1,5):C.UVGC_227_166})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.d] ], [ [P.d, P.g] ], [ [P.d, P.Z] ], [ [P.u, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_209_111,(0,0,1):C.UVGC_209_112,(0,0,2):C.UVGC_235_178,(0,0,3):C.UVGC_230_173,(0,1,0):C.UVGC_209_111,(0,1,1):C.UVGC_209_112,(0,1,2):C.UVGC_209_113})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.s] ], [ [P.c, P.G__plus__] ], [ [P.c, P.W__plus__] ], [ [P.g, P.s] ], [ [P.s, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_209_111,(0,0,1):C.UVGC_227_167,(0,0,2):C.UVGC_230_173,(0,0,3):C.UVGC_209_112,(0,0,4):C.UVGC_235_178,(0,1,0):C.UVGC_209_111,(0,1,3):C.UVGC_209_112,(0,1,4):C.UVGC_209_113})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0], [P.b, P.H] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.t, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_209_111,(0,0,1):C.UVGC_209_112,(0,0,2):C.UVGC_241_188,(0,0,3):C.UVGC_235_178,(0,0,4):C.UVGC_245_198,(0,0,5):C.UVGC_230_173,(0,1,0):C.UVGC_209_111,(0,1,1):C.UVGC_209_112,(0,1,2):C.UVGC_241_188,(0,1,3):C.UVGC_209_113,(0,1,4):C.UVGC_241_189})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.d, P.u] ], [ [P.a, P.d, P.W__plus__] ], [ [P.a, P.u, P.W__plus__] ], [ [P.d, P.g, P.u] ], [ [P.d, P.u, P.Z] ], [ [P.d, P.W__plus__, P.Z] ], [ [P.u, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_345_547,(0,0,1):C.UVGC_345_549,(0,0,2):C.UVGC_345_548,(0,0,3):C.UVGC_345_550,(0,0,4):C.UVGC_345_552,(0,0,5):C.UVGC_345_554,(0,0,6):C.UVGC_345_553})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.c, P.s] ], [ [P.a, P.c, P.W__plus__] ], [ [P.a, P.s, P.W__plus__] ], [ [P.c, P.G0, P.G__plus__], [P.c, P.G__plus__, P.H] ], [ [P.c, P.g, P.s] ], [ [P.c, P.s, P.Z] ], [ [P.c, P.W__plus__, P.Z] ], [ [P.s, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_345_547,(0,0,1):C.UVGC_345_548,(0,0,2):C.UVGC_345_549,(0,0,4):C.UVGC_345_550,(0,0,3):C.UVGC_345_551,(0,0,5):C.UVGC_345_552,(0,0,6):C.UVGC_345_553,(0,0,7):C.UVGC_345_554})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.b, P.t] ], [ [P.a, P.b, P.W__plus__] ], [ [P.a, P.t, P.W__plus__] ], [ [P.b, P.G0, P.G__plus__], [P.b, P.G__plus__, P.H] ], [ [P.b, P.G0, P.G__plus__], [P.b, P.H, P.t], [P.G0, P.G__plus__, P.t] ], [ [P.b, P.G0, P.t], [P.b, P.G__plus__, P.H], [P.G__plus__, P.H, P.t] ], [ [P.b, P.g, P.t] ], [ [P.b, P.t, P.Z] ], [ [P.b, P.W__plus__, P.Z] ], [ [P.G0, P.G__plus__, P.t], [P.G__plus__, P.H, P.t] ], [ [P.t, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_345_547,(0,0,1):C.UVGC_345_549,(0,0,2):C.UVGC_345_548,(0,0,6):C.UVGC_345_550,(0,0,3):C.UVGC_359_643,(0,0,7):C.UVGC_345_552,(0,0,8):C.UVGC_345_554,(0,0,9):C.UVGC_359_644,(0,0,10):C.UVGC_345_553,(0,1,4):C.UVGC_348_561,(0,1,5):C.UVGC_348_562})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.d, P.u] ], [ [P.a, P.d, P.W__plus__] ], [ [P.a, P.u, P.W__plus__] ], [ [P.d, P.g, P.u] ], [ [P.d, P.u, P.Z] ], [ [P.d, P.W__plus__, P.Z] ], [ [P.u, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_345_547,(0,0,1):C.UVGC_345_549,(0,0,2):C.UVGC_345_548,(0,0,3):C.UVGC_345_550,(0,0,4):C.UVGC_345_552,(0,0,5):C.UVGC_345_554,(0,0,6):C.UVGC_345_553})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.c, P.s] ], [ [P.a, P.c, P.W__plus__] ], [ [P.a, P.s, P.W__plus__] ], [ [P.c, P.G0, P.G__plus__], [P.c, P.G__plus__, P.H] ], [ [P.c, P.g, P.s] ], [ [P.c, P.s, P.Z] ], [ [P.c, P.W__plus__, P.Z] ], [ [P.s, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_345_547,(0,0,1):C.UVGC_345_548,(0,0,2):C.UVGC_345_549,(0,0,4):C.UVGC_345_550,(0,0,3):C.UVGC_345_551,(0,0,5):C.UVGC_345_552,(0,0,6):C.UVGC_345_553,(0,0,7):C.UVGC_345_554})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.b, P.t] ], [ [P.a, P.b, P.W__plus__] ], [ [P.a, P.t, P.W__plus__] ], [ [P.b, P.G0, P.G__plus__], [P.b, P.G__plus__, P.H] ], [ [P.b, P.G0, P.G__plus__], [P.b, P.H, P.t], [P.G0, P.G__plus__, P.t] ], [ [P.b, P.G0, P.t], [P.b, P.G__plus__, P.H], [P.G__plus__, P.H, P.t] ], [ [P.b, P.g, P.t] ], [ [P.b, P.t, P.Z] ], [ [P.b, P.W__plus__, P.Z] ], [ [P.G0, P.G__plus__, P.t], [P.G__plus__, P.H, P.t] ], [ [P.t, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_345_547,(0,0,1):C.UVGC_345_549,(0,0,2):C.UVGC_345_548,(0,0,6):C.UVGC_345_550,(0,0,3):C.UVGC_359_643,(0,0,7):C.UVGC_345_552,(0,0,8):C.UVGC_345_554,(0,0,9):C.UVGC_359_644,(0,0,10):C.UVGC_345_553,(0,1,4):C.UVGC_348_561,(0,1,5):C.UVGC_348_562})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.e__plus__, P.ve, P.W__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.e__minus__, P.W__plus__] ], [ [P.e__minus__, P.ve, P.Z] ], [ [P.e__minus__, P.W__plus__, P.Z] ], [ [P.ve, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_363_649,(0,0,1):C.UVGC_363_650,(0,0,2):C.UVGC_363_651,(0,0,3):C.UVGC_363_652})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.mu__minus__, P.W__plus__] ], [ [P.mu__minus__, P.vm, P.Z] ], [ [P.mu__minus__, P.W__plus__, P.Z] ], [ [P.vm, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_363_649,(0,0,1):C.UVGC_363_650,(0,0,2):C.UVGC_363_651,(0,0,3):C.UVGC_363_652})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.ta__minus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.ta__minus__], [P.G__plus__, P.H, P.ta__minus__] ], [ [P.ta__minus__, P.vt, P.Z] ], [ [P.ta__minus__, P.W__plus__, P.Z] ], [ [P.vt, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_363_649,(0,0,1):C.UVGC_370_679,(0,0,2):C.UVGC_363_650,(0,0,3):C.UVGC_363_651,(0,0,4):C.UVGC_363_652})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.e__minus__, P.W__plus__] ], [ [P.e__minus__, P.ve, P.Z] ], [ [P.e__minus__, P.W__plus__, P.Z] ], [ [P.ve, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_363_649,(0,0,1):C.UVGC_363_650,(0,0,2):C.UVGC_363_651,(0,0,3):C.UVGC_363_652})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.mu__minus__, P.W__plus__] ], [ [P.mu__minus__, P.vm, P.Z] ], [ [P.mu__minus__, P.W__plus__, P.Z] ], [ [P.vm, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_363_649,(0,0,1):C.UVGC_363_650,(0,0,2):C.UVGC_363_651,(0,0,3):C.UVGC_363_652})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.a, P.ta__minus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.ta__minus__], [P.G__plus__, P.H, P.ta__minus__] ], [ [P.ta__minus__, P.vt, P.Z] ], [ [P.ta__minus__, P.W__plus__, P.Z] ], [ [P.vt, P.W__plus__, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_363_649,(0,0,1):C.UVGC_370_679,(0,0,2):C.UVGC_363_650,(0,0,3):C.UVGC_363_651,(0,0,4):C.UVGC_363_652})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.u] ], [ [P.d, P.W__plus__] ], [ [P.g, P.u] ], [ [P.u, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_266_217,(0,0,1):C.UVGC_266_218,(0,0,2):C.UVGC_266_219,(0,0,3):C.UVGC_266_220,(0,1,0):C.UVGC_265_214,(0,1,2):C.UVGC_265_215,(0,1,3):C.UVGC_265_216})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0], [P.c, P.H] ], [ [P.c, P.G0, P.H] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s] ], [ [P.s, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_266_217,(0,0,1):C.UVGC_266_219,(0,0,2):C.UVGC_329_453,(0,0,4):C.UVGC_266_220,(0,0,6):C.UVGC_266_218,(0,0,3):C.UVGC_329_454,(0,1,0):C.UVGC_265_214,(0,1,1):C.UVGC_265_215,(0,1,2):C.UVGC_328_450,(0,1,4):C.UVGC_265_216,(0,1,5):C.UVGC_328_451,(0,1,3):C.UVGC_328_452})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.W__plus__] ], [ [P.G0, P.H, P.t] ], [ [P.G0, P.t], [P.H, P.t] ], [ [P.g, P.t] ], [ [P.t, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_266_217,(0,0,1):C.UVGC_347_558,(0,0,2):C.UVGC_266_218,(0,0,5):C.UVGC_266_219,(0,0,4):C.UVGC_347_559,(0,0,6):C.UVGC_266_220,(0,0,3):C.UVGC_347_560,(0,1,0):C.UVGC_265_214,(0,1,1):C.UVGC_346_555,(0,1,5):C.UVGC_265_215,(0,1,4):C.UVGC_346_556,(0,1,6):C.UVGC_265_216,(0,1,3):C.UVGC_346_557})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.d] ], [ [P.d, P.g] ], [ [P.d, P.Z] ], [ [P.u, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_237_179,(0,0,1):C.UVGC_237_182,(0,0,2):C.UVGC_237_183,(0,0,3):C.UVGC_237_181,(0,1,0):C.UVGC_210_114,(0,1,1):C.UVGC_210_115,(0,1,2):C.UVGC_210_116})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.s] ], [ [P.c, P.G__plus__] ], [ [P.c, P.W__plus__] ], [ [P.g, P.s] ], [ [P.s, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_237_179,(0,0,1):C.UVGC_237_180,(0,0,2):C.UVGC_237_181,(0,0,3):C.UVGC_237_182,(0,0,4):C.UVGC_237_183,(0,1,0):C.UVGC_210_114,(0,1,3):C.UVGC_210_115,(0,1,4):C.UVGC_210_116})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0], [P.b, P.H] ], [ [P.b, P.G0, P.H] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.t, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_237_179,(0,0,1):C.UVGC_237_182,(0,0,2):C.UVGC_326_444,(0,0,4):C.UVGC_237_183,(0,0,5):C.UVGC_326_445,(0,0,6):C.UVGC_237_181,(0,0,3):C.UVGC_326_446,(0,1,0):C.UVGC_210_114,(0,1,1):C.UVGC_210_115,(0,1,2):C.UVGC_327_447,(0,1,4):C.UVGC_210_116,(0,1,5):C.UVGC_327_448,(0,1,3):C.UVGC_327_449})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.ve, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.e__minus__, P.W__plus__] ], [ [P.ve, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_271_228,(0,0,1):C.UVGC_271_229})

V_248 = CTVertex(name = 'V_248',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.vm, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.mu__minus__, P.W__plus__] ], [ [P.vm, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_271_228,(0,0,1):C.UVGC_271_229})

V_249 = CTVertex(name = 'V_249',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.vt, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.G__plus__, P.ta__minus__] ], [ [P.ta__minus__, P.W__plus__] ], [ [P.vt, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_282_234,(0,0,1):C.UVGC_271_228,(0,0,2):C.UVGC_271_229})

V_250 = CTVertex(name = 'V_250',
                 type = 'UV',
                 particles = [ P.e__plus__, P.e__minus__, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.e__minus__] ], [ [P.e__minus__, P.Z] ], [ [P.ve, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_269_224,(0,0,1):C.UVGC_269_225,(0,0,2):C.UVGC_269_226,(0,1,0):C.UVGC_213_121,(0,1,1):C.UVGC_213_122})

V_251 = CTVertex(name = 'V_251',
                 type = 'UV',
                 particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.mu__minus__] ], [ [P.mu__minus__, P.Z] ], [ [P.vm, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_269_224,(0,0,1):C.UVGC_269_225,(0,0,2):C.UVGC_269_226,(0,1,0):C.UVGC_213_121,(0,1,1):C.UVGC_213_122})

V_252 = CTVertex(name = 'V_252',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.G0, P.H, P.ta__minus__] ], [ [P.G0, P.ta__minus__], [P.H, P.ta__minus__] ], [ [P.G__plus__, P.vt] ], [ [P.ta__minus__, P.Z] ], [ [P.vt, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_269_224,(0,0,2):C.UVGC_360_645,(0,0,4):C.UVGC_269_225,(0,0,5):C.UVGC_269_226,(0,0,1):C.UVGC_360_646,(0,1,0):C.UVGC_213_121,(0,1,2):C.UVGC_361_647,(0,1,3):C.UVGC_361_648,(0,1,4):C.UVGC_213_122,(0,1,1):C.UVGC_282_234})

V_253 = CTVertex(name = 'V_253',
                 type = 'UV',
                 particles = [ P.H ],
                 color = [ '1' ],
                 lorentz = [ L.S1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0] ], [ [P.ghWm], [P.ghWp] ], [ [P.ghZ] ], [ [P.G__plus__] ], [ [P.H] ], [ [P.P__tilde__SDM] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_205_88,(0,0,1):C.UVGC_205_89,(0,0,2):C.UVGC_205_90,(0,0,3):C.UVGC_205_91,(0,0,4):C.UVGC_205_92,(0,0,5):C.UVGC_205_93,(0,0,6):C.UVGC_205_94,(0,0,7):C.UVGC_205_95,(0,0,8):C.UVGC_205_96,(0,0,9):C.UVGC_205_97,(0,0,10):C.UVGC_205_98,(0,0,11):C.UVGC_205_99})

V_254 = CTVertex(name = 'V_254',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.ve ],
                 color = [ '1' ],
                 lorentz = [ L.FF3 ],
                 loop_particles = [ [ [P.e__minus__, P.W__plus__] ], [ [P.ve, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_228_169,(0,0,1):C.UVGC_270_227})

V_255 = CTVertex(name = 'V_255',
                 type = 'UV',
                 particles = [ P.e__plus__, P.e__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.e__minus__] ], [ [P.e__minus__, P.Z] ], [ [P.ve, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_211_117,(0,0,1):C.UVGC_267_221,(0,0,2):C.UVGC_228_169,(0,1,0):C.UVGC_211_117,(0,1,1):C.UVGC_211_118})

V_256 = CTVertex(name = 'V_256',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.vm ],
                 color = [ '1' ],
                 lorentz = [ L.FF3 ],
                 loop_particles = [ [ [P.mu__minus__, P.W__plus__] ], [ [P.vm, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_228_169,(0,0,1):C.UVGC_270_227})

V_257 = CTVertex(name = 'V_257',
                 type = 'UV',
                 particles = [ P.mu__plus__, P.mu__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.mu__minus__] ], [ [P.mu__minus__, P.Z] ], [ [P.vm, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_211_117,(0,0,1):C.UVGC_267_221,(0,0,2):C.UVGC_228_169,(0,1,0):C.UVGC_211_117,(0,1,1):C.UVGC_211_118})

V_258 = CTVertex(name = 'V_258',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.ta__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.a, P.ta__minus__] ], [ [P.G0, P.ta__minus__] ], [ [P.G0, P.ta__minus__], [P.H, P.ta__minus__] ], [ [P.G__plus__, P.vt] ], [ [P.H, P.ta__minus__] ], [ [P.ta__minus__, P.Z] ], [ [P.vt, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_254_210,(0,0,1):C.UVGC_254_211,(0,0,4):C.UVGC_254_212,(0,0,5):C.UVGC_254_213,(0,2,0):C.UVGC_254_210,(0,2,1):C.UVGC_254_211,(0,2,4):C.UVGC_254_212,(0,2,5):C.UVGC_254_213,(0,1,0):C.UVGC_211_117,(0,1,2):C.UVGC_277_230,(0,1,5):C.UVGC_267_221,(0,1,6):C.UVGC_228_169,(0,3,0):C.UVGC_211_117,(0,3,2):C.UVGC_277_230,(0,3,3):C.UVGC_277_231,(0,3,5):C.UVGC_211_118})

V_259 = CTVertex(name = 'V_259',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.vt ],
                 color = [ '1' ],
                 lorentz = [ L.FF3 ],
                 loop_particles = [ [ [P.G__plus__, P.ta__minus__] ], [ [P.ta__minus__, P.W__plus__] ], [ [P.vt, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_277_231,(0,0,1):C.UVGC_228_169,(0,0,2):C.UVGC_270_227})

V_260 = CTVertex(name = 'V_260',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.u] ], [ [P.d, P.W__plus__] ], [ [P.g, P.u] ], [ [P.u, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_197_64,(0,0,1):C.UVGC_228_169,(0,0,2):C.UVGC_207_106,(0,0,3):C.UVGC_228_168,(0,1,0):C.UVGC_197_64,(0,1,2):C.UVGC_207_106,(0,1,3):C.UVGC_225_157})

V_261 = CTVertex(name = 'V_261',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.d] ], [ [P.d, P.g] ], [ [P.d, P.Z] ], [ [P.u, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_207_105,(0,0,1):C.UVGC_207_106,(0,0,2):C.UVGC_232_174,(0,0,3):C.UVGC_228_169,(0,1,0):C.UVGC_207_105,(0,1,1):C.UVGC_207_106,(0,1,2):C.UVGC_207_107})

V_262 = CTVertex(name = 'V_262',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.a, P.c] ], [ [P.c, P.g] ], [ [P.c, P.G0] ], [ [P.c, P.G0], [P.c, P.H] ], [ [P.c, P.H] ], [ [P.c, P.Z] ], [ [P.G__plus__, P.s] ], [ [P.s, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_206_100,(0,0,1):C.UVGC_206_101,(0,0,2):C.UVGC_206_102,(0,0,4):C.UVGC_206_103,(0,0,5):C.UVGC_206_104,(0,2,0):C.UVGC_206_100,(0,2,1):C.UVGC_206_101,(0,2,2):C.UVGC_206_102,(0,2,4):C.UVGC_206_103,(0,2,5):C.UVGC_206_104,(0,1,0):C.UVGC_197_64,(0,1,1):C.UVGC_207_106,(0,1,3):C.UVGC_225_156,(0,1,5):C.UVGC_228_168,(0,1,7):C.UVGC_228_169,(0,3,0):C.UVGC_197_64,(0,3,1):C.UVGC_207_106,(0,3,3):C.UVGC_225_156,(0,3,5):C.UVGC_225_157,(0,3,6):C.UVGC_225_158})

V_263 = CTVertex(name = 'V_263',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.a, P.s] ], [ [P.c, P.G__plus__] ], [ [P.c, P.W__plus__] ], [ [P.g, P.s] ], [ [P.s, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_207_105,(0,0,1):C.UVGC_225_158,(0,0,2):C.UVGC_228_169,(0,0,3):C.UVGC_207_106,(0,0,4):C.UVGC_232_174,(0,1,0):C.UVGC_207_105,(0,1,3):C.UVGC_207_106,(0,1,4):C.UVGC_207_107})

V_264 = CTVertex(name = 'V_264',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.a, P.t] ], [ [P.b, P.G__plus__] ], [ [P.b, P.W__plus__] ], [ [P.G0, P.t] ], [ [P.G0, P.t], [P.H, P.t] ], [ [P.g, P.t] ], [ [P.H, P.t] ], [ [P.t, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_252_204,(0,0,1):C.UVGC_252_205,(0,0,5):C.UVGC_252_206,(0,0,3):C.UVGC_252_207,(0,0,6):C.UVGC_252_208,(0,0,7):C.UVGC_252_209,(0,2,0):C.UVGC_252_204,(0,2,1):C.UVGC_252_205,(0,2,5):C.UVGC_252_206,(0,2,3):C.UVGC_252_207,(0,2,6):C.UVGC_252_208,(0,2,7):C.UVGC_252_209,(0,1,0):C.UVGC_197_64,(0,1,1):C.UVGC_239_185,(0,1,2):C.UVGC_228_169,(0,1,5):C.UVGC_207_106,(0,1,4):C.UVGC_246_199,(0,1,7):C.UVGC_228_168,(0,3,0):C.UVGC_197_64,(0,3,1):C.UVGC_243_196,(0,3,5):C.UVGC_207_106,(0,3,4):C.UVGC_246_199,(0,3,7):C.UVGC_225_157})

V_265 = CTVertex(name = 'V_265',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.a, P.b] ], [ [P.b, P.g] ], [ [P.b, P.G0] ], [ [P.b, P.G0], [P.b, P.H] ], [ [P.b, P.H] ], [ [P.b, P.Z] ], [ [P.G__plus__, P.t] ], [ [P.t, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_242_190,(0,0,1):C.UVGC_242_191,(0,0,2):C.UVGC_242_192,(0,0,4):C.UVGC_242_193,(0,0,5):C.UVGC_242_194,(0,0,6):C.UVGC_242_195,(0,2,0):C.UVGC_242_190,(0,2,1):C.UVGC_242_191,(0,2,2):C.UVGC_242_192,(0,2,4):C.UVGC_242_193,(0,2,5):C.UVGC_242_194,(0,2,6):C.UVGC_242_195,(0,1,0):C.UVGC_207_105,(0,1,1):C.UVGC_207_106,(0,1,3):C.UVGC_239_184,(0,1,5):C.UVGC_232_174,(0,1,6):C.UVGC_243_196,(0,1,7):C.UVGC_228_169,(0,3,0):C.UVGC_207_105,(0,3,1):C.UVGC_207_106,(0,3,3):C.UVGC_239_184,(0,3,5):C.UVGC_207_107,(0,3,6):C.UVGC_239_185})

V_266 = CTVertex(name = 'V_266',
                 type = 'UV',
                 particles = [ P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.SS1, L.SS3, L.SS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0] ], [ [P.G0, P.Z] ], [ [P.ghWm], [P.ghWp] ], [ [P.ghZ] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.P__tilde__SDM] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_294_266,(0,0,1):C.UVGC_294_267,(0,0,2):C.UVGC_294_268,(0,0,4):C.UVGC_294_269,(0,0,5):C.UVGC_294_270,(0,0,6):C.UVGC_294_271,(0,0,8):C.UVGC_294_272,(0,0,9):C.UVGC_294_273,(0,0,10):C.UVGC_294_274,(0,0,11):C.UVGC_294_275,(0,0,12):C.UVGC_294_276,(0,0,13):C.UVGC_294_277,(0,0,3):C.UVGC_294_278,(0,0,7):C.UVGC_294_279,(0,2,0):C.UVGC_291_253,(0,2,1):C.UVGC_291_254,(0,2,10):C.UVGC_291_255,(0,2,11):C.UVGC_291_256,(0,2,3):C.UVGC_291_257,(0,2,7):C.UVGC_291_258,(0,1,3):C.UVGC_292_259,(0,1,7):C.UVGC_292_260})

V_267 = CTVertex(name = 'V_267',
                 type = 'UV',
                 particles = [ P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.SS1, L.SS3, L.SS4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.G0] ], [ [P.G0, P.H] ], [ [P.ghWm], [P.ghWp] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.H, P.Z] ], [ [P.P__tilde__SDM] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.W__plus__] ], [ [P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_305_324,(0,0,1):C.UVGC_305_325,(0,0,2):C.UVGC_305_326,(0,0,4):C.UVGC_305_327,(0,0,5):C.UVGC_305_328,(0,0,7):C.UVGC_305_329,(0,0,9):C.UVGC_305_330,(0,0,10):C.UVGC_305_331,(0,0,11):C.UVGC_305_332,(0,0,12):C.UVGC_305_333,(0,0,13):C.UVGC_305_334,(0,0,3):C.UVGC_305_335,(0,0,6):C.UVGC_294_279,(0,0,8):C.UVGC_305_336,(0,2,0):C.UVGC_291_253,(0,2,1):C.UVGC_291_254,(0,2,10):C.UVGC_291_255,(0,2,11):C.UVGC_291_256,(0,2,6):C.UVGC_291_258,(0,2,8):C.UVGC_291_257,(0,1,6):C.UVGC_292_260,(0,1,8):C.UVGC_292_259})

V_268 = CTVertex(name = 'V_268',
                 type = 'UV',
                 particles = [ P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.SS1, L.SS2, L.SS3 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.G0] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__], [P.H, P.W__plus__] ], [ [P.ghWm, P.ghZ], [P.ghWp, P.ghZ] ], [ [P.G__plus__] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.Z] ], [ [P.H] ], [ [P.H, P.W__plus__] ], [ [P.P__tilde__SDM] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,4):C.UVGC_324_419,(0,0,8):C.UVGC_324_420,(0,0,11):C.UVGC_305_329,(0,0,13):C.UVGC_305_330,(0,0,15):C.UVGC_305_333,(0,0,17):C.UVGC_324_421,(0,0,0):C.UVGC_324_422,(0,0,1):C.UVGC_324_423,(0,0,2):C.UVGC_324_424,(0,0,3):C.UVGC_305_325,(0,0,5):C.UVGC_324_425,(0,0,7):C.UVGC_324_426,(0,0,9):C.UVGC_305_335,(0,0,10):C.UVGC_324_427,(0,0,12):C.UVGC_324_428,(0,0,14):C.UVGC_305_332,(0,0,16):C.UVGC_324_429,(0,1,0):C.UVGC_297_303,(0,1,2):C.UVGC_297_304,(0,1,3):C.UVGC_291_254,(0,1,6):C.UVGC_297_305,(0,1,10):C.UVGC_297_306,(0,1,14):C.UVGC_291_256,(0,2,0):C.UVGC_298_307,(0,2,6):C.UVGC_298_308,(0,2,10):C.UVGC_298_309})

V_269 = CTVertex(name = 'V_269',
                 type = 'UV',
                 particles = [ P.a, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.VV1, L.VV2, L.VV4, L.VV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.ghWm], [P.ghWp] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_197_64,(0,0,1):C.UVGC_197_65,(0,0,2):C.UVGC_197_66,(0,0,3):C.UVGC_198_70,(0,0,4):C.UVGC_197_68,(0,0,6):C.UVGC_198_71,(0,1,3):C.UVGC_289_247,(0,1,6):C.UVGC_289_248,(0,1,5):C.UVGC_289_249,(0,3,0):C.UVGC_197_64,(0,3,1):C.UVGC_197_65,(0,3,2):C.UVGC_197_66,(0,3,3):C.UVGC_197_67,(0,3,4):C.UVGC_197_68,(0,3,6):C.UVGC_197_69,(0,2,6):C.UVGC_159_6})

V_270 = CTVertex(name = 'V_270',
                 type = 'UV',
                 particles = [ P.a, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VV1, L.VV2, L.VV4, L.VV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.ghWm], [P.ghWp] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_202_78,(0,0,1):C.UVGC_202_79,(0,0,2):C.UVGC_202_80,(0,0,3):C.UVGC_203_84,(0,0,4):C.UVGC_202_82,(0,0,6):C.UVGC_203_85,(0,1,3):C.UVGC_290_250,(0,1,6):C.UVGC_290_251,(0,1,5):C.UVGC_290_252,(0,3,0):C.UVGC_202_78,(0,3,1):C.UVGC_202_79,(0,3,2):C.UVGC_202_80,(0,3,3):C.UVGC_202_81,(0,3,4):C.UVGC_202_82,(0,3,6):C.UVGC_202_83,(0,2,6):C.UVGC_164_11})

V_271 = CTVertex(name = 'V_271',
                 type = 'UV',
                 particles = [ P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VV1, L.VV2, L.VV4, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.d], [P.s] ], [ [P.c] ], [ [P.c], [P.t], [P.u] ], [ [P.e__minus__], [P.mu__minus__], [P.ta__minus__] ], [ [P.G0] ], [ [P.G0, P.H] ], [ [P.ghWm], [P.ghWp] ], [ [P.G__plus__] ], [ [P.G__plus__, P.W__plus__] ], [ [P.H] ], [ [P.H, P.Z] ], [ [P.t] ], [ [P.ta__minus__] ], [ [P.ve], [P.vm], [P.vt] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,1):C.UVGC_215_127,(0,0,3):C.UVGC_215_128,(0,0,4):C.UVGC_215_129,(0,0,7):C.UVGC_216_135,(0,0,8):C.UVGC_215_131,(0,0,14):C.UVGC_215_132,(0,0,15):C.UVGC_216_136,(0,0,6):C.UVGC_215_134,(0,1,0):C.UVGC_307_337,(0,1,2):C.UVGC_307_338,(0,1,5):C.UVGC_307_339,(0,1,7):C.UVGC_307_340,(0,1,10):C.UVGC_307_341,(0,1,12):C.UVGC_307_342,(0,1,13):C.UVGC_307_343,(0,1,15):C.UVGC_307_344,(0,1,6):C.UVGC_307_345,(0,1,9):C.UVGC_307_346,(0,1,11):C.UVGC_307_347,(0,3,1):C.UVGC_215_127,(0,3,3):C.UVGC_215_128,(0,3,4):C.UVGC_215_129,(0,3,7):C.UVGC_215_130,(0,3,8):C.UVGC_215_131,(0,3,14):C.UVGC_215_132,(0,3,15):C.UVGC_215_133,(0,3,6):C.UVGC_215_134,(0,2,15):C.UVGC_162_9})

V_272 = CTVertex(name = 'V_272',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3, L.VV4 ],
                 loop_particles = [ [ [P.a, P.G__plus__] ], [ [P.a, P.W__plus__] ], [ [P.b, P.t] ], [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.c, P.s] ], [ [P.e__minus__, P.ve], [P.mu__minus__, P.vm], [P.ta__minus__, P.vt] ], [ [P.G0] ], [ [P.G0, P.G__plus__] ], [ [P.G0, P.G__plus__], [P.G__plus__, P.H] ], [ [P.ghA, P.ghWm], [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ], [P.ghWp, P.ghZ] ], [ [P.G__plus__] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.Z] ], [ [P.H] ], [ [P.H, P.W__plus__] ], [ [P.ta__minus__, P.vt] ], [ [P.W__plus__] ], [ [P.W__plus__, P.Z] ], [ [P.Z] ] ],
                 couplings = {(0,0,1):C.UVGC_198_71,(0,0,3):C.UVGC_311_356,(0,0,5):C.UVGC_311_357,(0,0,8):C.UVGC_311_358,(0,0,9):C.UVGC_198_70,(0,0,10):C.UVGC_216_135,(0,0,18):C.UVGC_216_136,(0,1,6):C.UVGC_323_402,(0,1,11):C.UVGC_323_403,(0,1,14):C.UVGC_323_404,(0,1,17):C.UVGC_323_405,(0,1,19):C.UVGC_323_406,(0,1,0):C.UVGC_323_407,(0,1,1):C.UVGC_323_408,(0,1,2):C.UVGC_323_409,(0,1,4):C.UVGC_323_410,(0,1,7):C.UVGC_323_411,(0,1,9):C.UVGC_323_412,(0,1,10):C.UVGC_323_413,(0,1,12):C.UVGC_323_414,(0,1,13):C.UVGC_323_415,(0,1,15):C.UVGC_323_416,(0,1,16):C.UVGC_323_417,(0,1,18):C.UVGC_323_418,(0,2,1):C.UVGC_197_69,(0,2,3):C.UVGC_311_356,(0,2,5):C.UVGC_311_357,(0,2,8):C.UVGC_311_358,(0,2,9):C.UVGC_197_67,(0,2,10):C.UVGC_215_130,(0,2,18):C.UVGC_215_133,(0,3,1):C.UVGC_159_6,(0,3,18):C.UVGC_162_9})

V_273 = CTVertex(name = 'V_273',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV4, L.VV5 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g], [P.ghG] ] ],
                 couplings = {(0,0,0):C.UVGC_183_41,(0,0,1):C.UVGC_183_42,(0,0,2):C.UVGC_183_43,(0,2,0):C.UVGC_183_41,(0,2,3):C.UVGC_184_44,(0,1,1):C.UVGC_150_1})

V_274 = CTVertex(name = 'V_274',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.vt, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.ta__minus__, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_166_13})

V_275 = CTVertex(name = 'V_275',
                 type = 'UV',
                 particles = [ P.a, P.a, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.ghWm], [P.ghWp] ], [ [P.G__plus__, P.W__plus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_287_241,(0,0,2):C.UVGC_287_242,(0,0,1):C.UVGC_287_243})

V_276 = CTVertex(name = 'V_276',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.ghWm], [P.ghWp] ], [ [P.G__plus__, P.W__plus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_288_244,(0,0,2):C.UVGC_288_245,(0,0,1):C.UVGC_288_246})

V_277 = CTVertex(name = 'V_277',
                 type = 'UV',
                 particles = [ P.a, P.G0, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.G__plus__, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_284_236,(0,1,0):C.UVGC_283_235})

V_278 = CTVertex(name = 'V_278',
                 type = 'UV',
                 particles = [ P.a, P.a, P.a, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.ghWm], [P.ghWp] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_199_72,(0,0,1):C.UVGC_199_73,(0,1,0):C.UVGC_199_72,(0,1,1):C.UVGC_199_73,(0,2,0):C.UVGC_199_72,(0,2,1):C.UVGC_199_73})

V_279 = CTVertex(name = 'V_279',
                 type = 'UV',
                 particles = [ P.a, P.a, P.a, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.ghWm], [P.ghWp] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_204_86,(0,0,1):C.UVGC_204_87,(0,1,0):C.UVGC_204_86,(0,1,1):C.UVGC_204_87,(0,2,0):C.UVGC_204_86,(0,2,1):C.UVGC_204_87})

V_280 = CTVertex(name = 'V_280',
                 type = 'UV',
                 particles = [ P.a, P.a, P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.ghWm], [P.ghWp] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_201_76,(0,0,1):C.UVGC_201_77,(0,1,0):C.UVGC_201_76,(0,1,1):C.UVGC_201_77,(0,2,0):C.UVGC_201_76,(0,2,1):C.UVGC_201_77})

V_281 = CTVertex(name = 'V_281',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.ghWm], [P.ghWp] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_200_74,(0,0,1):C.UVGC_200_75,(0,1,0):C.UVGC_200_74,(0,1,1):C.UVGC_200_75,(0,2,0):C.UVGC_200_74,(0,2,1):C.UVGC_200_75})

V_282 = CTVertex(name = 'V_282',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.G0], [P.H] ], [ [P.G0, P.H] ], [ [P.ghWm], [P.ghWp] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_218_139,(0,0,2):C.UVGC_218_140,(0,0,3):C.UVGC_218_141,(0,0,1):C.UVGC_218_142,(0,1,0):C.UVGC_218_139,(0,1,2):C.UVGC_218_140,(0,1,3):C.UVGC_218_141,(0,1,1):C.UVGC_218_142,(0,2,0):C.UVGC_218_139,(0,2,2):C.UVGC_218_140,(0,2,3):C.UVGC_218_141,(0,2,1):C.UVGC_218_142})

V_283 = CTVertex(name = 'V_283',
                 type = 'UV',
                 particles = [ P.a, P.a, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.G__plus__, P.W__plus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,1):C.UVGC_285_237,(0,0,0):C.UVGC_285_238})

V_284 = CTVertex(name = 'V_284',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.G__plus__, P.W__plus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,1):C.UVGC_286_239,(0,0,0):C.UVGC_286_240})

V_285 = CTVertex(name = 'V_285',
                 type = 'UV',
                 particles = [ P.a, P.a, P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.G__plus__, P.W__plus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,1):C.UVGC_285_237,(0,0,0):C.UVGC_285_238})

V_286 = CTVertex(name = 'V_286',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.G__plus__, P.W__plus__] ], [ [P.W__plus__] ] ],
                 couplings = {(0,0,1):C.UVGC_286_239,(0,0,0):C.UVGC_286_240})

V_287 = CTVertex(name = 'V_287',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__minus__, P.G__plus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G0] ], [ [P.a, P.G0, P.W__plus__] ], [ [P.a, P.H] ], [ [P.a, P.H, P.W__plus__] ], [ [P.G0, P.G__plus__] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_382_771,(0,0,2):C.UVGC_321_388,(0,0,4):C.UVGC_382_767,(0,0,7):C.UVGC_391_887,(0,0,9):C.UVGC_382_779,(0,0,10):C.UVGC_382_775,(0,0,13):C.UVGC_391_888,(0,0,15):C.UVGC_391_889,(0,0,1):C.UVGC_391_890,(0,0,3):C.UVGC_391_891,(0,0,5):C.UVGC_391_892,(0,0,6):C.UVGC_382_785,(0,0,8):C.UVGC_391_893,(0,0,11):C.UVGC_391_894,(0,0,12):C.UVGC_391_895,(0,0,14):C.UVGC_391_896})

V_288 = CTVertex(name = 'V_288',
                 type = 'UV',
                 particles = [ P.W__plus__, P.W__plus__, P.G__minus__, P.G__minus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.a, P.G0] ], [ [P.a, P.G0, P.W__plus__] ], [ [P.a, P.H] ], [ [P.a, P.H, P.W__plus__] ], [ [P.G0, P.G__plus__] ], [ [P.G0, P.G__plus__, P.W__plus__] ], [ [P.G0, P.G__plus__, P.Z] ], [ [P.G0, P.W__plus__] ], [ [P.G0, P.W__plus__, P.Z] ], [ [P.G0, P.Z] ], [ [P.G__plus__, P.H] ], [ [P.G__plus__, P.H, P.W__plus__] ], [ [P.G__plus__, P.H, P.Z] ], [ [P.H, P.W__plus__] ], [ [P.H, P.W__plus__, P.Z] ], [ [P.H, P.Z] ] ],
                 couplings = {(0,0,0):C.UVGC_382_771,(0,0,2):C.UVGC_321_388,(0,0,4):C.UVGC_382_767,(0,0,7):C.UVGC_391_887,(0,0,9):C.UVGC_382_779,(0,0,10):C.UVGC_382_775,(0,0,13):C.UVGC_391_888,(0,0,15):C.UVGC_391_889,(0,0,1):C.UVGC_391_890,(0,0,3):C.UVGC_391_891,(0,0,5):C.UVGC_391_892,(0,0,6):C.UVGC_382_785,(0,0,8):C.UVGC_391_893,(0,0,11):C.UVGC_391_894,(0,0,12):C.UVGC_391_895,(0,0,14):C.UVGC_391_896})

V_289 = CTVertex(name = 'V_289',
                 type = 'UV',
                 particles = [ P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.S1 ],
                 loop_particles = [ [ [P.ghWm] ], [ [P.ghWp] ] ],
                 couplings = {(0,0,0):C.UVGC_180_34,(0,0,1):C.UVGC_180_35})

V_290 = CTVertex(name = 'V_290',
                 type = 'UV',
                 particles = [ P.G0, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.ghWm] ], [ [P.ghWp] ] ],
                 couplings = {(0,0,0):C.UVGC_181_36,(0,0,1):C.UVGC_181_37})

V_291 = CTVertex(name = 'V_291',
                 type = 'UV',
                 particles = [ P.P__tilde__SDM, P.P__tilde__SDM ],
                 color = [ '1' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.G0] ], [ [P.G__plus__] ], [ [P.H] ], [ [P.H, P.P__tilde__SDM] ], [ [P.P__tilde__SDM] ] ],
                 couplings = {(0,0,0):C.UVGC_221_151,(0,0,1):C.UVGC_221_152,(0,0,2):C.UVGC_221_153,(0,0,4):C.UVGC_221_154,(0,0,3):C.UVGC_221_155})

V_292 = CTVertex(name = 'V_292',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.ve, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.e__minus__, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_166_13})

V_293 = CTVertex(name = 'V_293',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.vm, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.mu__minus__, P.W__plus__] ] ],
                 couplings = {(0,0,0):C.UVGC_166_13})

V_294 = CTVertex(name = 'V_294',
                 type = 'UV',
                 particles = [ P.a, P.a, P.a ],
                 color = [ '1' ],
                 lorentz = [ L.VVV11, L.VVV13, L.VVV7 ],
                 loop_particles = [ [ [P.ghWm] ], [ [P.ghWp] ], [ [P.W__plus__] ] ],
                 couplings = {(0,1,0):C.UVGC_151_2,(0,2,2):C.UVGC_160_7,(0,0,1):C.UVGC_151_2})

V_295 = CTVertex(name = 'V_295',
                 type = 'UV',
                 particles = [ P.a, P.a, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVV11, L.VVV13, L.VVV7 ],
                 loop_particles = [ [ [P.ghWm] ], [ [P.ghWp] ], [ [P.W__plus__] ] ],
                 couplings = {(0,1,0):C.UVGC_154_5,(0,2,2):C.UVGC_165_12,(0,0,1):C.UVGC_154_5})

V_296 = CTVertex(name = 'V_296',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVV12, L.VVV13, L.VVV7 ],
                 loop_particles = [ [ [P.ghWm] ], [ [P.ghWp] ], [ [P.W__plus__] ] ],
                 couplings = {(0,1,0):C.UVGC_153_4,(0,2,2):C.UVGC_163_10,(0,0,1):C.UVGC_153_4})

V_297 = CTVertex(name = 'V_297',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.Z ],
                 color = [ '1' ],
                 lorentz = [ L.VVV11, L.VVV13, L.VVV7 ],
                 loop_particles = [ [ [P.ghWm] ], [ [P.ghWp] ], [ [P.W__plus__] ] ],
                 couplings = {(0,1,0):C.UVGC_152_3,(0,2,2):C.UVGC_161_8,(0,0,1):C.UVGC_152_3})

V_298 = CTVertex(name = 'V_298',
                 type = 'UV',
                 particles = [ P.a, P.a, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.ghWm] ], [ [P.ghWp] ] ],
                 couplings = {(0,0,0):C.UVGC_179_32,(0,0,1):C.UVGC_179_33})

V_299 = CTVertex(name = 'V_299',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.ghWm] ], [ [P.ghWp] ] ],
                 couplings = {(0,0,0):C.UVGC_178_30,(0,0,1):C.UVGC_178_31})

V_300 = CTVertex(name = 'V_300',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.ghWm] ], [ [P.ghWp] ] ],
                 couplings = {(0,0,0):C.UVGC_177_28,(0,0,1):C.UVGC_177_29})

V_301 = CTVertex(name = 'V_301',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.ghA, P.ghWm] ], [ [P.ghA, P.ghWp] ], [ [P.ghWm, P.ghZ] ], [ [P.ghWp, P.ghZ] ] ],
                 couplings = {(0,0,0):C.UVGC_214_123,(0,0,1):C.UVGC_214_124,(0,0,2):C.UVGC_214_125,(0,0,3):C.UVGC_214_126})

V_302 = CTVertex(name = 'V_302',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.P__tilde__SDM, P.P__tilde__SDM ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.G0], [P.H] ], [ [P.G0, P.H] ] ],
                 couplings = {(0,0,0):C.UVGC_217_137,(0,0,1):C.UVGC_217_138})

V_303 = CTVertex(name = 'V_303',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.P__tilde__SDM, P.P__tilde__SDM ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.G0, P.G__plus__], [P.G__plus__, P.H] ], [ [P.G0], [P.H] ], [ [P.G__plus__] ] ],
                 couplings = {(0,0,1):C.UVGC_219_143,(0,0,2):C.UVGC_219_144,(0,0,0):C.UVGC_219_145})

