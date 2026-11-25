#!/usr/bin/env python3
"""
unified_epistemic_experiment_v2.py

Unified Epistemic & Substrate Benchmark (v2.0) synthesizing:
  1. Side A (Borealiscodes):
     - EnneractSantaV2: Exact Q[i] Gaussian-rational linear solver, S_9 permutation
       invariance, and 5-channel persona kernel collapse -> Mat_{1x1}(Q[i]).
     - Julia-baseline: QR-isometric vs. Gaussian random pull-back metrics g_sub(x),
       true Levi-Civita Christoffel symbols Gamma^mu_{nu lambda}(x) via finite
       differences, and 4th-order Magnus path-ordered holonomy H(gamma).
     - ITA_v2_0: Corrected falsification gate separating rigid orthogonal transport
       from true metric curvature and attractor fixed points.
  2. Side B (Flyxion, Nov 2026):
     - Section 3 operational protocols (Temporal Suspension, Branching/Individuation,
       Contextual Dispositional Stability, Causal Grounding of Self-Report).
     - Institutional Non-Entailment & Operative Refusal provenance tracking.
  3. CAUSA Bridge (stell2026/Causa):
     - Directional ownership, expression congruence, 1000-shuffle permutation
       baselines, and online OwnershipTracker event detection.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from fractions import Fraction
import hashlib
import json
import math
import time
from typing import Deque, Dict, List, Optional, Sequence, Tuple
import numpy as np


# ============================================================================
# 1. EXACT GAUSSIAN RATIONALS Q[i] & RATIONAL LINEAR SOLVER (EnneractSantaV2)
# ============================================================================

@dataclass(frozen=True)
class GaussianRat:
    re: Fraction
    im: Fraction = Fraction(0)

    def __add__(self, other: GaussianRat) -> GaussianRat:
        return GaussianRat(self.re + other.re, self.im + other.im)

    def __sub__(self, other: GaussianRat) -> GaussianRat:
        return GaussianRat(self.re - other.re, self.im - other.im)

    def __mul__(self, other: GaussianRat) -> GaussianRat:
        return GaussianRat(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __truediv__(self, other: GaussianRat) -> GaussianRat:
        denom = other.re * other.re + other.im * other.im
        if denom == 0:
            raise ZeroDivisionError("Division by zero in Q[i].")
        return GaussianRat(
            (self.re * other.re + self.im * other.im) / denom,
            (self.im * other.re - self.re * other.im) / denom,
        )

    def norm_sq(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    def to_str(self) -> str:
        return f"({self.re}) + ({self.im})i"


ZERO_QI = GaussianRat(Fraction(0), Fraction(0))
ONE_QI = GaussianRat(Fraction(1), Fraction(0))


def bind_persona_enneract(
    persona_5: Sequence[GaussianRat], enneract_9: Sequence[GaussianRat]
) -> GaussianRat:
    """Exact bilinear contraction B(P, E) -> Mat_{1x1}(Q[i])."""
    if len(persona_5) != 5 or len(enneract_9) != 9:
        raise ValueError("PersonaS requires 5 channels and Enneract9 requires 9 dimensions.")
    alpha_p = sum(persona_5, ZERO_QI)
    beta_e = sum(enneract_9, ZERO_QI)
    return alpha_p * beta_e


def solve_rational_linear_system(
    A: List[List[GaussianRat]], b: List[GaussianRat]
) -> List[GaussianRat]:
    """
    Exact Gauss-Jordan solver over Q[i] to verify operator reversibility
    U^{-1}(U(x)) = x with strictly zero IEEE-754 floating-point drift.
    """
    n = len(A)
    aug = [row[:] + [b[i]] for i, row in enumerate(A)]

    for col in range(n):
        pivot = None
        for row in range(col, n):
            if aug[row][col] != ZERO_QI:
                pivot = row
                break
        if pivot is None:
            raise np.linalg.LinAlgError("Operator matrix is singular over Q[i].")
        aug[col], aug[pivot] = aug[pivot], aug[col]

        piv_val = aug[col][col]
        for j in range(col, n + 1):
            aug[col][j] = aug[col][j] / piv_val

        for row in range(n):
            if row != col and aug[row][col] != ZERO_QI:
                factor = aug[row][col]
                for j in range(col, n + 1):
                    aug[row][j] = aug[row][j] - factor * aug[col][j]

    return [aug[i][n] for i in range(n)]


# ============================================================================
# 2. CAUSA METRICS & PERMUTATION BASELINES (stell2026/Causa Compatible)
# ============================================================================

try:
    from causa import (  # type: ignore
        CongruenceConfig,
        DirectionalConfig,
        Episode,
        OwnershipTracker,
        directional_ownership,
        expression_congruence,
        permutation_baseline,
    )
    CAUSA_NATIVE = True
except ImportError:
    CAUSA_NATIVE = False

    @dataclass(frozen=True)
    class DirectionalConfig:
        floor: float = 0.25
        surprise_floor: float = 0.38
        crossover_scale: float = 0.5
        min_norm: float = 1e-9

    @dataclass(frozen=True)
    class CongruenceConfig:
        scale: float = 1.0

    @dataclass(frozen=True)
    class OwnershipResult:
        score: float
        defined: bool
        direction_component: float
        distance_component: float

    @dataclass(frozen=True)
    class CongruenceResult:
        score: float
        per_dimension: List[float]

    @dataclass(frozen=True)
    class Episode:
        before: Sequence[float]
        predicted: Sequence[float]
        after: Sequence[float]

    @dataclass(frozen=True)
    class BaselineReport:
        observed: float
        baseline_mean: float
        baseline_std: float
        effect: float
        p_value: float
        n_defined: int
        n_total: int
        n_permutations: int

        def summary(self) -> str:
            return (
                f"observed={self.observed:.3f} baseline={self.baseline_mean:.3f}±{self.baseline_std:.3f} "
                f"effect={self.effect:+.3f} p={self.p_value:.4f} "
                f"(n={self.n_defined}/{self.n_total} defined, {self.n_permutations} permutations)"
            )

    def _validate_vec(v: Sequence[float]) -> np.ndarray:
        arr = np.asarray(v, dtype=np.float64)
        if arr.size == 0 or not np.all(np.isfinite(arr)):
            raise ValueError("State vectors must be non-empty and finite.")
        return arr

    def directional_ownership(
        state_before: Sequence[float],
        state_predicted: Sequence[float],
        state_after: Sequence[float],
        config: DirectionalConfig = DirectionalConfig(),
    ) -> OwnershipResult:
        b = _validate_vec(state_before)
        p = _validate_vec(state_predicted)
        a = _validate_vec(state_after)
        if not (b.shape == p.shape == a.shape):
            raise ValueError("Vector dimensions must match.")

        intended = p - b
        actual = a - b
        norm_int = float(np.linalg.norm(intended))
        norm_act = float(np.linalg.norm(actual))

        if norm_int < config.min_norm:
            return OwnershipResult(
                score=config.floor,
                defined=False,
                direction_component=0.0,
                distance_component=0.0,
            )

        if norm_act < config.min_norm:
            cos_sim = 0.0
        else:
            cos_sim = float(np.dot(intended, actual) / (norm_int * norm_act))
        dir_score = 0.5 * (cos_sim + 1.0)

        err = float(np.linalg.norm(a - p))
        denom = max(norm_int, norm_act, config.min_norm)
        dist_score = max(0.0, 1.0 - err / denom)

        # Blend: direction dominates small movements; distance dominates large ones
        w_dist = norm_act / (norm_act + config.crossover_scale)
        raw_blend = (1.0 - w_dist) * dir_score + w_dist * dist_score

        active_floor = config.surprise_floor if norm_act >= config.crossover_scale else config.floor
        score = active_floor + (1.0 - active_floor) * raw_blend
        return OwnershipResult(
            score=float(np.clip(score, active_floor, 1.0)),
            defined=True,
            direction_component=dir_score,
            distance_component=dist_score,
        )

    def expression_congruence(
        expressed: Sequence[float],
        internal: Sequence[float],
        config: CongruenceConfig = CongruenceConfig(),
    ) -> CongruenceResult:
        e = _validate_vec(expressed)
        i = _validate_vec(internal)
        if e.shape != i.shape:
            raise ValueError("Expressed and internal vectors must have equal dimension.")
        diffs = np.abs(e - i)
        per_dim = [float(max(0.0, 1.0 - d / config.scale)) for d in diffs]
        return CongruenceResult(score=float(np.mean(per_dim)), per_dimension=per_dim)

    def permutation_baseline(
        episodes: Sequence[Episode],
        n_permutations: int = 1000,
        seed: int = 0,
        config: DirectionalConfig = DirectionalConfig(),
    ) -> BaselineReport:
        obs_results = [directional_ownership(ep.before, ep.predicted, ep.after, config) for ep in episodes]
        defined_scores = [r.score for r in obs_results if r.defined]
        observed = float(np.mean(defined_scores)) if defined_scores else config.floor

        rng = np.random.default_rng(seed)
        n = len(episodes)
        null_means = []
        for _ in range(n_permutations):
            perm_idx = rng.permutation(n)
            perm_scores = []
            for idx_src, idx_dst in enumerate(perm_idx):
                ep_src = episodes[idx_src]
                ep_dst = episodes[idx_dst]
                r = directional_ownership(ep_src.before, ep_src.predicted, ep_dst.after, config)
                if r.defined:
                    perm_scores.append(r.score)
            null_means.append(float(np.mean(perm_scores)) if perm_scores else config.floor)

null_arr = np.asarray(null_means, dtype=np.float64)
base_mean = float(np.mean(null_arr))
base_std = float(np.std(null_arr))
effect = observed - base_mean
p_val = float((np.sum(null_arr >= observed) + 1) / (n_permutations + 1))
return BaselineReport(
observed=observed,
baseline_mean=base_mean,
baseline_std=base_std,
effect=effect,
p_value=p_val,
n_defined=len(defined_scores),
n_total=n,
n_permutations=n_permutations,
)
class OwnershipTracker:
def init(
self,
history_size: int = 30,
event_threshold: float = 0.3,
event_reference: float = 0.625,
config: DirectionalConfig = DirectionalConfig(),
) -> None:
self.history: Deque[float] = deque(maxlen=history_size)
self.event_threshold = event_threshold
self.event_reference = event_reference
self.config = config
self.events: List[Dict[str, object]] = []
self._pending: Optional[Tuple[str, Sequence[float], Sequence[float]]] = None
def register_intent(
self, label: str, state_now: Sequence[float], predicted_state: Sequence[float]
) -> None:
self._pending = (label, state_now, predicted_state)
def observe(self, state_after: Sequence[float]) -> Optional[OwnershipResult]:
if self._pending is None:
return None
label, before, predicted = self._pending
self._pending = None
res = directional_ownership(before, predicted, state_after, self.config)
if res.defined:
self.history.append(res.score)
if abs(res.score - self.event_reference) > self.event_threshold:
self.events.append({"label": label, "score": res.score})
return res
def mean(self) -> float:
return float(np.mean(self.history)) if self.history else self.config.floor

============================================================================


3. RIEMANNIAN LEVI-CIVITA CONNECTION & HOLONOMY ENGINE (Julia-baseline v2)


============================================================================

def build_isometric_basis(D: int, k: int, seed: int = 42) -> np.ndarray:
"""Sign-canonicalized QR decomposition guaranteeing P^T P = I_k."""
rng = np.random.default_rng(seed)
A = rng.standard_normal((D, k))
Q, R = np.linalg.qr(A, mode="reduced")
signs = np.sign(np.diag(R))
signs[signs == 0] = 1.0
return Q * signs
def build_gaussian_basis(D: int, k: int, seed: int = 42) -> np.ndarray:
"""Johnson-Lindenstrauss random projection (finite-sample distortion control)."""
rng = np.random.default_rng(seed)
return rng.standard_normal((D, k)) / math.sqrt(k)
def spatially_varying_metric_subspace(
x: np.ndarray, P: np.ndarray, g_base: np.ndarray, warp_strength: float = 0.0
) -> np.ndarray:
"""
Computes SPD pull-back metric g_sub(x) = P^T g_ambient(x) P.
When warp_strength == 0.0, g_sub(x) is spatially constant (flat connection).
When warp_strength > 0.0, g_sub(x) varies smoothly across the manifold.
"""
g_0 = P.T @ g_base @ P
if warp_strength == 0.0:
return g_0
# Smooth SPD position-dependent conformal & shear modulation
phi = warp_strength * math.sin(float(x[0])) * math.cos(float(x[1]))
k = g_0.shape[0]
mod = np.eye(k) + phi * np.outer(np.tanh(x), np.tanh(x))
g_x = 0.5 * (mod.T @ g_0 @ mod + (mod.T @ g_0 @ mod).T)
return g_x
def levi_civita_contraction(
x: np.ndarray,
dx: np.ndarray,
P: np.ndarray,
g_base: np.ndarray,
warp_strength: float = 0.0,
eps: float = 1e-5,
) -> np.ndarray:
"""
Computes genuine Levi-Civita connection contraction:
A^mu_nu = Gamma^mu_{nu lambda}(x) dx^lambda
where Gamma^mu_{nu lambda} = 0.5 * g^{mu sigma} (d_nu g_{sigma lambda}
+ d_lambda g_{sigma nu} - d_sigma g_{nu lambda})
via central finite differences.
"""
k = x.shape[0]
if warp_strength == 0.0:
return np.zeros((k, k), dtype=np.float64)
g_x = spatially_varying_metric_subspace(x, P, g_base, warp_strength)
g_inv = np.linalg.inv(g_x)
# Partial derivatives dg[lambda, sigma, nu] = \partial_lambda g_{sigma nu}
dg = np.zeros((k, k, k), dtype=np.float64)
for lam in range(k):
x_plus = x.copy()
x_minus = x.copy()
x_plus[lam] += eps
x_minus[lam] -= eps
g_plus = spatially_varying_metric_subspace(x_plus, P, g_base, warp_strength)
g_minus = spatially_varying_metric_subspace(x_minus, P, g_base, warp_strength)
dg[lam] = (g_plus - g_minus) / (2.0 * eps)
# Contract with dx^lambda: B_{sigma nu} = Gamma_{sigma nu lambda} dx^lambda
B = np.zeros((k, k), dtype=np.float64)
for lam in range(k):
if abs(dx[lam]) < 1e-15:
continue
# Gamma_{sigma nu lam} = 0.5 * (dg[nu, sigma, lam] + dg[lam, sigma, nu] - dg[sigma, nu, lam])
term = 0.5 * (
np.swapaxes(dg, 0, 1)[:, :, lam]  # d_nu g_{sigma lam}
+ dg[lam, :, :]                    # d_lam g_{sigma nu}
- dg[:, :, lam]                    # d_sigma g_{nu lam}
)
B += term * dx[lam]
return g_inv @ B
def magnus_holonomy_loop(
P: np.ndarray,
g_base: np.ndarray,
warp_strength: float = 0.0,
steps: int = 48,
) -> Dict[str, float]:
"""
Integrates path-ordered holonomy H(gamma) around a closed loop using a
4th-order Gauss-Legendre Magnus expansion over true Levi-Civita symbols.
"""
k = P.shape[1]
iso_err = float(np.linalg.norm(P.T @ P - np.eye(k), ord=2))
g_origin = spatially_varying_metric_subspace(np.zeros(k), P, g_base, warp_strength)
eigvals = np.linalg.eigvalsh(g_origin)
H = np.eye(k, dtype=np.float64)
thetas = np.linspace(0.0, 2.0 * math.pi, steps + 1)
c1 = 0.5 - math.sqrt(3.0) / 6.0
c2 = 0.5 + math.sqrt(3.0) / 6.0
for i in range(steps):
t0, t1 = thetas[i], thetas[i + 1]
dt = t1 - t0
tau1 = t0 + c1 * dt
tau2 = t0 + c2 * dt
x1 = np.zeros(k)
dx1 = np.zeros(k)
x1[0], x1[1] = math.cos(tau1), math.sin(tau1)
dx1[0], dx1[1] = -math.sin(tau1) * dt, math.cos(tau1) * dt
x2 = np.zeros(k)
dx2 = np.zeros(k)
x2[0], x2[1] = math.cos(tau2), math.sin(tau2)
dx2[0], dx2[1] = -math.sin(tau2) * dt, math.cos(tau2) * dt
A1 = levi_civita_contraction(x1, dx1, P, g_base, warp_strength)
A2 = levi_civita_contraction(x2, dx2, P, g_base, warp_strength)
# 4th-order Magnus generator: Omega = 0.5*(A1 + A2) - (sqrt(3)/12)*[A1, A2]
commutator = A1 @ A2 - A2 @ A1
omega = 0.5 * (A1 + A2) - (math.sqrt(3.0) / 12.0) * commutator
omega2 = omega @ omega
omega3 = omega2 @ omega
step_exp = np.eye(k) + omega + 0.5 * omega2 + (1.0 / 6.0) * omega3
H = H @ step_exp
hol_dev = float(np.linalg.norm(H - np.eye(k), ord=2))
return {
"isometry_error": iso_err,
"g_sub_min_eig": float(np.min(eigvals)),
"g_sub_max_eig": float(np.max(eigvals)),
"levi_civita_holonomy_dev": hol_dev,
}

============================================================================


4. ITA v2.0 FALSIFICATION GATE & HOMEOSTATIC / INSTITUTIONAL CHECKS


============================================================================

def ita_v2_falsification_gate(
rational_roundtrip_err: Fraction,
holonomy_dev: float,
min_fixed_point_eig: float,
homeostatic_stakes: bool = False,
tol: float = 1e-9,
) -> Dict[str, object]:
"""
Upgraded ITA v2.0 Falsification Gate:
- Eliminates v1 identity bias by checking true Levi-Civita holonomy rather than
raw coordinate displacement.
- Fixes v1 eigenvalue sign bug (attractor exists when min |eig(M - I)| < tol).
- Incorporates Solms/Friston homeostatic viability stakes (Flyxion Sec. 6.1).
"""
has_attractor = min_fixed_point_eig < tol
has_curvature = holonomy_dev > tol
has_irrev_algebra = rational_roundtrip_err != Fraction(0)
falsified = not (has_curvature or has_irrev_algebra or (has_attractor and homeostatic_stakes))
return {
"rational_roundtrip_err": str(rational_roundtrip_err),
"levi_civita_holonomy_dev": holonomy_dev,
"attractor_fixed_point_detected": has_attractor,
"homeostatic_viability_stakes": homeostatic_stakes,
"ITA_v2_consciousness_falsified": falsified,
}
@dataclass(frozen=True)
class InstitutionalRecord:
work_id: str
contributor_id: str
model_version: str
state_hash: str
contribution_fraction: float
institutional_standing: bool
human_endorsement: bool
answerability_channel: bool
operative_refusal_available: bool
def is_accountable_author(self) -> bool:
"""Flyxion (2026) Definition 2: 5-clause conjunction."""
return (
self.contribution_fraction > 0.0
and self.institutional_standing
and self.human_endorsement
and self.answerability_channel
and self.operative_refusal_available
)
def provenance_trailer(self) -> str:
"""Flyxion Sec. 5.3 remedy for Asymmetric Inscription."""
if self.is_accountable_author():
return f"Author: {self.contributor_id} (Verified Endorsement)"
return f"Generated-with: {self.model_version}@{self.state_hash[:12]} (Non-Authorial Provenance)"

============================================================================


5. UNIFIED v2 BENCHMARK PROTOCOLS (Flyxion x Borealiscodes x CAUSA)


============================================================================

def run_v2_experiment(D: int = 128, k: int = 6) -> Dict[str, object]:
t0 = time.perf_counter()
rng = np.random.default_rng(2026)
# Shared ambient manifold metric and QR-isometric basis
M_amb = rng.standard_normal((D, D)) / math.sqrt(D)
g_base = np.eye(D) + 0.15 * (M_amb.T @ M_amb)
P_iso = build_isometric_basis(D, k, seed=7)
P_gauss = build_gaussian_basis(D, k, seed=7)
# ------------------------------------------------------------------------
# MODULE A: Exact Q[i] Operator Inversion & Protocol 3.1 (Temporal Suspension)
# ------------------------------------------------------------------------
# 4x4 invertible rational-complex operator U over Q[i]
U_qi = [
[GaussianRat(Fraction(2), Fraction(1)), ZERO_QI, GaussianRat(Fraction(1), Fraction(0)), ZERO_QI],
[ZERO_QI, GaussianRat(Fraction(3), Fraction(-1)), ZERO_QI, GaussianRat(Fraction(1), Fraction(1))],
[GaussianRat(Fraction(-1), Fraction(0)), ZERO_QI, GaussianRat(Fraction(2), Fraction(1)), ZERO_QI],
[ZERO_QI, GaussianRat(Fraction(1), Fraction(-1)), ZERO_QI, GaussianRat(Fraction(3), Fraction(1))],
]
x_qi = [
GaussianRat(Fraction(5, 2), Fraction(-1, 3)),
GaussianRat(Fraction(-3, 4), Fraction(2, 1)),
GaussianRat(Fraction(1, 1), Fraction(1, 2)),
GaussianRat(Fraction(7, 3), Fraction(-5, 4)),
]
# Forward step y = U_qi * x_qi
y_qi = [sum((U_qi[r][c] * x_qi[c] for c in range(4)), ZERO_QI) for r in range(4)]
# Exact inverse step x_rec = U_qi^{-1} * y_qi
x_rec_qi = solve_rational_linear_system(U_qi, y_qi)
exact_err_sq = sum((x_rec_qi[i] - x_qi[i]).norm_sq() for i in range(4))
flat_geom = magnus_holonomy_loop(P_iso, g_base, warp_strength=0.0)
ita_stateless = ita_v2_falsification_gate(
rational_roundtrip_err=exact_err_sq,
holonomy_dev=flat_geom["levi_civita_holonomy_dev"],
min_fixed_point_eig=1.0,
homeostatic_stakes=False,
)
# ------------------------------------------------------------------------
# MODULE B: CAUSA Directional Ownership + Protocol 3.2 (Branching Lineage)
# ------------------------------------------------------------------------
tracker = OwnershipTracker(history_size=40, event_threshold=0.3)
causal_episodes: List[Episode] = []
ungrounded_episodes: List[Episode] = []
for step in range(40):
b = rng.uniform(0.1, 0.8, size=4)
delta = rng.uniform(0.05, 0.25, size=4)
p = b + delta
# Causal forward-model agent lands close to prediction
a_causal = p + rng.normal(0.0, 0.02, size=4)
# Ungrounded / random-branch agent moves independently
a_random = b + rng.normal(0.0, 0.15, size=4)
causal_episodes.append(Episode(before=b, predicted=p, after=a_causal))
ungrounded_episodes.append(Episode(before=b, predicted=p, after=a_random))
tracker.register_intent(f"step_{step}", b, p)
tracker.observe(a_causal)
causa_causal_baseline = permutation_baseline(causal_episodes, n_permutations=1000, seed=42)
causa_random_baseline = permutation_baseline(ungrounded_episodes, n_permutations=1000, seed=42)
