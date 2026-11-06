# Musterwerke GmbH – fiktive Fallstudie

## Unternehmen
Die Musterwerke GmbH ist ein vollständig **erfundenes** Maschinenbauunternehmen mit 800 Beschäftigten an zwei Standorten. Sie will bessere Vertriebs- und Produktionsanalysen sowie perspektivisch einen technischen Wissensassistenten aufbauen. Gewachsene Insellösungen erschweren Datenintegration, Qualitätssicherung und Governance.

## Sechs Quellsysteme
| System | Rolle | Beispieldatei | Owner-Rolle | Update | Hinweise |
|---|---|---|---|---|---|
| ERP (SAP-ähnlich, simuliert) | führend für Aufträge | `erp_orders.csv` | ERP Application Owner | täglich | Mengen, Material, Kundenreferenzen |
| CRM (simuliert) | Kundenstamm | `crm_customers.csv` | Sales Operations | täglich | Dubletten möglich |
| Team-Excel (CSV-Repräsentation) | Produktpreise | `price_list.csv` | Product Management | monatlich | zeitliche Gültigkeit |
| PostgreSQL (simuliert) | Produktionsqualität | `production_quality.csv` | Plant Data Owner | wöchentlich | Chargen und Ausschuss |
| SharePoint (Markdown-Repräsentation) | technische Handbücher | `documents/*.md` | Engineering Knowledge Owner | unregelmäßig | Freigabe und Version wichtig |
| Fileserver (JSON-Repräsentation) | Legacy-Archiv | `legacy_archive.json` | IT Archive Owner | statisch | Retention unbekannt |

**Die Datensätze sind keine echten SAP-, SharePoint- oder PostgreSQL-Exporte.** Sie simulieren ihre Informationsstruktur, sodass du ohne externe Zugänge üben kannst.

## Geschäftsziele
- **UC1 Vertriebsübersicht:** Auftragsdaten mit Kundendaten und gültigen Preisen auswerten.
- **UC2 Produktionsqualität:** Ausschussquoten und Qualitätsindikatoren je Produkt, Charge und Monat ermitteln.
- **UC3 Wissensassistent:** Fragen zu Produkthandbüchern beantworten, dabei Freigaben, Aktualität, Quellen und Dokumentenrechte beachten.

## Eingebaute Herausforderungen
- Unbekannte Kunden-/Produkt-IDs in ERP-Bestellungen.
- Mögliche Dublette im CRM, die erst fachlich verifiziert werden muss.
- Preisänderung/Überschneidung und fehlende bzw. unplausible Preise.
- Fehlende und fachlich unmögliche Produktionsqualitätswerte.
- Aktuelle und veraltete Produktanleitungen mit unterschiedlichen Intervallen.
- Altarchiv mit unklarem Aufbewahrungsstatus.

## Arbeitsprinzip
Trenne stets nachweisbare Beobachtungen, hypothetische Ursachen und offene Fragen. Lösche nie Daten wegen eines automatischen Scores; Retention, Berechtigungen und Compliance müssen fachlich bestätigt werden.
