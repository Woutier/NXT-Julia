# NXT-Julia
**Exploring the Control of LEGO Mindstorms NXT Robots Using Julia**  
*Author: Wouter Vanderzwalmen*  

---

## 📚 About This Project

This repository is part of my bachelor's thesis titled **"Exploring the Control of LEGO Mindstorms NXT Robots Using Julia"**. The goal of this research project was to investigate whether it is feasible to control the LEGO Mindstorms NXT 2.0 robot using the Julia programming language — a language not originally intended for robotics or this hardware.

By bridging Julia with Python using the `PyCall.jl` library, I was able to communicate with the NXT via the existing `nxt-python` library. This repository contains all the core scripts that were developed and tested during the thesis.

---

## 🧠 Thesis Objectives

- Connect to the LEGO NXT 2.0 brick via USB
- Control the NXT robot's motors using Julia
- Read sensor input (touch sensor)
- Create an autonomous "Roomba-style" rover script
- Build a real-time ZQSD-controlled driving mode using keyboard input
- Compare performance and limitations between Python and Julia implementations

---

## 🗂 Repository Structure

```bash
📁 NXT-Julia/
├── Roomba2.py                 # Python Roomba-style autonomous obstacle avoider
├── zsqd driving.py           # Python script for real-time ZQSD keyboard control
├── Dual motor driving1.py    # Basic synchronous motor test in Python
├── drive_forward.jl          # Julia version of motor driving test
├── roomba.jl                 # Julia Roomba-style script using PyCall
├── ...
