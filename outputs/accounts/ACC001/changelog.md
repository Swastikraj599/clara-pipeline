# Changelog: ACC001

**Transition:** v1 → v2

## What Changed

1. Changed business hours to include Saturday from 8am to noon because Mike confirmed the updated schedule
2. Added call transfer timeout of 30 seconds before trying next number as per Jake's request
3. Updated emergency routing rules with a timeout of 30 seconds and a fail message as per Mike's instructions
4. Added integration constraint to never create a ServiceTrade job for sprinkler leak calls as per Mike's requirement

## Field Diff

| Field | v1 | v2 |
|---|---|---|
| emergency_routing_rules | {'primary': '614-555-0192', 'fallback': '614-555-0100', 'tim | {'primary': '614-555-0192', 'fallback': '614-555-0100', 'tim |
| call_transfer_rules | {'timeout_seconds': None, 'retries': 1, 'fail_message': "We' | {'timeout_seconds': 30, 'retries': 1, 'fail_message': "We'll |
| integration_constraints | ['ServiceTrade'] | ['ServiceTrade: never create job for sprinkler leak calls'] |
| business_hours | {'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Fri | {'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Fri |
