#
# PySNMP MIB module SIAE-UNITYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./sm_unitype.mib
# Produced by pysmi-0.3.2 at Fri Jul 19 08:22:05 2019
# On host 0e190c6811ee platform Linux version 4.9.125-linuxkit by user root
# Using Python version 3.7.3 (default, Apr  3 2019, 05:39:12) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, Gauge32, IpAddress, ObjectIdentity, ModuleIdentity, TimeTicks, iso, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Gauge32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "iso", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
unitTypeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 506))
unitTypeMib.setRevisions(('2015-03-04 00:00', '2014-12-01 00:00', '2014-03-19 00:00', '2014-02-07 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: unitTypeMib.setLastUpdated('201503040000Z')
if mibBuilder.loadTexts: unitTypeMib.setOrganization('SIAE MICROELETTRONICA spa')
unitType = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3))
unitTypeUnequipped = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1))
if mibBuilder.loadTexts: unitTypeUnequipped.setStatus('current')
unitTypeODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 5))
if mibBuilder.loadTexts: unitTypeODU.setStatus('current')
unitTypeALFO80HD = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 200))
if mibBuilder.loadTexts: unitTypeALFO80HD.setStatus('current')
unitTypeALFO80HDelectrical = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 201))
if mibBuilder.loadTexts: unitTypeALFO80HDelectrical.setStatus('current')
unitTypeALFO80HDelectricalOptical = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 202))
if mibBuilder.loadTexts: unitTypeALFO80HDelectricalOptical.setStatus('current')
unitTypeALFO80HDoptical = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 203))
if mibBuilder.loadTexts: unitTypeALFO80HDoptical.setStatus('current')
unitTypeAGS20ARI1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 210))
if mibBuilder.loadTexts: unitTypeAGS20ARI1.setStatus('current')
unitTypeAGS20ARI2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 211))
if mibBuilder.loadTexts: unitTypeAGS20ARI2.setStatus('current')
unitTypeAGS20ARI4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 212))
if mibBuilder.loadTexts: unitTypeAGS20ARI4.setStatus('current')
unitTypeAGS20DRI4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 213))
if mibBuilder.loadTexts: unitTypeAGS20DRI4.setStatus('current')
unitTypeAGS20ARI1TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 214))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2.setStatus('current')
unitTypeAGS20ARI1TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 215))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3.setStatus('current')
unitTypeAGS20ARI2TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 216))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM2.setStatus('current')
unitTypeAGS20ARI2TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 217))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM3.setStatus('current')
unitTypeAGS20ARI4TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 218))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM2.setStatus('current')
unitTypeAGS20ARI4TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 219))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM3.setStatus('current')
unitTypeAGS20DRI4TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 220))
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM2.setStatus('current')
unitTypeAGS20DRI4TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 221))
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM3.setStatus('current')
unitTypeAGS20CORE = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 222))
if mibBuilder.loadTexts: unitTypeAGS20CORE.setStatus('current')
unitTypeAGS20ARI1DP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 223))
if mibBuilder.loadTexts: unitTypeAGS20ARI1DP.setStatus('current')
unitTypeAGS20ARI1TDM2DP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 224))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2DP.setStatus('current')
unitTypeAGS20ARI1TDM3DP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 225))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3DP.setStatus('current')
unitTypeALFOplus2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 230))
if mibBuilder.loadTexts: unitTypeALFOplus2.setStatus('current')
unitTypeAGS20ODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 231))
if mibBuilder.loadTexts: unitTypeAGS20ODU.setStatus('current')
mibBuilder.exportSymbols("SIAE-UNITYPE-MIB", unitTypeALFO80HDelectrical=unitTypeALFO80HDelectrical, unitTypeAGS20ARI1TDM2=unitTypeAGS20ARI1TDM2, unitTypeAGS20ARI4=unitTypeAGS20ARI4, unitTypeAGS20DRI4TDM3=unitTypeAGS20DRI4TDM3, unitTypeAGS20ARI2TDM3=unitTypeAGS20ARI2TDM3, PYSNMP_MODULE_ID=unitTypeMib, unitTypeAGS20ARI2=unitTypeAGS20ARI2, unitTypeMib=unitTypeMib, unitTypeALFO80HD=unitTypeALFO80HD, unitTypeALFOplus2=unitTypeALFOplus2, unitTypeAGS20DRI4TDM2=unitTypeAGS20DRI4TDM2, unitTypeAGS20ODU=unitTypeAGS20ODU, unitTypeAGS20ARI1=unitTypeAGS20ARI1, unitType=unitType, unitTypeAGS20ARI4TDM3=unitTypeAGS20ARI4TDM3, unitTypeAGS20DRI4=unitTypeAGS20DRI4, unitTypeAGS20ARI1DP=unitTypeAGS20ARI1DP, unitTypeAGS20ARI1TDM2DP=unitTypeAGS20ARI1TDM2DP, unitTypeAGS20ARI1TDM3=unitTypeAGS20ARI1TDM3, unitTypeAGS20ARI2TDM2=unitTypeAGS20ARI2TDM2, unitTypeODU=unitTypeODU, unitTypeALFO80HDelectricalOptical=unitTypeALFO80HDelectricalOptical, unitTypeAGS20ARI4TDM2=unitTypeAGS20ARI4TDM2, unitTypeUnequipped=unitTypeUnequipped, unitTypeAGS20ARI1TDM3DP=unitTypeAGS20ARI1TDM3DP, unitTypeALFO80HDoptical=unitTypeALFO80HDoptical, unitTypeAGS20CORE=unitTypeAGS20CORE)
