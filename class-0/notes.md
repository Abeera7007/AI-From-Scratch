# 📘 Class 0 | Why We're Doing This the Hard Way

## Let's be honest first

Math has a reputation problem. Most people hear "linear algebra" or "derivatives" and immediately think: *boring, pointless, why do I need this.* Fair enough a LOT of math gets taught disconnected from anything real, so it feels like memorizing symbols for no reason.

Here's the twist though: **you can't actually learn AI without it.** Not because some professor said so because AI models are *literally made of math*. There's no version of "understanding how a neural network thinks" that skips the math part. The math isn't a boring gate you pass through before the "real" AI content starts the math **IS** the AI content.

So instead of running from it, this repo does the opposite: **learn AI completely from scratch, no libraries, no shortcuts** meaning we write the math and the code ourselves, by hand, before ever touching a tool like scikit-learn or PyTorch. Once you understand what's happening underneath, using those libraries later will feel like cheating (in a good way) instead of feeling like magic you don't trust.

## The Rule for This Whole Repo

> If I can't build it myself with plain Python and basic math, I don't actually understand it ,I just know how to call a function.

That's it. That's the whole philosophy. Libraries come *later*, as a reward for doing it the hard way firstnot as a shortcut around it.

## What "a little math" Actually Means Here

We're not doing abstract theoretical math for its own sake. Every concept covered is scoped tight to *only* what shows up when you build AI models nothing more, nothing decorative. Expect:
- Just enough vectors & matrices to represent data and neuron weights
- Just enough dot products to understand what a neuron computes
- Later on: just enough calculus to understand how a model learns from its mistakes

No proofs, no abstract theory, no "why does math work this way" rabbit holes. Just: here's the concept, here's a real example, here's the code.

## How Each Class Will Work

1. **Plain-English intuition first** using a relatable example (a house, a decision, something normal)
2. **Then the math**, showing that the math was just a formal way of writing down what you already understood
3. **Then the code**, built from scratch, no libraries
4. **A short recap** at the end tying it all together

## What's Next

Head to `Class 1` to meet your first real building block: **the neuron** and see that it's really just your own decision-making process, written down as a formula.

---

*No shortcuts. No libraries (yet). Just understanding, one small piece at a time.*
