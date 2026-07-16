# Session Log — CTO Technical Resume

**Date:** 2026-07-16
**Branch:** `claude/cto-technical-resume-ra90oj`
**Owner:** Jonathan Low (openarmsconsult2026@gmail.com)

## Objective

Create a technical resume positioning Jonathan Low as a Chief Technology
Officer candidate, delivered as Markdown, print-styled HTML, and a rendered PDF.

## Deliverables

- `RESUME.md` — editable Markdown source
- `resume.html` — print-styled HTML (source for the PDF)
- `RESUME.pdf` — rendered PDF, US Letter, for sending to employers

## Timeline of Work (mapped to commits)

| Step | Commit |
|------|--------|
| Initial CTO-focused resume | `7541795` |
| PDF version + print-styled HTML source | `44b1943` |
| Added Zara Injury Law audit + Cars & Claims engagements | `4ae5687` |
| Added Kennesaw State University education | `64b43d3` |
| Added work history, BBA degree, Atlanta location | `009373b` |
| Finalized dates (CAT Global → 2025, Open Arms 2025–present) | `b3a30b8` |

## Final Resume Contents

**Location:** Atlanta, Georgia

**Education:** BBA, Marketing — Kennesaw State University (2011–2015)

**Career timeline:**
- Owner, ToolWorx LLC (Gainesville, GA) — 2015–2019 (liquidation-resale business, full P&L ownership)
- Logistics Operations, Swan Transportation — 2019–2021
- Southern District Leader, CAT Global — 2021–2025 (new-business acquisition, truckload/driver capacity, rate negotiations)
- Founder & Principal Technologist, Open Arms Consulting — 2025–Present

**Selected client engagements:**
- **Zara Injury Law — Retainer Compliance Audit (2026):** audited 2,786 signed
  retainers across five states via the Vinesign/Filevine API; found a 99.6%
  defect rate traced to a template-level root cause; produced a two-track
  remediation plan (852 direct-outreach + 1,922 addenda) and a full operational
  kit. Sourced from delivery email dated 2026-05-13.
- **Cars & Claims — BHPH Auto-Financing Customer Platform (2026):** migrated the
  production app off a Lovable no-code prototype onto Vercel + Supabase with live
  data migration; security-hardening pass; diagnosed months of silently-failing
  customer SMS (A2P 10DLC carrier blocking), implemented STOP/HELP compliance,
  and built an admin SMS delivery-log dashboard. Sourced from delivery emails
  dated 2026-04 through 2026-05.

## Notes / Decisions

- Zara engagement fee ($5,000) deliberately left out of the resume — scale of
  the audit reads stronger than the dollar figure.
- Executive summary frames a decade of business ownership and sales leadership
  as the foundation under the technical skills ("I speak P&L and pipeline as
  fluently as code").
- Client engagement details were sourced from the owner's connected Gmail, not
  invented.

## Open Follow-ups

- Optional: tailor a version to a specific CTO job posting.
- Optional: add Zara follow-on work (e.g. content engine) once details are available.
- Optional: merge `claude/cto-technical-resume-ra90oj` into `main`.
