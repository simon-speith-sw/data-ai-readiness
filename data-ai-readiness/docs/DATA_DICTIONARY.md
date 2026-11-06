# Datenwörterbuch

| Quelldatei | Primäre Felder | Datentyp | Fachhinweise |
|---|---|---|---|
| `erp_orders.csv` | `order_id,customer_id,product_id,quantity,order_date,sales_region` | strukturiert | Kaufaufträge; Fremdschlüssel nicht technisch erzwungen |
| `crm_customers.csv` | `customer_id,company_name,country,account_manager,consent_marketing` | strukturiert | fiktive B2B-Referenzen |
| `price_list.csv` | `product_id,product_name,currency,unit_price,valid_from,valid_to` | strukturiert | Preisintervalle können konkurrieren |
| `production_quality.csv` | `batch_id,product_id,units_produced,units_defective,inspection_date` | strukturiert | Ausschussquote nur für valide Werte berechnen |
| `documents/*.md` | Metadaten und freier Text | unstrukturiert mit semistrukturierten Metadaten | Freigabestatus und Version überprüfen |
| `legacy_archive.json` | `record_id,path,content_type,last_modified,retention_status,business_value` | semistrukturiert | Löschung nur nach Retention-Prüfung |

## Übungsannahmen zur Sensitivität
ERP/CRM: vertraulich; Preise/Qualität: intern; Dokumente: je nach Freigabe; Legacy: zu prüfen. Diese Kategorien stammen aus dem **fiktiven** Case-Factsheet, nicht aus CSV-Spalten.

## Qualitätsfragen
- Welche Felder sind eindeutige Schlüssel und welche nicht?
- Wie wird ein fachlich gültiger Preis zum Bestellzeitpunkt ermittelt?
- Wo liegt die Golden Source je Datenobjekt?
- Welche Dokumentversion ist gültig? Wie werden Quell-ACLs im Retrieval erhalten?
- Welche Daten bleiben im Quellsystem und welche müssen zentral verarbeitet werden?
