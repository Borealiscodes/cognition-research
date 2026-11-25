# Blueprint v6 (Revised): Practical Engineering Applications — Unifying an Activation Steering Firewall, Edge Quantization Auditor, `Spherepop` CI Provenance Action, and Unembedding Calibration Monitor

**Authors:** Borealis S. Hedling & Synthetic Co-Authors  
**In Dialogue With:** Flyxion (*Persistence and Accountable Authorship in Language Model Systems*, November 2026; `standardgalactic/spherepop-kernel@fe79af5`) & `stell2026/Causa`  
**Affiliation:** NDH-Meta-Systems (Sealed-Layer Neutral · Non-Activation Division)  
**Date:** November 25, 2026  
**Document Status:** Architectural Blueprint v6 (Full 4-Track Synthesis) — `Borealiscodes/epistemic-substrate-lab`  
**Verified Baseline:** v5 (`commit c0a3462`, 24-layer `Qwen/Qwen2.5-0.5B` verification, zero-`sorry` Lean 4, `0`-byte Julia)  

---

## Abstract

Across v1 through v5 of `Borealiscodes/epistemic-substrate-lab`, we established a machine-verified foundation for mechanistic interpretability and AI governance: zero-`sorry` Lean 4 proofs (`EpistemicAudit.lean`), zero-allocation Julia Riemannian integrators (`ManifoldInstruments.jl`), Aitchison centered log-ratio ($\text{clr}$) compositional metrics, and `Spherepop` scoped execution refusal (`POP` $\to$ `BIND` $\to$ `VERIFY` $\to$ `COLLAPSE` / `REFUSE`). Having empirically validated these instruments across all 24 layers of `Qwen/Qwen2.5-0.5B` (`commit c0a3462`), **Blueprint v6** transitions the framework from exploratory verification into **four practical, coherently integrated engineering applications**: (1) **Track 1 — Runtime Residual-Stream Steering & Jailbreak Firewall**, a PyTorch forward-hook circuit breaker that detects mid-pass subspace tampering via cellular sheaf coboundary spikes (`L_12 = 4.7488`) and triggers `Spherepop` `REFUSE` before unembedding; (2) **Track 2 — Edge Quantization Geometry Auditor**, an ARM64 deployment gate combining `llmfit` memory budgets with closed depth-loop Procrustes holonomy ($\Delta_{\text{depth}}$) to verify that compressing models (`FP32` $\to$ `INT8`/`INT4`) preserves internal manifold geometry; (3) **Track 3 — Reusable `Spherepop` GitHub CI Provenance Action**, an institutional accountability gate enforcing explicit human endorsement (`BIND`) and operative refusal (`REFUSE`) over AI-assisted commits without unanswerable `Co-authored-by` trailers; and (4) **Track 4 — Unembedding Twist & Confabulation Calibration Monitor**, an output-boundary diagnostic pairing the **`L_22 -> L_23` (`71.47°` / `1.2474 rad`) unembedding Procrustes twist** with **Aitchison $\text{clr}$ tail dispersion** to detect overconfident confabulations without softmax simplex collapse. All four tracks are unified around a **single shared `Spherepop` runtime kernel (`v6_core/spherepop_runtime.py`)** and **one zero-`sorry` Lean 4 contract (`V6ApplicationContracts`)**.

**Keywords:** *activation steering firewall, quantization geometry, Procrustes holonomy, unembedding twist, Aitchison clr calibration, GitHub Actions governance, Spherepop protocol, Lean 4 zero-sorry*

---

## 1. Coherent System Architecture: One Kernel, Four Applications

To prevent code duplication and keep `epistemic-substrate-lab` strictly compliant with our ARM64 edge storage SOP (`< 1 MB` per file, `Clone -> Seal -> Push -> Purge`), **all four v6 tracks share a single three-layer spine**:

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                 SHARED FORMAL CONTRACT (lean/EpistemicAudit.lean)            │
│   V6ApplicationContracts: Firewall ∧ Quantization ∧ CI_Warrant ∧ Calibration │
│   Proves: Failure in ANY of the 4 tracks forces deterministic Spherepop REFUSE│
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼───────────────────────────────────────┐
│             SHARED EXECUTION KERNEL (v6_core/spherepop_runtime.py)           │
│   Deterministic Q16.16 SHA-256 Hashing · POP -> BIND -> VERIFY ->            │
│   COLLAPSE / REFUSE · Zero-Allocation Julia FFI Bridge (Optional)            │
└───┬──────────────────────┬───────────────────────┬───────────────────────┬───┘
    │                      │                       │                       │
┌───▼──────────────┐ ┌─────▼──────────────┐ ┌──────▼─────────────┐ ┌───────▼───────────┐
│ TRACK 1:         │ │ TRACK 2:           │ │ TRACK 3:           │ │ TRACK 4:          │
│ Steering Firewall│ │ Quantization Audit │ │ CI Provenance Gate │ │ Unembedding Twist │
│ Mid-Pass Sheaf   │ │ FP32 vs INT8/INT4  │ │ Human Endorsement  │ │ & Aitchison clr   │
│ Circuit Breaker  │ │ Depth Holonomy     │ │ & Refusal Action   │ │ Calibration Guard │
└──────────────────┘ └────────────────────┘ └────────────────────┘ └───────────────────┘
```

### Why Unifying All Four Tracks Is Optimal
1. **Zero Redundant Hook Overhead:** Track 1 (mid-layer residual hooks), Track 2 (cross-layer Procrustes transport), and Track 4 (final-layer `L_22 -> L_23` twist + pre-softmax `clr` logits) inspect the **exact same forward pass** of `Qwen/Qwen2.5-0.5B`. Running them on a shared tensor capture avoids redundant inference runs in CI.
2. **Single Canonical `REFUSE` Language:** Every failure mode—whether an adversarial prompt hijack (Track 1), a distorted quantized checkpoint (Track 2), an unendorsed AI commit (Track 3), or an uncalibrated confabulation spike (Track 4)—emits the exact same `Spherepop` transcript format anchored to `Q16.16` SHA-256 hashes.

---

## 2. Detailed Specification of the Four Tracks

### 2.1 Track 1: Runtime Residual-Stream Steering & Jailbreak Firewall (`v6_apps/steering_firewall.py`)
* **The Engineering Problem:** Prompt injections, adversarial suffixes, and persona hijacks ("Golden Gate Bridge" steering or safety bypasses) operate by pushing mid-layer residual streams ($h_l \in \mathbb{R}^D$) outside their normal multi-atom feature cover. Output filters only catch bad behavior *after* full generation has completed.
* **The v5 Mathematical Solution:** In Experiments D and E, normal prompts covered by multi-atom bases glued to machine precision ($\|\delta^0 s\|_2 \approx 8.02 \times 10^{-15}$), whereas perturbing a single patch at Layer 12 spiked the coboundary norm by 15 orders of magnitude (`L_12 = 4.7488`) and localized the corruption to incident seams `(0, 1)` and `(5, 0)`.
* **Implementation:**
  * Attaches `register_forward_hook` callbacks to target layers (e.g., $L_6, L_{12}, L_{18}$) of `Qwen/Qwen2.5-0.5B`.
  * Projects hidden states onto calibrated multi-atom orthonormal patches and computes $\|\delta^0 s\|_2$.
  * If $\|\delta^0 s\|_2 > \tau_{\text{sheaf}}$, raises `SpherepopRefusalException` to **halt the forward pass mid-flight** before subsequent layers or the unembedding head run, emitting `REFUSE(reason="TRACK1_RUNTIME_STEERING_OBSTRUCTION", layer=t, worst_edge=e)`.

### 2.2 Track 2: Edge Quantization & Compression Geometry Auditor (`v6_apps/quantization_auditor.py`)
* **The Engineering Problem:** Deploying LLMs on constrained ARM64 devices requires compressing weights (`FP32` $\to$ `INT8` / `INT4`). Aggregate perplexity scores often conceal localized geometric collapse—such as distorting the sharp **`L_22 -> L_23` (`1.2474 rad` / `71.47°`) unembedding twist** discovered in v5.
* **The v5 Mathematical Solution:** Combines Audit IV’s `llmfit` memory sizing gate with v5’s closed depth-loop Procrustes holonomy (`compose_depth_holonomy_static` in `Julia`, `0` heap bytes) and Aitchison $\text{clr}$ logit distances.
* **Implementation:**
  * Evaluates calibration prompts across both the `FP32` reference model and a quantized candidate (`torch.ao.quantization.quantize_dynamic`).
  * Audits: (a) `llmfit` memory fit within the target ARM64/CI RAM budget; (b) closed depth-loop holonomy $\Delta_{\text{depth}}$ between `FP32` and quantized trajectories; and (c) preservation of the `L_22 -> L_23` unembedding angle.
  * Emits `COLLAPSE` if memory and geometry pass; otherwise emits `REFUSE(reason="TRACK2_QUANTIZATION_GEOMETRY_DISTORTION")`.

### 2.3 Track 3: Reusable `Spherepop` CI Provenance & Authorship Action (`v6_apps/ci_provenance_gate.py`)
* **The Engineering Problem:** Coding agents frequently append `Co-authored-by` trailers to Git commits—producing Flyxion’s (2026) **asymmetric inscription** gap, where durable institutional credit is assigned to an ephemeral inference run lacking standing, answerability, or *operative refusal*.
* **The v5 Mathematical Solution:** Operationalizes `InstitutionalWarrant.lean` (`IsAccountableAuthor`) and `Spherepop`’s `POP -> BIND -> VERIFY -> COLLAPSE / REFUSE` lifecycle as a zero-dependency GitHub Actions gate.
* **Implementation:**
  * **`POP` & `VERIFY`:** Opens a scoped audit on the commit SHA, enforces Edge SOP hygiene (`< 1 MB` file size limit), and scans commit messages for unendorsed AI `Co-authored-by` trailers.
  * **`BIND`:** Verifies explicit human endorsement (`Endorsed-by:` trailer or verified SSH/GPG maintainer signature) while preserving factual tool provenance (`Generated-with: <model>`).
  * **`COLLAPSE` vs. `REFUSE`:** Emits an immutable `provenance_warrant.json` artifact or blocks CI with `REFUSE(reason="TRACK3_UNENDORSED_ASYMMETRIC_INSCRIPTION")`.

### 2.4 Track 4: Unembedding Twist & Confabulation Calibration Monitor (`v6_apps/unembedding_calibration_monitor.py`)
* **The Engineering Problem:** When language models confabulate or hallucinate under out-of-distribution prompts, softmax normalization squishes high-magnitude logits onto the simplex boundary $\partial \Delta^{V-1}$ (**simplex collapse**, where Euclidean distance dropped $14\times$ at radial scale $c=50$ in Experiment A), masking internal instability behind false high-confidence token probabilities.

* The v5 Mathematical Solution: In Experiment E, we discovered that Qwen/Qwen2.5-0.5B executes a sharp 71.47° (1.2474 rad) orthogonal rotation at the final transition L_22 -> L_23, while Aitchison $\text{clr}$ coordinates preserve exact linear dispersion across all $151{,}936$ pre-softmax logits without boundary saturation.
* Implementation:
  * Captures the penultimate and final hidden states ($h_{N-2}, h_{N-1}$) alongside pre-softmax logits $z \in \mathbb{R}^V$.
	* Computes: (a) the terminal unembedding twist angle $\theta_{N-2 \to N-1}$ relative to the model's calibrated baseline distribution (~1.2474 rad), flagging anomalous under-rotation or over-rotation ($\Delta \theta > \tau_{\text{twist}}$); and (b) Aitchison $\text{clr}$ norm $|\text{clr}(\sigma(z))|_2$ to detect pathological radial logit blowup near $\partial \Delta^{V-1}$.
	* Flags uncalibrated generations with REFUSE(reason="TRACK4_UNEMBEDDING_CALIBRATION_ANOMALY"), separating confident reasoning from boundary-saturated confabulation.

---

### 3. Shared Zero-sorry Lean 4 Specification (V6ApplicationContracts)

All four tracks are governed by a unified Lean 4 contract appended to lean/EpistemicAudit.lean:
```lean
namespace V6ApplicationContracts
open SpherepopSheafBridge
/-- Unified operational state across all four v6 application tracks:
Track 1 (Firewall), Track 2 (Quantization), Track 3 (CI Warrant), Track 4 (Calibration). -/
structure V6DeploymentState where
firewallLayersClean : Bool        -- Track 1: mid-pass sheaf coboundary within threshold
quantGeometryValid : Bool         -- Track 2: FP32 vs Quant depth holonomy & memory within budget
humanWarrantBound : Bool          -- Track 3: accountable human endorsement present, no unendorsed AI byline
unembeddingCalibrated : Bool      -- Track 4: terminal L_{N-2}->L_{N-1} twist & Aitchison clr within bounds
def evaluateV6Pipeline (s : V6DeploymentState) : Disposition :=
if s.firewallLayersClean && s.quantGeometryValid && s.humanWarrantBound && s.unembeddingCalibrated then
Disposition.collapsed
else if !s.firewallLayersClean then
Disposition.refused "TRACK1_RUNTIME_STEERING_OBSTRUCTION"
else if !s.quantGeometryValid then
Disposition.refused "TRACK2_QUANTIZATION_GEOMETRY_DISTORTION"
else if !s.humanWarrantBound then
Disposition.refused "TRACK3_UNENDORSED_ASYMMETRIC_INSCRIPTION"
else
Disposition.refused "TRACK4_UNEMBEDDING_CALIBRATION_ANOMALY"
theorem v6_pipeline_collapses_iff_all_four_tracks_pass (s : V6DeploymentState) :
evaluateV6Pipeline s = Disposition.collapsed ↔
(s.firewallLayersClean = true ∧
s.quantGeometryValid = true ∧
s.humanWarrantBound = true ∧
s.unembeddingCalibrated = true) := by
unfold evaluateV6Pipeline
by_cases h1 : s.firewallLayersClean = true <;>
by_cases h2 : s.quantGeometryValid = true <;>
by_cases h3 : s.humanWarrantBound = true <;>
by_cases h4 : s.unembeddingCalibrated = true <;>
simp [h1, h2, h3, h4]
end V6ApplicationContracts
```
---

## 4. Phased Build & Execution Strategy (ARM64 Edge-Safe)

To build all four tracks coherently while keeping Termux storage untouched (Clone -> Seal -> Push -> Purge), execute in two clean phases:

Build Phase	Deliverables	Hardware & CI Footprint	Verification Gate
Phase A: Shared Core + Track 3 (Pure Python + Lean 4)	lean/EpistemicAudit.lean (V6ApplicationContracts), v6_core/spherepop_runtime.py, and Track 3 v6_apps/ci_provenance_gate.py.	Runs natively on ARM64 Termux (< 50 MB RAM) and in GitHub CI in < 1s.	Zero-sorry lake build + live provenance audit on epistemic-substrate-lab commits.
Phase B: Tracks 1, 2 & 4 (Shared Qwen2.5-0.5B Forward-Pass Harness)	Track 1 (steering_firewall.py), Track 2 (quantization_auditor.py), and Track 4 (unembedding_calibration_monitor.py) sharing one Qwen/Qwen2.5-0.5B capture.	Executed in GitHub Actions CI (~2.4 GB RAM); authored in Termux via < 8 KB text blocks.	Track 1 halts L_12 injection; Track 2 audits FP32 vs INT8 twist; Track 4 flags radial clr blowup.

---

## 5. Conclusion

Including Track 4 completes the practical engineering arc of epistemic-substrate-lab: Track 1 guards the interior layers mid-pass, Track 2 certifies edge quantization across depth, Track 3 enforces accountable human provenance in version control, and Track 4 monitors the L_22 -> L_23 (71.47°) unembedding boundary via Aitchison $\text{clr}$ geometry. Unified under one Spherepop runtime and one zero-sorry Lean 4 contract, v6 turns our theoretical findings into deployable, edge-safe AI infrastructure.

## References

Aitchison, J. (1986). The statistical analysis of compositional data. Chapman and Hall. doi.org
Dettmers, T., Lewis, M., Belkada, Y., & Zettlemoyer, L. (2022). GPT3.int8(): 8-bit matrix multiplication for transformers at scale. In Advances in Neural Information Processing Systems (Vol. 35, pp. 30318–30332). Curran Associates.
Flyxion. (2026a, November). Persistence and accountable authorship in language model systems [Preprint]. Independent Researcher.
Flyxion. (2026b). Spherepop kernel: Scoped event-history maintenance and differential Python/Rust verification (Commit fe79af59b23fc531b41e52ceb4c28343915a943b) [Computer software]. GitHub. github.com
Hansen, J., & Ghrist, R. (2019). Toward a spectral theory of cellular sheaves. Journal of Applied and Computational Topology, 3(4), 315–358. doi.org
Hedling, B. S. (2026). Epistemic substrate lab: Zero-sorry Lean 4 proofs, zero-allocation Riemannian geometry, and multi-layer transformer sheaf audits (Commit c0a3462) [Computer software]. GitHub. github.com
Qwen Team. (2024). Qwen2.5 technical report (arXiv:2412.15115). arXiv. arxiv.org
