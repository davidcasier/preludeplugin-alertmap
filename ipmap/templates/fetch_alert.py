import preludedb
import GeoIP
from math import *
from decimal import Decimal

db = preludedb.DB(preludedb.SQL("type=mysql host=localhost name=prelude user=preludeuser pass=prelude"))

def geoip_lat_lon(ip):
    """
    This function uses the MaxMind library and databases to geolocate IP addresses
    Returns two lists (latitude and longitude).
    
    """
    gi = GeoIP.open("/usr/lib/python2.6/site-packages/prewikka/plugins/PluginMap/ipmap/htdocs/txt/GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)
    latlon = []

    if ip is not None:
        r = gi.record_by_addr(ip)
        if r is not None:
            latlon.append(int((r['latitude']*100)+0.5)/100.0)
            latlon.append(int((r['longitude']*100)+0.5)/100.0)
            latlon.append(r['country_name'])
            latlon.append(r['country_code'])
    return latlon


def query_alert (alert_list):
    i= len(alert_list)
    list_ip = []
    results = db.getValues(["alert.source.node.address.address","alert.Classification.text","alert.assessment.impact.severity"], criteria="alert.source.node.address.address != NULL",offset = i)
    for row in results:
        loca = geoip_lat_lon(row[0])
        lat=''
        lng=''
        if loca:
            lat = loca[0]
            lng = loca[1]
            country = loca[2]
            country_code = loca[3]
            if (lat,lng) not in list_ip:
                alert_list.append([row[0],[row[1]],row[2],lat,lng,country,country_code,1])
                list_ip.append((lat,lng))
            else:
                for j in alert_list:
                    if j[3] == lat and j[4] == lng:
                        j[1].append(row[1])
                        if (j[2] == 'low' and row[2]!='low') or (j[2] == 'medium' and row[2]=='high'):
                            j[2] = row[2]
                        if row[2] == 'medium':
                            j[7]=j[7]+1
                        elif row[2] == 'high':
                            j[7]=j[7]+2
    return alert_list
       


def alert_type_list(list_type):
    nb =[]
    ret=[]
    for el in list_type:
        found=0
        for i in range(0, len(ret)):
            if ret[i] == el:
                nb[i]=nb[i]+1
                found=1
        if found == 0:
            ret.append(el)
            nb.append(1)
    str_ret = ret[0]
    if nb[0]!= 1:
        str_ret = str_ret+"(x"+str(nb[0])+")"
    for j in range(1,len(ret)):
        str_ret = str_ret+", "+ ret[j]
        if nb[j]!= 1:
            str_ret = str_ret+"(x"+str(nb[j])+")"
    return str_ret




def country_list(alert_list):
    ret = []
    for alert in alert_list:
        if alert[6] not in ret:
            ret.append(alert[6])
    return ret

def country_name_list(alert_list):
    ret = []
    for alert in alert_list:
        if alert[5] not in ret:
            ret.append(alert[5])
    return ret
