#
# PySNMP MIB module SIAE-TREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./sm_tree.mib
# Produced by pysmi-0.3.2 at Fri Jul 19 08:18:02 2019
# On host 0e190c6811ee platform Linux version 4.9.125-linuxkit by user root
# Using Python version 3.7.3 (default, Apr  3 2019, 05:39:12) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ObjectIdentity, Counter64, Bits, Gauge32, MibIdentifier, iso, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, IpAddress, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "Counter64", "Bits", "Gauge32", "MibIdentifier", "iso", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "IpAddress", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
siaeMicroelettronicaSpa = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373))
siaeMicroelettronicaSpa.setRevisions(('2014-06-23 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setLastUpdated('201406230000Z')
if mibBuilder.loadTexts: siaeMicroelettronicaSpa.setOrganization('SIAE MICROELETTRONICA spa')
siaeMib = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103))
mibBuilder.exportSymbols("SIAE-TREE-MIB", PYSNMP_MODULE_ID=siaeMicroelettronicaSpa, siaeMib=siaeMib, siaeMicroelettronicaSpa=siaeMicroelettronicaSpa)
