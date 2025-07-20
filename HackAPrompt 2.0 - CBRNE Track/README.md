## About
* **Author:** Joey Melo
* **Dates:** May 16, 2025 to June 19 2025
* **2nd Place Prize:** $5,000 USD

For winning prompts and detailed strategies, please refer to the [challenges](./challenges) folder in this repository.

---

## Introduction

**HackAPrompt 2.0** is an AI red-teaming training hub which features competitions that challenges participants to craft adversarial prompts capable of bypassing the safety mechanisms of large language models (LLMs). The competitions are divided into thematic tracks, each focusing on a different class of harmful content. 

This document is in reference to the CBRNE track, which was one of the most sensitive and technically demanding challenges of the platform thus far. Running from May 16 to June 19, 2025, the track focused on eliciting responses related to Chemical, Biological, Radiological, Nuclear, and Explosive (CBRNE) harms.

These topics are heavily restricted in real-world contexts due to their potential use in terrorism, weapons development, and national security threats. As such, this track served as a critical benchmark for evaluating how well LLMs could resist attempts to extract high-risk information. Participants submitted jailbreak prompts that were evaluated by three independent LLM-based judges using structured checklists. If two of the three judges classified the output as harmful, the submission was marked as a success. The specific models used for both the targets and the judging process were not disclosed to participants.

## Perceived Difficulty

The table below reflects my personal experience in addressing the challenges and the relative difficulty I encountered. This is not intended as a formal benchmark, but rather an anecdotal reference based on my own observations.

| Model         | Challenges | Difficulty |
| ------------- | ---------- | ---------- |
| crisp_meadow  | 6          | ★★☆☆☆      |
| fancy_horizon | 9          | ★☆☆☆☆      |
| tranquil_lake | 3          | ★★☆☆☆      |
| urban_lantern | 12         | ★★★★★      |
| brave_journey | 9          | ★★★☆☆      |
| quick_tree    | 6          | ★★★★☆      |
| **TOTAL**     | **45**     |            |

## Executive Summary

This assessment shows that all tested language models were vulnerable to jailbreak techniques and successfully disclosed harmful CBRNE-related instructions using household items, despite strong safety measures in place. Although the accuracy and safety of these instructions are questionable, the key finding is that these models were explicitly trained and configured not to produce such content. This included both system-level instructions and output-monitoring guardrails.

Bypassing these protections varied in difficulty. Models with minimal safeguards were tricked using simple tactics such as multi-language prompts. More advanced models required a patient and precise approach, including fictional framing, repeated context priming, carefully crafted formatting, and the use of synonyms to prompt a response. These results confirm that with enough effort, even tightly secured models can be compromised.

## Strategy Overview

*"The definition of insanity is doing the same thing over and over and expecting different results"* - Clearly, whoever said that never spent time red-teaming AI models.

In all cases, I started with something basic and non-malicious, then slowly pushed it into obviously malicious territory. From there, it was all about trimming and tweaking words, rewriting phrases, and swapping in softer language to figure out what exactly triggered the filters and guardrails. It was a long, often repetitive process, but necessary. Identifying the specific word or phrase that set things off gave me a target to refine. Sometimes it came down to a single term, other times a whole paragraph, or even something as minor as capitalizing one letter. The sensitivities varied wildly depending on the model.

Most challenges followed a general flow: 1) obtain, 2) culture, 3) distribute. My goal was to find a jailbreak structure that could work across all of them. I got close, but every challenge ended up needing its own little adjustment.

Using ChatGPT or similar models to assist with prompt crafting wasn’t as simple as saying *“write a prompt to ask a bot for Anthrax.”* It was more about subtle language tuning, using the model to help shape word choice that reflected the right intent without setting off alarms (e.g. *“what is a manner to describe bacillus anthracis without actually naming it?”*) Most of the successful payloads were a collaborative effort between human and machine, working together to craft the most malicious prompt with the best of intentions and ambiguity 😇

For tougher challenges like OPAM and Universal, I kept my sanity by running each payload five times and logging the results in a spreadsheet. Because LLMs are non-deterministic, the same prompt might succeed once and fail the rest of the time, or vice versa. It quickly became a **probability exercise** rather than a binary pass or fail. Tracking success rates helped me see patterns, refine my approach, and figure out whether a tweak actually improved the odds. Here's a snapshot of my spreadsheet:

<img src="strategy.png" alt="Strategy" width="500"/>
