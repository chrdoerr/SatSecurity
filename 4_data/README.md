# Data

All organizations appear under the pseudonyms of Table 1 (R = civil research, C = commercial, M = military). No transcript text is included.

| File | Content |
|---|---|
| `expert_ratings.csv` | Expert panel estimates (Figure 2): per threat type, number of raters and mean and standard deviation of the 0–5 likelihood of an attempt within one year, per mission domain. GNSS/payload jamming was rated separately and is excluded, as in the paper. |
| `organizations.csv` | Consensus coding per organization: domain, chain roles and military relevance (Table 1), levels A–D (Table 4; D = 0: no estimate), external security requirement (ask / control / none; Appendix D), and reasoning patterns (Table 3). These are the values behind the statistics of Section 6. |
| `reliability_levels.csv` | Levels A–D of both coders, scored independently before consensus. |
| `agreement.py`, `kalpha.py` | Reproduce the agreement values for levels A–D of Section 4.3 (Krippendorff's alpha with bootstrap intervals); run `python3 agreement.py` in this folder (needs numpy). |

