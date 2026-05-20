# Herpes Agent Post-Launch Report

Status: template only. Fill this after Papu explicitly approves and a public post is actually published. Do not use this template as permission to post, reply, DM, or mutate account settings.

Herpes Agent is a parody fork of [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent). Keep upstream credit visible in the final public record and keep the viral language clearly framed as open-source workflow metaphor.

## 1. Approval Recap

- Approved by: `<Papu / explicit approver>`
- Approval timestamp: `<YYYY-MM-DD HH:MM TZ>`
- Approved account: `<@handle>`
- Approved action scope:
  - [ ] one public post only
  - [ ] profile avatar update
  - [ ] profile header update
  - [ ] limited replies
  - [ ] metrics/read-only monitoring
  - [ ] other: `<describe>`
- Approved asset files:
  - avatar: `<path or none>`
  - header: `<path or none>`
- Approved post text source: `<launch pack option / edited text / direct Papu text>`

## 2. Final Published Post

- Post URL: `<paste final URL>`
- Posted at: `<YYYY-MM-DD HH:MM TZ>`
- Account: `<@handle>`
- Final text:

```text
<paste exact public post text here>
```

- Included links:
  - Repo: `https://github.com/Hesoyam67/herpes-agent`
  - Upstream: `https://github.com/NousResearch/hermes-agent`
  - Demo/docs: `<optional links>`

## 3. Safety / Brand Check

Confirm after posting:

- [ ] Upstream credit is visible.
- [ ] “Herpes Agent” name is correct.
- [ ] No medical advice or medical-realism claims.
- [ ] No actual malware/spam/credential-theft implication.
- [ ] No harassment or targeted nastiness.
- [ ] No unapproved DMs/replies/follows/profile changes happened.
- [ ] Tone is funny/sarcastic but still clear about open-source tooling.

If anything fails, record the correction path before doing more public actions. The rash does not get to improvise with a megaphone.

## 4. Initial Metrics Snapshot

Capture at posting time or soon after:

| Metric | Value | Timestamp |
| --- | ---: | --- |
| GitHub stars | `<n>` | `<time>` |
| GitHub forks | `<n>` | `<time>` |
| GitHub open issues | `<n>` | `<time>` |
| Post views/impressions | `<n or unavailable>` | `<time>` |
| Likes | `<n>` | `<time>` |
| Reposts | `<n>` | `<time>` |
| Replies | `<n>` | `<time>` |
| Profile clicks / link clicks | `<n or unavailable>` | `<time>` |

Commands/read-only checks used:

```bash
gh repo view Hesoyam67/herpes-agent --json stargazerCount,forkCount,issues,url
# Add platform metrics manually or via approved read-only tooling.
```

## 5. Replies Worth Considering

Do not auto-reply unless reply mode was approved. Queue candidates here.

| Link / Author | Summary | Suggested response | Needs approval? |
| --- | --- | --- | --- |
| `<url>` | `<what they said>` | `<draft>` | yes |

## 6. Follow-Up Decisions

- Should we post a demo GIF/video?
  - Decision: `<yes/no/hold>`
  - Notes: `<notes>`
- Should we open a release/tag?
  - Decision: `<yes/no/hold>`
  - Notes: `<notes>`
- Should we invite issues/contributions?
  - Decision: `<yes/no/hold>`
  - Notes: `<notes>`
- Should we continue with another public post?
  - Decision: `<yes/no/hold>`
  - Notes: `<notes>`

## 7. Next Mutations

Turn launch feedback into repo-safe work items:

- [ ] `<issue idea from replies/metrics>`
- [ ] `<demo or docs improvement>`
- [ ] `<safety clarification if needed>`

## 8. Final Notes

What worked:

- `<notes>`

What was cringe and must be burned with disinfectant:

- `<notes>`

What to remember for the next launch loop:

- `<durable lesson, if any>`
