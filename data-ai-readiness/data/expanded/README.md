# Erweiterter synthetischer Datensatz

Alle Daten sind erfunden. Die Dateien simulieren Systeme und sind keine echten SAP-, CRM- oder SharePoint-Exporte.

- CRM: 262 Datensätze, darunter 12 mögliche Dubletten.
- Produktstamm: 80 Produkte; 244 historische Preiszeilen mit teils überlappender Gültigkeit.
- ERP: 12.001 Aufträge mit absichtlichen Referenzfehlern, einer doppelten ID und negativen Mengen.
- Produktionsqualität: 3.200 Chargen mit einzelnen fehlenden oder unmöglichen Ausschusswerten.
- Legacy: 200 Metadatenobjekte mit unterschiedlichen Aufbewahrungshinweisen.
- 24 Dokumente und Metadaten: Versionen, Freigaben, Gültigkeit und Zugriffsgruppen.

CSV ist UTF-8 und kommasepariert. Bestelldatum ist zwischen 2024-01-01 und 2026-09-26; Preise gelten inklusiv am Anfangs- und Enddatum. Pro Bestellung nur dann einen Preis übernehmen, wenn exakt ein gültiger Preis für Produkt und Datum vorliegt. Mehrdeutige Zuordnung markieren. Vergleiche unternehmensnamenbasierte Kundendubletten nur als Kandidaten: eine echte Zusammenlegung benötigt Freigabe. ERP-Kunden referenzieren IDs 1 bis 250; Kunden 251 bis 262 sind mögliche Dubletten. Dokumente der Version 2 sind freigegeben, V1 archiviert, V3 Entwurf. Keine automatische Löschung oder Freigabe aus den Übungsdaten ableiten.

Die alten Daten unter data/raw bleiben unverändert. Das bestehende src/pipeline.py arbeitet weiterhin mit diesen alten Dateien. Für diese Daten eine eigene Kopie/Anpassung erstellen, nicht erwarten, dass die vorhandene Demo automatisch data/expanded verarbeitet.
