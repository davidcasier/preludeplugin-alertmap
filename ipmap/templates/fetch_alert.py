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
    #print "Debut du Fetch"
    i= len(alert_list)
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
        alert_list.append([row[0],row[1],row[2],lat,lng,country,country_code])
        i = i +1
    #print "Fin du Fetch"
    return alert_list
       

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
