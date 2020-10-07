import isotools.splice_graph 
from importlib import reload
import logging
isotools.splice_graph.log.setLevel(logging.DEBUG)
#todo: this was made for debugging, make a testcase out of it
ref=[[(40040232, 40040783),  (40059336, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066320),  (40067539, 40067717),  (40069689, 40069874),  (40070158, 40070282),  (40070429, 40070512),  (40070835, 40070979),  (40071449, 40072649)], 
    [(40040239, 40040783),  (40059333, 40059458),  (40060069, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066320),  (40067539, 40067717),  (40069689, 40069874),  (40070158, 40070282),  (40070429, 40070512),  (40070835, 40070979),  (40071449, 40072515)], 
    [(40040322, 40040467),  (40059333, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064558)], 
    [(40040582, 40040783),  (40059333, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066300)], 
    [(40040719, 40040801),  (40059336, 40059458),  (40060066, 40060089),  (40066272, 40066320),  (40067539, 40067717),  (40069689, 40069764)], 
    [(40040731, 40040801),  (40041428, 40041493),  (40059333, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066314)], 
    [(40040732, 40040783),  (40041428, 40041493),  (40059333, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066229)], 
    [(40040748, 40040801),  (40059333, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066320),  (40067539, 40067717),  (40069689, 40069874),  (40070158, 40070282),  (40070429, 40070512),  (40070835, 40070979),  (40071449, 40071535)], 
    [(40040751, 40040801),  (40059333, 40059458),  (40060069, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066320),  (40067539, 40067717),  (40069689, 40069874),  (40070158, 40070282),  (40070429, 40070512),  (40070835, 40070979),  (40071449, 40071608)], 
    [(40040752, 40040801),  (40059336, 40059458),  (40060069, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066320),  (40067539, 40067717),  (40069689, 40069874),  (40070158, 40070282),  (40070429, 40070512),  (40070835, 40070979),  (40071449, 40072641)], 
    [(40040760, 40040801),  (40059336, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066320),  (40067539, 40067717),  (40069689, 40069874),  (40070158, 40070282),  (40070429, 40070512),  (40070835, 40070979),  (40071449, 40072271)], 
    [(40040764, 40040783),  (40059336, 40059458),  (40060069, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066320),  (40067539, 40067700)], 
    [(40040766, 40040783),  (40041428, 40041493),  (40059336, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066320),  (40067539, 40067556)], 
    [(40040779, 40040801),  (40057445, 40057495),  (40059336, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066218)], 
    [(40040779, 40040801),  (40041428, 40041493),  (40059336, 40059458),  (40060066, 40060170),  (40061734, 40061812),  (40064226, 40064370),  (40064473, 40064559),  (40066214, 40066295)], 
    [(40040881, 40040965), (40059333, 40059458), (40060066, 40060130)], 
    [(40067269, 40067311),  (40067539, 40067717),  (40069689, 40069874),  (40070158, 40070282),  (40070429, 40070512),  (40070835, 40070979),  (40071449, 40071581)], 
    [(40069565, 40069874),  (40070158, 40070282),  (40070429, 40070512),  (40070835, 40070979),  (40071449, 40071645)], 
    [(40070469, 40070979), (40071449, 40071683)]]
exons= [[40040791, 40041493],  [40059336, 40059458],  [40060066, 40060170],  [40061734, 40061812],  [40064226, 40064370],  [40064473, 40064559],  [40066214, 40066320],  [40067539, 40067717],  [40069689, 40069874],  [40070158, 40070282],  [40070429, 40070512],  [40070835, 40070979],  [40071449, 40072246]]
strand='+'
sg=isotools.splice_graph.SpliceGraph(ref)
sg.get_alternative_splicing(exons, strand)
#{'retained intron': [[40040801, 40041428], [40040965, 40059333]]}
#issue: overlapping "retained introns", second is partly intronic

reload(isotools.splice_graph)
isotools.splice_graph.log.setLevel(logging.DEBUG)

#minimized example
exons= [[40040791, 40041493],  [40059336, 40059458],  [40060066, 40060170]]
ref=[
    [(40040881, 40040965),                         (40059333, 40059458), (40060066, 40060130)],
    [(40040779, 40040801),  (40041428, 40041493),  (40059336, 40059458),  (40060066, 40060170)]
]
isotools.splice_graph.SpliceGraph(ref).get_alternative_splicing(exons, strand)

exons=[[40040791,                                             40041493],    [40059336, 40059458]]
ref=[
    [                       (40040881, 40040965),                         (40059333,   40059458)],
    [(40040779, 40040801),                         (40041428, 40041493),    (40059336, 40059458)]
]
isotools.splice_graph.SpliceGraph(ref).get_alternative_splicing(exons, strand)

[[(219173843, 219173981),
  (219179146, 219179246),
  (219193081, 219193251),
  (219210531, 219210647),
  (219211491, 219212865)],
 [(219173868, 219173981),
  (219179146, 219179246),
  (219210531, 219210647),
  (219211491, 219212865)],
 [(219173874, 219173981),
  (219179146, 219179246),
  (219193129, 219193251),
  (219210531, 219210647),
  (219211491, 219212865)],
 [(219173875, 219173981),
  (219179146, 219179246),
  (219179380, 219179426),
  (219193081, 219193485)],
 [(219173883, 219173981),
  (219179146, 219179246),
  (219179399, 219179426),
  (219210531, 219210647),
  (219211491, 219212865)],
 [(219173894, 219173981),
  (219179146, 219179246),
  (219179399, 219179426),
  (219193081, 219193251),
  (219210531, 219210647),
  (219211491, 219212865)],
 [(219173895, 219174304),
  (219179146, 219179246),
  (219193081, 219193251),
  (219210531, 219210647),
  (219211491, 219212865)],
 [(219173926, 219173981),
  (219179146, 219179246),
  (219210514, 219210647),
  (219211491, 219212865)],
 [(219174193, 219174304),
  (219179146, 219179246),
  (219210531, 219210647),
  (219211491, 219212865)],
 [(219174970, 219175020),
  (219179146, 219179246),
  (219193081, 219193251),
  (219210531, 219210647),
  (219211491, 219211530)],
 [(219198542, 219198767), (219210531, 219210647), (219211491, 219212865)],
 [(219210341, 219210647), (219211491, 219211827)]]