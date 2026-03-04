# Changelog: ACC002

**Transition:** v1 → v2

## What Changed

1. Changed business hours to include Saturday end time and timezone details because onboarding call confirmed
2. Added heat pump emergency definition because onboarding call introduced new emergency scenario
3. Updated call transfer rules with 40 second timeout and 2 retries because onboarding call specified
4. Added ServiceTitan integration constraints for residential and commercial calls because onboarding call introduced new rules
5. Updated voice style to efficient and direct because onboarding call specified
6. Removed Saturday end time question from questions or unknowns because onboarding call answered

## Field Diff

| Field | v1 | v2 |
|---|---|---|
| questions_or_unknowns | ['Saturday end time', 'Fallback emergency routing', 'Office  | ['Fallback emergency routing', 'Office hours flow summary'] |
| voice_style | None | Efficient, direct, to the point |
| emergency_definition | ['No heat in winter for elderly or infant household', 'Compl | ['No heat in winter for elderly or infant household', 'Compl |
| call_transfer_rules | {'timeout_seconds': None, 'retries': 1, 'fail_message': 'Col | {'timeout_seconds': 40, 'retries': 2, 'fail_message': 'Colle |
| integration_constraints | ['ServiceTitan'] | ['ServiceTitan', 'Residential calls create ServiceTitan job  |
| business_hours | {'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Fri | {'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Fri |
