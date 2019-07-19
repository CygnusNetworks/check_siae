#
# PySNMP MIB module SIAE-UNIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./sm_unit.mib
# Produced by pysmi-0.3.2 at Fri Jul 19 08:22:05 2019
# On host 0e190c6811ee platform Linux version 4.9.125-linuxkit by user root
# Using Python version 3.7.3 (default, Apr  3 2019, 05:39:12) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
unitTypeUnequipped, = mibBuilder.importSymbols("SIAE-UNITYPE-MIB", "unitTypeUnequipped")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, Gauge32, IpAddress, ObjectIdentity, ModuleIdentity, TimeTicks, iso, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Gauge32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "iso", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Unsigned32")
AutonomousType, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "DisplayString", "RowStatus")
unit = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6))
unit.setRevisions(('2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: unit.setLastUpdated('201402030000Z')
if mibBuilder.loadTexts: unit.setOrganization('SIAE MICROELETTRONICA spa')
unitMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitMibVersion.setStatus('current')
unitTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2), )
if mibBuilder.loadTexts: unitTable.setStatus('current')
unitRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1), ).setIndexNames((0, "SIAE-UNIT-MIB", "unitId"))
if mibBuilder.loadTexts: unitRecord.setStatus('current')
unitId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitId.setStatus('current')
unitExpectedType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 2), AutonomousType().clone((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitExpectedType.setStatus('current')
unitActualType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 3), AutonomousType().clone((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitActualType.setStatus('current')
unitLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitLabel.setStatus('current')
unitFailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 5), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitFailAlarm.setStatus('current')
unitMissingAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 6), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitMissingAlarm.setStatus('current')
unitNotRespondingAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 7), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitNotRespondingAlarm.setStatus('current')
unitHwMismatchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 8), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitHwMismatchAlarm.setStatus('current')
unitSwMismatchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 9), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitSwMismatchAlarm.setStatus('current')
unitHwEdition = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitHwEdition.setStatus('current')
unitPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitPartNumber.setStatus('current')
unitParentPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitParentPartNumber.setStatus('current')
unitParentSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitParentSerialNumber.setStatus('current')
unitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitRowStatus.setStatus('current')
unitFailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 4), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitFailAlarmSeverityCode.setStatus('current')
unitMissingAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitMissingAlarmSeverityCode.setStatus('current')
unitNotRespondingAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitNotRespondingAlarmSeverityCode.setStatus('current')
unitHwMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitHwMismatchAlarmSeverityCode.setStatus('current')
unitSwMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitSwMismatchAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-UNIT-MIB", unitId=unitId, unitRowStatus=unitRowStatus, unitParentPartNumber=unitParentPartNumber, unitSwMismatchAlarm=unitSwMismatchAlarm, unitParentSerialNumber=unitParentSerialNumber, unitHwMismatchAlarmSeverityCode=unitHwMismatchAlarmSeverityCode, unitRecord=unitRecord, unitSwMismatchAlarmSeverityCode=unitSwMismatchAlarmSeverityCode, PYSNMP_MODULE_ID=unit, unitExpectedType=unitExpectedType, unitHwMismatchAlarm=unitHwMismatchAlarm, unit=unit, unitLabel=unitLabel, unitActualType=unitActualType, unitMissingAlarm=unitMissingAlarm, unitPartNumber=unitPartNumber, unitHwEdition=unitHwEdition, unitFailAlarmSeverityCode=unitFailAlarmSeverityCode, unitTable=unitTable, unitFailAlarm=unitFailAlarm, unitNotRespondingAlarm=unitNotRespondingAlarm, unitMibVersion=unitMibVersion, unitNotRespondingAlarmSeverityCode=unitNotRespondingAlarmSeverityCode, unitMissingAlarmSeverityCode=unitMissingAlarmSeverityCode)
