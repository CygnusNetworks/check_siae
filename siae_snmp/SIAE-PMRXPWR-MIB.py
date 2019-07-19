#
# PySNMP MIB module SIAE-PMRXPWR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./sm_pmrxpwr.mib
# Produced by pysmi-0.3.2 at Fri Jul 19 08:21:48 2019
# On host 0e190c6811ee platform Linux version 4.9.125-linuxkit by user root
# Using Python version 3.7.3 (default, Apr  3 2019, 05:39:12) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, NotificationType, Counter32, Unsigned32, IpAddress, ModuleIdentity, Counter64, Gauge32, MibIdentifier, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "NotificationType", "Counter32", "Unsigned32", "IpAddress", "ModuleIdentity", "Counter64", "Gauge32", "MibIdentifier", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
pmRxPwr = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 12))
pmRxPwr.setRevisions(('2014-10-07 00:00', '2014-05-13 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: pmRxPwr.setLastUpdated('201410070000Z')
if mibBuilder.loadTexts: pmRxPwr.setOrganization('SIAE MICROELETTRONICA spa')
pmRxPwrMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrMibVersion.setStatus('current')
pmRxPwrCounterTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2), )
if mibBuilder.loadTexts: pmRxPwrCounterTable.setStatus('current')
pmRxPwrCounterRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1), ).setIndexNames((0, "SIAE-PMRXPWR-MIB", "pmRxPwrBranchId"), (0, "SIAE-PMRXPWR-MIB", "pmRxPwrCounterBlockId"))
if mibBuilder.loadTexts: pmRxPwrCounterRecord.setStatus('current')
pmRxPwrBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrBranchId.setStatus('current')
pmRxPwrCounterBlockId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrCounterBlockId.setStatus('current')
pmRxPwrCounterBlockType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("daily", 1), ("fifteenMin", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrCounterBlockType.setStatus('current')
pmRxPwrCounterBlockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("meaningless", 1), ("meaningfull", 2), ("incomplete", 3), ("dummy", 4), ("lost", 5), ("restarted", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrCounterBlockStatus.setStatus('current')
pmRxPwrCounterTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrCounterTimeStamp.setStatus('current')
pmRxPwrRlts1Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts1Counter.setStatus('current')
pmRxPwrRlts2Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts2Counter.setStatus('current')
pmRxPwrRlts3Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts3Counter.setStatus('current')
pmRxPwrRlts4Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts4Counter.setStatus('current')
pmRxPwrRlts5Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts5Counter.setStatus('current')
pmRxPwrTMMax = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTMMax.setStatus('current')
pmRxPwrTMMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTMMin.setStatus('current')
pmRxPwrAverageRxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrAverageRxLevel.setStatus('current')
pmRxPwrTpClassTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3), )
if mibBuilder.loadTexts: pmRxPwrTpClassTable.setStatus('current')
pmRxPwrTpClassRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1), ).setIndexNames((0, "SIAE-PMRXPWR-MIB", "pmRxPwrTpClassBranchId"))
if mibBuilder.loadTexts: pmRxPwrTpClassRecord.setStatus('current')
pmRxPwrTpClassBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClassBranchId.setStatus('current')
pmRxPwrTpClassStartStop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassStartStop.setStatus('current')
pmRxPwrTpClassLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClassLabel.setStatus('current')
pmRxPwrTpClassTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClassTimeStamp.setStatus('current')
pmRxPwrTpClass15MRlts1Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts1Alarm.setStatus('current')
pmRxPwrTpClass15MRlts2Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts2Alarm.setStatus('current')
pmRxPwrTpClass15MRlts3Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts3Alarm.setStatus('current')
pmRxPwrTpClass15MRlts4Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts4Alarm.setStatus('current')
pmRxPwrTpClass15MRlts5Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts5Alarm.setStatus('current')
pmRxPwrTpClass24HRlts1Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts1Alarm.setStatus('current')
pmRxPwrTpClass24HRlts2Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 11), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts2Alarm.setStatus('current')
pmRxPwrTpClass24HRlts3Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 12), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts3Alarm.setStatus('current')
pmRxPwrTpClass24HRlts4Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 13), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts4Alarm.setStatus('current')
pmRxPwrTpClass24HRlts5Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 14), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts5Alarm.setStatus('current')
pmRxPwrTpClassRlt1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-40)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt1Threshold.setStatus('current')
pmRxPwrTpClassRlt2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt2Threshold.setStatus('current')
pmRxPwrTpClassRlt3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt3Threshold.setStatus('current')
pmRxPwrTpClassRlt4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-70)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt4Threshold.setStatus('current')
pmRxPwrTpClassRlt5Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-80)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt5Threshold.setStatus('current')
pmRxPwrTpClass15MRlts1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 20), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts1Threshold.setStatus('current')
pmRxPwrTpClass15MRlts2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 21), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts2Threshold.setStatus('current')
pmRxPwrTpClass15MRlts3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 22), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts3Threshold.setStatus('current')
pmRxPwrTpClass15MRlts4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 23), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts4Threshold.setStatus('current')
pmRxPwrTpClass15MRlts5Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 24), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts5Threshold.setStatus('current')
pmRxPwrTpClass24HRlts1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 25), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts1Threshold.setStatus('current')
pmRxPwrTpClass24HRlts2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 26), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts2Threshold.setStatus('current')
pmRxPwrTpClass24HRlts3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 27), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts3Threshold.setStatus('current')
pmRxPwrTpClass24HRlts4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 28), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts4Threshold.setStatus('current')
pmRxPwrTpClass24HRlts5Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 29), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts5Threshold.setStatus('current')
pmRxPwrTpClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 30), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRowStatus.setStatus('current')
pmRxPwrTpMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4), )
if mibBuilder.loadTexts: pmRxPwrTpMaintTable.setStatus('current')
pmRxPwrTpMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4, 1), ).setIndexNames((0, "SIAE-PMRXPWR-MIB", "pmRxPwrTpClassBranchId"))
if mibBuilder.loadTexts: pmRxPwrTpMaintRecord.setStatus('current')
pmRxPwrTpMaintCounterClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmRxPwrTpMaintCounterClear.setStatus('current')
pmRxPwrTpMaintAlarmClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmRxPwrTpMaintAlarmClear.setStatus('current')
pmRxPwrTpClass15MRltsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRltsAlarmSeverityCode.setStatus('current')
pmRxPwrTpClass24HRltsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRltsAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-PMRXPWR-MIB", pmRxPwrTpClass15MRlts3Alarm=pmRxPwrTpClass15MRlts3Alarm, pmRxPwrTpClassRecord=pmRxPwrTpClassRecord, pmRxPwrTpClass24HRlts2Alarm=pmRxPwrTpClass24HRlts2Alarm, pmRxPwrTMMin=pmRxPwrTMMin, pmRxPwrRlts3Counter=pmRxPwrRlts3Counter, pmRxPwrMibVersion=pmRxPwrMibVersion, pmRxPwrTpMaintAlarmClear=pmRxPwrTpMaintAlarmClear, pmRxPwrTpClass24HRlts1Threshold=pmRxPwrTpClass24HRlts1Threshold, pmRxPwrTpClassStartStop=pmRxPwrTpClassStartStop, pmRxPwrTpClass24HRlts5Alarm=pmRxPwrTpClass24HRlts5Alarm, pmRxPwrTpClass24HRlts5Threshold=pmRxPwrTpClass24HRlts5Threshold, pmRxPwrTpMaintRecord=pmRxPwrTpMaintRecord, pmRxPwrTpClassRlt1Threshold=pmRxPwrTpClassRlt1Threshold, pmRxPwrTpClass24HRltsAlarmSeverityCode=pmRxPwrTpClass24HRltsAlarmSeverityCode, pmRxPwrTpClassRlt5Threshold=pmRxPwrTpClassRlt5Threshold, pmRxPwr=pmRxPwr, pmRxPwrTpClassBranchId=pmRxPwrTpClassBranchId, pmRxPwrTpClass24HRlts3Alarm=pmRxPwrTpClass24HRlts3Alarm, pmRxPwrTpClass15MRlts1Alarm=pmRxPwrTpClass15MRlts1Alarm, pmRxPwrTpClassRlt3Threshold=pmRxPwrTpClassRlt3Threshold, pmRxPwrTpClass15MRlts4Threshold=pmRxPwrTpClass15MRlts4Threshold, pmRxPwrTpClass15MRlts4Alarm=pmRxPwrTpClass15MRlts4Alarm, pmRxPwrTpClass15MRlts1Threshold=pmRxPwrTpClass15MRlts1Threshold, pmRxPwrCounterTimeStamp=pmRxPwrCounterTimeStamp, pmRxPwrRlts2Counter=pmRxPwrRlts2Counter, pmRxPwrRlts5Counter=pmRxPwrRlts5Counter, pmRxPwrTpClassRowStatus=pmRxPwrTpClassRowStatus, pmRxPwrTpClass15MRltsAlarmSeverityCode=pmRxPwrTpClass15MRltsAlarmSeverityCode, pmRxPwrCounterBlockStatus=pmRxPwrCounterBlockStatus, pmRxPwrCounterBlockType=pmRxPwrCounterBlockType, pmRxPwrTpClass24HRlts1Alarm=pmRxPwrTpClass24HRlts1Alarm, pmRxPwrTpClass24HRlts4Threshold=pmRxPwrTpClass24HRlts4Threshold, pmRxPwrBranchId=pmRxPwrBranchId, PYSNMP_MODULE_ID=pmRxPwr, pmRxPwrTpClass15MRlts3Threshold=pmRxPwrTpClass15MRlts3Threshold, pmRxPwrRlts1Counter=pmRxPwrRlts1Counter, pmRxPwrTpMaintTable=pmRxPwrTpMaintTable, pmRxPwrTpClass15MRlts2Alarm=pmRxPwrTpClass15MRlts2Alarm, pmRxPwrTMMax=pmRxPwrTMMax, pmRxPwrTpClass15MRlts2Threshold=pmRxPwrTpClass15MRlts2Threshold, pmRxPwrTpClass15MRlts5Threshold=pmRxPwrTpClass15MRlts5Threshold, pmRxPwrTpClass24HRlts4Alarm=pmRxPwrTpClass24HRlts4Alarm, pmRxPwrTpClass24HRlts2Threshold=pmRxPwrTpClass24HRlts2Threshold, pmRxPwrRlts4Counter=pmRxPwrRlts4Counter, pmRxPwrTpClassRlt2Threshold=pmRxPwrTpClassRlt2Threshold, pmRxPwrTpMaintCounterClear=pmRxPwrTpMaintCounterClear, pmRxPwrTpClass24HRlts3Threshold=pmRxPwrTpClass24HRlts3Threshold, pmRxPwrTpClass15MRlts5Alarm=pmRxPwrTpClass15MRlts5Alarm, pmRxPwrAverageRxLevel=pmRxPwrAverageRxLevel, pmRxPwrTpClassTable=pmRxPwrTpClassTable, pmRxPwrCounterRecord=pmRxPwrCounterRecord, pmRxPwrCounterTable=pmRxPwrCounterTable, pmRxPwrTpClassRlt4Threshold=pmRxPwrTpClassRlt4Threshold, pmRxPwrTpClassLabel=pmRxPwrTpClassLabel, pmRxPwrCounterBlockId=pmRxPwrCounterBlockId, pmRxPwrTpClassTimeStamp=pmRxPwrTpClassTimeStamp)
