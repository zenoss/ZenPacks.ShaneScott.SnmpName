import re
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, MultiArgs

class SnmpName(SnmpPlugin):

    maptype = "SnmpName"

    snmpGetMap = GetMap({
        '.1.3.6.1.2.1.1.5.0': 'setTitle',
         })


    def process(self, device, results, log):
        """collect snmp name information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        om = self.objectMap(getdata)
        if om.setTitle:
           log.info('snmpSysName %s found', om.setTitle)
           om.setTitle = om.setTitle

        return om
