
# Apache Beam Tutorial Series

This repository contains step-by-step tutorials for learning Apache Beam with Python.

---

## 📚 Table of Contents

1. **Beam Basics**
   - [beambasic.py](./beam_tutorial/beambasic.py) 
     *Introduction to Apache Beam concepts: Pipeline, PCollection, Transform.*

2. **Pub/Sub Integration**
   - [pubsub_pipeline.py](./beam_tutorial/pubsub_pipeline.py)  
     *Learn how to read/write streaming data using Google Pub/Sub.*

3. **Introductory Beam Pipeline**
   - ./beam-pubsub-local-lab  
     *Instructions for setting up a local environment for Beam + Pub/Sub.*

---

## 🚀 How to Run
1. Clone repo
   ```bash
   git clone https://github.com/vigneshmailappan/dataengineering.git
   
2. Add virtual env
   ```bash
   python -m venv .venv

3. Install Apache Beam:
   ```bash
   pip install apache-beam
   pip install google-cloud-pubsub
