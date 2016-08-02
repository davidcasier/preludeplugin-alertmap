from prewikka import database, view, pluginmanager, env
from pkg_resources import resource_filename
import fetch_alert
from . import templates
import os


class AlertsDatabase(database.DatabaseHelper):
    """Handle database queries related to the alerts""" 

    
    def empty_db(self):
        print "DROP THE DATABASE"
        self.query("DELETE FROM Alerts")

    
    def get_db(self):
        return self.query("SELECT * FROM Alerts")


    def write_db(self,alrts):
        tmp_alerts = open('/usr/lib/python2.6/site-packages/prewikka/plugins/PluginMap/ipmap/htdocs/txt/alrt.txt','w')
        start= 1
        for row in alrts:
            if row[3]:
                str_type = fetch_alert.alert_type_list(row[2])
                if start:
                    tmp_alerts.write(row[4]+","+row[5]+"?"+str_type+"?"+row[8])
                    start =0
                else:
                    tmp_alerts.write("\n"+row[4]+","+row[5]+"?"+str_type+"?"+row[8])
        tmp_alerts.close()


    def get_alert(self,lat,lng):
         search_query = "SELECT * FROM Alerts WHERE lat =%(lat)s AND lng =%(lng)s"%{"lat":self.escape(lat), "lng":self.escape(lng)}
         return self.query(search_query)


    def update_alert(self,old_alrt,new_alrt):
        if new_alrt[2]=='high':
            sev = 2
            old_alrt[2] ='high'
        elif new_alrt[2] =='medium':
            sev = 1
            if old_alrt[2] =='low':
                old_alrt[2] = 'medium'
        else:
            sev = 0
        
        old_alrt[1] += ","+new_alrt[1]
        old_alrt[7] += sev
        self.query("UPDATE Alerts "
        "SET name = %(name)s "
        "severity = %(severity)s "
        "count_severity = %(count_sev)s "
        "WHERE lat  = %(lat)s AND lng = %(lng)s" %{"name":self.escape(old_alrt[1]),
                                                   "severity":self.escape(old_alrt[2]),
                                                   "count_sev":self.escape(old_alrt[7]),
                                                   "lat":self.escape(old_alrt[3]),
                                                   "lng":self.escape(old_alrt[4])})


    def add_alert(self,alert):
  
        list_ip = fetch_alert.ip_list(alert[0])
        #print list_ip
        self.query("INSERT INTO Alerts (address,name,severity,lat,lng,country,code_country,count_severity) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"%(
                self.escape(list_ip),
                self.escape(alert[1]),
                self.escape(alert[2]),
                self.escape(alert[3]),
                self.escape(alert[4]),
                self.escape(alert[5]),
                self.escape(alert[6]),
                self.escape(alert[7])
                ))


class IpMapParameters(view.Parameters):

    def register(self):
        pluginmanager.PluginBase.__init__(self)


class IpMap(view.View): 
    plugin_name = "IpMap" 
    plugin_description = "A plugin that display an IpMap" 
    plugin_version = "1.0.0" 
    plugin_database_version = "0"
    view_name = "IpMap" 
    view_section = "IpMap"
    view_template = templates.ipmap
    view_parameters = IpMapParameters

    def __init__(self):
        view.View.__init__(self)
        self._db = AlertsDatabase()
        self._db.empty_db()


    plugin_htdocs = (("ipmap", resource_filename(__name__, "htdocs")),)


    def render(self):
        self._db.empty_db()
        alerts = []
        get_res = []
        alerts_to_send = []
        i= 0
        j= 0
        alerts = fetch_alert.query_alert(i, 400)
        for row in alerts:
            get_res = self._db.get_alert(row[3],row[4])
            if get_res:
                self._db.update_alert(get_res,row)
            else:
                self._db.add_alert(row)
            alerts_to_send.append(row)
            alerts_to_send[j][1] = fetch_alert.alert_type_list(alerts_to_send[j][1])
            alerts_to_send[j][0] = fetch_alert.ip_list(alerts_to_send[j][0])
            j+=1
            
        alerts = self._db.get_db()
        self._db.write_db(alerts)
        

        params = self.parameters
        self.dataset["country_list"] = fetch_alert.country_name_list(alerts)
        self.dataset["country_codes"] = fetch_alert.country_list(alerts)
        self.dataset["alert_list"] = alerts_to_send
 
