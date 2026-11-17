# World Happiness Report 2026 — Course Project

Analysis of the World Happiness Report 2026 data (Figure 2.1, 2011–2025): national
life evaluations (Cantril ladder, 3-year average) and the share explained by GDP per
capita, social support, healthy life expectancy, freedom, generosity and perceptions
of corruption.

## Repository structure

```
Data/
  raw/WHR26_Data_Figure_2.1.xlsx   original download (2,116 country-year rows)
  working_set.csv                  80% — used for all exploration and modeling
  reporting_set.csv                20% — HELD OUT, untouched until the final phase
  reporting_set.sha256             checksum proving the reporting set is unchanged
src/make_split.py                  script that produced the split
Results/                           final results (added at end of course)
Report/                            final report (added at end of course)
```

## Reporting set (20% hold-out)

- 424 of 2,116 rows, drawn at random with `random_state=42`, stratified by `Year`
  so every year 2011–2025 is represented in the same proportion.
- **Do not open, explore or train on `Data/reporting_set.csv` until the final phase.**
- Verify it is untouched: `sha256sum -c Data/reporting_set.sha256`
  (expected: `45d1254d6b703947b1b47acda7a9ce2646e7216a59220ab033002d6ba6e3f242`).

## Data notes

- Columns: Year, Rank, Country name, Life evaluation (3-year average), Lower/Upper
  whisker, six "Explained by" components, Dystopia + residual.
- The whiskers and "Explained by" columns are missing for roughly half the rows
  (earlier years), so they will need handling in the working set.
- Source: World Happiness Report 2026, Data for Figure 2.1 — https://worldhappiness.report/
