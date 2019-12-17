from IPython.display import HTML
import pandas as pd
import numpy as np
###
#Just some styling code for Tables, don't worry about this!
###
def hover(hover_color="#ffff99"):
    return dict(selector="tr:hover",
                props=[("background-color", "%s" % hover_color)])

styles = [
    hover(),
    dict(selector="th", props=[("font-size", "130%"),
                               ("text-align", "center"),("text-align", "center")]),
    dict(selector="caption", props=[("caption-side", "top"),("font-size", "150%")])
]
###
#
###

class cluster:
    def __init__(self, name, RA, DEC, dist):
    	self.name = name
        self.RA_HMS = RA #RA  in 'Hours Minutes Seconds'
        self.DEC_DMS = DEC #DEC in DMS
	self.dist = dist
    def get_RA_deg(self):
        #Convert RA from HMS to decimal degrees
        rs = 1
        H, M, S = [float(i) for i in self.RA_HMS.split()]
        if str(H)[0] == '-':
          rs, H = -1, abs(H)
        deg = (H*15) + (M/4) + (S/240)
        RA = '{0}'.format(deg*rs)
        return float(RA)
    
    def get_DEC_deg(self):
        #Convert DEC from DMS to decimal degrees
        ds = 1
        D, M, S = [float(i) for i in self.DEC_DMS.split()]
        if str(D)[0] == '-':
          ds, D = -1, abs(D)
        deg = D + (M/60) + (S/3600)
        DEC = '{0}'.format(deg*ds)
        return float(DEC)
    
    def get_position_degrees(self, dict = False):
        return self.get_RA_deg(), self.get_DEC_deg()
    
# All open Clusters
NGC_3293 = cluster('NGC 3293','10 35 49', '-58 13 48', 2750)
M_11 = cluster('M 11', '18 51 05', '-06 16 12', 1900)
M_26 = cluster('M 26', '18 45 18', '-09 23 00', 1533)
M_35 = cluster('M 35', '06 08 54', '+24 20 00', 858)
M_44 = cluster('M 44', '08 40 24', '+19 40 00', 177)
M_45 = cluster('M 45', '03 47 00', '+24 07 00', 135)
M_46 = cluster('M 46', '07 41 46', '-14 48 36', 1656)

open_clusters = [NGC_3293, M_11, M_26, M_35, M_44, M_45, M_46]

# All Globular Clusters
_47_Tuc = cluster('47 Tuc', '00 24 05.4', '-72 04 53.2', 4001)
M_2 = cluster('M 2', '21 33 27.0', '-00 49 23.7', 16863)
M_3 = cluster('M 3', '13 42 11.6', '+28 22 38.2', 10400)
M_5 = cluster('M 5', '15 18 33.2', '+02 04 51.7', 7499)
M_13 = cluster('M 13', '16 41 41.6', '+36 27 40.8', 6800)
M_14 = cluster('M 14', '17 37 36.2', '-03 14 45.3', 9290)
M_30 = cluster('M 30', '21 40 22.1', '-23 10 47.5', 8300)

globular_clusters = [_47_Tuc, M_2, M_3, M_5, M_13, M_14, M_30]


open_data = {'Name':[open_clusters[i].name for i in range(len(open_clusters))],'Distance (pc)':[open_clusters[i].dist for i in range(len(open_clusters))],'DEC (DEG)':[open_clusters[i].get_DEC_deg() for i in range(len(open_clusters))],'RA (DEG)':[open_clusters[i].get_RA_deg() for i in range(len(open_clusters))], 'RA (J2000)':[open_clusters[i].RA_HMS for i in range(len(open_clusters))], 'DEC (J2000)':[open_clusters[i].DEC_DMS for i in range(len(open_clusters))]}
open_df = pd.DataFrame(data = open_data, columns = ['Name', 'RA (J2000)', 'DEC (J2000)', 'RA (DEG)', 'DEC (DEG)', 'Distance (pc)' ])

open_cluster_out = (open_df.style.set_table_styles(styles)
          .set_caption("Open Clusters."))

globular_data = {'Name':[globular_clusters[i].name for i in range(len(globular_clusters))],'Distance (pc)':[globular_clusters[i].dist for i in range(len(globular_clusters))],'DEC (DEG)':[globular_clusters[i].get_DEC_deg() for i in range(len(globular_clusters))],'RA (DEG)':[globular_clusters[i].get_RA_deg() for i in range(len(globular_clusters))], 'RA (J2000)':[globular_clusters[i].RA_HMS for i in range(len(globular_clusters))], 'DEC (J2000)':[globular_clusters[i].DEC_DMS for i in range(len(globular_clusters))]}
globular_df = pd.DataFrame(data = globular_data, columns = ['Name', 'RA (J2000)', 'DEC (J2000)', 'RA (DEG)', 'DEC (DEG)', 'Distance (pc)' ])
globular_cluster_out = (globular_df.style.set_table_styles(styles)
          .set_caption("Globular Clusters."))
