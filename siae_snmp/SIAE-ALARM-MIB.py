# PySNMP SMI module. Autogenerated from smidump -f python SIAE-ALARM-MIB
# by libsmi2pysnmp-0.1.3 at Wed Apr  3 15:06:28 2019,
# Python version sys.version_info(major=2, minor=7, micro=15, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( siaeMib, siaeMicroelettronicaSpa, ) = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib", "siaeMicroelettronicaSpa")
( accessControlLoginIpAddress, ) = mibBuilder.importSymbols("SIAE-USER-MIB", "accessControlLoginIpAddress")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")

# Types

class AlarmSeverityCode(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(6,3,1,4,22,20,19,18,5,2,21,)
    namedValues = NamedValues(("disable", 1), ("statusTrapDisable", 18), ("warningTrapDisable", 19), ("statusTrapEnable", 2), ("minorTrapDisable", 20), ("majorTrapDisable", 21), ("criticalTrapDisable", 22), ("warningTrapEnable", 3), ("minorTrapEnable", 4), ("majorTrapEnable", 5), ("criticalTrapEnable", 6), )
    
class AlarmStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(3,4,2,5,1,6,)
    namedValues = NamedValues(("cleared", 1), ("activeReportableStatus", 2), ("activeReportableWarning", 3), ("activeReportableMinor", 4), ("activeReportableMajor", 5), ("activeReportableCritical", 6), )
    

# Objects

alarmTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 0))
smalarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 4)).setRevisions(("2015-07-17 00:00","2015-03-23 00:00","2015-03-16 00:00","2014-06-23 00:00","2014-03-03 00:00","2014-02-03 00:00","2013-04-16 00:00",))
if mibBuilder.loadTexts: smalarm.setOrganization("SIAE MICROELETTRONICA spa")
if mibBuilder.loadTexts: smalarm.setContactInfo("SIAE MICROELETTONICA s.p.a.\nVia Michelangelo Buonarroti, 21\n20093 - Cologno Monzese\nMilano - ITALY\nPhone :  +39-02-27325-1\nE-mail: help@siaemic.com")
if mibBuilder.loadTexts: smalarm.setDescription("Logger of the transitions of NE alarms and active alarm table.")
alarmMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMibVersion.setDescription("Numerical version of this module.\nThe string version of this MIB have the following format:\n   XX.YY.ZZ\nso, for example, the value 1 should be interpreted as 00.00.01\nand the value 10001 should be interpreted as 01.00.01.")
siaeNotificationEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2))
alarmObjectId = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 1), ObjectIdentifier()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: alarmObjectId.setDescription("OID of the status changed alarm")
alarmObjectVal = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 2), AlarmStatus()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: alarmObjectVal.setDescription("INTEGER value of the status changed alarm")
alarmTrapDescription = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: alarmTrapDescription.setDescription("Optional Description of the notification")
alarmTrapNumber = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTrapNumber.setDescription("Sequential number of trap sent from NE")
alarmIpSnmpAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 5), Unsigned32()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: alarmIpSnmpAgentAddress.setDescription("Reflects the value of equipIpSnmpAgentAddress.")
alarmLogTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3))
if mibBuilder.loadTexts: alarmLogTable.setDescription("Table with Alarm records of the logger.")
alarmLogRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1)).setIndexNames((0, "SIAE-ALARM-MIB", "alarmLogRecordId"))
if mibBuilder.loadTexts: alarmLogRecord.setDescription("Alarm record of the logger.")
alarmLogRecordId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogRecordId.setDescription("This object is used as Index of alarmLogTable.")
alarmLogObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogObjectId.setDescription("The Object Identifier of the Managed Object with\nAlarms or Controls active (not cleared Alarm Status).")
alarmLogObjectVal = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 3), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogObjectVal.setDescription("Alarm Status with associated severity.")
alarmLogObjectSev = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 4), AlarmSeverityCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogObjectSev.setDescription("Severity associated to the Alarm ")
alarmLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogDescription.setDescription("ASCII string used to describe the event.")
alarmLogEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogEventTime.setDescription("The time (in secs) when the event was registered in the Log since\n01-Gen-1970.")
alarmLogActionRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(0,2,1,)).subtype(namedValues=NamedValues(("notActive", 0), ("delete", 1), ("read", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogActionRequest.setDescription("This object is used to delete or to read the LOG using Ftp (file transfer).")
alarmLogFTPfile = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogFTPfile.setDescription("Path and file name used when the log is transferred using Ftp (action = read).")
alarmLogAlarmSeverityEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 6), Integer32().clone(31)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogAlarmSeverityEnable.setDescription("This object enables the event record write in the log according to\nthe severity:\nBit0 = Status\nBit1 = Warning\nBit2 = Minor\nBit3 = Major\nBit4 = Critical.")
alarmLogStartHourEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)).clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogStartHourEnable.setDescription("This object defines whit AlarmLogEndHourEnable the period during\na day when the alarm records must be written in the log.")
alarmLogEndHourEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)).clone(23)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogEndHourEnable.setDescription("This object defines whit AlarmLogStartHourEnable the period during\na day when the alarm records must be written in the log.")
alarmLogStartTimeFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 9), Unsigned32().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogStartTimeFilter.setDescription("The events with EventTime greater than this object are read/delete\nfrom the log. Null value means no filter.")
alarmLogEndTimeFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 10), Unsigned32().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogEndTimeFilter.setDescription("The events with EventTime less than this object are read/delete\nfrom the log. Null value means no filter.")
alarmLogManagedObjectFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 11), ObjectIdentifier().clone((1, 3, 6, 1, 4, 1, 3373))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogManagedObjectFilter.setDescription("The Object Identifier of the Managed Object that has to be\nread/delete from the log. Null value means no filter.")
alarmLogAlarmSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 12), Integer32().clone(31)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogAlarmSeverityFilter.setDescription("This object defines the alarm severity of the records that must\nbe read/delete from the log.\nBit0 = Status\nBit1 = Warning\nBit2 = Minor\nBit3 = Major\nBit4 = Critical.")
alarmLogFTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 14), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,4,)).subtype(namedValues=NamedValues(("transferring", 1), ("completed", 2), ("interrupted", 3), ("empty", 4), )).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogFTPStatus.setDescription("Status of alarm logger Ftp transfer operation.")
alarmLogFTPStatusTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 15), Integer().subtype(subtypeSpec=SingleValueConstraint(1,34,2,)).subtype(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithACK", 34), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogFTPStatusTrapNotification.setDescription("Enables/disables the trap generation on FTP tranfer operation.")
alarmLogLastEventTime = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogLastEventTime.setDescription("It is the Event time of the last alarm inserted into the alarm log.")
alarmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17))
if mibBuilder.loadTexts: alarmActiveTable.setDescription("Table with one record for each Alarms&Controls that is active in\nthe NE.")
alarmActiveRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1)).setIndexNames((0, "SIAE-ALARM-MIB", "alarmActiveObjectId"))
if mibBuilder.loadTexts: alarmActiveRecord.setDescription("Alarms&Controls record.")
alarmActiveObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveObjectId.setDescription("The Object Identifier of the Managed Object with\nAlarms or Controls active (not cleared Alarm Status).")
alarmActiveObjectVal = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 2), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveObjectVal.setDescription("Alarm Status with associated severity.")
alarmActiveDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveDescription.setDescription("ASCII string used to describe the event.")
alarmActiveEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveEventTime.setDescription("The time when the Alarm became active.\nIn seconds since 01/01/70.")
alarmActiveFloodingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("off", 1), ("on", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveFloodingStatus.setDescription("Indicates the 'flooding' status.")
alarmSyntesysCritical = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 18), Integer().subtype(subtypeSpec=SingleValueConstraint(6,1,)).subtype(namedValues=NamedValues(("cleared", 1), ("activeReportableCritical", 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysCritical.setDescription("OR of all Critical Alarms.")
alarmSyntesysCriticalSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 19), Integer().subtype(subtypeSpec=SingleValueConstraint(22,1,6,)).subtype(namedValues=NamedValues(("disable", 1), ("criticalTrapDisable", 22), ("criticalTrapEnable", 6), )).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysCriticalSeverityCode.setDescription("Defines the severity associated to the alarmSyntesysCritical\nand enables/disables the trap generation on status change event.")
alarmSyntesysMajor = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 20), Integer().subtype(subtypeSpec=SingleValueConstraint(5,1,)).subtype(namedValues=NamedValues(("cleared", 1), ("activeReportableMajor", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysMajor.setDescription("OR of all Major Alarms.")
alarmSyntesysMajorSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 21), Integer().subtype(subtypeSpec=SingleValueConstraint(1,5,21,)).subtype(namedValues=NamedValues(("disable", 1), ("majorTrapDisable", 21), ("majorTrapEnable", 5), )).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysMajorSeverityCode.setDescription("Defines the severity associated to alarmSyntesysMajor\nand enables/disables the trap generation on status change event.")
alarmSyntesysMinor = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 22), Integer().subtype(subtypeSpec=SingleValueConstraint(1,4,)).subtype(namedValues=NamedValues(("cleared", 1), ("activeReportableMinor", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysMinor.setDescription("OR of all Minor Alarms.")
alarmSyntesysMinorSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 23), Integer().subtype(subtypeSpec=SingleValueConstraint(4,20,1,)).subtype(namedValues=NamedValues(("disable", 1), ("minorTrapDisable", 20), ("minorTrapEnable", 4), )).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysMinorSeverityCode.setDescription("Defines the severity associated to alarmSyntesysMinor\nand enables/disables the trap generation on status change event.")
alarmSyntesysWarning = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 24), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,)).subtype(namedValues=NamedValues(("cleared", 1), ("activeReportableWarning", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysWarning.setDescription("OR of all Warning Alarms.")
alarmSyntesysWarningSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 25), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,19,)).subtype(namedValues=NamedValues(("disable", 1), ("warningTrapDisable", 19), ("warningTrapEnable", 3), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysWarningSeverityCode.setDescription("Defines the severity associated to alarmSyntesysStatus\nand enables/disables the trap generation on status change event.")
alarmSyntesysStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 26), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("cleared", 1), ("activeReportableStatus", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysStatus.setDescription("OR of all Warning Alarms.")
alarmSyntesysStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 27), Integer().subtype(subtypeSpec=SingleValueConstraint(1,18,2,)).subtype(namedValues=NamedValues(("disable", 1), ("statusTrapDisable", 18), ("statusTrapEnable", 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysStatusSeverityCode.setDescription("Defines the severity associated to alarmSyntesysStatus\nand enables/disables the trap generation on status change event.")
alarmAntiFlooding = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 28), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("disable", 1), ("enable", 2), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAntiFlooding.setDescription("Enables or disables the alarm anti-flooding (filtering)\nalgorithm. According to such algorithm if the number of\nevent notifications that an alarm receives within a\nspecified time period, namely the observation period, exceeds\na given high threshold value, the alarm enters a 'flooding'\nstate. Once an alarm has entered such flooding state,\nits status is forced to active, according to its related\nseverity, and no further event notifications are processed\n(neither trapped nor logged).\nAn alarm exits the flooding state when the number of event\nnotifications, received within a subsequent observation\nperiod, drops below a given low thresold value. On exiting\nthe flooding state, the trap and log status of an alarm get\naligned to the last notified event.")
alarmAntiFloodingWindow = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 120)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAntiFloodingWindow.setDescription("Defines the time duration in seconds of the observation\nperiod, during which the number of event notifications\nof any alarm is checked to determine the alarm flooding\nstate.")
alarmAntiFloodingHighWater = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAntiFloodingHighWater.setDescription("Defines the threshold value of the number of event\nnotifications, occurring during the observation period,\nbeyond which an alarm enters the flooding state.")
alarmAntiFloodingLowWater = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAntiFloodingLowWater.setDescription("Defines the threshold value of the number of event\nnotifications, occurring during the observation period,\nbelow which an alarm exits the flooding state. The value\nbeing assigned to this leaf must be strictly lower than \nthe current value of leaf alarmAntiFloodingHighWater.")
alarmItemTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32))
if mibBuilder.loadTexts: alarmItemTable.setDescription("Table with record of available alarms in the NE.\nThis table reports every created alarm in the NE.")
alarmRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32, 1)).setIndexNames((0, "SIAE-ALARM-MIB", "alarmOid"))
if mibBuilder.loadTexts: alarmRecord.setDescription("Alarm record.")
alarmOid = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmOid.setDescription("The Object Identifier of the Managed Object with\nAlarms or Controls active (not cleared Alarm Status).")
alarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmDescription.setDescription("ASCII string used to describe the alarm.")

# Augmentions

# Notifications

alarmLogFTPStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 401)).setObjects(*(("SIAE-ALARM-MIB", "alarmLogFTPStatus"), ("SIAE-USER-MIB", "accessControlLoginIpAddress"), ("SIAE-ALARM-MIB", "alarmIpSnmpAgentAddress"), ) )
if mibBuilder.loadTexts: alarmLogFTPStatusTrap.setDescription("This event is generated when the status of FTP transfer is changed.\nThe data passed with the event are:\n   1) alarmIpSnmpAgentAddress\n   2) alarmLogFTPStatus\n   3) accessControlLoginIpAddress")
alarmTrapObject = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 3373)).setObjects(*(("SIAE-ALARM-MIB", "alarmObjectId"), ("SIAE-ALARM-MIB", "alarmTrapDescription"), ("SIAE-ALARM-MIB", "alarmTrapNumber"), ("SIAE-ALARM-MIB", "alarmObjectVal"), ("SIAE-ALARM-MIB", "alarmIpSnmpAgentAddress"), ) )
if mibBuilder.loadTexts: alarmTrapObject.setDescription("This event is generated for every changed alarm status. ")

# Exports

# Module identity
mibBuilder.exportSymbols("SIAE-ALARM-MIB", PYSNMP_MODULE_ID=smalarm)

# Types
mibBuilder.exportSymbols("SIAE-ALARM-MIB", AlarmSeverityCode=AlarmSeverityCode, AlarmStatus=AlarmStatus)

# Objects
mibBuilder.exportSymbols("SIAE-ALARM-MIB", alarmTrap=alarmTrap, smalarm=smalarm, alarmMibVersion=alarmMibVersion, siaeNotificationEntry=siaeNotificationEntry, alarmObjectId=alarmObjectId, alarmObjectVal=alarmObjectVal, alarmTrapDescription=alarmTrapDescription, alarmTrapNumber=alarmTrapNumber, alarmIpSnmpAgentAddress=alarmIpSnmpAgentAddress, alarmLogTable=alarmLogTable, alarmLogRecord=alarmLogRecord, alarmLogRecordId=alarmLogRecordId, alarmLogObjectId=alarmLogObjectId, alarmLogObjectVal=alarmLogObjectVal, alarmLogObjectSev=alarmLogObjectSev, alarmLogDescription=alarmLogDescription, alarmLogEventTime=alarmLogEventTime, alarmLogActionRequest=alarmLogActionRequest, alarmLogFTPfile=alarmLogFTPfile, alarmLogAlarmSeverityEnable=alarmLogAlarmSeverityEnable, alarmLogStartHourEnable=alarmLogStartHourEnable, alarmLogEndHourEnable=alarmLogEndHourEnable, alarmLogStartTimeFilter=alarmLogStartTimeFilter, alarmLogEndTimeFilter=alarmLogEndTimeFilter, alarmLogManagedObjectFilter=alarmLogManagedObjectFilter, alarmLogAlarmSeverityFilter=alarmLogAlarmSeverityFilter, alarmLogFTPStatus=alarmLogFTPStatus, alarmLogFTPStatusTrapNotification=alarmLogFTPStatusTrapNotification, alarmLogLastEventTime=alarmLogLastEventTime, alarmActiveTable=alarmActiveTable, alarmActiveRecord=alarmActiveRecord, alarmActiveObjectId=alarmActiveObjectId, alarmActiveObjectVal=alarmActiveObjectVal, alarmActiveDescription=alarmActiveDescription, alarmActiveEventTime=alarmActiveEventTime, alarmActiveFloodingStatus=alarmActiveFloodingStatus, alarmSyntesysCritical=alarmSyntesysCritical, alarmSyntesysCriticalSeverityCode=alarmSyntesysCriticalSeverityCode, alarmSyntesysMajor=alarmSyntesysMajor, alarmSyntesysMajorSeverityCode=alarmSyntesysMajorSeverityCode, alarmSyntesysMinor=alarmSyntesysMinor, alarmSyntesysMinorSeverityCode=alarmSyntesysMinorSeverityCode, alarmSyntesysWarning=alarmSyntesysWarning, alarmSyntesysWarningSeverityCode=alarmSyntesysWarningSeverityCode, alarmSyntesysStatus=alarmSyntesysStatus, alarmSyntesysStatusSeverityCode=alarmSyntesysStatusSeverityCode, alarmAntiFlooding=alarmAntiFlooding, alarmAntiFloodingWindow=alarmAntiFloodingWindow, alarmAntiFloodingHighWater=alarmAntiFloodingHighWater, alarmAntiFloodingLowWater=alarmAntiFloodingLowWater, alarmItemTable=alarmItemTable, alarmRecord=alarmRecord, alarmOid=alarmOid, alarmDescription=alarmDescription)

# Notifications
mibBuilder.exportSymbols("SIAE-ALARM-MIB", alarmLogFTPStatusTrap=alarmLogFTPStatusTrap, alarmTrapObject=alarmTrapObject)
