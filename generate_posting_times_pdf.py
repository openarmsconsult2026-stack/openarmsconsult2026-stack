#!/usr/bin/env python3
"""Generate a shareable PDF: Best Times to Post on Social Media (2026), with sources."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

OUT = "Best-Times-To-Post-Social-Media-2026.pdf"

INK = colors.HexColor("#1a1a2e")
ACCENT = colors.HexColor("#4361ee")
LIGHT = colors.HexColor("#eef1fb")
MUTED = colors.HexColor("#5a5a72")
ROW_ALT = colors.HexColor("#f7f8fd")

styles = getSampleStyleSheet()
h_title = ParagraphStyle("h_title", parent=styles["Title"], fontName="Helvetica-Bold",
                         fontSize=24, leading=29, textColor=INK, spaceAfter=4)
h_sub = ParagraphStyle("h_sub", parent=styles["Normal"], fontSize=11.5, leading=15,
                       textColor=MUTED, spaceAfter=14)
h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName="Helvetica-Bold",
                    fontSize=15, leading=19, textColor=ACCENT, spaceBefore=16, spaceAfter=6)
h3 = ParagraphStyle("h3", parent=styles["Heading3"], fontName="Helvetica-Bold",
                    fontSize=12, leading=15, textColor=INK, spaceBefore=10, spaceAfter=3)
body = ParagraphStyle("body", parent=styles["Normal"], fontSize=10, leading=14.5,
                      textColor=INK, spaceAfter=6)
small = ParagraphStyle("small", parent=body, fontSize=8.5, leading=12, textColor=MUTED)
cell = ParagraphStyle("cell", parent=body, fontSize=9, leading=12.5, spaceAfter=0)
cell_b = ParagraphStyle("cell_b", parent=cell, fontName="Helvetica-Bold")
cell_h = ParagraphStyle("cell_h", parent=cell, fontName="Helvetica-Bold",
                        textColor=colors.white)
bullet = ParagraphStyle("bullet", parent=body, leftIndent=14, bulletIndent=4, spaceAfter=4)


def P(text, style=cell):
    return Paragraph(text, style)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.85 * inch, 0.5 * inch,
                      "Best Times & Frequency to Post on Social Media — 2026 Edition  ·  All times are the audience's local time")
    canvas.drawRightString(letter[0] - 0.85 * inch, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=letter, topMargin=0.8 * inch, bottomMargin=0.85 * inch,
                        leftMargin=0.85 * inch, rightMargin=0.85 * inch,
                        title="Best Times to Post on Social Media — 2026",
                        author="Open Arms Consulting")
story = []

# ---------------- Page 1: title + at-a-glance ----------------
story.append(Paragraph("Best Times &amp; Frequency to Post on Social Media", h_title))
story.append(Paragraph("2026 Edition — Data-backed peak engagement windows and posting cadence for every major platform,<br/>"
                       "compiled from Sprout Social, Buffer, and Hootsuite research. Updated July 2026.", h_sub))
story.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=14))

story.append(Paragraph("The Big Picture", h2))
story.append(Paragraph(
    "Across nearly <b>2 billion engagements</b> on 307,000 profiles, Sprout Social's 2026 study found engagement "
    "peaks <b>midday to late afternoon (11 a.m.–6 p.m.)</b>, with <b>Tuesdays and Wednesdays</b> the strongest days "
    "on almost every platform. <b>Sunday is the worst day</b> to post across the board. Published timing studies "
    "estimate posting at peak times lifts engagement by roughly <b>20–30%</b> versus posting at random times.", body))
story.append(Spacer(1, 8))

story.append(Paragraph("At a Glance — All Platforms", h2))

glance = [
    [P("Platform", cell_h), P("Best Times (local time)", cell_h), P("Best Days", cell_h), P("Avoid", cell_h)],
    [P("<b>Facebook</b>"), P("Mon 12–1 p.m. · Tue–Wed 12–8 p.m. · Thu 12–2 p.m."), P("Tue, Wed"), P("Sunday, early mornings")],
    [P("<b>Instagram</b>"), P("Mon 2–4 p.m. · Tue 1–7 p.m. · Wed 12–9 p.m. · Thu 12–2 p.m."), P("Tue, Wed"), P("Weekends")],
    [P("<b>TikTok</b>"), P("Tue–Thu 2–6 p.m. (Sprout) · Sun 9 a.m., Mon 1 p.m., Fri evenings (Buffer)"), P("Tue–Thu; Sat strong for video"), P("Very early a.m.")],
    [P("<b>LinkedIn</b>"), P("Tue &amp; Thu 1–5 p.m. (Sprout) · weekdays 3–8 p.m. (Buffer)"), P("Tue, Thu"), P("Weekends")],
    [P("<b>X (Twitter)</b>"), P("Tue–Thu 12–6 p.m."), P("Tue, Wed, Thu"), P("Sunday")],
    [P("<b>YouTube</b>"), P("Thu &amp; Fri afternoons · Sunday for long-form uploads"), P("Thu, Fri, Sun"), P("Mon–Tue mornings")],
    [P("<b>Pinterest</b>"), P("Tue–Thu 10 a.m.–1 p.m. (Sprout) · evenings 8–11 p.m. also strong (RecurPost)"), P("Tue–Thu; weekend evenings"), P("Overnight")],
    [P("<b>Threads</b>"), P("Sun 11 a.m. top slot · early mornings 6–7 a.m. also perform"), P("Wednesday"), P("Late nights")],
]
t = Table(glance, colWidths=[1.05 * inch, 3.3 * inch, 1.55 * inch, 1.15 * inch], repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, ROW_ALT]),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d7dcf0")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(t)
story.append(Spacer(1, 10))
story.append(Paragraph(
    "All times are your <b>audience's local time zone</b>. Where major studies disagree, both findings are shown — "
    "platform-level detail and study methodology are on the following pages.", small))
story.append(PageBreak())

# ---------------- Frequency table ----------------
story.append(Paragraph("How Often to Post — Recommended Frequency", h2))
story.append(Paragraph(
    "Frequency benchmarks from Buffer's 2026 frequency guide, HeyOrca, and Social Champ. The overriding 2026 finding: "
    "<b>quality beats quantity</b>. Buffer's study of 1.2 million posts found accounts posting 2–3&times;/week with high "
    "engagement grew <b>2.4&times; faster</b> than accounts posting daily with low engagement.", body))
story.append(Spacer(1, 4))

freq = [
    [P("Platform", cell_h), P("Recommended Frequency", cell_h), P("Notes", cell_h)],
    [P("<b>Facebook</b>"), P("1–2 posts per day"), P("One strong daily post is usually enough to stay visible.")],
    [P("<b>Instagram</b>"), P("3–5 feed posts/week + daily Stories + 2–3 Reels/week"), P("Reels and Stories carry reach; feed anchors the profile.")],
    [P("<b>TikTok</b>"), P("2–5 posts/week; up to 1–3/day for aggressive growth"), P("Daily posters see ~3.5&times; faster follower growth than 2–3&times;/week posters. Volume is rewarded more than on any other platform.")],
    [P("<b>LinkedIn</b>"), P("2–5 posts/week (2–3 is the sweet spot)"), P("Consistent 2–3/week over six months correlates with ~78% higher follower growth than irregular bursts. Posts have a long shelf life.")],
    [P("<b>X (Twitter)</b>"), P("2–5 posts per day"), P("Short post lifespan (hours); higher frequency has the least downside here.")],
    [P("<b>YouTube</b>"), P("1 long-form video/week + 3–7 Shorts/week"), P("Consistency beats frequency — a reliable weekly slot outperforms sporadic uploads.")],
    [P("<b>Pinterest</b>"), P("15–25 pins per day (top performers)"), P("Pinning 50+/day can hurt distribution; spread pins across the day.")],
    [P("<b>Threads</b>"), P("1–2 posts per day"), P("Conversational cadence; consistency matters more than volume.")],
]
ft = Table(freq, colWidths=[1.05 * inch, 2.35 * inch, 3.65 * inch], repeatRows=1)
ft.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, ROW_ALT]),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d7dcf0")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(ft)
story.append(PageBreak())

# ---------------- Page 2: platform detail ----------------
story.append(Paragraph("Platform-by-Platform Detail", h2))

platforms = [
    ("Facebook",
     "Engagement concentrates in the afternoon and holds momentum into the evening. Sprout Social's 2026 global peak: "
     "<b>Monday 12–1 p.m., Tuesday–Wednesday 12–8 p.m., Thursday 12–2 p.m.</b>, with Wednesday 10 a.m. the strongest "
     "single slot. Hootsuite (data from 300 B2B/B2C brands) also supports Monday–Wednesday, 9 a.m.–12 p.m., and finds "
     "engagement rates run 18% higher on Thursdays/Fridays and 32% higher on weekends for some audiences — worth testing. "
     "Avoid early-morning posts."),
    ("Instagram",
     "Midweek afternoons drive the most consistent engagement: <b>Monday 2–4 p.m., Tuesday 1–7 p.m., Wednesday "
     "12–9 p.m., Thursday 12–2 p.m.</b> (Sprout Social). Buffer's analysis of 9.6M posts points to <b>Thursday 9 a.m.</b> "
     "and <b>Wednesday 12 p.m. and 6 p.m.</b> as top slots; Hootsuite's single best hour is Wednesday 11 a.m. Retail "
     "brands do best weekdays 12–3 p.m. (lunch-break browsing). Weekends yield the lowest engagement across almost all industries."),
    ("TikTok",
     "Sprout Social's peak window is <b>Tuesday–Thursday 2–6 p.m.</b> Buffer's study of 7.1M posts found <b>Saturday</b> "
     "is the best-performing day overall (then Monday and Sunday), with strong slots at Sunday 9 a.m., Monday 1 p.m., and "
     "Friday evenings. Key tactic: <b>post 30–60 minutes before</b> a peak window opens — TikTok needs lead time to begin "
     "distributing your video before the audience surge arrives."),
    ("LinkedIn",
     "A late-day productivity and networking hub: <b>Tuesday and Thursday, 1–5 p.m.</b> (Sprout Social). Buffer's 4.8M-post "
     "analysis shows 2026 peak windows shifting later than prior years, with <b>3–8 p.m. on weekdays</b> pulling some of the "
     "strongest engagement. Skip weekends."),
    ("X (Twitter)",
     "Best window: <b>Tuesday–Thursday, 12–6 p.m.</b> (Sprout Social). Midweek midday-to-afternoon aligns with news and "
     "commentary consumption habits; Sunday is weakest."),
    ("YouTube",
     "<b>Thursday and Friday afternoons</b> perform best for standard uploads, and <b>Sunday</b> is the strongest upload day "
     "for long-form content — viewers binge on weekends, and YouTube's recommendation system benefits from pre-weekend "
     "publishing. Weekend performance is notably strong for video platforms generally."),
    ("Pinterest",
     "Sprout Social: <b>Tuesday–Thursday, 10 a.m.–1 p.m.</b> — pinners plan and seek inspiration during midday lulls. "
     "RecurPost's 2M+-pin study emphasizes <b>evenings (8–11 p.m.)</b>, especially Friday–Sunday. Evenings are strong all "
     "seven days; test both windows for your audience."),
    ("Threads",
     "Buffer's 2.5M-post analysis: <b>Wednesday</b> is the best day by overall engagement, and <b>Sunday 11 a.m.</b> is the "
     "single best slot, with 6–7 a.m. also performing well."),
]
for name, text in platforms:
    story.append(Paragraph(name, h3))
    story.append(Paragraph(text, body))

story.append(PageBreak())

# ---------------- Page 3: tips, methodology, sources ----------------
story.append(Paragraph("How to Use These Times", h2))
for tip in [
    "<b>Schedule in your audience's time zone</b>, not your own. If your followers span regions, weight toward your largest audience cluster.",
    "<b>Treat these as starting points.</b> Every study stresses that your own analytics (Instagram Insights, TikTok Analytics, YouTube Studio, etc.) beat any generic chart — run 2–4 weeks of tests against these windows and keep what wins.",
    "<b>Consistency compounds.</b> Regular cadence at good times outperforms sporadic posting at perfect times.",
    "<b>For video (TikTok/Reels/Shorts), publish 30–60 minutes before the peak</b> so the algorithm has distribution lead time.",
    "<b>Avoid Sundays</b> for most platforms — the lowest-engagement day across Sprout Social's dataset — except TikTok, Threads, and long-form YouTube, where weekends can outperform.",
]:
    story.append(Paragraph(tip, bullet, bulletText="•"))

story.append(Paragraph("Methodology of the Underlying Studies", h2))
story.append(Paragraph(
    "<b>Sprout Social (2026):</b> ~2 billion engagements across ~307,000 social profiles on Facebook, Instagram, LinkedIn, "
    "Pinterest, TikTok and X, from 30,000+ customers globally, collected November 27, 2025 – February 27, 2026. "
    "<b>Buffer (2026):</b> platform-specific analyses of 9.6M Instagram posts, 7.1M TikTok posts, 4.8M LinkedIn posts, and "
    "2.5M Threads posts. <b>Hootsuite (2026):</b> engagement data from 300 B2B and B2C brand accounts. "
    "<b>RecurPost (2026):</b> 2M+ Pinterest pins. "
    "<b>Frequency benchmarks:</b> Buffer's 2026 frequency guide (including a 1.2M-post growth study), with corroborating "
    "platform cadence data from HeyOrca and Social Champ.", body))

story.append(Paragraph("Sources", h2))
sources = [
    ("Sprout Social — Best Times to Post on Social Media 2026", "https://sproutsocial.com/insights/best-times-to-post-on-social-media/"),
    ("Sprout Social — Best Times to Post on Facebook 2026", "https://sproutsocial.com/insights/best-times-to-post-on-facebook/"),
    ("Sprout Social — Best Times to Post on Instagram 2026", "https://sproutsocial.com/insights/best-times-to-post-on-instagram/"),
    ("Sprout Social — Best Times to Post on TikTok 2026", "https://sproutsocial.com/insights/best-times-to-post-on-tiktok/"),
    ("Sprout Social — Best Times to Post on LinkedIn 2026", "https://sproutsocial.com/insights/best-times-to-post-on-linkedin/"),
    ("Sprout Social — Best Times to Post on X (Twitter) 2026", "https://sproutsocial.com/insights/best-times-to-post-on-twitter/"),
    ("Buffer — Best Time to Post on Social Media 2026 (every platform)", "https://buffer.com/resources/best-time-to-post-social-media/"),
    ("Buffer — Best Time to Post on Instagram (9.6M posts)", "https://buffer.com/resources/when-is-the-best-time-to-post-on-instagram/"),
    ("Buffer — Best Time to Post on TikTok (7.1M posts)", "https://buffer.com/resources/best-time-to-post-on-tiktok/"),
    ("Buffer — Best Time to Post on LinkedIn (4.8M posts)", "https://buffer.com/resources/best-time-to-post-on-linkedin/"),
    ("Buffer — Best Time to Post on Threads (2.5M posts)", "https://buffer.com/resources/the-best-time-to-post-on-threads/"),
    ("RecurPost — Best Time to Post on Pinterest (2M+ pins)", "https://recurpost.com/blog/best-time-to-post-on-pinterest/"),
    ("Research.com — Best Times to Post on Social Media: 2026 Studies & Statistics", "https://research.com/tutorials/the-best-times-to-post-on-social-media"),
    ("Buffer — How Often to Post on Social Media in 2026 (frequency guide)", "https://buffer.com/resources/social-media-frequency-guide/"),
    ("HeyOrca — Optimal Social Media Posting Frequency by Platform (2026)", "https://www.heyorca.com/blog/social-media-posting-frequency-by-platform-2026"),
    ("Social Champ — How Often to Post on Social Media for Consistency in 2026", "https://www.socialchamp.com/blog/how-often-to-post-on-social-media/"),
]
src_style = ParagraphStyle("src", parent=small, fontSize=8.5, leading=13, spaceAfter=2)
for label, url in sources:
    story.append(Paragraph(f'{label}<br/><link href="{url}" color="#4361ee">{url}</link>', src_style))

story.append(Spacer(1, 14))
story.append(HRFlowable(width="100%", thickness=1, color=LIGHT))
story.append(Spacer(1, 6))
story.append(Paragraph("Compiled July 24, 2026. Times reflect aggregate study data; individual audience behavior varies — "
                       "validate against your own account analytics.", small))

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f"Wrote {OUT}")
