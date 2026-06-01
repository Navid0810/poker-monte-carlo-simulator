# Poker Monte Carlo Simulator

## Overview
This project implements a Texas Hold'em poker simulation engine in Python. 
It evaluates poker hands, simulates game outcomes using Monte Carlo methods, and analyses probabilistic properties of poker such as hand frequencies, equity between starting hands, and convergence behaviour of probability estimates.

The goal is to explore how combinatorics and probability theory can be applied to a structured real-world system.

---

## Features

- 52-card deck generation and shuffling
- Texas Hold'em 7-card hand evaluation
- Full poker hand ranking system
- Monte Carlo simulation engine
- Preflop equity estimation between hands
- Empirical validation of known poker probabilities

---

## Key Experiments

### 1. Hand Type Frequencies
Simulates 7-card poker hands and compares empirical frequencies to theoretical values.

### 2. Preflop Equity
Estimates win probabilities for common starting hands (e.g. AA vs KK, QQ vs AKs).

### 3. Law of Large Numbers
Demonstrates convergence of Monte Carlo estimates as sample size increases.

---

## Example Results

- AA vs KK ≈ 82.6% / 17.4%
- QQ vs AKs ≈ 53–47%
- Hand frequency distribution closely matches known theoretical values

---

## Technologies

- Python
- itertools
- collections (Counter)
- Monte Carlo simulation techniques

---
