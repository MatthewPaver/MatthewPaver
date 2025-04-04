## 📚 Assignment Overview

This practical assignment for COMP318 is composed of **three tasks**, each designed to assess your knowledge of key semantic web technologies:

1. **RDF(S) Modelling**  
2. **Deductive Reasoning with RDF(S)**  
3. **SPARQL Querying and Semantic Data Processing**

All solutions are implemented in Python and documented via PDFs as required. No external libraries or frameworks are used, ensuring compatibility with university systems.

---

## ✅ Task Breakdown & File Mapping

### 🔹 Task 1: RDF(S) Modelling (20 marks)
- **Objective:**  
  Analyse a given RDF graph representing a research collaboration network for:
  - RDF syntax validity
  - Domain/range violations
  - Schema consistency
  - Inferred classification issues

- **Deliverable:**  
  `Task 1/Task1.pdf`  
  A written report answering all modelling questions with justifications.

---

### 🔹 Task 2: RDFS Deductive Reasoning (25 marks)
- **Objective:**  
  Given an RDF graph G:
  - Derive **4 non-trivial RDFS-entailment triples** using rules like domain, range, subClassOf, etc.
  - Prove each derivation
  - Implement a program to compute **all** RDFS entailments
  - Verify the derived triples programmatically

---

### 🔹 Task 3: SPARQL Querying and Semantic Data Integration (45 marks)
- **Objective:**  
Using the **Nobel Laureates KG** and **scientistsBio.ttl**, complete the following:
- Integrate matching entities from both graphs and output `updatedKG.ttl`
- Write and execute SPARQL queries to:
  1. List Chemistry Nobel Laureates born in France awarded with one co-laureate.
  2. Find individuals who won more than one Nobel Prize, with year and name.
  3. Identify Laureates affiliated with German universities who won the Physics prize.
