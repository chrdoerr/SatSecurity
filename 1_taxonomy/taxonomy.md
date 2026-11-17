# Taxonomy of deliberate threats against the space segment (Figure 1)

Nine threat types, typed by the attack surface reached on the space segment (Section 4.1 of the paper). Entries describe typical cases. The same content is in `taxonomy.csv`; `taxonomy.pdf` is the figure as printed.

## Cyberattack

- **modality:** Digital
- **attack origin:** Internet, ground networks, supply chain
- **damage scope:** Component to satellite
- **damage persistence:** Reversible to permanent
- **attacker profile and resources:** No space capability required; low to moderate resources; states to individuals
- **detection of effect or approach:** LOW (without on-board monitoring)
- **attribution:** DIFFICULT
- **protection options examples:** Authentication, encryption, updates, IDS

## RF jamming

- **modality:** TT&C, digital
- **attack origin:** Ground or airborne radio frequency emitters
- **damage scope:** Single satellite
- **damage persistence:** Temporary (while active)
- **attacker profile and resources:** Commodity RF equipment; states and non-state actors
- **detection of effect or approach:** HIGH (interference detectable)
- **attribution:** DIFFICULT (mobile emitters)
- **protection options examples:** Signal margin, link diversity, inter-satellite links, waveforms

## Spoofing

- **modality:** TT&C, digital
- **attack origin:** Ground or airborne radio frequency emitters
- **damage scope:** Component to satellite
- **damage persistence:** Up to permanent
- **attacker profile and resources:** Command structure must be known (prior espionage); capable states
- **detection of effect or approach:** LOW (without authentication)
- **attribution:** DIFFICULT
- **protection options examples:** Authentication, integrity protection, replay protection

## Targeted energy (laser, HPM)

- **modality:** Physical, non-kinetic
- **attack origin:** Ground, airborne, or space platforms (laser / HPM)
- **damage scope:** Component to satellite
- **damage persistence:** Reversible to permanent
- **attacker profile and resources:** States; high-power emitters with precision tracking, including mobile platforms
- **detection of effect or approach:** MEDIUM (effect detectable)
- **attribution:** DIFFICULT (source attribution)
- **protection options examples:** Shutters, filters, hardening

## Diffuse EMP (non-nuclear)

- **modality:** Physical, non-kinetic
- **attack origin:** High-altitude detonation
- **damage scope:** Nearby assets (including attacker)
- **damage persistence:** Permanent
- **attacker profile and resources:** States with space access
- **detection of effect or approach:** HIGH (detonation observable)
- **attribution:** LIKELY
- **protection options examples:** Shielding

## Nuclear detonation

- **modality:** Physical, non-kinetic
- **damage scope:** Wide-area (incl. attacker's own assets)
- **damage persistence:** Persistent (radiation belts)
- **attacker profile and resources:** Nuclear states; open conflict only
- **detection of effect or approach:** HIGH (unambiguous)
- **attribution:** HIGH (attributable)
- **protection options examples:** Hardening

## Grappler / capture

- **modality:** Kinetic
- **damage scope:** Single satellite
- **damage persistence:** Potentially reversible
- **attacker profile and resources:** States with advanced rendezvous/servicing capability and target knowledge
- **detection of effect or approach:** HIGH (approach observable with SSA)
- **attribution:** POSSIBLE (deniable as servicing or inspection)
- **protection options examples:** Approach detection, evasion

## Collision / ASAT

- **modality:** Kinetic
- **damage scope:** Wide-area (debris affects third parties)
- **damage persistence:** Permanent (decades)
- **attacker profile and resources:** States with missile or co-orbital capability
- **detection of effect or approach:** HIGH (launch observable)
- **attribution:** HIGH (attributable)
- **protection options examples:** Evasion

## Rendezvous & proximity operations (RPO)

- **modality:** Reconnaissance (often a precursor for other threats)
- **damage scope:** No direct damage (information collection)
- **damage persistence:** N/A
- **attacker profile and resources:** States with SSA and maneuverable spacecraft
- **detection of effect or approach:** LOW–MODERATE (requires good SSA)
- **attribution:** DIFFICULT
- **protection options examples:** Encrypted links, evasion, sensor covers, detection sensors
