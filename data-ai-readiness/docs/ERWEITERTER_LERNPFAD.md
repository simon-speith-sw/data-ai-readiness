# Erweiterter Lernpfad 16 Wochen

Fortsetzung nach dem ersten gehörten DP-900-Teil. Pro Woche 4 Stunden: 60 Minuten Lernen, 90 Minuten praktische Aufgabe, 60 Minuten Dokumentation, 30 Minuten Abschlusscheck. Insgesamt 64 Stunden. Der vorhandene Lernplan und Fortschritt bleiben unverändert; dies ist ein ergänzender, auf data/expanded zugeschnittener Pfad.

Die reguläre DP-900-Prüfung ist in diesen 64 Stunden nicht verbindlich eingeplant. Falls du sie machen möchtest, plane Prüfungsübungen und Prüfung separat oder ersetze Lernzeit nach Rücksprache. Das Bestehen ist Voraussetzung für das Zertifikat.

Quellen: [DP-900](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/), [Microsoft Fabric Medallion](https://microsoftlearning.github.io/mslearn-fabric/Instructions/Labs/03b-medallion-lakehouse.html), [Azure RAG](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide), [AWS Skill Builder](https://skillbuilder.aws/).

## Woche 01 Datenquellen und Ziele

- 60 min Lernen: DP-900 Grundlagen rekapitulieren; data/expanded/README.md und Datenquellen sichten.
- 90 min Praxis: Zähle Zeilen, beschreibe die sechs Systeme, markiere Datentyp, Owner, Schutzbedarf und drei Use Cases.
- 60 min Dokumentation: Erstelle eine IST-Systemlandkarte und erfasse Quellen und ungelöste Fragen im Dateninventar.
- 30 min Abschluss: Inventar umfasst sämtliche Dateien und unterscheidet Annahme/Befund.


## Woche 02 Relationale Daten und Cloud Grundlagen

- 60 min Lernen: DP-900: relational/nichtrelational, OLTP/OLAP, IaaS/PaaS/SaaS und Shared Responsibility.
- 90 min Praxis: Prüfe Primär-/Fremdschlüssel und finde Kunden ohne CRM-Treffer; vergleiche Azure und AWS auf Infrastruktur-Ebene.
- 60 min Dokumentation: Ergänze Dateninventar um Datenflüsse, Zugriff und Schutzbedarf; dokumentiere ein Beispiel für eine fehlerhafte Verknüpfung.
- 30 min Abschluss: Du erklärst, warum ERP und CRM voneinander abweichen können.


## Woche 03 Datenprofiling und Geschäftsbedeutung

- 60 min Lernen: Nullwerte, Kardinalität, Domänen und Aktualität kennenlernen.
- 90 min Praxis: Profile Kunden, Orders und Produkte; identifiziere doppelte IDs und negative Mengen.
- 60 min Dokumentation: Definiere drei businessrelevante Qualitätsregeln und deren Owner.
- 30 min Abschluss: Eine Auswertung zeigt betroffene Zeilen und Trennung von Befund und Annahme.


## Woche 04 Preise und Historisierung

- 60 min Lernen: Gültigkeitsintervalle und zeitabhängige Joins lernen.
- 90 min Praxis: Ordne Auftragspreise anhand von Produkt und Bestelldatum zu; trenne keine, eine und mehrere gültige Preiszeilen.
- 60 min Dokumentation: Beschreibe, weshalb mehrdeutige Preise nicht automatisch aggregiert werden sollen.
- 30 min Abschluss: Grenzen der Intervalle und Preisüberschneidungen sind nachvollziehbar.


## Woche 05 Lake Warehouse Lakehouse

- 60 min Lernen: Architekturprinzipien und Bronze Silver Gold kennenlernen.
- 90 min Praxis: Entwirf eine Zielarchitektur: SAP-ähnliches ERP, CRM, Dateien und Produktionsdaten; auch dezentrale Variante betrachten.
- 60 min Dokumentation: Beschreibe drei Architekturentscheidungen mit Alternativen, Vor- und Nachteilen.
- 30 min Abschluss: Kopieren, Verknüpfen und Beibehalten sind pro Quelle begründet.


## Woche 06 Azure AWS und Integration

- 60 min Lernen: Vergleiche Storage, Datenbanken, Identität und Datenintegration auf Azure und AWS.
- 90 min Praxis: Zeichne Datenflüsse und ordne Quellsysteme, APIs, Batch und mögliche CDC ein.
- 60 min Dokumentation: Erstelle eine Vergleichsmatrix mit Betrieb, Sicherheit, Kosten und Portabilität.
- 30 min Abschluss: Du kannst die Systemkategorien erklären, ohne einen Anbieter vorauszusetzen.


## Woche 07 Migration und Datenselektion

- 60 min Lernen: Lerne Inventarisierung, Business Value, Abhängigkeiten, Schutzbedarf und Retention.
- 90 min Praxis: Entscheide für 20 Archivobjekte: migrieren, zugänglich halten, archivieren oder prüfen; legal_hold bleibt gesperrt.
- 60 min Dokumentation: Erstelle Auswahlmatrix samt Freigaberollen und Pilotumfang.
- 30 min Abschluss: Jede Entscheidung enthält Begründung, Evidenz und offene Frage; keine automatische Löschung.


## Woche 08 Zwischenpräsentation und Migration

- 60 min Lernen: Plane Reihenfolge, Datenabgleich, Tests, Rückfall und Betriebsübernahme.
- 90 min Praxis: Fasse IST, Risiken und Zielbild zusammen; skizziere Pilot und Migrationswellen.
- 60 min Dokumentation: Stelle ein Zwischenergebnis von sechs bis acht Folien vor und erfasse Feedback.
- 30 min Abschluss: Management kann die drei wichtigsten Entscheidungen und Risiken erkennen.


## Woche 09 ETL ELT und reproduzierbarer Import

- 60 min Lernen: Lerne Unterschiede zwischen Roh-, Bereinigungs- und fachlicher Schicht.
- 90 min Praxis: Erstelle einen eigenen reproduzierbaren Import für data/expanded; Herkunft und Ladezeit erfassen.
- 60 min Dokumentation: Erzeuge ein Fehlerprotokoll und dokumentiere Transformationen.
- 30 min Abschluss: Ein wiederholter Lauf fügt keine ungeplanten Duplikate hinzu.


## Woche 10 Qualitätsregeln und Tests

- 60 min Lernen: Vertiefe Vollständigkeit, Konsistenz, Plausibilität und referenzielle Integrität.
- 90 min Praxis: Prüfe mindestens fünf Fehlerklassen in Orders, Preisen und Produktionsqualität.
- 60 min Dokumentation: Formuliere Tests und Eskalationspfad je Regel; zähle betroffene Datensätze.
- 30 min Abschluss: Fehlerfälle sind reproduzierbar und fehlerhafte Records verschwinden nicht still.


## Woche 11 Star Schema und Kennzahlen

- 60 min Lernen: Lerne Dimensionen, Faktentabellen, Grain und Historisierung.
- 90 min Praxis: Entwerfe Kunden-, Produkt- und Zeitdimension und Order- bzw. Qualitätsfakten.
- 60 min Dokumentation: Dokumentiere Grain, Join-Logik, Ausschussquote und ihre Grenzen.
- 30 min Abschluss: Kennzahlen lassen sich auf Detailzeilen zurückführen; ungültige Werte werden gesondert ausgewiesen.


## Woche 12 Stammdaten und Data Governance

- 60 min Lernen: Lerne Data Owner, Steward, Datenprodukt und MDM.
- 90 min Praxis: Bewerte CRM-Dubletten als Kandidaten; kläre führende Quellen und Entscheidungszuständigkeit.
- 60 min Dokumentation: Erstelle Rollenmatrix und einen Datenprodukt-Steckbrief mit Qualitätsziel.
- 30 min Abschluss: Keine Dublette wird ohne fachliche Prüfung als sicher identisch dargestellt.


## Woche 13 Dokumente für RAG vorbereiten

- 60 min Lernen: Lerne Dokument-Parsing, Metadaten, Versionen, Chunking und Retrieval.
- 90 min Praxis: Inventarisiere Dokumente und erstelle zwei Chunking-Varianten; beachte Tabellen und Überschriften.
- 60 min Dokumentation: Dokumentiere Chunkgröße, Überlappung, Metadaten und Tradeoffs.
- 30 min Abschluss: Chunks behalten Quellen-ID und Version; es gibt konkrete Vergleichsfälle.


## Woche 14 RAG Evaluation und Berechtigungen

- 60 min Lernen: Lerne Suchqualität, Quellenbezug, Berechtigungsfilter und Aktualisierung.
- 90 min Praxis: Teste zehn Fragen mit zwei Rollen: freigegebene, archivierte und Entwürfe getrennt berücksichtigen.
- 60 min Dokumentation: Dokumentiere erwartete Quellen, Treffer und unerlaubte Antworten; Cloud-Dienst optional.
- 30 min Abschluss: Kein Zugriff auf nicht autorisierte Dokumente im manuellen Test; Auswertung nennt Grenzen.


## Woche 15 Sicherheit Datenschutz und AI Act

- 60 min Lernen: Lerne Schutzbedarf, Cloud-Shared-Responsibility und risikobasierte KI-Governance.
- 90 min Praxis: Zeichne Datenflüsse inklusive Support/Backups; unterscheide personenbezogene und technische Daten.
- 60 min Dokumentation: Erstelle Vorprüfungscheckliste mit offenen Fragen an Datenschutz und Security.
- 30 min Abschluss: Eine EU-Region allein gilt nicht als vollständiger Nachweis; Rechtsfragen werden fachlich geprüft.


## Woche 16 Roadmap und Abschluss

- 60 min Lernen: Wiederhole Prinzipien und offene Architekturentscheidungen.
- 90 min Praxis: Stelle Maßnahmen nach Nutzen, Abhängigkeit, Verantwortlichkeit und Aufwand zusammen.
- 60 min Dokumentation: Fertige Präsentation und Assessment-Vorlagen für das KI-Strategie-Team; Feedback einholen.
- 30 min Abschluss: Deck, Inventar, Migrationsmatrix und Governance-/RAG-Notizen sind referenzierbar.

