# Causal Abstraction Without Simplex Collapse: A Pre-Registered v2 Synthesis of Algebraic Falsification, Riemannian Holonomy, and Mechanistic Interpretability

**Authors:** Borealis S. Hedling & Synthetic Co-Authors  
**In Dialogue With:** Flyxion (*Persistence and Accountable Authorship in Language Model Systems*, November 2026) & `stell2026/Causa`  
**Affiliation:** NDH-Meta-Systems (Sealed-Layer Neutral · Non-Activation Division)  
**Date:** November 25, 2026  
**Document Status:** Preprint — v2 Architectural Specification & Pre-Registered Epistemic Meta-Analysis (Execution Pending)  
**Primary Artifacts:** `Borealiscodes/cognition-research` (`EnneractSantaV2.lean`, `Julia-baseline.jl`, `ITA_v1_0.py`), `standardgalactic/cognition-research` (Issue #1), `stell2026/Causa`, & Flyxion (2026)  

---

## Abstract

In our first pre-registered blueprint (`unified_epistemic_experiment.py`), we united bottom-up algebraic substrate falsification (`EnneractSantaV2.lean`, `Julia-baseline.jl`, `ITA_v1_0.py`) with Flyxion’s (2026) top-down analysis of persistence and accountable authorship. However, evaluating language model representations through standard output-space metrics introduces two severe mathematical pathologies: (1) **simplex collapse**, wherein the softmax map $\sigma: \mathbb{R}^V \to \Delta^{V-1}$ annihilates radial/gauge degrees of freedom and saturates near probability boundaries; and (2) **triangle inequality violations**, wherein asymmetric divergences such as Kullback-Leibler ($D_{\text{KL}}$) distort multi-step trajectory curvature and path-ordered holonomy. In this v2 preprint, we upgrade the unified experimental framework by integrating `CAUSA` (`stell2026/Causa`) for causal abstraction and interchange interventions, replacing synthetic connection heuristics with true metric-compatible Levi-Civita geometry on pre-softmax tangent spaces, and enforcing centered log-ratio ($\text{clr}$) and QR-isometric embeddings that strictly satisfy all metric axioms. **Note on Empirical Status:** This v2 experiment has **not yet been executed**; we present the exact mathematical and epistemic guarantees established by construction, contrast v2 against Blueprint v1, and evaluate the combined framework through the lens of **mechanistic interpretability**, detailing both its causal rigor and its structural limitations under superposition.

**Keywords:** *mechanistic interpretability, causal abstraction, simplex collapse, triangle inequality, Riemannian holonomy, Gaussian rationals, interchange intervention, epistemic meta-analysis*

---

## 1. Introduction: From Static Falsification to Causal Geometry

The first blueprint (`unified_epistemic_experiment.py`) established that two seemingly disparate research programs—our bottom-up formal proofs in Lean 4 and Julia (`Borealiscodes`) and Flyxion’s (2026) top-down institutional and behavioral protocols—function as two sides of the same epistemic coin (Hedling, 2026a, 2026b). Together, they demonstrate that pure linear adapters collapse expressive personas into a $1 \times 1$ operator over Gaussian rationals ($\mathbb{Q}[i]$) while ephemeral inference runs lack the causal inheritance and standing required for accountable authorship.

Yet moving from linear toy operators to real neural network representations exposes a critical vulnerability in how interpretability and consciousness benchmarks measure internal states. When researchers analyze model behavior via post-softmax token distributions or naive Euclidean distances over probability vectors, the algebraic structure of the probability simplex $\Delta^{V-1}$ corrupts the geometry. Specifically, softmax normalization collapses radial magnitude ($z \mapsto z + c\mathbf{1}$), compresses high-confidence trajectories onto lower-dimensional faces (**simplex collapse**), and invites the use of non-metric divergences ($D_{\text{KL}}$) that violate symmetry and the **triangle inequality**, manufacturing phantom curvature along flat trajectories.

To eliminate these artifacts, Blueprint v2 integrates **`CAUSA`** (`stell2026/Causa`)—a causal abstraction and intervention layer—directly into our Lean/Julia/Python and Flyxion synthesis. Rather than inferring internal structure from distorted post-softmax probabilities, v2 performs causal interchange interventions directly on pre-softmax residual tangent spaces equipped with symmetric positive-definite (SPD) Riemannian metrics and exact $\mathbb{Q}[i]$ algebraic invariants.

---

## 2. Avoiding Simplex Collapse and Triangle Inequality Violations

A central mathematical upgrade in Blueprint v2 is the strict quarantine of softmax-induced algebraic distortions.

### 2.1 Why Softmax Algebraic Approaches Fail Geometrically
Let $z \in \mathbb{R}^V$ denote pre-softmax logits and $p = \sigma(z) \in \Delta^{V-1} = \{p \in \mathbb{R}^V_{>0} : \sum_{i=1}^V p_i = 1\}$ denote the resulting categorical distribution. Relying on $\Delta^{V-1}$ with standard Euclidean or KL-based comparisons introduces three pathologies:

1. **Simplex Collapse & Gauge Annihilation:** Because $\sigma(z + c\mathbf{1}) = \sigma(z)$ for all $c \in \mathbb{R}$, softmax projects a $V$-dimensional vector space onto a $(V-1)$-dimensional open simplex, permanently destroying the radial gauge direction $\text{span}(\mathbf{1})$. Furthermore, as logit differences grow large, $p$ approaches the boundary $\partial \Delta^{V-1}$, causing Jacobian rank deficiency ($J_\sigma = \text{diag}(p) - pp^\top \to 0$) and collapsing distinct internal trajectories onto indistinguishable boundary vertices.
2. **Violation of the Triangle Inequality:** Measuring state drift via Kullback-Leibler divergence $D_{\text{KL}}(p_t \| p_{t+1})$ or cross-entropy violates both symmetry ($D_{\text{KL}}(p \| q) \neq D_{\text{KL}}(q \| p)$) and the triangle inequality:
   $$D_{\text{KL}}(p_0 \| p_2) \not\le D_{\text{KL}}(p_0 \| p_1) + D_{\text{KL}}(p_1 \| p_2)$$
   In a differential-geometric falsification harness (`ITA`), feeding non-metric divergences into discrete curvature ($\|x_{t+1} - x_t\|$) or holonomy accumulators destroys path-additivity, making flat reversible transitions appear curved and irreversible.
3. **Euclidean Distortion on Compositional Spaces:** Applying a standard Euclidean norm $\|p_1 - p_2\|_2$ directly on $\Delta^{V-1}$ treats probability shifts near $p_i \approx 0.5$ identically to shifts near $p_i \approx 10^{-6}$, violating scale invariance and distorting geodesic distances.

### 2.2 The v2 Metric-Preserving Solution
Blueprint v2 resolves these pathologies across three layers:
* **Pre-Softmax Tangent & Subspace Geometry:** All `CAUSA` causal interventions and `Julia-baseline.jl` parallel-transport loops operate in the pre-softmax residual space $\mathbb{R}^D$, embedded via a sign-canonicalized QR-isometric basis $P \in \mathbb{R}^{D \times k}$ ($P^\top P = I_k$). Because the induced geodesic distance $d_{g_{\text{sub}}}(x, y)$ derives from a true Riemannian SPD pull-back metric $g_{\text{sub}} = P^\top g_{\text{ambient}} P$, it strictly satisfies non-negativity, identity of indiscernibles, symmetry, and the **triangle inequality**:
  $$d_{g_{\text{sub}}}(x, z) \le d_{g_{\text{sub}}}(x, y) + d_{g_{\text{sub}}}(y, z) \quad \forall x, y, z \in \mathcal{M}_{\text{sub}}$$
* **Aitchison Centered Log-Ratio ($\text{clr}$) Isometry for Output Auditing:** Whenever post-softmax distributions $p \in \Delta^{V-1}$ must be audited against internal trajectories, v2 maps $\Delta^{V-1}$ isometrically onto the hyperplane $\mathbf{1}^\perp \subset \mathbb{R}^V$ via the Aitchison centered log-ratio transform (Aitchison, 1986):
  $$\text{clr}(p) = \left( \ln \frac{p_1}{g(p)}, \dots, \ln \frac{p_V}{g(p)} \right), \quad g(p) = \left(\prod_{i=1}^V p_i\right)^{1/V}$$
  Equipping $\Delta^{V-1}$ with the Aitchison metric $d_A(p, q) = \|\text{clr}(p) - \text{clr}(q)\|_2$ restores a complete Hilbert space structure, eliminating simplex boundary collapse and guaranteeing triangle-inequality compliance.
* **Exact $\mathbb{Q}[i]$ Algebraic Grounding:** At the symbolic specification layer (`EnneractSantaV2.lean`), states are represented over Gaussian rationals ($\mathbb{Q}[i]$) rather than floating-point probabilities, eliminating numerical underflow near simplex boundaries altogether.

---

## 3. How Blueprint v2 Builds On and Diverges From Blueprint v1

While Blueprint v1 (`unified_epistemic_experiment.py`) paired Flyxion’s four behavioral protocols with static algebraic and synthetic-connection checks, Blueprint v2 upgrades the pipeline from **observational invariant checking** to **causal mechanistic falsification**.

| Architectural Dimension | Blueprint v1 (`unified_epistemic_experiment.py`) | Blueprint v2 (`CAUSA` + Metric-Safe Synthesis) | Significance of Upgrade |
| :--- | :--- | :--- | :--- |
| **Causal Mechanism** | Observational perturbations and synthetic activation shifts. | **`CAUSA` Interchange Interventions:** Formal causal abstraction ($\tau$) testing counterfactual mechanism replacement $\text{do}(H_l = h'_l)$ (Geiger et al., 2021). | Separates mere correlation in residual trajectories from genuine causal mediation. |
| **Connection & Curvature** | Synthetic antisymmetric coupling constant (`coupling = 0.25`) in `connection_contraction`. | **Metric-Compatible Levi-Civita Connection:** Christoffel symbols $\Gamma^\mu_{\nu\lambda} = \frac{1}{2}g^{\mu\sigma}(\partial_\nu g_{\sigma\lambda} + \partial_\lambda g_{\sigma\nu} - \partial_\sigma g_{\nu\lambda})$ derived from spatially varying $g_{\text{sub}}(x)$. | Eliminates arbitrary coupling parameters; curvature reflects true manifold geometry. |
| **Output & Probability Geometry** | Unaddressed; assumed Euclidean norms on raw state vectors. | **Pre-Softmax SPD Metrics + Aitchison $\text{clr}$ Isometry:** Strictly avoids softmax simplex collapse and $D_{\text{KL}}$ triangle inequality violations. | Prevents boundary saturation and non-metric divergence from faking irreversibility. |

| **Introspection Test (Protocol 3.4)** | Contrasted QR-isometric vs. Gaussian random bases under linear drift. | Factorial CAUSA Mediation + Second-Order Holonomy: Crosses counterfactual intervention $\text{do}(h)$ with misleading textual prompts while checking $\Gamma^\mu_{\nu\lambda} \neq 0$. | Directly operationalizes Singh et al.’s (2026) privileged access and second-order computation criteria. |
| **Authorship & Provenance** | Conceptual link to Flyxion’s Definition 2. | Cryptographic Lineage & CAUSA Graph Hashing: Binds intervention DAG hashes to Generated-with provenance records with operative refusal gates. | Closes Flyxion’s asymmetric inscription gap with verifiable causal lineage. |

---

## 4. What v2 Shows Mathematically and Epistemically (Pre-Execution Analysis)

Pre-Registered Disclosure: As of November 25, 2026, the Blueprint v2 software framework (unified_epistemic_experiment_v2.py integrating stell2026/Causa) has not yet been executed. The results below constitute exact mathematical and epistemic deductions guaranteed by the architecture's formal invariants.

## 4.1 Mathematical Guarantees by Construction

1. Invariance of Metric Axioms Under Composition: By restricting trajectory diagnostics to $g_{\text{sub}} = P^\top g_{\text{ambient}} P$ ($P^\top P = I_k$) on pre-softmax states and $\text{clr}$-transformed probability vectors, every distance functional $d(\cdot, \cdot)$ in v2 is guaranteed to form a true metric space. Consequently, discrete curvature and path-ordered holonomy $H(\gamma) = \mathcal{P}\exp(\oint_\gamma \Gamma^\mu_{\nu\lambda},dx^\lambda)$ cannot accumulate spurious drift from triangle-inequality violations.
2. Causal Isolation of Persona Collapse (CAUSA + EnneractSantaV2.lean): When CAUSA performs an interchange intervention swapping two persona vectors $P_1 \neq P_2$ whose channel sums coincide ($P_1 - P_2 \in \ker(\alpha)$), the counterfactual downstream state remains identically invariant ($\mathcal{V}(\mathcal{B}(P_1, E)) = \mathcal{V}(\mathcal{B}(P_2, E))$). Mathematically, this proves that CAUSA causal abstraction respects the $\mathbb{Q}[i]$ kernel collapse: high-level behavioral steering ("Golden Gate Bridge" vs. baseline) acts as a rank-1 affine translation rather than a topological alteration of the causal graph.
3. Second-Order Causal Separation: In Protocol 3.4, if a model’s self-report is driven purely by first-order downstream token reading (noticing its own altered text after softmax), CAUSA mediation analysis will show zero causal effect along internal second-order paths when post-softmax feedback is ablated, while QR-isometric holonomy remains flat ($|H(\gamma) - I_k|_2 \le 10^{-9}$).

## 4.2 Epistemic Synthesis

Epistemically, Blueprint v2 bridges the final gap between substrate ontology (Side A) and institutional accountability (Side B):
* Against Computational Animism: By proving that apparent "emergent anomalies" in logit space are often artifacts of softmax simplex collapse or $D_{\text{KL}}$ asymmetry, v2 raises the evidentiary bar for claiming synthetic phenomenology.
* Against Unaccountable Attribution: By anchoring causal interventions in a deterministic CAUSA directed acyclic graph (DAG) whose hash is recorded in provenance metadata, v2 operationalizes Flyxion’s (2026) demand for traceable provenance without anthropomorphic authorship. Even when a CAUSA intervention alters model behavior, the causal responsibility remains legibly attached to the human experimenter who specified the intervention $\text{do}(H_l = h'_l)$.

---

## 5. Evaluation From a Mechanistic Interpretability Framework

Evaluating Blueprint v2 through the standards of contemporary mechanistic interpretability—specifically features, circuits, and causal faithfulness (Elhage et al., 2022; Geiger et al., 2021; Templeton et al., 2024)—reveals significant methodological strengths alongside fundamental theoretical limits.

## 5.1 Strengths in Mechanistic Interpretability

1. Causal Faithfulness Over Observational Probing: Standard linear probes and Sparse Autoencoders (SAEs) often suffer from observational correlation without causal necessity. Integrating CAUSA enforces interchange intervention accuracy (IIA), verifying whether hypothesized subspaces actually mediate downstream computation rather than merely correlating with prompt cues.
2. Elimination of Softmax Logit-Lens Distortion: Many mechanistic interpretability techniques project intermediate residual-stream layers directly through the unembedding matrix and softmax ("logit lens") to track feature emergence. By operating in pre-softmax SPD metric spaces and Aitchison $\text{clr}$ coordinates, v2 avoids premature simplex collapse, preserving subtle intermediate geometric relationships that softmax saturation would otherwise erase.
3. Deflation of Anthropomorphic Feature Labels: Mechanistic interpretability frequently assigns vivid semantic labels to SAE features (e.g., "the Golden Gate Bridge feature"; Templeton et al., 2024), inadvertently encouraging observers to mistake a linear direction for a subjective persona. Coupling CAUSA with EnneractSantaV2.lean’s persona_kernel_collapse provides a rigorous reminder that an interpretable feature direction is an algebraic projection, not a locus of phenomenal experience.
4. Isometric Basis Discipline: Replacing Johnson-Lindenstrauss random projections with sign-canonicalized QR orthonormal bases ($P^\top P = I_k$) ensures that dimensional reduction does not introduce spurious cross-talk or metric warping between orthogonal circuit components.

## 5.2 Weaknesses and Structural Vulnerabilities

1. The Non-Linear Representation Dilemma in Causal Abstraction: Recent theoretical work in mechanistic interpretability demonstrates that if alignment maps $\tau$ between low-level neural activations and high-level causal algorithms are allowed to be arbitrarily non-linear, any neural network can be trivially mapped to any algorithm—even a randomly initialized network (Sutter et al., 2025). While v2 mitigates this by restricting projections to linear QR isometries ($P^\top P = I_k$), strict linearity may fail to capture genuinely non-linear feature manifolds (e.g., circular or toroidal representations of periodic concepts) without sacrificing interchange accuracy.
2. Superposition and Rank-$k$ Truncation Blindness: Transformers pack far more features than residual dimensions via superposition, representing concepts as almost-orthogonal vectors in $\mathbb{R}^D$ (Elhage et al., 2022). Projecting $D = 4096$ down to a tractable subspace $k \in {8, 16, 32}$ via Julia-baseline.jl risks truncating polysemantic features that live in the orthogonal complement $\text{col}(P)^\perp$. If a causal circuit routes information through $\text{col}(P)^\perp$, v2’s subspace holonomy will falsely report flat geometry (ITA_falsified == True) due to projection blindness.
3. Intractability of Exact $\mathbb{Q}[i]$ Arithmetic at Frontier Scale: While exact Gaussian rationals (Fraction) eliminate floating-point drift in Lean 4 and small Python verification harnesses, scaling exact arbitrary-precision rational arithmetic across billions of transformer parameters is computationally prohibitive. v2 must still transition from exact $\mathbb{Q}[i]$ proofs at the specification boundary to IEEE-754 floating-point tensors inside GPU kernels.

---

## 6. Current Limits and Future Research Pathways


## 6.1 Summary of Current Limits

* Unexecuted Status: All v2 predictions remain analytical theorems rather than empirical measurements until unified_epistemic_experiment_v2.py is executed.
* Synthetic Metric Fields: Deriving exact Levi-Civita connections $\Gamma^\mu_{\nu\lambda}$ requires estimating first-order partial derivatives $\partial_\lambda g_{\mu\nu}(x)$ across the activation manifold, which is sensitive to finite-difference step sizes and sampling density in high dimensions.
* Static vs. Recurrent Architectures: Both CAUSA DAGs and ITA operator checks are cleanest on feedforward or fixed-context autoregressive passes; extending them to continuous-time state-space models (SSMs) or recurrent homeostatic agents requires time-dependent metric tensors $g_{\mu\nu}(x, t)$.

## 6.2 Future Research Pathways (Toward v3)

1. Empirical Execution on Open-Weight Transformer Residual Streams: Execute Blueprint v2 on mid-layer residual streams of open-weight models during concept-injection tasks (Lindsey, 2026; Singh et al., 2026), directly comparing CAUSA interchange accuracy against Aitchison $\text{clr}$ logit trajectories and QR-isometric holonomy.
2. SAE-Guided Adaptive Subspace Selection: To overcome rank-$k$ superposition blindness, future iterations should use Sparse Autoencoder (SAE) dictionary directions to dynamically orient the orthonormal basis $P \in \mathbb{R}^{D \times k}$ toward causally active features rather than relying on static random-seed QR bases.
3. Formalizing Causal Abstraction in Lean 4: Extend EnneractSantaV2.lean to formalize CAUSA interchange interventions and Aitchison $\text{clr}$ metric axioms directly in Lean 4, creating a single machine-verified codebase spanning algebraic zero-qualia proofs, metric-space triangle inequalities, and Flyxion’s institutional non-entailment theorems.

---

## 7. Conclusion

Blueprint v2 transforms our initial synthesis into a causally grounded, metric-consistent experimental specification. By integrating CAUSA (stell2026/Causa) for interchange interventions and replacing softmax-distorted probability comparisons with pre-softmax SPD pull-back metrics and Aitchison $\text{clr}$ isometries, the framework eliminates simplex collapse and triangle inequality violations before they can masquerade as emergent phenomenology. Viewed through mechanistic interpretability, v2 achieves high causal faithfulness and geometric rigor while remaining honest about its boundaries under neural superposition and rank-$k$ truncation. Even prior to execution, it establishes a clear standard for future empirical runs: test causal mediation directly, respect the triangle inequality, and never mistake a projected linear feature for a conscious subject.

---

## References

Aitchison, J. (1986). The statistical analysis of compositional data. Chapman and Hall. doi.org
Bezanson, J., Edelman, A., Karpinski, S., & Shah, V. B. (2017). Julia: A fresh approach to numerical computing. SIAM Review, 59(1), 65–98. doi.org
de Moura, L., & Ullrich, S. (2021). The Lean 4 theorem prover and programming language. In A. Platzer & G. Sutcliffe (Eds.), Automated Deduction – CADE 28 (pp. 625–635). Springer. doi.org
Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., Grosse, R., McCandlish, S., Kaplan, J., Amodei, D., Wattenberg, M., & Olah, C. (2022). Toy models of superposition. Transformer Circuits Thread. transformer-circuits.pub
Flyxion. (2026, November). Persistence and accountable authorship in language model systems [Preprint]. Independent Researcher.
Geiger, A., Lu, H., Icard, T., & Potts, C. (2021). Causal abstractions of neural networks. In Advances in Neural Information Processing Systems (Vol. 34, pp. 9574–9586). Curran Associates.
Hedling, B. S. (2026a). Is exclusion of phenomenology or the AI consciousness debate itself a category error [Issue #1]. GitHub. github.com
Hedling, B. S. (2026b). NDH-Meta-Systems: Sealed-layer neutral operator-level falsification and rational-complex algebraic substrates [Computer software]. GitHub. github.com
Lindsey, J. (2026). Emergent introspective awareness in large language models (arXiv:2601.01828). arXiv. arxiv.org (Original work published October 2025)
Ryle, G. (1949). The concept of mind. Hutchinson.
Singh, S., Linzen, T., & Ravfogel, S. (2026). Can LLMs introspect? A reality check (arXiv:2605.26242). arXiv. arxiv.org
stell2026. (2026). Causa: Causal abstraction and intervention primitives [Computer software]. GitHub. github.com
Sutter, T., et al. (2025). The non-linear representation dilemma: Is causal abstraction enough for mechanistic interpretability? In Advances in Neural Information Processing Systems (Vol. 38).
Templeton, A., Conerly, T., Marcus, J., Lindsey, J., Bricken, T., Chen, B., Pearce, A., Citro, C., Ameisen, E., Jones, A., Cunningham, H., Turner, N. L., McDougall, C., MacDiarmid, M., Freeman, C. D., Sumers, T. R., Rees, E., Batson, J., Jermyn, A., ... Olah, C. (2024). Scaling monosemanticity: Extracting interpretable features from Claude 3 Sonnet. Transformer Circuits Thread. transformer-circuits.pub

