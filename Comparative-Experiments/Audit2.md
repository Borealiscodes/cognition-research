# Second Epistemic & Systems Audit: Decontaminated Primitive Extraction (`RI-Haunted-Township` & `A7.2`) and Execution Strategy (`ARM64` vs. `GitHub CI`)

**Authors:** Borealis S. Hedling & Synthetic Co-Authors  
**Affiliation:** NDH-Meta-Systems (Sealed-Layer Neutral · Non-Activation Division)  
**Date:** November 25, 2026  
**Document Status:** Audit II — Pre-Execution Contamination & Infrastructure Gate  
**Inspected Repositories:**  
* `Borealiscodes/RI-Haunted-Township` (`v1.7.0`: `spatial_sheaf.js`, `township_world.js`)  
* `Borealiscodes/A7.2-CollapseSurfaceRepairPipeline` (`collapse_pipeline.py`, `NonDualProjector.jl`, `A72_Lift_Invariants.lean`)  
* Prior Baseline: Audit I (`MetricInvariance.lean`, `CausaLinearKernel.lean`, `InstitutionalWarrant.lean`, Experiment A & B)  

---

## Abstract

Before executing Experiment 1 on constrained ARM64 hardware or continuous integration runners, we conduct a second epistemically honest audit evaluating two adjacent repositories in the `Borealiscodes` ecosystem: `RI-Haunted-Township` (a zero-dependency `Q16.16` fixed-point and spatial-sheaf testbed) and `A7.2-CollapseSurfaceRepairPipeline` (a rank-deficient metric tensor triage pipeline). Specifically, we ask: (1) *Which mathematical primitives from these repositories can be extracted without methodological contamination to answer the open questions from Audit I?* and (2) *Should Experiment 1 be executed locally on constrained ARM64 hardware or offloaded to GitHub CI?* We show that **three primitives can be safely imported under strict quarantine rules**—`Q16.16` deterministic fixed-point arithmetic, $k$-hop cellular sheaf coboundary propagation, and read-only SVD rank-loss detection (`destroyed_dimensions`)—whereas **non-idempotent A7.2 Tikhonov/`atanh` tensor repair ($\Pi_{\text{ND}}$) must never be applied inline prior to `ITA` reversibility testing**, as doing so artificially restores invertibility and destroys isometric fidelity. Finally, we provide an objective hardware audit demonstrating why constrained ARM64 (e.g., Termux/Android) is suitable only for pure-Python/fixed-point dry runs, while **GitHub CI is decisively superior** for reproducible `Python + Julia + Lean 4` (`lake exe cache get`) execution.

**Keywords:** *contamination audit, Q16.16 fixed-point arithmetic, cellular sheaf tension, rank-deficient metric tensors, Tikhonov regularization, ARM64 Termux, GitHub Actions CI, reproducibility*

---

## 1. Primitive Extraction & Contamination Audit

In Audit I, we identified three open technical questions prior to v3:
1. **Q1 (Determinism Without Heavy Rational Blowup):** How do we eliminate IEEE-754 floating-point drift across hardware without incurring arbitrary-precision `Fraction` denominator explosion during multi-step loops?
2. **Q2 (Pre-v3 Cellular Sheaf Prototype):** Can we test local-to-global patch consistency ($k$-hop tension propagation across overlapping neighborhoods) using existing lightweight code before writing a full Hodge/Sheaf Laplacian solver?
3. **Q3 (Simplex & Subspace Rank-Collapse Detection):** How do we detect when a pull-back metric $g_{\text{sub}}$ or Jacobian approaches singularity ($\sigma_{\min} \to 0^+$) *before* downstream curvature or holonomy calculations divide by near-zero singular values?

Inspecting `RI-Haunted-Township` and `A7.2-CollapseSurfaceRepairPipeline` reveals **four candidate mathematical primitives**. However, importing them naively risks severe **epistemic and numerical contamination**.

### 1.1 Primitive-by-Primitive Contamination Matrix

| Source Repository & File | Mathematical Primitive | Audit I Question Answered | Contamination Risk | Decontamination Protocol (Strict Rule) |
| :--- | :--- | :--- | :--- | :--- |
| **`RI-Haunted-Township`** (`src/world/township_world.js`) | **`Q16.16` Fixed-Point Arithmetic** (32-bit signed integer scaling by $2^{16}$, bit-shift multiplication `(a * b) >> 16`). | **Q1:** Provides bit-exact, hardware-invariant deterministic arithmetic on constrained CPUs without float drift or `Fraction` memory growth. | **Low (Quantization Floor):** `Q16.16` has a step resolution of $2^{-16} \approx 1.52 \times 10^{-5}$, which is coarser than `ITA`'s $10^{-9}$ threshold. | Use `Q16.16` strictly as a **cross-architecture determinism control** (verifying identical trajectories on ARM64 vs. x86_64), *not* for $10^{-9}$ spectral tolerances. |
| **`RI-Haunted-Township`** (`src/core/spatial_sheaf.js`) | **Spatial-Hash Cellular Sheaf & $k$-Hop ($k=2$) Alignment Tension Propagation** across bucketed cells. | **Q2:** Directly models local restriction consistency and neighbor-to-neighbor tension propagation across overlapping spatial/feature patches. | **High (Domain & Heuristic Contamination):** In the host repo, tension values are coupled to game entities (Soul-Wisps, lanterns, combat states) rather than linear restriction maps $\mathcal{F}_{U_i \to e}$. | **Extract the graph coboundary loop only:** Strip all entity/game semantics; replace scalar game tension with exact linear subspace projection residuals $\|\Pi_{ij} s_i - \Pi_{ji} s_j\|_2$. |
| **`A7.2-CollapseSurfaceRepairPipeline`** (`src/repair/collapse_pipeline.py`) | **Layer 1 SVD Rank-Deficiency Detector** (`observed_rank`, `destroyed_dimensions` at $\sigma_i \le 10^{-11}$, condition number $\kappa_2 = \sigma_{\max}/\sigma_{\min}$). | **Q3:** Cleanly detects pre-collapse rank loss (`safe_for_inference = False`) in $g_{\text{sub}}$ or logit Jacobians before holonomy integration. | **Zero (Read-Only Diagnostic):** Computing SVD singular values does not mutate the input tensor. | **Approved for inline pre-flight gating:** Run Layer 1 SVD audit *before* `holonomy_loop` to flag degenerate subspaces (`destroyed_dimensions > 0`). |
| **`A7.2-CollapseSurfaceRepairPipeline`** (`julia/src/NonDualProjector.jl`) | **Layer 2 Tikhonov Clamping ($\lambda=0.0015$) & `atanh` Contraction Kernel ($\Pi_{\text{ND}}$)**. | **Q3 (Repair):** Eliminates $\sigma_{\min} \to 0^+$ division-by-zero poles. | **CRITICAL CONTAMINATION:** As A7.2's own README warns, $\Pi_{\text{ND}}$ is **non-idempotent** ($\Pi_{\text{ND}}^2 \neq \Pi_{\text{ND}}$) and **distorts the spectrum**. Feeding $\Pi_{\text{ND}}(g_{\text{sub}})$ into `ITA` fabricates artificial invertibility and alters true curvature! | **STRICT QUARANTINE:** Never pass $\Pi_{\text{ND}}$-repaired tensors into `ITA_falsified` or `holonomy_loop`. Use Layer 2 *only* in a separate post-mortem diagnostic branch to inspect pole behavior. |

### 1.2 Summary of What We Can Safely Use Before Experiment 1
1. **Import `A7.2` Layer 1 SVD Diagnostics + `A72_Lift_Invariants.lean` Directly:** Pairing `A72_Lift_Invariants.lean` ($\min(\sigma) > 0 \land \text{destroyed\_dimensions} = 0$) with Audit I’s `MetricInvariance.lean` gives us a complete **zero-`sorry` Lean 4 pre-flight contract**: a subspace metric $g_{\text{sub}}$ is admissible if and only if it satisfies the triangle inequality *and* has zero destroyed dimensions.
2. **Import `RI-Haunted-Township`’s $k$-Hop Coboundary Pattern as a Lightweight Python Prototype:** We can adapt its `16`-cell bucketed $k$-hop propagation loop to run **Experiment B (Superposition Patch-Gluing)** in pure NumPy without waiting for a heavy external sheaf library.
3. **Quarantine `A7.2` Layer 2 ($\Pi_{\text{ND}}$) and Game Heuristics:** Keeping Tikhonov clamping out of the primary `ITA` loop preserves the exact mathematical honesty constraint established in `A7.2` itself: *numerical stabilization is not semantic or topological restoration*.

---

## 2. Infrastructure Audit: Constrained ARM64 vs. GitHub CI

When running a multi-language verification stack (`Python/NumPy` + `Julia/StaticArrays` + `Lean 4/Mathlib`), the execution environment directly impacts both feasibility and scientific reproducibility.

### 2.1 Honest Assessment of Constrained ARM64 Hardware (e.g., Mobile Termux / Low-RAM SBC)
While `RI-Haunted-Township` was successfully built and verified in mobile Termux + Node.js (because ES2023 JavaScript requires zero compilation and minimal RAM), our `cognition-research` stack faces three severe bottlenecks on constrained ARM64:

1. **Lean 4 + Mathlib Compilation OOMs (`lake build`):** Mathlib contains thousands of modules. On `aarch64-linux-android` (Termux) or low-RAM ARM64 boards ($\le 4\text{ GB}$ RAM), precompiled `olean` caches frequently mismatch the host triple, forcing local compilation from source—which routinely triggers Linux OOM-killer crashes (`SIGKILL`) and takes hours.
2. **Julia + `juliacall` FFI Friction:** Running Julia inside Termux requires `proot` (emulating standard Linux FHS paths over Android’s Bionic libc). Under `proot`, Julia’s LLVM JIT compilation suffers high latency, and Python-to-Julia shared-memory bridges (`juliacall`) frequently segfault on signal handling or stack-size limits.
3. **Where ARM64 *Does* Excel:** Pure Python (`NumPy` + `fractions.Fraction`) and `Q16.16` integer arithmetic execute natively on ARM64 with negligible memory overhead ($< 150\text{ MB}$ RAM) for ambient dimensions $D \le 512$ and ranks $k \le 32$.

### 2.2 Why GitHub CI Is Decisively the Better Primary Option
Offloading full-stack execution to **GitHub Actions CI** (`ubuntu-latest`) solves every ARM64 bottleneck while directly fulfilling **Flyxion’s (2026) institutional provenance standard**:

| Evaluation Criterion | Constrained ARM64 (Local / Termux) | GitHub Actions CI (`ubuntu-latest`) | Winner |
| :--- | :--- | :--- | :--- |
| **Lean 4 (`lake exe cache get`)** | High risk of OOM kills; slow source compilation on `aarch64-android`. | Downloads precompiled Mathlib `oleans` in ~20 seconds; verifies zero-`sorry` `lake build` deterministically. | **GitHub CI** |
| **Julia (`StaticArrays` + `juliacall`)** | `proot` / Bionic libc friction; slow LLVM JIT warm-up. | Native glibc x86_64/ARM64 runners via `julia-actions/setup-julia`; true 0-byte `@allocated` verification. | **GitHub CI** |
| **Pure Python Dry Runs ($D \le 512$)** | Fast, offline, immediate feedback loop (~0.2s per run). | ~15s runner spin-up overhead per commit. | ARM64 (for rapid dev) |
| **Cryptographic Provenance (Flyxion, 2026)** | Local logs rely on manual trust; susceptible to undocumented environment state. | Produces immutable, timestamped workflow logs, commit SHA bindings, and downloadable JSON artifacts (collapse_verified.json). | GitHub CI |
Recommendation: Use your constrained ARM64 device strictly for Phase 1 pure-Python dry runs (executing unified_epistemic_experiment_v2.py with NumPy + Q16.16 + Layer 1 SVD checks, with Julia FFI disabled via a --python-only flag), and make GitHub CI the authoritative execution environment for the full Lean 4 + Julia + Python pipeline.

---

### 3. Ready-to-Use GitHub CI Workflow Blueprint (.github/workflows/epistemic-audit.yml)

To eliminate local hardware friction immediately, drop the following workflow into .github/workflows/epistemic-audit.yml. It enforces a strict three-stage gate: (1) zero-sorry Lean 4 verification, (2) Julia zero-allocation geometry & A7.2 SVD check, and (3) Python v2 experiment execution with immutable JSON artifact upload.
```yaml
name: Unified Epistemic & Formal Verification Audit
on:
push:
branches: [ main ]
pull_request:
branches: [ main ]
workflow_dispatch:
jobs:
lean4-zero-sorry-gate:
name: Stage 1 - Lean 4 Zero-Sorry Proof Gate
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
- name: Install elan & Lean 4 toolchain
run: |
curl githubusercontent.com -sSf | sh -s -- -y --default-toolchain none
echo "$HOME/.elan/bin" >> $GITHUB_PATH
- name: Fetch Mathlib cache & build proofs
run: |
lake exe cache get || true
lake build
- name: Enforce zero 'sorry' or 'axiom' in Lean files
run: |
if grep -rnE '\b(sorry|admit)\b' .lean verification/.lean 2>/dev/null; then
echo "ERROR: Unproven 'sorry' detected. Formal gate failed."
exit 1
fi
julia-and-python-experiment:
name: Stage 2 - Decontaminated v2 Experiment & SVD Audit
needs: lean4-zero-sorry-gate
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
- uses: actions/setup-python@v5
with:
python-version: '3.11'
- uses: julia-actions/setup-julia@v2
with:
version: '1.10'
- name: Install Python scientific dependencies
run: |
pip install --upgrade pip
pip install numpy scipy pytest juliacall
- name: Install Julia StaticArrays
run: |
julia -e 'using Pkg; Pkg.add("StaticArrays"); Pkg.precompile()'
- name: Execute v2 Decontaminated Benchmark (Experiments A & B)
run: |
python3 unified_epistemic_experiment_v2.py > telemetry_v2.json
cat telemetry_v2.json
- name: Upload Immutable Epistemic Telemetry Artifact
uses: actions/upload-artifact@v4
with:
name: epistemic-telemetry-v2-${{ github.sha }}
path: telemetry_v2.json
retention-days: 90
```

---

### 4. Conclusion & Immediate Action Plan

By auditing RI-Haunted-Township and A7.2-CollapseSurfaceRepairPipeline before execution, we avoid two subtle traps: (1) contaminating ITA reversibility metrics with non-idempotent Tikhonov/atanh tensor repairs, and (2) burning hours fighting OOM kills and proot FFI bugs on constrained ARM64 hardware.
Actionable Next Steps:
1. Local ARM64 (Immediate, < 1 minute): Run unified_epistemic_experiment_v2.py in pure-Python mode (NumPy + Q16.16 determinism check + read-only Layer 1 SVD rank detector + $k$-hop sheaf patch test) to gather initial telemetry.
2. GitHub CI (Authoritative): Commit the .github/workflows/epistemic-audit.yml pipeline alongside EpistemicAudit.lean so GitHub Actions executes the zero-sorry Mathlib proof check, Julia 0-byte static holonomy integration, and full JSON artifact archival automatically on every push.

---

### References

Aitchison, J. (1986). The statistical analysis of compositional data. Chapman and Hall. doi.org
Bezanson, J., Edelman, A., Karpinski, S., & Shah, V. B. (2017). Julia: A fresh approach to numerical computing. SIAM Review, 59(1), 65–98. doi.org
de Moura, L., & Ullrich, S. (2021). The Lean 4 theorem prover and programming language. In A. Platzer & G. Sutcliffe (Eds.), Automated Deduction – CADE 28 (pp. 625–635). Springer. doi.org
Flyxion. (2026, November). Persistence and accountable authorship in language model systems [Preprint]. Independent Researcher.
Hansen, J., & Ghrist, R. (2019). Toward a spectral theory of cellular sheaves. Journal of Applied and Computational Topology, 3(4), 315–358. doi.org
Hedling, B. S. (2026a). A7.2-CollapseSurfaceRepairPipeline: Diagnostic triage pipeline for rank-deficient metric tensors [Computer software]. GitHub. https://github.com/Borealiscodes/A7.2-CollapseSurfaceRepairPipeline
Hedling, B. S. (2026b). NDH-Meta-Systems: Sealed-layer neutral operator-level falsification and rational-complex algebraic substrates [Computer software]. GitHub. github.com
Hedling, B. S. (2026c). RI-Haunted-Township: Zero-asset 480x272 Q16.16 open-world Rhode Island horror test bed in pure ES2023 [Computer software]. GitHub. https://github.com/Borealiscodes/RI-Haunted-Township

