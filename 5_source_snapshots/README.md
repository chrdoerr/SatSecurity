# Snapshots of changing web sources

Some figures in the paper come from web pages that are updated continuously. This folder keeps the values as retrieved.

| Reference | Statement in the paper | Snapshot | Status |
|---|---|---|---|
| `mcdowell2026active` (J. McDowell, Satellite and Debris Population) | "More than 17,000 active satellites ... as of October 2026" | `mcdowell_active_2026-10-26.txt` | Page retrieved 15 Nov 2026, still showing the data as of 26 Oct 2026: 17,099 active satellites. |
| `mcdowell2026starlink` (J. McDowell, Starlink Statistics) | "Starlink alone operates more than 11,000" | `mcdowell_active_2026-10-26.txt` | The cited page (data as of 9 Nov 2026) has since been updated; the population page above gives 11,148 active Starlinks as of 26 Oct 2026. |
| `celestrak2026satcat` (CelesTrak SATCAT) | "more than 70 active satellites" (Germany) | `celestrak_satcat_GER_payloads_operational_2026-11-15.csv` | 78 payloads. Procedure below. Same count as at the cited access (13 Nov 2026). |
| `esa2026discos` (ESA Space Debris Office, Space Environment Statistics) | "some 47,000 objects ... over a million centimetre-scale fragments" | `esa_discosweb_statistics_2026-11-13.txt` | Page retrieved 16 Nov 2026 (last update 13 Nov 2026): about 47,270 objects regularly tracked; 1.5 million objects of 1–10 cm estimated by statistical models. |

## CelesTrak query

From the full catalog `https://celestrak.org/pub/satcat.csv` (file dated 15 Nov 2026, 04:33 GMT), keep the rows with

- `OWNER` = `GER`,
- `OBJECT_TYPE` = `PAY` (payload),
- `OPS_STATUS_CODE` = `+` (operational) or `P` (partially operational),
- empty `DECAY_DATE` (still in orbit).

This gives the 78 rows of the CSV.
