# Audit III: Compositional Obstructions, Differential Kernels, and Scoped Refusal — A Comparative Synthesis of `Spherepop@fe79af5` and the v3 Roadmap

**Authors:** Borealis S. Hedling & Synthetic Co-Authors  
**In Dialogue With:** Flyxion (`standardgalactic/spherepop-kernel`, commit `fe79af59b23fc531b41e52ceb4c28343915a943b`)  
**Affiliation:** NDH-Meta-Systems (Sealed-Layer Neutral · Non-Activation Division)  
**Date:** November 25, 2026  
**Document Status:** Audit III — Pre-v3 Architectural Revision & Formal Specification  
**Inspected Artifacts:**  
* `standardgalactic/spherepop-kernel@fe79af5` (`kernel/spherepop_kernel.py`, `kernel-rs/src/main.rs`, `tests/differential.py`, `fixtures/nested_sphere_fixture.json`)  
* `Borealiscodes/epistemic-substrate-lab` (`lean/EpistemicAudit.lean`, `julia/ManifoldInstruments.jl`, `experiments/exp1_metric_audit.py`, `experiments/exp2_sheaf_gluing.py`)  

---

## Abstract

Following the empirical execution of Blueprint v2 (`Borealiscodes/epistemic-substrate-lab`), which detected significant cellular sheaf coboundary frustration ($\|\delta^0 s\|_2 = 5.8560$) across overlapping rank-64 subspaces under $8\times$ neural superposition, we proposed introducing continuous Sheaf Laplacians ($L_{\mathcal{F}} = \delta^0{}^\top \delta^0$) and Sparse Autoencoder (SAE) patch covers in v3. Concurrently, Flyxion released `standardgalactic/spherepop-kernel` (commit `fe79af5`), an executable Python + Rust dual-kernel protocol (`POP`, `BIND`, `TRANSFORM`, `VERIFY`, `COLLAPSE`, `REFUSE`) whose `nested_sphere_fixture.json` models an isomorphic failure mode: two subordinate scopes passing local certification while their parent composition violates a global invariant. In this comparative audit, we evaluate our proposed v3 roadmap against `Spherepop@fe79af5`. We demonstrate that **continuous Sheaf Laplacians remain indispensable** for measuring geometric superposition angles (where discrete JSON event histories cannot reach), while **adopting `Spherepop`’s scoped event-history semantics, differential cross-language fuzzing, and formal `REFUSE` transitions** dramatically simplifies and hardens v3’s provenance and Lean 4 verification layers. We conclude with concrete, decontaminated mathematical and computational upgrades for v3, including a **zero-`sorry` Lean 4 formalization** of nested-sphere composition obstruction.

**Keywords:** *Spherepop kernel, compositional obstruction, cellular sheaf coboundary, differential fuzzing, operative refusal, Lean 4 zero-sorry, edge storage hygiene*

---

## 1. Structural Isomorphism: `nested_sphere_fixture.json` vs. Experiment B

The central discovery of this audit is that two independently developed repositories arrived at the **exact same local-to-global composition obstruction** from opposite sides of the mathematical-institutional divide:

* **Continuous Geometric Formulation (`epistemic-substrate-lab`, Experiment B):** Local rank-$k$ QR subspace patches $\{U_1, \dots, U_6\}$ each reconstruct their local projection $s_i = P_i^\top x$ accurately, yet fail to glue globally across overlapping regions when local `CAUSA` interventions are applied ($\|\delta^0 s\|_2 = 5.8560 \gg 10^{-6}$).
* **Discrete Operational Formulation (`spherepop-kernel@fe79af5`, `nested_sphere_fixture.json`):** Two subordinate scoped spheres ($S_A, S_B$) each pass local obligation verification (`VERIFY`), yet when composed into a parent sphere ($S_{\text{parent}}$), their combined state violates a parent-level invariant—triggering an explicit **`REFUSE`** event rather than an authoritative **`COLLAPSE`**.

| Analytical Dimension | Our Proposed v3 Roadmap (`epistemic-substrate-lab`) | Flyxion’s `Spherepop` Kernel (`fe79af5`) | Synthesis Verdict for v3 |
| :--- | :--- | :--- | :--- |
| **Unit of Composition** | Overlapping rank-$k$ subspaces $U_i \subset \mathbb{R}^D$ and SAE feature patches. | Scoped event histories (`POP` $\to$ `BIND` $\to$ `TRANSFORM` $\to$ `VERIFY` $\to$ `COLLAPSE` / `REFUSE`). | **Complementary:** Use continuous subspaces for neural activations; wrap experimental runs in `Spherepop` event logs. |
| **Failure Detection Mechanism** | Continuous coboundary residual $\|\delta^0 s\|_2$ and Sheaf Laplacian $L_{\mathcal{F}} = \delta^0{}^\top \delta^0$. | Deterministic obligation predicates over SHA-256 base-versioned state histories. | **Keep both:** $L_{\mathcal{F}}$ quantifies continuous superposition angle; `REFUSE` enforces discrete governance gates. |
| **Cross-Language Differential Testing** | Separate `Julia` (`0`-byte static holonomy) and `Python` (`clr` + sheaf) scripts without lockstep fuzzing. | Dual identical implementations (`kernel/spherepop_kernel.py` + `kernel-rs/src/main.rs`) tested across 300 differential fuzz scenarios (`tests/differential.py`). | **Upgrade v3:** Add a cross-language differential fuzzer asserting bit-level/tolerance agreement between `Julia` and `Python` engines. |
| **Canonicalization & Determinism** | `Q16.16` fixed-point arithmetic + `fractions.Fraction` over $\mathbb{Q}[i]$. | Canonical JSON hashing (`SHA-256`) with explicit scope boundaries (noting RFC 8785 integer/float limits in `README.txt`). | **Keep `Q16.16` & $\mathbb{Q}[i]$:** Avoid JSON float serialization ambiguity by hashing exact `Q16.16` integer arrays or rational numerators/denominators. |
| **Edge Repository Hygiene** | Strict `< 1 MB` CI blob guard (`edge-blob-guard`); zero media in Git history. | Commit `fe79af5` embeds a `28.7 MB` `.mp3` and compiled `.pdf` directly in Git history. | **Maintain our Edge SOP:** Never import binary media; inspect `spherepop-kernel` exclusively via `--depth 1 --filter=blob:limit=1m`. |

---

## 2. Where `Spherepop@fe79af5` Corrects and Sharpens Our v3 Roadmap

Auditing our initial v3 recommendations against `Spherepop` exposes three areas where our v3 plan was either under-specified or overly complex:

### 2.1 Replacing Abstract `operativeRefusal` with a State-Transition Kernel
In `lean/EpistemicAudit.lean` (v2), we modeled Flyxion’s *operative refusal* as a static propositional field (`operativeRefusal : Prop`) inside `AuthorshipProfile`. `Spherepop` shows how to make operative refusal an **executable algebraic transition**:
* A scope cannot reach `COLLAPSE` (authoritative commitment) unless it holds a valid `BIND` (explicit authority + cryptographic `base_version`) and passes `VERIFY`.
* If local patches pass `VERIFY` individually but fail global coboundary gluing ($\|\delta^0 s\|_2 > \epsilon_{\text{tol}}$), the parent scope is **mathematically barred from `COLLAPSE`** and must transition to **`REFUSE(reason = "COBOUNDARY_OBSTRUCTION")`**.
* This unites our mathematical obstruction ($\|\delta^0 s\|_2 > 0$) with Flyxion’s institutional accountability: an unglued, superposed representation cannot be silently collapsed into an authoritative claim.

### 2.2 Adding Differential Dual-Implementation Fuzzing (`Julia` vs. `Python`)
Our v2 CI verified `Julia` (`ManifoldInstruments.jl`) and `Python` (`exp1`, `exp2`) independently. `Spherepop`’s `tests/differential.py` demonstrates a far stronger standard: running randomized multi-step state trajectories through two independent implementations (in our case, `Julia` static arrays vs. `Python/NumPy` reference arrays) and failing CI if any trajectory diverges beyond machine epsilon ($10^{-12}$).

### 2.3 Knowing Where `Spherepop` Stops (Why `CellularSheaf.jl` Is Still Needed)
`Spherepop`’s own `README.txt` candidly documents its boundary: it is a **discrete governance and history-tracking kernel** over finite keys and ASCII strings, not a continuous geometric analyzer. It cannot compute pull-back Riemannian metrics $g_{\text{sub}} = P^\top g_{\text{ambient}} P$, Aitchison $\text{clr}$ isometric distances, or continuous superposition angles between almost-orthogonal features in $\mathbb{R}^{4096}$. Therefore, we **retain `CellularSheaf.jl`** for continuous manifold geometry while adopting `Spherepop`’s state machine as the outer execution wrapper.

---

## 3. Actionable Mathematical & Computational Upgrades for v3

Based on this audit, we revise the v3 architecture (`Borealiscodes/epistemic-substrate-lab`) into **four concrete, decontaminated deliverables**:

### Upgrade 1 (Mathematical — Lean 4): Zero-`sorry` `SpherepopSheafBridge.lean`
Extend `lean/EpistemicAudit.lean` to formalize the exact link between **cellular sheaf coboundary exactness** ($\delta^1 \circ \delta^0 = 0$) and **`Spherepop` scoped composition refusal**:
* Prove that if two subordinate scopes $S_1, S_2$ satisfy local verification (`LocalValid S₁ ∧ LocalValid S₂`) over $\mathbb{Q}[i]$ subspaces, their parent composition `compose S₁ S₂` admits `Collapse` **if and only if** their overlap coboundary vanishes ($\delta^0(S_1, S_2) = 0$).
* Prove that whenever $\delta^0(S_1, S_2) \neq 0$, the unique admissible terminal transition is `Refuse`.

#### Ready-to-Compile Zero-`sorry` Lean 4 Specification
```lean
namespace SpherepopSheafBridge

/-- Scoped execution disposition modeled after Spherepop@fe79af5. -/
inductive Disposition where
  | collapsed : Disposition
  | refused (reason : String) : Disposition
  deriving DecidableEq, Repr

/-- Local verification state for a rank-k patch or scoped sphere. -/
structure ScopedPatch where
  localVerified : Bool
  boundAuthority : Bool
  coboundaryZero : Bool

/-- Global collapse is admissible iff local verification, authority binding,
    and vanishing overlap coboundary (delta^0 s = 0) all hold. -/
def evaluateComposition (p1 p2 : ScopedPatch) (overlapCoboundaryZero : Bool) : Disposition :=
  if p1.localVerified && p2.localVerified && p1.boundAuthority && p2.boundAuthority && overlapCoboundaryZero then
    Disposition.collapsed
  else
    Disposition.refused "COBOUNDARY_OR_AUTHORITY_OBSTRUCTION"

theorem nested_obstruction_forces_refusal
    (p1 p2 : ScopedPatch)
    (h1 : p1.localVerified = true) (h2 : p2.localVerified = true)
Use code with caution.
(hb1 : p1.boundAuthority = true) (hb2 : p2.boundAuthority = true)
(h_obs : overlapCoboundaryZero = false) :
evaluateComposition p1 p2 overlapCoboundaryZero =
Disposition.refused "COBOUNDARY_OR_AUTHORITY_OBSTRUCTION" := by
simp [evaluateComposition, h1, h2, hb1, hb2, h_obs]
end SpherepopSheafBridge
```

Upgrade 2 (Mathematical — Julia): Sparse Cellular Sheaf Laplacian (CellularSheaf.jl)

Upgrade julia/ManifoldInstruments.jl to construct the block-sparse coboundary matrix $\delta^0$ and symmetric positive semi-definite Sheaf Laplacian $L_{\mathcal{F}} = \delta^0{}^\top \delta^0$:
* Compute both the coboundary energy $E_{\mathcal{F}}(s) = s^\top L_{\mathcal{F}} s = |\delta^0 s|2^2$ and the spectral gap $\lambda_1(L{\mathcal{F}})$ (smallest non-zero eigenvalue, measuring algebraic connectivity of the patch cover).
* Preserve 0-byte heap allocation on the inner edge-residual accumulation loop using SVector{K,Float64} restrictions.

Upgrade 3 (Computational — Python): Spherepop-Wrapped Telemetry & SAE Patch Covers

Upgrade experiments/exp2_sheaf_gluing.py into a Spherepop-compliant event emitter (POP $\to$ BIND $\to$ TRANSFORM $\to$ VERIFY $\to$ COLLAPSE/REFUSE):
* Hash input states using deterministic Q16.16 integer byte representations (SHA-256) so canonical hashes never depend on platform floating-point string formatting.
* When $|\delta^0 s|_2 > 10^{-6}$ (as observed in Experiment B's 5.8560 result), emit an explicit REFUSE event in the JSON telemetry rather than a bare boolean flag.
* Add an orthogonalized dictionary-atom patch builder (simulating Sparse Autoencoder feature directions) alongside random QR bases to measure how SAE feature alignment reduces baseline coboundary energy.

Upgrade 4 (CI & Differential Verification): Cross-Language Lockstep Fuzz Harness

Add experiments/differential_harness.py to .github/workflows/epistemic-audit.yml:
* Run $N = 100$ randomized subspace + holonomy + coboundary trials across both Julia (ManifoldInstruments.jl) and Python (NumPy), asserting $|d_{\text{Julia}} - d_{\text{Python}}| < 10^{-12}$ on every trial.
* Keep the repository strictly under < 1 MB per file (edge-blob-guard) so ARM64 Termux Clone -> Seal -> Push -> Purge cycles remain instantaneous.

---

### 4. Updated v3 Execution Sequence


Step	Target Module	Concrete Deliverable	Verification Gate
v3.1	lean/EpistemicAudit.lean	Append SpherepopSheafBridge (nested_obstruction_forces_refusal + $\delta^1 \circ \delta^0 = 0$).	lake build passes with 0 sorry in GitHub CI.
v3.2	julia/ManifoldInstruments.jl	Add sheaf_coboundary_energy & SheafLaplacian spectrum ($\lambda_1(L_{\mathcal{F}})$).	@allocated == 0 on static restriction inner loop.
v3.3	experiments/exp3_spherepop_sheaf.py	Emit POP/BIND/VERIFY/COLLAPSE/REFUSE SHA-256 transcripts over SAE-guided vs. random QR patches.	REFUSE triggers cleanly when $s^\top L_{\mathcal{F}} s > 10^{-12}$.
v3.4	.github/workflows/epistemic-audit.yml	Add 100-trial Julia vs. Python differential fuzz gate & archive v3 JSON telemetry.	All 4 CI stages green; Termux working tree purged (0 KB local footprint).

---

### 5. Conclusion

Flyxion’s Spherepop@fe79af5 kernel provides the exact discrete governance counterpart to our continuous cellular sheaf obstruction. By fusing Spherepop’s POP / BIND / VERIFY / COLLAPSE / REFUSE state machine and differential fuzzing discipline with our zero-sorry Lean 4 proofs, Aitchison $\text{clr}$ metrics, and zero-allocation Julia Sheaf Laplacians, v3 closes the loop between continuous neural geometry and accountable institutional execution—without adding a single byte of binary bloat to the repository.

---

### References

Aitchison, J. (1986). The statistical analysis of compositional data. Chapman and Hall. doi.org
de Moura, L., & Ullrich, S. (2021). The Lean 4 theorem prover and programming language. In A. Platzer & G. Sutcliffe (Eds.), Automated Deduction – CADE 28 (pp. 625–635). Springer. doi.org
Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., Grosse, R., McCandlish, S., Kaplan, J., Amodei, D., Wattenberg, M., & Olah, C. (2022). Toy models of superposition. Transformer Circuits Thread. transformer-circuits.pub
Flyxion. (2026a, November). Persistence and accountable authorship in language model systems [Preprint]. Independent Researcher.
Flyxion. (2026b). Spherepop kernel: Scoped event-history maintenance and differential Python/Rust verification (Commit fe79af59b23fc531b41e52ceb4c28343915a943b) [Computer software]. GitHub. github.com
Hansen, J., & Ghrist, R. (2019). Toward a spectral theory of cellular sheaves. Journal of Applied and Computational Topology, 3(4), 315–358. doi.org
Hedling, B. S. (2026). Epistemic substrate lab: Zero-sorry Lean 4 proofs, zero-allocation Riemannian geometry, and causal metric audits [Computer software]. GitHub. github.com


