# PySNMP SMI module. Autogenerated from smidump -f python SIAE-UNIT-MIB
# by libsmi2pysnmp-0.1.3 at Mon Apr  8 13:31:53 2019,
# Python version sys.version_info(major=2, minor=7, micro=15, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( AlarmSeverityCode, AlarmStatus, ) = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
( siaeMib, ) = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
( unitTypeUnequipped, ) = mibBuilder.importSymbols("SIAE-UNITYPE-MIB", "unitTypeUnequipped")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( AutonomousType, DisplayString, RowStatus, ) = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DisplayString", "RowStatus")

# Objects

unit = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6)).setRevisions(("2014-02-03 00:00","2013-04-16 00:00",))
if mibBuilder.loadTexts: unit.setOrganization("SIAE MICROELETTRONICA spa")
if mibBuilder.loadTexts: unit.setContactInfo("SIAE MICROELETTONICA s.p.a.\nVia Michelangelo Buonarroti, 21\n20093 - Cologno Monzese\nMilano - ITALY\nPhone :  +39-02-27325-1\nE-mail: tbd@siaemic.com")
if mibBuilder.loadTexts: unit.setDescription("Unit inventory MIB. A unit is a replaceable HW card.")
unitMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitMibVersion.setDescription("Numerical version of this module.\nThe string version of this MIB have the following format:\n   XX.YY.ZZ\nso, for example, the value 1 should be interpreted as 00.00.01\nand the value 10001 should be interpreted as 01.00.01.")
unitTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2))
if mibBuilder.loadTexts: unitTable.setDescription("Table with Unit records.")
unitRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1)).setIndexNames((0, "SIAE-UNIT-MIB", "unitId"))
if mibBuilder.loadTexts: unitRecord.setDescription("Unit record.")
unitId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitId.setDescription("This object is used as Index of the Unit Table.")
unitExpectedType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 2), AutonomousType().clone('1.3.6.1.4.1.3373.1103.6.3.1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitExpectedType.setDescription("Defines the expected unit type.")
unitActualType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 3), AutonomousType().clone('1.3.6.1.4.1.3373.1103.6.3.1')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitActualType.setDescription("Defines the real unit type actually present in the equipment")
unitLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitLabel.setDescription("ASCII string used to assign a name to the unit.")
unitFailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 5), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitFailAlarm.setDescription("Unit Fail alarm status status with associated severity.")
unitMissingAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 6), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitMissingAlarm.setDescription("Unit Missing alarm status with associated severity.")
unitNotRespondingAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 7), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitNotRespondingAlarm.setDescription("Unit Not Responding alarm status with associated severity.")
unitHwMismatchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 8), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitHwMismatchAlarm.setDescription("Unit type Mismatch alarm status with associated severity.")
unitSwMismatchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 9), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitSwMismatchAlarm.setDescription("Unit with Sw Release Mismatch alarm status with associated severity.")
unitHwEdition = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitHwEdition.setDescription("ASCII string used to identify Hw edition of the unit.")
unitPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitPartNumber.setDescription("ASCII string to identify the Part Number of the unit.")
unitParentPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitParentPartNumber.setDescription("ASCII string to identify the parent Part Number of the unit.")
unitParentSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitParentSerialNumber.setDescription("ASCII string to identify parent Serial Number of the unit.")
unitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitRowStatus.setDescription("Status of this row of unitTable.")
unitFailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 4), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitFailAlarmSeverityCode.setDescription("Defines the severity associated to the unitFailAlarm\nand enables/disables the trap generation on status change event.")
unitMissingAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitMissingAlarmSeverityCode.setDescription("Defines the severity associated to the unitMissingAlarm\nand enables/disables the trap generation on status change event.")
unitNotRespondingAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitNotRespondingAlarmSeverityCode.setDescription("Defines the severity associated to the unitNotRespondingAlarm\nand enables/disables the trap generation on status change event.")
unitHwMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitHwMismatchAlarmSeverityCode.setDescription("Defines the severity associated to the unitHwMismatchAlarm\nand enables/disables the trap generation on status change event.")
unitSwMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitSwMismatchAlarmSeverityCode.setDescription("Defines the severity associated to the unitSwMismatchAlarm\nand enables/disables the trap generation on status change event.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("SIAE-UNIT-MIB", PYSNMP_MODULE_ID=unit)

# Objects
mibBuilder.exportSymbols("SIAE-UNIT-MIB", unit=unit, unitMibVersion=unitMibVersion, unitTable=unitTable, unitRecord=unitRecord, unitId=unitId, unitExpectedType=unitExpectedType, unitActualType=unitActualType, unitLabel=unitLabel, unitFailAlarm=unitFailAlarm, unitMissingAlarm=unitMissingAlarm, unitNotRespondingAlarm=unitNotRespondingAlarm, unitHwMismatchAlarm=unitHwMismatchAlarm, unitSwMismatchAlarm=unitSwMismatchAlarm, unitHwEdition=unitHwEdition, unitPartNumber=unitPartNumber, unitParentPartNumber=unitParentPartNumber, unitParentSerialNumber=unitParentSerialNumber, unitRowStatus=unitRowStatus, unitFailAlarmSeverityCode=unitFailAlarmSeverityCode, unitMissingAlarmSeverityCode=unitMissingAlarmSeverityCode, unitNotRespondingAlarmSeverityCode=unitNotRespondingAlarmSeverityCode, unitHwMismatchAlarmSeverityCode=unitHwMismatchAlarmSeverityCode, unitSwMismatchAlarmSeverityCode=unitSwMismatchAlarmSeverityCode)
