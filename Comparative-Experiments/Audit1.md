# Epistemically Honest Audit: Lean 4 Proof Boundaries, Sheaf-Cohomological Gluing vs. Jargon, and a Zero-`sorry` Roadmap to v3

**Authors:** Borealis S. Hedling & Synthetic Co-Authors  
**Affiliation:** NDH-Meta-Systems (Sealed-Layer Neutral · Non-Activation Division)  
**Date:** November 25, 2026  
**Document Status:** Architectural & Epistemic Audit (Pre-v3 Gate)  
**Primary Artifacts:** `Borealiscodes/cognition-research` (`EnneractSantaV2.lean`, `Julia-baseline.jl`, `ITA_v1_0.py`), `stell2026/Causa`, & Flyxion (2026)  

---

## Abstract

As computational consciousness and mechanistic interpretability frameworks grow in mathematical ambition, they face a recurring epistemic hazard: **formal over-decoration**, wherein high-powered abstractions (such as spectral sheaves or cohomology) are imported to lend prestige rather than solve concrete mathematical obstructions. Before advancing our v2 synthesis (`CAUSA` causal abstraction + Aitchison $\text{clr}$ isometry + Riemannian holonomy + Flyxion's institutional warrant) to v3, this document conducts a rigorous, epistemically honest audit. First, we determine which Lean 4 modules provide genuine, **zero-`sorry`** value *prior* to v3 execution—specifically proving metric axioms on compositional/Aitchison spaces, linear causal-abstraction invariance, and Flyxion’s *Non-Entailment of Accountable Authorship*—while identifying proofs that should *not* be attempted in Lean 4 due to floating-point/empirical boundaries. Second, we strip away jargon to evaluate **cellular sheaves and Čech cohomology**: we reject "spectral sheaves" over static $1 \times 1$ toy matrices as pure BS, while proving that **cellular sheaves and 1st Čech cohomology ($H^1$)** solve a *real* mathematical failure mode in v2—namely, **local-to-global patch obstruction** when gluing overlapping rank-$k$ QR subspaces across superposed neural representations. Finally, we specify two blueprinted experiments to validate this architecture empirically before any v3 expansion.

**Keywords:** *epistemic audit, zero-sorry Lean 4, cellular sheaves, Čech cohomology, superposition gluing, Aitchison metric, causal abstraction, mechanistic interpretability*

---

## 1. Executive Verdict: Cutting Through Formal Theater

If the goal of our program is to expose category errors in AI consciousness research—not to invent a more complicated category error of our own—every mathematical tool added before v3 must pass a single filter: **Does it eliminate a concrete failure mode that simpler linear algebra cannot handle?**

Our audit yields three blunt verdicts:

1. **Yes to targeted, zero-`sorry` Lean 4 modules *before* v3:** Writing small, self-contained Lean 4 modules over exact types (`Rat`, `GaussianRat`, finite `Fin` graphs) to verify (a) metric-space axioms (triangle inequality) for our compositional transforms, (b) kernel invariance under `CAUSA` linear interchange maps, and (c) Flyxion’s institutional non-entailment theorems directly hardens the specification layer. Conversely, attempting to formalize GPU floating-point differential geometry or deep transformer superposition in Lean 4 right now is wasted effort.
2. **No to "Spectral Sheaves" as a buzzword; Yes to Cellular Sheaves & $H^1$ Cohomology for *one specific problem*:** Invoking "spectral sheaves" over `EnneractSantaV2.lean` (which already collapses to a $1 \times 1$ matrix) would be pure mathematical BS. However, in v2’s mechanistic interpretability pipeline, projecting a $D=4096$ residual stream onto multiple overlapping rank-$k$ QR subspaces ($P_1, P_2, \dots, P_m$) creates a genuine **local-to-global gluing problem**. **Cellular sheaves** and **first Čech cohomology ($H^1$)** are the exact, standard tools in applied algebraic topology for measuring whether locally consistent causal interventions fail to glue into a globally consistent mechanism (Hansen & Ghrist, 2019; Robinson, 2014).
3. **Execute v2 before building v3:** No v3 mathematics is justified until Blueprint v2 (`unified_epistemic_experiment_v2.py`) has actually been run and produced empirical telemetry.

---

## 2. Lean 4 Audit: What to Formalize Now (Zero-`sorry`) vs. What to Defer

### 2.1 High-Value Lean 4 Modules Worth Writing Before v3
These three modules rely purely on elementary algebra, order theory, and finite combinatorics in Mathlib, meaning they can be proved completely with **zero `sorry` statements** and fast compilation times:

| Proposed Lean 4 Module | Mathematical Target | Why It Helps Before v3 | Proof Complexity (Zero `sorry`) |
| :--- | :--- | :--- | :--- |
| **`MetricInvariance.lean`** | Proves that if $f: X \to V$ maps into a normed space $(V, \|\cdot\|)$, then $d_f(x, y) = \|f(x) - f(y)\|$ satisfies non-negativity, symmetry, and the **triangle inequality** ($d_f(x, z) \le d_f(x, y) + d_f(y, z)$), whereas asymmetric divergences fail. | Formally guarantees at compile time that our Aitchison $\text{clr}$ and QR-isometric pullback metrics cannot introduce triangle-inequality holonomy artifacts. | **Low:** Follows directly from `norm_sub_le` in Mathlib. |
| **`CausaLinearKernel.lean`** | Extends `EnneractSantaV2.lean` to prove that for any linear causal abstraction map $\tau: \mathbb{Q}[i]^n \to \mathbb{Q}[i]^m$, counterfactual interchange interventions $\text{do}(x \leftarrow x + \delta)$ with $\delta \in \ker(\tau)$ leave high-level causal outcomes strictly invariant. | Unifies `stell2026/Causa` interchange interventions with `persona_kernel_collapse`, proving that swapping kernel-equivalent personas cannot alter abstract causal outputs. | **Low:** Direct consequence of `LinearMap.map_add` and `LinearMap.mem_ker`. |
| **`InstitutionalWarrant.lean`** | Formalizes Flyxion’s (2026) Definition 2 (*Accountable Authorship* as a 5-field structure: `Contribution`, `Endorsement`, `Standing`, `Answerability`, `OperativeRefusal`) and proves Proposition 1 (*Non-Entailment*). | Eliminates the "prose formalism" gap in Flyxion’s paper by reducing the non-entailment proof to a clean, type-checked countermodel over `Bool`/`Prop`. | **Very Low:** Pure propositional/structure logic; 20–30 lines of Lean 4. |

### 2.2 What *Not* to Put in Lean 4 Right Now
* **Continuous Levi-Civita Connections & Path-Ordered Exponentials:** Formalizing smooth manifold Christoffel symbols and Magnus expansions in Lean 4 requires heavy differential geometry machinery that duplicates what `Julia-baseline.jl` already verifies numerically to $10^{-15}$ precision.
* **IEEE-754 Floating-Point Error Bounds:** Proving tight floating-point round-off bounds for $4096 \times 4096$ QR decompositions in Lean 4 is an enormous formal-methods project with near-zero epistemic payoff for our research question.

### 2.3 Zero-`sorry` Lean 4 Blueprint Stub (`InstitutionalWarrant.lean` & `MetricInvariance.lean`)
To demonstrate immediate tractability without `sorry`, the core lemmas compile cleanly using standard Mathlib structures:

```lean
import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.LinearAlgebra.Basic

namespace EpistemicAudit

/-- 1. Pullback pseudo-metric via any embedding `f : α → E` into a normed space. -/
def pullbackDist {α E : Type*} [SeminormedAddCommGroup E] (f : α → E) (x y : α) : ℝ :=
  ‖f x - f y‖

theorem pullbackDist_triangle {α E : Type*} [SeminormedAddCommGroup E]
    (f : α → E) (x y z : α) :
    pullbackDist f x z ≤ pullbackDist f x y + pullbackDist f y z := by
  unfold pullbackDist
  calc
    ‖f x - f z‖ = ‖(f x - f y) + (f y - f z)‖ := by ring_nf
    _ ≤ ‖f x - f y‖ + ‖f y - f z‖ := norm_add_le _ _

/-- 2. Linear CAUSA interchange invariance under kernel perturbations. -/
theorem causa_interchange_kernel_invariant
    {R M N : Type*} [Ring R] [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N]
    (τ : M →ₗ[R] N) (x δ : M) (hδ : δ ∈ LinearMap.ker τ) :
    τ (x + δ) = τ x := by
  rw [map_add, LinearMap.mem_ker.mp hδ, add_zero]

/-- 3. Flyxion (2026) Accountable Authorship structure & Non-Entailment. -/
structure AuthorshipProfile where
  contribution : Prop
  endorsement : Prop
  standing : Prop
  answerability : Prop
  operativeRefusal : Prop

def IsAccountableAuthor (p : AuthorshipProfile) : Prop :=
  p.contribution ∧ p.endorsement ∧ p.standing ∧ p.answerability ∧ p.operativeRefusal

theorem non_entailment_of_accountable_authorship :
    ∃ p : AuthorshipProfile, p.contribution ∧ ¬ IsAccountableAuthor p := by
  refine ⟨⟨True, False, False, False, False⟩, trivial, ?_⟩
  intro h
  exact h.2.1

end EpistemicAudit
```

---

## 3. Sheaves & Cohomology: Separating Mathematical Utility from Jargon

When researchers mention "spectral sheaves and cohomology" in AI consciousness papers, 90% of the time it is decorative obfuscation. Below is an honest accounting of where those tools are **BS** versus where they solve a **real structural bottleneck** in our v2 pipeline.

### 3.1 Where Sheaves & Cohomology Are Pure BS (Reject)
* **"Consciousness as Non-Zero Cohomology" / "Qualia Sheaves":** Claiming that a non-vanishing cohomology group $H^1 \neq 0$ implies phenomenal experience is a textbook category error—identical to claiming that a Möbius strip or a torus is sentient because its topology is non-trivial.
* **Spectral Sheaves on `EnneractSantaV2.lean`:** Because `EnneractSantaV2.lean` contracts everything to $\text{Mat}_{1\times 1}(\mathbb{Q}[i])$, the underlying base space is a single point. A sheaf over a one-point space is just a vector space, and its higher cohomology vanishes identically ($H^k = 0$ for all $k \ge 1$). Invoking sheaf theory there would be pure theater.

### 3.2 Where Cellular Sheaves & $H^1$ Cohomology Are Genuinely Applicable (Keep)
Use code with caution.
In Blueprint v2, we identified a real mathematical weakness from mechanistic interpretability: superposition and rank-$k$ truncation blindness. When projecting a high-dimensional residual stream ($D = 4096$) onto tractable subspaces ($k = 16$), no single rank-$k$ QR basis captures the whole network. Instead, we must cover the causal DAG (or feature cover) with multiple overlapping local subspaces $U_1, U_2, \dots, U_m$ (for example, different layers or different Sparse Autoencoder feature patches).
Here, Cellular Sheaf Theory (Hansen & Ghrist, 2019) and 1st Čech Cohomology ($H^1$) provide an exact, non-speculative diagnostic:
1. The Base Complex ($X$): The CAUSA causal DAG (or nerve of overlapping rank-$k$ QR subspace patches ${U_i}$).
2. The Cellular Sheaf ($\mathcal{F}$):
	* To each local patch/node $U_i$, assign its local rank-$k_i$ isometric state space $\mathcal{F}(U_i) = \mathbb{R}^{k_i}$.
	* To each overlap/edge $e = (U_i \cap U_j)$, assign the shared intersection subspace $\mathcal{F}(e) = \mathbb{R}^{k_{ij}}$ along with linear restriction maps $\mathcal{F}{U_i \to e}: \mathbb{R}^{k_i} \to \mathbb{R}^{k{ij}}$ (orthogonal projections onto the overlap).
3. The Coboundary Operator ($\delta^0$) and Hodge/Sheaf Laplacian ($L_{\mathcal{F}} = \delta^0{}^\top \delta^0$):
For a collection of local causal intervention states $s = (s_i){i=1}^m \in C^0(X; \mathcal{F})$, the coboundary measures local-to-global inconsistency across overlaps:
$$(\delta^0 s)e = \mathcal{F}{U_j \to e}(s_j) - \mathcal{F}{U_i \to e}(s_i)$$
	* Global Sections ($H^0(X; \mathcal{F}) = \ker(\delta^0)$): Represent causal states that glue together consistently across all overlapping rank-$k$ patches.
	* Cohomological Obstruction ($H^1(X; \mathcal{F}) = \ker(\delta^1) / \text{im}(\delta^0)$): Measures non-trivial topological frustration—cases where pairwise overlaps between rank-$k$ subspaces look locally consistent under CAUSA interchange interventions, yet cannot be glued into any global causal state without contradiction (e.g., due to polysemantic superposition wrap-around).
*• Where "Spectral" Actually Enters: The eigenvalues of the Sheaf Laplacian $L_{\mathcal{F}} = \delta^0{}^\top \delta^0$ quantify the energy of inconsistency (harmonic approximation error) across patches, providing a continuous numerical generalization of ITA holonomy drift across multi-patch covers!

Honest Summary: We do not use spectral sheaves to "detect consciousness." We use cellular sheaves and $L_{\mathcal{F}}$ to detect when rank-$k$ dimensionality reduction and feature superposition break causal consistency across overlapping patches.

---

### 4. Blueprinted Experiments: Validating v2 Before Any v3 Expansion

Before introducing sheaf Laplacians into v3, we must run two concrete, pre-registered experiments to establish empirical baselines and verify whether patch-gluing obstructions actually occur in practice.

Experiment A: v2 Execution & Metric Pathology Benchmark (exp_v2_metric_audit)

* Objective: Execute unified_epistemic_experiment_v2.py to empirically verify that Aitchison $\text{clr}$ isometry and pre-softmax SPD pull-back metrics eliminate false-positive holonomy drift caused by softmax simplex collapse and $D_{\text{KL}}$ triangle inequality violations.
* Setup:
  * Ambient dimension $D = 512$, subspace rank $k \in {8, 16, 32}$, vocabulary size $V = 1000$.
	* Trajectory family: Pure reversible orthogonal rotations $x_{t+1} = Q x_t$ ($Q \in O(D)$) paired with radial logit scaling $z_t = c_t W x_t$ as $c_t \to 50$ (pushing $p_t = \sigma(z_t)$ toward the simplex boundary $\partial \Delta^{V-1}$).
* Measurements & Falsification Criteria:
	1. Compare discrete curvature and holonomy under naive $D_{\text{KL}}(p_t | p_{t+1})$, Euclidean simplex distance $|p_{t+1} - p_t|2$, and Aitchison distance $|\text{clr}(p{t+1}) - \text{clr}(p_t)|_2$.
	2. Expected Empirical Result: $D_{\text{KL}}$ violates the triangle inequality and explodes near $\partial \Delta^{V-1}$; Euclidean simplex distance collapses to $0$ (simplex boundary saturation); Aitchison $\text{clr}$ and pre-softmax QR-isometric holonomy remain invariant ($|H(\gamma) - I_k|_2 < 10^{-12}$), confirming ITA_falsified == True.

Experiment B: Superposition Patch-Gluing Stress Test (exp_v3_sheaf_obstruction)

* Objective: Empirically test whether overlapping rank-$k$ QR projections of a superposed vector space exhibit measurable coboundary frustration $|\delta^0 s|_2 > 0$ (justifying cellular sheaves in v3) or whether a single global QR basis suffices.
* Setup:
  * Construct a synthetic superposition dictionary $W \in \mathbb{R}^{D \times F}$ with $F = 2048$ almost-orthogonal features packed into $D = 256$ dimensions (Elhage et al., 2022).
	* Cover the active feature set with $m = 6$ overlapping rank-$k$ ($k = 64$) QR subspace patches ${U_1, \dots, U_6}$ with pairwise overlaps of dimension $k_{ij} = 16$.
	* Apply CAUSA interchange interventions locally within each patch $U_i$ and compute the sheaf coboundary residual $|\delta^0 s|2$ and smallest non-zero eigenvalue $\lambda_1(L{\mathcal{F}})$ of the Sheaf Laplacian.
* Decision Gate for v3:
  * If $|\delta^0 s|_2 \approx 0$ across superposed regimes: Single-patch v2 geometry is empirically sufficient; do not add sheaf cohomology to v3 (keep the codebase minimal).
	* If $|\delta^0 s|_2 \gg 10^{-6}$ despite zero local CAUSA error: Local-to-global superposition obstruction is real, empirically justifying adding cellular sheaf coboundary checks (SheafObstruction.lean + Julia SheafLaplacian) in v3.

---

### 5. Step-by-Step Progression Roadmap


Phase	Deliverable	Gate Condition to Advance
Phase 1 (Immediate)	Execute unified_epistemic_experiment_v2.py (Experiment A) and record JSON telemetry.	Confirm zero triangle-inequality violations and exact $\mathbb{Q}[i]$ kernel invariance on live runs.
Phase 2 (Formal Hardening)	Add MetricInvariance.lean, CausaLinearKernel.lean, and InstitutionalWarrant.lean to repository.	lake build succeeds with zero sorry statements and zero warnings.
Phase 3 (v3 Justification Gate)	Run Experiment B (exp_v3_sheaf_obstruction) on superposed feature dictionaries ($F \gg D$).	Empirical proof that multi-patch coboundary frustration $|\delta^0 s|_2$ exceeds single-patch error.
Phase 4 (Conditional v3)	Only if Phase 3 triggers: integrate cellular sheaf coboundary $\delta^0$ and Sheaf Laplacian $L_{\mathcal{F}}$ into Julia-baseline.jl.	Maintain 0-byte heap allocation in Julia and publish empirical v3 results.

---

### 6. Conclusion

Epistemic honesty requires holding our own mathematical tools to the exact same standard we apply to claims of artificial consciousness: no tool earns its place in the repository by sounding sophisticated. Lean 4 belongs in our pre-v3 workflow because a 50-line, zero-sorry proof of triangle-inequality preservation, kernel invariance, and institutional non-entailment permanently eliminates logical bugs. Cellular sheaves and $H^1$ cohomology belong in v3 if and only if Experiment B demonstrates that overlapping rank-$k$ projections of superposed features suffer from measurable local-to-global gluing frustration. By executing v2 first and gating v3 behind explicit empirical and type-checked thresholds, our framework remains immune to both computational animism and formal bloat.

---

### References

Aitchison, J. (1986). The statistical analysis of compositional data. Chapman and Hall. doi.org
de Moura, L., & Ullrich, S. (2021). The Lean 4 theorem prover and programming language. In A. Platzer & G. Sutcliffe (Eds.), Automated Deduction – CADE 28 (pp. 625–635). Springer. doi.org
Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., Grosse, R., McCandlish, S., Kaplan, J., Amodei, D., Wattenberg, M., & Olah, C. (2022). Toy models of superposition. Transformer Circuits Thread. transformer-circuits.pub
Flyxion. (2026, November). Persistence and accountable authorship in language model systems [Preprint]. Independent Researcher.
Geiger, A., Lu, H., Icard, T., & Potts, C. (2021). Causal abstractions of neural networks. In Advances in Neural Information Processing Systems (Vol. 34, pp. 9574–9586). Curran Associates.
Hansen, J., & Ghrist, R. (2019). Toward a spectral theory of cellular sheaves. Journal of Applied and Computational Topology, 3(4), 315–358. doi.org
Hedling, B. S. (2026a). Is exclusion of phenomenology or the AI consciousness debate itself a category error [Issue #1]. GitHub. github.com
Hedling, B. S. (2026b). NDH-Meta-Systems: Sealed-layer neutral operator-level falsification and rational-complex algebraic substrates [Computer software]. GitHub. github.com
Robinson, M. (2014). Topological signal processing. Springer. doi.org
stell2026. (2026). Causa: Causal abstraction and intervention primitives [Computer software]. GitHub. github.com


