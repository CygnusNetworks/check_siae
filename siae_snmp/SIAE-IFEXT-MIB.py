# PySNMP SMI module. Autogenerated from smidump -f python SIAE-IFEXT-MIB
# by libsmi2pysnmp-0.1.3 at Tue Apr  9 12:00:21 2019,
# Python version sys.version_info(major=2, minor=7, micro=15, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( AlarmSeverityCode, AlarmStatus, ) = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
( siaeMib, ) = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, RowStatus, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus")

# Objects

ifext = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 73)).setRevisions(("2015-07-21 00:00","2014-12-02 00:00","2014-09-26 00:00","2014-06-05 00:00","2014-02-21 00:00","2013-10-28 00:00",))
if mibBuilder.loadTexts: ifext.setOrganization("SIAE MICROELETTRONICA spa")
if mibBuilder.loadTexts: ifext.setContactInfo("SIAE MICROELETTONICA s.p.a.\nVia Michelangelo Buonarroti, 21\n20093 - Cologno Monzese\nMilano - ITALY\nPhone :  +39-02-27325-1\nE-mail: tbd@siaemic.com")
if mibBuilder.loadTexts: ifext.setDescription("SIAE's Interface Extension MIB.")
ifextMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextMibVersion.setDescription("Numerical version of this module.\nThe string version of this MIB have the following format:\n   XX.YY.ZZ\nso, for example, the value 1 should be interpreted as 00.00.01\nand the value 10001 should be interpreted as 01.00.01.")
ifextTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2))
if mibBuilder.loadTexts: ifextTable.setDescription("Table with SIAE's Interface extension records.")
ifextTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1)).setIndexNames((0, "SIAE-IFEXT-MIB", "ifextIfIndex"))
if mibBuilder.loadTexts: ifextTableEntry.setDescription("SIAE's Interface extension record.")
ifextIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ifextIfIndex.setDescription("A unique value, greater than zero, for each\ninterface. This object is identical to the ifIndex\nof the standard MIB-2 ifTable.")
ifextLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextLabel.setDescription("A textual string containing information about the\ninterface.")
ifextAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(2,4,3,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("loopback", 4), )).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextAdminStatus.setDescription("The desired state of the interface. This object\ncan be set only when the ifMainRowStatus of the\ninterface is active. This object has the semantics\nof the ifAdminStatus of the standard ifTable.\n\nThe testing(3) state indicates that no operational \npackets can be passed - this state is not currently\nsupported. \n\nWhen a managed system initializes, all \ninterfaces start with ifMainAdminStatus in the\ndown(2) state, it's a default state also. As a result\nof either explicit management action or per \nconfiguration information retained by the managed\nsystem, ifMainAdminStatus is then changed to\nthe up (1) state (or remains in the\ndown(2) state).\n\nThis object reflects the value of ifMainAdminStatus")
ifextPortUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,2,6,5,3,4,)).subtype(namedValues=NamedValues(("unused", 0), ("lan", 1), ("radio", 2), ("mgmt", 3), ("stack", 4), ("aux", 5), ("pwe3", 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextPortUsage.setDescription("Port usage in the system. lan(1) and radio(2) are traffic ports,\nmgmt(3) are ports dedicated to management traffic, stack(4) ports\nare port to interconnect switch to stack, aux(5) ports are ports \ndedicated to other purpose, pwe3(6) ports are dedicated to pseudowire.")
ifextMediumType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(4,1,2,3,)).subtype(namedValues=NamedValues(("copper", 1), ("fiber", 2), ("combo", 3), ("other", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextMediumType.setDescription("Physical medium of this interface. Medium type 'combo'\ncan be set as copper or as fiber by ifextMediumSelection.")
ifextMediumSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(1,0,2,)).subtype(namedValues=NamedValues(("none", 0), ("copper", 1), ("fiber", 2), )).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextMediumSelection.setDescription("Selection of physical medium of this interface. Only 'combo' \ninterfaces can be set as copper or as fiber.")
ifextAlarmReportEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("disable", 1), ("enable", 2), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifextAlarmReportEnable.setDescription("On interfaces with ifextPortUsage set to mgmg, this object enables\nor disables collection and report of the alarms.")
ifextSfpId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextSfpId.setDescription("This object specifies a row in sfpTable. This object is 0 if\nthere isn't any SFP connectied to this interface.")
ifextCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 9), Bits().subtype(namedValues=NamedValues(("ifextCapabilityLoop", 0), ("ifextCapability2g5Bps", 1), ("ifextCapabilityMabSensor", 2), ("ifextCapabilityEncrypt", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextCapabilities.setDescription("This indicates which capability is supported from this interface.")
ifextLosAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextLosAlarm.setDescription("Interface Loss of Signal alarm")
ifextRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifextRowStatus.setDescription("Status of this row of ifextTable")
ifextMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 3))
if mibBuilder.loadTexts: ifextMaintTable.setDescription("Table with object used to maintain Interfaces described in \nifextTable")
ifextMaintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 3, 1)).setIndexNames((0, "SIAE-IFEXT-MIB", "ifextIfIndex"))
if mibBuilder.loadTexts: ifextMaintTableEntry.setDescription("SIAE's Interface extension maintenance record.")
ifextLineLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 3, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("disable", 1), ("enable", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifextLineLoop.setDescription("This object is set from admin status of an interface \nto enable/disable line loop.")
ifextLosAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 73, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifextLosAlarmSeverityCode.setDescription("Defines the severity associated to the ifextLosAlarm\nand enables/disables the trap generation on status change event.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("SIAE-IFEXT-MIB", PYSNMP_MODULE_ID=ifext)

# Objects
mibBuilder.exportSymbols("SIAE-IFEXT-MIB", ifext=ifext, ifextMibVersion=ifextMibVersion, ifextTable=ifextTable, ifextTableEntry=ifextTableEntry, ifextIfIndex=ifextIfIndex, ifextLabel=ifextLabel, ifextAdminStatus=ifextAdminStatus, ifextPortUsage=ifextPortUsage, ifextMediumType=ifextMediumType, ifextMediumSelection=ifextMediumSelection, ifextAlarmReportEnable=ifextAlarmReportEnable, ifextSfpId=ifextSfpId, ifextCapabilities=ifextCapabilities, ifextLosAlarm=ifextLosAlarm, ifextRowStatus=ifextRowStatus, ifextMaintTable=ifextMaintTable, ifextMaintTableEntry=ifextMaintTableEntry, ifextLineLoop=ifextLineLoop, ifextLosAlarmSeverityCode=ifextLosAlarmSeverityCode)
