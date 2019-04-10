# PySNMP SMI module. Autogenerated from smidump -f python SIAE-RABR-MIB
# by libsmi2pysnmp-0.1.3 at Thu Apr  4 09:19:34 2019,
# Python version sys.version_info(major=2, minor=7, micro=15, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( AlarmSeverityCode, AlarmStatus, alarmTrap, ) = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus", "alarmTrap")
( equipIpSnmpAgentAddress, ) = mibBuilder.importSymbols("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress")
( siaeMib, ) = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, RowStatus, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")

# Types

class ChannelSpacing(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(12,6,14,9,3,0,10,8,11,2,5,7,4,1,13,)
    namedValues = NamedValues(("bw3M5Hz", 0), ("bw7Mhz", 1), ("bw1000Mhz", 10), ("bw10Mhz", 11), ("bw20Mhz", 12), ("bw30Mhz", 13), ("bw50Mhz", 14), ("bw14MHz", 2), ("bw28MHz", 3), ("bw56MHz", 4), ("bw40MHz", 5), ("bw112MHz", 6), ("bw250Mhz", 7), ("bw500Mhz", 8), ("bw750Mhz", 9), )
    
class ConfigMismatchReason(Bits):
    namedValues = NamedValues(("securityMismatch", 0), ("frequencyFailMismatch", 1), ("frequencyAlertMismatch", 2), ("ptxMismatch", 3), ("channelSpacingAndModulationMismatch", 4), ("remoteConfigurationMismatch", 5), ("acmMismatch", 6), ("profileSetMismatch", 7), )
    
class KeyFeatures(Bits):
    namedValues = NamedValues(("featureReserved", 0), ("featureTrafficSquelch", 1), ("featureBaseBandLoop", 2), ("featureMaxPower", 3), ("featureCarrierOnly", 4), ("featureIQLoop", 5), ("featureRFLoopCond", 6), ("featureRFLoopUncond", 7), )
    
class LoopCapabilities(Bits):
    namedValues = NamedValues(("loopbackAtAnyModulation", 0), ("loopbackAtFixedModulation", 1), )
    
class ModulationMap(Bits):
    namedValues = NamedValues(("modBPSK", 0), ("mod4QAM", 1), ("mod2048QAM", 10), ("mod8PSK", 2), ("mod16QAM", 3), ("mod32QAM", 4), ("mod64QAM", 5), ("mod128QAM", 6), ("mod256QAM", 7), ("mod512QAM", 8), ("mod1024QAM", 9), )
    

# Objects

radioBranch = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 39)).setRevisions(("2015-09-15 00:00","2015-03-23 00:00","2014-10-07 00:00","2014-03-04 00:00","2014-02-04 00:00","2013-04-16 00:00",))
if mibBuilder.loadTexts: radioBranch.setOrganization("SIAE MICROELETTRONICA spa")
if mibBuilder.loadTexts: radioBranch.setContactInfo("SIAE MICROELETTONICA s.p.a.\nVia Michelangelo Buonarroti, 21\n20093 - Cologno Monzese\nMilano - ITALY\nPhone :  +39-02-27325-1\nE-mail: help@siaemic.com")
if mibBuilder.loadTexts: radioBranch.setDescription("Radio Branch parameters")
radioBranchMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchMibVersion.setDescription("Numerical version of this module.\nThe string version of this MIB have the following format:\n   XX.YY.ZZ\nso, for example, the value 1 should be interpreted as 00.00.01\nand the value 10001 should be interpreted as 01.00.01.")
radioBranchTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2))
if mibBuilder.loadTexts: radioBranchTable.setDescription("Table with RadioBranch records: one record for 1+0 configuration and\ntwo record for 1+1 configuration.")
radioBranchRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1)).setIndexNames((0, "SIAE-RABR-MIB", "radioBranchId"))
if mibBuilder.loadTexts: radioBranchRecord.setDescription("RadioBranch record.")
radioBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchId.setDescription("This object identifies the Radio Branch.")
radioBranchTxFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchTxFrequency.setDescription("Transmitted frequency chooses by operator in KHz.")
radioBranchTxAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchTxAttenuation.setDescription("Transmitter attenuation related to radiobranchNomPwr (dBm).")
radioBranchAtpcManual = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("disable", 1), ("enable", 2), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchAtpcManual.setDescription("Enables/disables Atpc Manual operation.")
radioBranchAtpcPwrHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 6), Integer32().clone(-40)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchAtpcPwrHigh.setDescription("ATPC Control - Local Rx Power High (dBm range -30 to -80) -.")
radioBranchAtpcPwrLow = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 7), Integer32().clone(-60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchAtpcPwrLow.setDescription("ATPC Control - Local Rx Power Low (dBm range -30 to -80) -.")
radioBranchAtpcRange = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchAtpcRange.setDescription("Defines the range of the ATPC regulation (expressed in dB) with respect\nto the current value of maximum Tx output, that is intended as the upper\nlimit of the range. A null value means no limit: the lower limit\nof the range is equal to minimum Ptx.")
radioBranchKeyFeatures = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 9), KeyFeatures()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchKeyFeatures.setDescription("Bit map to describe the radio features.")
radioBranchTxShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 10), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("transmitterShutdown", 1), ("transmitterOn", 2), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchTxShutdown.setDescription("Permanent shutdown of the RF transmitter")
radioBranchPrx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchPrx.setDescription("Received power level (dBm).")
radioBranchPtx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchPtx.setDescription("Transmitted power level (dBm).")
radioBranchNormalizedMse = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchNormalizedMse.setDescription("Normalized MSE (Mean Squared Error) is an indicator of the Signal\nto Noise (S/N) ratio. It's in 0.1 dB steps")
radioBranchRFLoopCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 18), LoopCapabilities()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRFLoopCapabilities.setDescription("RF loopback mode supported by the radio branch")
radioBranchInvalidFrequencyAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 27), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchInvalidFrequencyAlarm.setDescription("Invalid frequency alarm with associated severity.")
radioBranchBaseBandRxAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 28), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchBaseBandRxAlarm.setDescription("Base Band Rx alarm status with associated severity.")
radioBranchModulatorFailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 29), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchModulatorFailAlarm.setDescription("Modulator Fail Alarm status with associated severity.")
radioBranchDemodulatorFailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 30), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchDemodulatorFailAlarm.setDescription("Demodulator Fail Alarm status with associated severity.")
radioBranchRxPowerLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 31), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRxPowerLowAlarm.setDescription("Receiver power low alarm status with associated severity.")
radioBranchTxPowerLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 32), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchTxPowerLowAlarm.setDescription("Transmitter power low alarm status with associated severity.")
radioBranchRemDemodulatorFailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 33), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRemDemodulatorFailAlarm.setDescription("Remote Demodulator Fail Alarm status with associated severity.")
radioBranchRtVcoFailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 37), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRtVcoFailAlarm.setDescription("RT VCO fail alarm status with associated severity.")
radioBranchRxAcgAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 38), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRxAcgAlarm.setDescription("RT IF fail alarm status with associated severity.")
radioBranchRxQualityLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 39), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRxQualityLowAlarm.setDescription("Low BER Alarm status with associated severity.")
radioBranchRxQualityWarningAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 40), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRxQualityWarningAlarm.setDescription("The RX signal is close to cause errors on payload.")
radioBranchConfigMismatchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 43), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchConfigMismatchAlarm.setDescription("Config Mismatch alarm status with associated severity and related map.")
radioBranchConfigAlarmReason = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 44), ConfigMismatchReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchConfigAlarmReason.setDescription("Bit map to describe the Config Mismatch Alarm")
radioBranchLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 45), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchLabel.setDescription("Label of Radio Branch.")
radioBranchChannelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchChannelNum.setDescription("Number of the radio channel.")
radioBranchTxMinFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 48), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchTxMinFrequency.setDescription("Minimum of available channel frequency in KHz.")
radioBranchTxMaxFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 49), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchTxMaxFrequency.setDescription("Maximum of available channel frequency in KHz.")
radioBranchTxChannelSpacing = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 50), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchTxChannelSpacing.setDescription("Half of transmitted signal channel spacing in KHz.")
radioBranchCurrentDuplexFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 51), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchCurrentDuplexFrequency.setDescription("Spacing between transmitted and received frequency in KHz.")
radioBranchStepFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 52), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchStepFrequency.setDescription("Minimum frequency step in KHz.")
radioBranchFractionalPrx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchFractionalPrx.setDescription("Received power level (tenth of dBm).")
radioBranchFractionalPtx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchFractionalPtx.setDescription("Transmitted power level (tenth of dBm).")
radioBranchMinPtxNominalValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 55), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchMinPtxNominalValue.setDescription("Minimum nominal Ptx in dBm.")
radioBranchMaxPtxNominalValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchMaxPtxNominalValue.setDescription("Maximum nominal Ptx in dBm.")
radioBranchExtendedMinPwr = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchExtendedMinPwr.setDescription("Minimum extended Ptx power for fade margin.")
radioBranchFreqTableSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 61), ChannelSpacing()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchFreqTableSelection.setDescription("RadioBranchFrequencyTable key (channel spacing & modulation) selection.")
radioBranchMaxChNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 62), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchMaxChNum.setDescription("Max channel number related to the bandwidth selected.\nIt define the number of radioBranchFreqTabRecord")
radioBranchDuplexFrequencyChoise1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 65), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchDuplexFrequencyChoise1.setDescription("Possible value of duplex frequency in KHz.\n0 means value undefined.")
radioBranchDuplexFrequencyChoise2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 66), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchDuplexFrequencyChoise2.setDescription("Possible value of duplex frequency in KHz.\n0 means value undefined.")
radioBranchDuplexFrequencyChoise3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 67), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchDuplexFrequencyChoise3.setDescription("Possible value of duplex frequency in KHz.\n0 means value undefined.")
radioBranchDuplexFrequencyChoise4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 68), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchDuplexFrequencyChoise4.setDescription("Possible value of duplex frequency in KHz.\n0 means value undefined.")
radioBranchDuplexFrequencyChoise5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 69), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchDuplexFrequencyChoise5.setDescription("Possible value of duplex frequency in KHz.\n0 means value undefined.")
radioBranchDuplexFrequencyChoise6 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 70), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchDuplexFrequencyChoise6.setDescription("Possible value of duplex frequency in KHz.\n0 means value undefined.")
radioBranchDuplexFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 71), Integer32().clone(-2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchDuplexFrequency.setDescription("Value of duplex frequency in KHz.")
radioBranchPermanentTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 72), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("transmitterOff", 1), ("transmitterOn", 2), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchPermanentTxStatus.setDescription("Transmitter status control.\nWhen active (1) it swithes off the transmitter\nin a permanent way.")
radioBranchRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 73), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: radioBranchRowStatus.setDescription("Row Status for the radioBranch table.")
radioBranchRxActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 74), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("cleared", 1), ("active", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRxActiveStatus.setDescription("Receiver Active status with associated Severity\nIn 1+1 Hot Standby radio system, only one RX is active.\nRXs are active in other configurations of the radio system.")
radioBranchTxActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 75), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("cleared", 1), ("active", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchTxActiveStatus.setDescription("Transmitter Active status with associated Severity.\nIn 1+1 Hot Standby radio system, only one TX is active.\nTXs are active in other configurations of the radio system.")
radioBranchCableOpenAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 76), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchCableOpenAlarm.setDescription("Cable connnecting ODU is open: alarm status with associated\nseverity.")
radioBranchCableShortAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 2, 1, 77), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchCableShortAlarm.setDescription("Cable connnecting ODU is in short-circuit: alarm status\nwith associated severity.")
radioBranchMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 3))
if mibBuilder.loadTexts: radioBranchMaintTable.setDescription("Table with Command for maintenance of radio branch.\nObjects in this table is not persistent. An Instance of this\ntable is created on creation of radioBranchRecord")
radioBranchMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 3, 1)).setIndexNames((0, "SIAE-RABR-MIB", "radioBranchId"))
if mibBuilder.loadTexts: radioBranchMaintRecord.setDescription("Radio branch Maintenance record.")
radioBranchTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 3, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("transmitterOff", 1), ("transmitterOn", 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchTxStatus.setDescription("Transmitter status control.")
radioBranchCarrierOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 3, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("carrierOnlyOff", 1), ("carrierOnlyOn", 2), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchCarrierOnly.setDescription("Carrier only transmission control.")
radioBranchLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 3, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(2,6,9,7,4,3,8,1,)).subtype(namedValues=NamedValues(("loopOff", 1), ("rFloopOn-RemTxOff", 2), ("iqloop", 3), ("baseBandloop", 4), ("rfLoopLimited", 6), ("baseBandEthloop", 7), ("rfLoopEthLimited", 8), ("iqEthloop", 9), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchLoop.setDescription("Enables/disables the Radio Branch loops.")
radioBranchRFLoopTestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 3, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(4,0,5,2,3,1,)).subtype(namedValues=NamedValues(("testNone", 0), ("testRunning", 1), ("testNotPossible", 2), ("testPassed", 3), ("testFail", 4), ("testInterrupted", 5), )).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRFLoopTestResult.setDescription("Radio branch RT loop test result.")
radioBranchRFLoopTestPercTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRFLoopTestPercTime.setDescription("Radio branch RT loop test time percentage")
radioBranchInvalidFrequencyAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 4), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchInvalidFrequencyAlarmSeverityCode.setDescription("Defines the severity associated to the radioBranchInvalidFrequencyAlarm\nand enables/disables the trap generation on status change event.")
radioBranchBaseBandRxAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchBaseBandRxAlarmSeverityCode.setDescription("Defines the severity associated to the radioBranchBaseBandRxAlarm\nand enables/disables the trap generation on status change event.")
radioBranchModulatorFailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchModulatorFailAlarmSeverityCode.setDescription("Defines the severity associated to the radioBranchModulatorFailAlarm\nand enables/disables the trap generation on status change event.")
radioBranchDemodulatorFailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchDemodulatorFailAlarmSeverityCode.setDescription("Defines the severity associated to the radioBranchDemodulatorFailAlarm\nand enables/disables the trap generation on status change event.")
radioBranchRxPowerLowAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchRxPowerLowAlarmSeverityCode.setDescription("Defines the severity associated to the RadioBranchRxPowerLowAlarm\nand enables/disables the trap generation on status change event.")
radioBranchTxPowerLowAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 9), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchTxPowerLowAlarmSeverityCode.setDescription("Defines the severity associated to the radioBranchTxPowerLowAlarm\nand enables/disables the trap generation on status change event.")
radioBranchRtVcoFailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 10), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchRtVcoFailAlarmSeverityCode.setDescription("Defines the severity associated to the RadioBranchRtVcoFailAlarm\nand enables/disables the trap generation on status change event.")
radioBranchRxAcgAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 11), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchRxAcgAlarmSeverityCode.setDescription("Defines the severity associated to the radioBranchRxAcgAlarm\nand enables/disables the trap generation on status change event.")
radioBranchRxQualityLowAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 12), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchRxQualityLowAlarmSeverityCode.setDescription("Define the severity associated to the radioBranchRxQualityLowAlarm\nand enable/disable the trap generation on status change event.")
radioBranchRxQualityWarningAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 13), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchRxQualityWarningAlarmSeverityCode.setDescription("Define the severity associated to the radioBranchRxQualityWarningAlarm\nand enable/disable the trap generation on status change event.")
radioBranchConfigMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 14), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchConfigMismatchAlarmSeverityCode.setDescription("Defines the severity associated to the RadioBranchConfigMismatchAlarm\nand enables/disables the trap generation on status change event.")
radioBranchPrxHysteresisValue = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 15), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchPrxHysteresisValue.setDescription("Defines the delta value associated to the radioBranchPrx before\nhaving a new trap generation (radioBranchPtxChange TRAP).\nThe zero value is not allowed.")
radioBranchPtxHysteresisValue = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 16), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchPtxHysteresisValue.setDescription("Defines the delta value associated to the radioBranchPtx before\nhaving a new trap generation (radioBranchPtxChange TRAP).\nThe zero value is not allowed.")
radioBranchPrxHysteresisValueTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 17), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchPrxHysteresisValueTrapNotification.setDescription("Enables/disables the Rx change trap generation on status change\nevent.")
radioBranchPtxHysteresisValueTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 18), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchPtxHysteresisValueTrapNotification.setDescription("Enables/disables the Tx change trap generation on status change\nevent.")
radioBranchFrequencyTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 19))
if mibBuilder.loadTexts: radioBranchFrequencyTable.setDescription("Availables channels for channel spacing and modulation selected\n(see leaf radioBranchFreqTableSelection and radioBranchMaxChNum).")
radioBranchFreqTabRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 19, 1)).setIndexNames((0, "SIAE-RABR-MIB", "radioBranchId"), (0, "SIAE-RABR-MIB", "radioBranchFreqTabChId"))
if mibBuilder.loadTexts: radioBranchFreqTabRecord.setDescription("RadioBranchFreqTab record.")
radioBranchFreqTabChId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 19, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchFreqTabChId.setDescription("This object identifies the channel id.")
radioBranchFreqTabChNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 19, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchFreqTabChNum.setDescription("Available channel number.")
radioBranchFreqTabFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 19, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchFreqTabFrequency.setDescription("Channel number frequency.")
radioBranchModulationTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 20))
if mibBuilder.loadTexts: radioBranchModulationTable.setDescription("List of modulation related to channel spacing.")
radioBranchModulationRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 20, 1)).setIndexNames((0, "SIAE-RABR-MIB", "radioBranchId"), (0, "SIAE-RABR-MIB", "radioBranchChanSpacing"))
if mibBuilder.loadTexts: radioBranchModulationRecord.setDescription("radioBranchModulation record.")
radioBranchChanSpacing = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 20, 1, 1), ChannelSpacing()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchChanSpacing.setDescription("This object identifies the channel spacing.")
radioBranchModulationMap = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 20, 1, 2), ModulationMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchModulationMap.setDescription("List of modulation in the radioBranchChanSpacing")
radioBranchRefModulationMap = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 20, 1, 3), ModulationMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radioBranchRefModulationMap.setDescription("List of modulations that can be selected as reference\nin the radioBranchChanSpacingId")
radioBranchRemDemodulatorFailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 21), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchRemDemodulatorFailAlarmSeverityCode.setDescription("Defines the severity associated to the radioBranchRemDemodulatorFailAlarm\nand enables/disables the trap generation on status change event.")
radioBranchRxActiveStatusTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 22), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchRxActiveStatusTrapNotification.setDescription("Define the severity associated to the radioBranchRxActivestatus and\nenable/disable the trap generation on status change event.")
radioBranchTxActiveStatusTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 23), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchTxActiveStatusTrapNotification.setDescription("Define the severity associated to the radioBranchTxActivestatus and\nenable/disable the trap generation on status change event.")
radioBranchCableOpenAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 24), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchCableOpenAlarmSeverityCode.setDescription("Defines the severity associated to the  radioBranchCableOpen\nand enables/disables the trap generation on status change event.")
radioBranchCableShortAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 39, 25), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radioBranchCableShortAlarmSeverityCode.setDescription("Defines the severity associated to the  radioBranchCableShort\nand enables/disables the trap generation on status change event.")

# Augmentions

# Notifications

radioBranchPrxChange = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 3901)).setObjects(*(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-RABR-MIB", "radioBranchLabel"), ("SIAE-RABR-MIB", "radioBranchPrx"), ("SIAE-RABR-MIB", "radioBranchId"), ) )
if mibBuilder.loadTexts: radioBranchPrxChange.setDescription("This event is generated when radioBranchPrx is changed, in\nmodulus, more than radioBranchPtxHysteresisValue from last TRAP.\nThe data passed with the event are:\n1) equipIpSnmpAgentAddress     - agent IP address\n2) radioBranchId               - branch index\n3) radioBranchLabel            - branch name\n4) radioBranchPrx              - PRX value")
radioBranchPtxChange = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 3902)).setObjects(*(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-RABR-MIB", "radioBranchLabel"), ("SIAE-RABR-MIB", "radioBranchPtx"), ("SIAE-RABR-MIB", "radioBranchId"), ) )
if mibBuilder.loadTexts: radioBranchPtxChange.setDescription("This event is generated when radioBranchPtx is changed, in\nmodulus, more than radioBranchPtxHysteresisValue from last TRAP.\nThe data passed with the event are:\n1) equipIpSnmpAgentAddress     - agent IP address\n2) radioBranchId               - branch index\n3) radioBranchLabel            - branch name\n4) radioBranchPtx              - PTX value")

# Exports

# Module identity
mibBuilder.exportSymbols("SIAE-RABR-MIB", PYSNMP_MODULE_ID=radioBranch)

# Types
mibBuilder.exportSymbols("SIAE-RABR-MIB", ChannelSpacing=ChannelSpacing, ConfigMismatchReason=ConfigMismatchReason, KeyFeatures=KeyFeatures, LoopCapabilities=LoopCapabilities, ModulationMap=ModulationMap)

# Objects
mibBuilder.exportSymbols("SIAE-RABR-MIB", radioBranch=radioBranch, radioBranchMibVersion=radioBranchMibVersion, radioBranchTable=radioBranchTable, radioBranchRecord=radioBranchRecord, radioBranchId=radioBranchId, radioBranchTxFrequency=radioBranchTxFrequency, radioBranchTxAttenuation=radioBranchTxAttenuation, radioBranchAtpcManual=radioBranchAtpcManual, radioBranchAtpcPwrHigh=radioBranchAtpcPwrHigh, radioBranchAtpcPwrLow=radioBranchAtpcPwrLow, radioBranchAtpcRange=radioBranchAtpcRange, radioBranchKeyFeatures=radioBranchKeyFeatures, radioBranchTxShutdown=radioBranchTxShutdown, radioBranchPrx=radioBranchPrx, radioBranchPtx=radioBranchPtx, radioBranchNormalizedMse=radioBranchNormalizedMse, radioBranchRFLoopCapabilities=radioBranchRFLoopCapabilities, radioBranchInvalidFrequencyAlarm=radioBranchInvalidFrequencyAlarm, radioBranchBaseBandRxAlarm=radioBranchBaseBandRxAlarm, radioBranchModulatorFailAlarm=radioBranchModulatorFailAlarm, radioBranchDemodulatorFailAlarm=radioBranchDemodulatorFailAlarm, radioBranchRxPowerLowAlarm=radioBranchRxPowerLowAlarm, radioBranchTxPowerLowAlarm=radioBranchTxPowerLowAlarm, radioBranchRemDemodulatorFailAlarm=radioBranchRemDemodulatorFailAlarm, radioBranchRtVcoFailAlarm=radioBranchRtVcoFailAlarm, radioBranchRxAcgAlarm=radioBranchRxAcgAlarm, radioBranchRxQualityLowAlarm=radioBranchRxQualityLowAlarm, radioBranchRxQualityWarningAlarm=radioBranchRxQualityWarningAlarm, radioBranchConfigMismatchAlarm=radioBranchConfigMismatchAlarm, radioBranchConfigAlarmReason=radioBranchConfigAlarmReason, radioBranchLabel=radioBranchLabel, radioBranchChannelNum=radioBranchChannelNum, radioBranchTxMinFrequency=radioBranchTxMinFrequency, radioBranchTxMaxFrequency=radioBranchTxMaxFrequency, radioBranchTxChannelSpacing=radioBranchTxChannelSpacing, radioBranchCurrentDuplexFrequency=radioBranchCurrentDuplexFrequency, radioBranchStepFrequency=radioBranchStepFrequency, radioBranchFractionalPrx=radioBranchFractionalPrx, radioBranchFractionalPtx=radioBranchFractionalPtx, radioBranchMinPtxNominalValue=radioBranchMinPtxNominalValue, radioBranchMaxPtxNominalValue=radioBranchMaxPtxNominalValue, radioBranchExtendedMinPwr=radioBranchExtendedMinPwr, radioBranchFreqTableSelection=radioBranchFreqTableSelection, radioBranchMaxChNum=radioBranchMaxChNum, radioBranchDuplexFrequencyChoise1=radioBranchDuplexFrequencyChoise1, radioBranchDuplexFrequencyChoise2=radioBranchDuplexFrequencyChoise2, radioBranchDuplexFrequencyChoise3=radioBranchDuplexFrequencyChoise3, radioBranchDuplexFrequencyChoise4=radioBranchDuplexFrequencyChoise4, radioBranchDuplexFrequencyChoise5=radioBranchDuplexFrequencyChoise5, radioBranchDuplexFrequencyChoise6=radioBranchDuplexFrequencyChoise6, radioBranchDuplexFrequency=radioBranchDuplexFrequency, radioBranchPermanentTxStatus=radioBranchPermanentTxStatus, radioBranchRowStatus=radioBranchRowStatus, radioBranchRxActiveStatus=radioBranchRxActiveStatus, radioBranchTxActiveStatus=radioBranchTxActiveStatus, radioBranchCableOpenAlarm=radioBranchCableOpenAlarm, radioBranchCableShortAlarm=radioBranchCableShortAlarm, radioBranchMaintTable=radioBranchMaintTable, radioBranchMaintRecord=radioBranchMaintRecord, radioBranchTxStatus=radioBranchTxStatus, radioBranchCarrierOnly=radioBranchCarrierOnly, radioBranchLoop=radioBranchLoop, radioBranchRFLoopTestResult=radioBranchRFLoopTestResult, radioBranchRFLoopTestPercTime=radioBranchRFLoopTestPercTime, radioBranchInvalidFrequencyAlarmSeverityCode=radioBranchInvalidFrequencyAlarmSeverityCode, radioBranchBaseBandRxAlarmSeverityCode=radioBranchBaseBandRxAlarmSeverityCode, radioBranchModulatorFailAlarmSeverityCode=radioBranchModulatorFailAlarmSeverityCode, radioBranchDemodulatorFailAlarmSeverityCode=radioBranchDemodulatorFailAlarmSeverityCode, radioBranchRxPowerLowAlarmSeverityCode=radioBranchRxPowerLowAlarmSeverityCode, radioBranchTxPowerLowAlarmSeverityCode=radioBranchTxPowerLowAlarmSeverityCode, radioBranchRtVcoFailAlarmSeverityCode=radioBranchRtVcoFailAlarmSeverityCode, radioBranchRxAcgAlarmSeverityCode=radioBranchRxAcgAlarmSeverityCode, radioBranchRxQualityLowAlarmSeverityCode=radioBranchRxQualityLowAlarmSeverityCode, radioBranchRxQualityWarningAlarmSeverityCode=radioBranchRxQualityWarningAlarmSeverityCode, radioBranchConfigMismatchAlarmSeverityCode=radioBranchConfigMismatchAlarmSeverityCode, radioBranchPrxHysteresisValue=radioBranchPrxHysteresisValue, radioBranchPtxHysteresisValue=radioBranchPtxHysteresisValue, radioBranchPrxHysteresisValueTrapNotification=radioBranchPrxHysteresisValueTrapNotification, radioBranchPtxHysteresisValueTrapNotification=radioBranchPtxHysteresisValueTrapNotification, radioBranchFrequencyTable=radioBranchFrequencyTable, radioBranchFreqTabRecord=radioBranchFreqTabRecord, radioBranchFreqTabChId=radioBranchFreqTabChId, radioBranchFreqTabChNum=radioBranchFreqTabChNum, radioBranchFreqTabFrequency=radioBranchFreqTabFrequency, radioBranchModulationTable=radioBranchModulationTable, radioBranchModulationRecord=radioBranchModulationRecord, radioBranchChanSpacing=radioBranchChanSpacing, radioBranchModulationMap=radioBranchModulationMap, radioBranchRefModulationMap=radioBranchRefModulationMap, radioBranchRemDemodulatorFailAlarmSeverityCode=radioBranchRemDemodulatorFailAlarmSeverityCode, radioBranchRxActiveStatusTrapNotification=radioBranchRxActiveStatusTrapNotification, radioBranchTxActiveStatusTrapNotification=radioBranchTxActiveStatusTrapNotification, radioBranchCableOpenAlarmSeverityCode=radioBranchCableOpenAlarmSeverityCode, radioBranchCableShortAlarmSeverityCode=radioBranchCableShortAlarmSeverityCode)

# Notifications
mibBuilder.exportSymbols("SIAE-RABR-MIB", radioBranchPrxChange=radioBranchPrxChange, radioBranchPtxChange=radioBranchPtxChange)

