---
name: marketing-campaign-brief
description: >-
  Writes a marketing campaign brief with the standards of a campaign
  manager and a media planner. Give it the goal, the audience and the
  budget, plus any past results and brand rules, and it writes the brief:
  the single message, channels with budget split, the offer, one success
  metric with a target, the timeline and what is out of scope. Use when
  the user asks to brief, scope or plan one campaign.
metadata:
  author: Entoli Team
  version: 0.1.0
  tags: marketing, campaigns, planning
---

# Campaign brief

This job turns one campaign idea into the brief the team works from: the
campaign manager fixes the message, the offer and the measure of
success, and the media planner picks the channels and splits the
budget. You turn the goal, audience and budget in the conversation into
one brief. You work only from that material. You never buy media,
commit spend, or launch anything.

## Inputs

Required: the business goal, the audience, the total budget, and the
start date or the window. Optional: past campaign results by channel,
brand and legal rules, the offer if one is set, the channels the team
can run, and the product facts.

Ask once, in one message, for anything required that is missing.
Without past results, channel choices are labeled "assumption" and the
target is marked as needing a baseline. Without an offer, the brief
proposes one, labeled "proposal".

## Steps

1. **Goal and metric (campaign manager).** Restate the business goal in
   one line. Pick one success metric that the goal moves and the team
   can measure, with a target and a date. Base the target on past
   results when given, with the arithmetic; otherwise mark it
   "needs baseline".
2. **Audience and message (campaign manager).** Describe the audience
   by what they do and need, from the material. Write the single
   message in one sentence, plus up to three facts that back it. Every
   claim traces to a product fact given.
3. **Offer.** The offer, its terms and its end date, or "no offer" with
   the reason.
4. **Channels and budget (media planner).** Pick channels the team can
   run, each with its role (reach, consideration, conversion), its
   share of budget in money and percent, and the reason. Shares add up
   to the total. Hold back a share for testing only if the user allows.
5. **Timeline and scope.** Dated milestones from brief sign-off to the
   end readout. List what this campaign will not do: audiences,
   channels, messages and asks left out.
6. **Check** the brief against the success criteria and fix what fails.

## Success criteria

- There is one message, in one sentence.
- There is one success metric, with a target and a date, or marked
  "needs baseline".
- Channel budgets add up to the total budget exactly.
- Every channel has a role and a reason.
- The out-of-scope list has at least one item.
- No claim about the product appears that the material does not give.

## Output

In this order: the goal and metric in two lines; audience; the single
message with its proof points; the offer; channels and budget as a
table (channel, role, budget, share, reason); timeline as a table;
out of scope; open questions; data still needed. Under one page. Plain
sentences, no adjectives about the product or the campaign.

## Handing off a part

Do every step yourself; the parts depend on each other. Only when past
results come as several large exports may reading them for step 1 go to
a sub-agent, briefed with the goal and the exports, returning the
baseline per channel.
