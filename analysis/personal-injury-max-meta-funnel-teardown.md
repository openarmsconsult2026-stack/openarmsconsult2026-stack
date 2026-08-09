# Personal Injury Max — Meta Ads Funnel Teardown

**Prepared for:** Mike Zara, Zara Injury Law
**Prepared by:** Jonathan Low / Open Arms Consult
**Date:** August 9, 2026
**Source:** Screenshot of `colorado-cl.personalinjurymax.com` opened from the Facebook in-app browser (sent by Mike)

---

## 1. What this company actually is

Personal Injury Max is **not a law firm** — it is a performance lead-generation
operation (a lead broker). The tells:

- **No public footprint.** The brand has no meaningful search presence, no
  reviews, no attorney profiles. Lead brokers deliberately stay invisible;
  the brand exists only to make the ad look legitimate for the 60 seconds it
  takes to fill the form.
- **Geo-coded subdomain:** `colorado-cl.personalinjurymax.com`. This is a
  landing-page factory pattern — one templated quiz page cloned per
  state/campaign (`colorado-cl` = Colorado + a campaign/vertical code, likely
  "case lead" or "car lead"). They spin up a subdomain wherever they have a
  law firm buying leads in that state. Each subdomain gets its own tracking
  segmentation, so conversion data per state stays clean.
- **"Fast Reply" promise.** Their revenue depends on speed-to-lead: the lead
  is sold (per-lead or per-signed-retainer) and transferred to a buyer firm
  or call center within minutes.

**Business model:** run Meta ads under a throwaway direct-response brand →
qualify motor-vehicle-accident victims through a quiz → sell the lead to law
firms. Market rates for qualified MVA leads run roughly $150–$600 per raw
lead and $1,500–$3,500+ per signed retainer depending on state and case type.
If Zara bought from them in the past, our invoices will show exactly which
model we were on — worth pulling before the meeting.

---

## 2. The funnel, deconstructed (what's visible in the screenshot)

### Placement & context
- Opened in the **Facebook in-app browser** on mobile → this is a Meta ads
  click (Facebook/Instagram feed or Reels), mobile-first by design.
- Page loads instantly to a **hero + quiz** with zero navigation, zero exit
  paths, no menu. Single conversion action.

### The hook (hero section)
> "You May Be Owed **More Than You Think** After Your Accident"
> "Most people accept the first offer without ever knowing what their case was *actually* worth"

This is the smartest part of the whole funnel:

1. **It doesn't ask "were you injured?"** — it targets people *further along*:
   people who already have a claim, an insurance offer, or even a lawyer, and
   makes them doubt the number. That reframe ("you're leaving money on the
   table") expands the audience beyond fresh accidents and creates urgency
   without a deadline.
2. **Loss aversion + curiosity gap.** "More than you think" is unfalsifiable
   and personally targeted; the only way to close the gap is to take the quiz.
3. Note this is exactly the **Money Mike value proposition** ("Top Dollar,
   finding the true value in everyone's claim"). They are running Mike's
   positioning as a faceless template. Mike can run it with a real face,
   a real firm, and real results — which beats the template.

### The CTA
> "Check What Your Case Could Be Worth (Takes 30 Seconds)"

- Framed as a **value calculator, not a lawyer consultation**. Asking someone
  to "talk to a lawyer" is high-commitment; "check what your case is worth"
  is a curiosity click. The lawyer appears only after the lead is captured.
- Trust bar of three checkmarks answers the three objections in six words
  each: ✅ No Win No Fee (cost) ✅ Takes 30 Seconds (effort) ✅ Fast Reply
  (delay).

### The quiz ("1 of 10")
- **Multi-step quiz = micro-commitment engine.** Ten small steps convert far
  better than one form. By step 5 the user has sunk effort ("might as well
  finish"). Contact info is almost certainly the *last* step, after
  investment is maximal.
- **Question 1 is a router, not a question.** Every option is a motor vehicle
  accident: Car / Truck / Bicycle-Pedestrian / Motorcycle / Other MVA. They
  only buy-and-sell MVA cases (clear liability, mandatory insurance coverage,
  predictable settlement values). Slip-and-fall and med-mal aren't even
  options. The answer also **prices the lead** — truck and commercial-vehicle
  leads resell for multiples of a standard car-accident lead.
- The remaining ~9 questions are predictable qualifiers: when it happened
  (statute of limitations), who was at fault, injuries/treatment received,
  whether they already have an attorney (dealbreaker), insurance status —
  then name/phone/email with TCPA consent language for the call transfer.

---

## 3. "The Meta algorithm" — what they're actually doing on the ads side

The funnel design *is* the targeting strategy. Here's the machine:

1. **Event-per-step conversion signals.** Each quiz step fires a pixel/CAPI
   event. The campaign is optimized not for clicks or page views but for the
   deep event — "qualified lead completed" — so Meta's delivery algorithm
   learns to find *people who finish the quiz and qualify*, not people who
   click green buttons. This is the core trick: **the quiz manufactures a
   high-quality conversion signal, and Meta's lookalike machinery does the
   targeting for them.**
2. **Broad targeting, creative does the filtering.** Personal injury is not a
   Meta "special ad category," so they can geo-target Colorado freely. Modern
   playbook is broad/Advantage+ audiences with the ad creative and Q1 of the
   quiz doing the qualification — cheap clicks in, the funnel filters.
3. **Server-side tracking (CAPI) almost certainly in place** — iOS privacy
   changes gutted pixel-only tracking; every serious lead-gen shop now runs
   Conversions API with event deduplication, likely passing lead-quality
   scores back as event values.
4. **Landing-page factory per geography** = per-state campaigns with isolated
   conversion datasets, so Colorado performance data never pollutes the
   Wisconsin campaign, and each buyer firm's volume can be throttled
   independently.
5. **Likely value-based optimization:** feeding lead resale value (truck >
   motorcycle > car) back to Meta so the algorithm chases higher-value case
   types over time.
6. **Creative style:** dark-green "money" palette, MAX branding, checkmark
   emoji, mobile-native typography — pure direct response, zero law-firm
   dignity signaling. It works because it looks like a consumer finance tool,
   not an attorney ad.

---

## 4. What this means for Zara / Money Mike

**We should not buy this — we should own this.** A firm running this funnel
in-house has structural advantages a broker can never have:

| | Personal Injury Max (broker) | Money Mike in-house |
|---|---|---|
| Brand | Disposable, faceless | Real attorney, real face, real results |
| Economics | Sells lead at $150–$600+ margin on top of ad cost | We keep the margin; CAC = ad cost only |
| Signal quality | Optimizes to "sellable lead" | We can optimize to **signed retainer** and even case value via CAPI |
| Compliance | Gray-area broker disclosures | Cleaner: we're the actual law firm advertising |
| Speed-to-lead | Sells to whoever answers | Straight into our own intake (Dio's phone team) |

Concretely, the build is: Money Mike-branded quiz funnel ("Find out what your
case is *really* worth") on state subdomains or paths, 8–10 step MVA-routed
quiz, pixel + CAPI events per step, optimization on the signed-retainer
event, intake call within 5 minutes of submission. This slots directly into
the 90-day organic → paid-ads plan Mike already approved in May: same
funnel, our brand, our margin.

**Compliance notes for the in-house version** (needs review per state bar):
attorney-advertising disclaimers, "No Win No Fee" qualified per state rules,
TCPA-compliant consent language on the contact step, and results
disclaimers. As the actual firm we have an easier compliance story than a
broker, but the pages must carry the right fine print per state.

---

## 5. Open questions to answer before/at the meeting

1. **Pull our history with them.** Which states did we buy? Per-lead or
   per-retainer pricing? What did leads cost and what % signed? That gives us
   the CAC benchmark our in-house funnel has to beat.
2. Do we know who's behind Personal Injury Max (contract counterparty name)?
   The public brand is deliberately anonymous.
3. Which states do we want the first Money Mike funnel live in?
4. Budget and timeline for a 2–3 week paid test once the funnel is built —
   this can front-run the 90-day organic milestone since the funnel build is
   independent of follower growth.

---

## 6. Recommended next steps

1. **Meeting with Mike** (invite sent) — walk this teardown, pull the old
   Personal Injury Max invoices, decide build-vs-buy.
2. If build: I'll stand up the Money Mike quiz funnel (landing template,
   quiz logic, pixel + CAPI, intake webhook to the phone team) as the first
   paid-ads deliverable of the 90-day plan.
3. Run their ads through the Meta Ad Library from a normal browser (the
   sandboxed environment here blocks Facebook) to catalog their live
   creatives per state — worth 30 minutes before the meeting.
