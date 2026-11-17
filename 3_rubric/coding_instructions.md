# Coding instructions

## Unit and procedure
- Unit of analysis: one organization, represented by one interview. If a participant's experience involved several missions, code the most recent one.
- Two coders score each transcript independently; agreement is computed before any discussion (Krippendorff's alpha, see `../4_data/agreement.py`); disagreements are then resolved by discussing the transcript, and the consensus value is reported.

## Deductive coding: four areas (rubric)
- Assign one level per area by best fit to the anchors (`rubric_anchors_en.md`, full wording in `rubric_full_de.md`); an organization need not meet every element of an anchor.
- Knowledge (A) is judged against the nine threat types of the taxonomy as far as they reach the actor's own area of responsibility; it summarizes demonstrated breadth, depth and role relevance, not the number of types named.
- Risk practice (C): the process element alone (none, discussed once, one-off, selective, continuous) yields the same assignments.
- Expected targeting (D) refers to an attack attempt against the organization's own mission within one year; 0 = no estimate (question not asked or not answered, e.g. because the mission is unknown to the participant).

## Attributes per organization
- **Chain role** (several allowed): Owner, Operator, Builder, Payload supplier, Component supplier, Test provider, Other; as the participant describes the organization's role in the most recent mission.
- **Domain:** civil research, commercial, military (given by the organization type).
- **Military relevance of the mission:** direct, indirect, none, unknown.
- **Experienced incident:** the organization reports an observed deliberate attack or attack attempt against its own mission (any segment, including jamming). Expected threats, suspicions or attacks on other missions do not count.
- **External security requirement:** a demand by an external party (customer, procurement, superordinate authority or command chain, law, partner) that concerns the protection of the space segment against deliberate attacks. Technical, test, qualification or hazard requirements (e.g. FMEA, debris analysis) and requirements on the supplier's own documentation or IT do not count.
  - **Ask:** the demand requires the organization to justify or account for protection.
  - **Control:** the demand prescribes a specific measure (e.g. encryption) without such an ask.
  - Each organization receives one code: ask, control, or none (an ask takes precedence).

## Inductive coding: reasoning patterns
- The reasoning patterns (Table 3 of the paper) were derived from recurring arguments about the participants' own risk. Assign an organization to a pattern when its participant voices the reasoning; an organization can voice several patterns.
- Mark passages where the interviewer suggested the argument before the participant made it.
