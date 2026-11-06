# Data & AI Readiness – 16-Wochen-Lernprojekt

**16 Wochen × 4 Stunden = 64 Stunden.** Rein synthetisches Lernprojekt für den fiktiven Industriekunden **Musterwerke GmbH**. Keine echten Kundendaten und keine internen statworx-Unterlagen.

## Dein Einstieg
1. Lies [Case Study](docs/CASE_STUDY.md) und [Datenwörterbuch](docs/DATA_DICTIONARY.md).
2. Öffne [Woche 01](weeks/week-01.md) und die sechs Datenquellen unter `data/raw/`.
3. Trage dein eigenes Dateninventar in [Vorlage](deliverables/data_inventory.md) ein.
4. Dokumentiere Arbeitsergebnisse im [Fortschrittstracker](PROGRESS.md).

## Lernmodule (je 2 Wochen)
1. Datentypen: strukturiert, semistrukturiert, unstrukturiert; DP-900.
2. Data Warehouse und OLAP.
3. Data Lake / Lakehouse, Snowflake, Fabric, Databricks.
4. Verteiltes Rechnen und Spark.
5. ETL/ELT, Data Quality und Quality Gates.
6. Datenmodellierung: Star Schema, Snowflake Schema, Data Vault.
7. Marktlandschaft, Cloud-Angebote, Datenmigration und RAG.
8. Operating Model, Data Governance, MDM, Purview und Roadmap.

**Zwischenpräsentation:** nach Woche 8 (32 Stunden). **Abschluss:** nach Woche 16 (64 Stunden).

## Übungen (lokal, ohne Cloud-Zugang)
Python 3.10+ genügt. Die vorhandene Pipeline ist eine Demo für die späteren Wochen; du sollst sie nicht einfach als fertige Lösung übernehmen.

```bash
python3 src/pipeline.py
python3 -m unittest discover -s tests -v
```

Die Pipeline schreibt `data/processed/quality_issues.csv`; dieses Verzeichnis wird nicht versioniert.

## Datenpolitik
Alle Informationen, Personennamen, Kundenunternehmen und Dokumente sind erfunden. Auch in einem öffentlichen Repository dürfen keine echten Kundendaten, Zugangsschlüssel, Verträge oder interne Projektinhalte ergänzt werden.
