# Formal Verification Methods Presentations

This repository contains the interactive slide decks for the Formal Verification Methods course content, built using [Slidev](https://sli.dev/).

## Running the Presentations Locally

Use the following npm scripts to launch the interactive presentation server for specific topics:

### Z3 Theorem Prover
```bash
npm run dev:z3
```
*Note: The Z3 presentation includes a local Node.js proxy backend for executing Python constraints interactively on the slides.*

### On Trusting Trust
```bash
npm run dev:trusting-trust
```

### Course Introduction
```bash
npm run dev:intro
```

### Main Index
```bash
npm run dev
```

## Building

To build the presentations into static single-page applications:
```bash
npm run build
```
Or to build all available decks:
```bash
npm run build:all
```
