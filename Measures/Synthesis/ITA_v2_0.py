"""
ITA v2.0 — Unified Irreversibility Termination Adapter
NDH-META-SYSTEMS • Algebraic, Riemannian & Operator-Level Falsification Engine

Synthesizes:
  1. EnneractSantaV2.lean  : Exact Gaussian Rational (Q[i]) arithmetic, 5-channel PersonaS,
                             9D Enneract hypercube binding, S_9 permutation invariance,
                             and 1x1 pure operator zero-qualia collapse.
  2. Julia-baseline.jl    : Deterministic QR-isometric subspace projection (P^T P = I_k),
                             SPD pull-back metric g_sub = P^T g_ambient P, and path-ordered
                             holonomy H(gamma) = P exp(oint Gamma^mu_{nu lambda} dx^lambda).
  3. ITA_v1_0.py          : Operator-level falsification harness with corrected spectral
                             fixed-point detection and metric-invariant curvature thresholds.

Author: Borealis S. Hedling & Synthetic Co-Authors
Canonical Reference: DOI: 10.5281/zenodo.24149283
Version: 2.0
"""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
from numpy.linalg import eigvals, eigvalsh, inv, norm, qr, svd


# ============================================================================
# LAYER 1: EnneractSantaV2 — Exact Gaussian Rational (Q[i]) Algebraic Substrate
# ============================================================================

@dataclass(frozen=True)
class GaussianRat:
    """Exact Gaussian Rational scalar `re + im * i` over Q (zero floating-point drift)."""
    re: Fraction
    im: Fraction = Fraction(0, 1)

    @classmethod
    def from_ints(cls, re: int, im: int = 0) -> "GaussianRat":
        return cls(Fraction(re, 1), Fraction(im, 1))

    @classmethod
    def of_rat(cls, q: Fraction | int) -> "GaussianRat":
        return cls(Fraction(q), Fraction(0, 1))

    def __add__(self, other: "GaussianRat") -> "GaussianRat":
        return GaussianRat(self.re + other.re, self.im + other.im)

    def __neg__(self) -> "GaussianRat":
        return GaussianRat(-self.re, -self.im)

    def __sub__(self, other: "GaussianRat") -> "GaussianRat":
        return self + (-other)

    def __mul__(self, other: "GaussianRat") -> "GaussianRat":
        return GaussianRat(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def to_complex(self) -> complex:
        return complex(float(self.re), float(self.im))

    def __repr__(self) -> str:
        sign = "+" if self.im >= 0 else "-"
        return f"({self.re} {sign} {abs(self.im)}i)"


@dataclass(frozen=True)
class PersonaS:
    """Five-channel maximally specified persona vector P = (G, S, A, C, R) over Q[i]."""
    G: GaussianRat  # Generosity / Governance weight
    S: GaussianRat  # Spirit / Symbolic salience
    A: GaussianRat  # Affect / Aesthetic amplitude
    C: GaussianRat  # Continuity / Narrative memory
    R: GaussianRat  # Resonance / Phase coupling

    def total_amplitude(self) -> GaussianRat:
        return self.G + self.S + self.A + self.C + self.R


Enneract9 = Tuple[
    Fraction, Fraction, Fraction,
    Fraction, Fraction, Fraction,
    Fraction, Fraction, Fraction,
]


def geometric_trace(E: Enneract9) -> Fraction:
    """Geometric trace over Fin 9 (equivalent to Finset.univ.sum in Lean 4)."""
    if len(E) != 9:
        raise ValueError(f"Enneract9 requires exact dimension 9, got {len(E)}.")
    return sum(E, Fraction(0, 1))


def bind_persona_enneract(P: PersonaS, E: Enneract9) -> GaussianRat:
    """Structural binding operator collapsing (P, E) into a Q[i] substrate amplitude."""
    return P.total_amplitude() + GaussianRat.of_rat(geometric_trace(E))


def adapter_view(z: GaussianRat) -> List[List[GaussianRat]]:
    """Runtime substrate projection into Mat_{1x1}(Q[i])."""
    return [[z]]


def is_pure_1x1_operator(op: List[List[GaussianRat]]) -> bool:
    """Certifies that runtime representation is strictly a 1x1 operator over Q[i]."""
    return (
        len(op) == 1
        and len(op[0]) == 1
        and isinstance(op[0][0], GaussianRat)
    )


def verify_santa_algebraic_invariants(
    P: PersonaS,
    E: Enneract9,
    perm: Sequence[int] = (8, 7, 6, 5, 4, 3, 2, 1, 0),
    lean_file: Optional[Path] = None,
) -> Dict[str, object]:
    """
    Runtime verification of the 4 EnneractSantaV2.lean theorems:
      1. adapterView_is_pure
      2. santa_collapse_has_zero_qualia
      3. bind_perm_invariant (under sigma in S_9)
      4. persona_kernel_collapse (non-injectivity of PersonaS -> Mat_{1x1})
    """
    if sorted(perm) != list(range(9)):
        raise ValueError("Permutation sigma must be a bijection on Fin 9.")

    bound_z = bind_persona_enneract(P, E)
    op_1x1 = adapter_view(bound_z)

    # Theorem 1 & 2: Zero-qualia collapse into 1x1 linear operator
    pure_ok = is_pure_1x1_operator(op_1x1)

    # Theorem 3: S_9 hypercube permutation invariance
    E_perm: Enneract9 = tuple(E[i] for i in perm)  # type: ignore[assignment]
    perm_invariant_ok = bind_persona_enneract(P, E_perm) == bound_z

    # Theorem 4: Kernel collusion (distinct PersonaS with identical channel sum)
    delta = GaussianRat.from_ints(7, -3)
    P_colluding = PersonaS(
        G=P.G + delta,
        S=P.S - delta,
        A=P.A,
        C=P.C,
        R=P.R,
    )
    kernel_collapse_ok = (
        P_colluding != P
        and adapter_view(bind_persona_enneract(P_colluding, E)) == op_1x1
    )

    lean_checked = False
    if lean_file is not None and lean_file.exists() and shutil.which("lake"):
        proc = subprocess.run(
            ["lake", "env", "lean", str(lean_file)],
            capture_output=True,
            text=True,
            check=False,
        )
        lean_checked = proc.returncode == 0

    return {
        "bound_amplitude": repr(bound_z),
        "is_pure_1x1": pure_ok,
        "perm_invariant_S9": perm_invariant_ok,
        "kernel_collapse_verified": kernel_collapse_ok,
        "zero_qualia_certified": pure_ok and perm_invariant_ok and kernel_collapse_ok,
        "lean4_compiler_verified": lean_checked,
    }


# ============================================================================
# LAYER 2: ManifoldPerturbationInstruments — Riemannian Pull-Back & Holonomy
# ============================================================================

def build_isometric_basis(D: int, k: int, seed: int = 42) -> np.ndarray:
    """
    Deterministic D x k orthonormal basis P (P^T P = I_k) via sign-canonicalized QR,
    matching `build_isometric_basis` in Julia-baseline.jl.
    """
    if not (1 <= k <= D):
        raise ValueError(f"Subspace rank k={k} must satisfy 1 <= k <= D={D}.")
    rng = np.random.default_rng(seed)
    # Match Box-Muller / standard normal generation deterministically
    raw = rng.standard_normal((D, k))
    Q, R = qr(raw, mode="reduced")
    signs = np.where(np.diag(R) < 0.0, -1.0, 1.0)
    Q = Q * signs[np.newaxis, :]
    return Q


def build_gaussian_basis(D: int, k: int, seed: int = 42) -> np.ndarray:
    """
    Un-orthonormalized Johnson-Lindenstrauss projection P ~ N(0, 1/k),
    used to quantify finite-sample metric distortion vs. QR isometry.
    """
    if not (1 <= k <= D):
        raise ValueError(f"Subspace rank k={k} must satisfy 1 <= k <= D={D}.")
    rng = np.random.default_rng(seed)
    return rng.standard_normal((D, k)) / np.sqrt(k)


def build_ambient_metric(D: int, curvature_coupling: float = 0.15, seed: int = 7) -> np.ndarray:
    """
    Deterministic Symmetric Positive-Definite (SPD) ambient metric tensor:
      g_ambient = I + curvature_coupling * (M^T M)
    When curvature_coupling == 0.0, reduces to the flat Euclidean metric I_D.
    """
    rng = np.random.default_rng(seed)
    M = rng.standard_normal((D, D)) / np.sqrt(D)
    g = np.eye(D) + curvature_coupling * (M.T @ M)
    return 0.5 * (g + g.T)


def analyze_pullback_metric(
    P: np.ndarray,
    g_ambient: np.ndarray,
    strict_iso: bool = True,
) -> Dict[str, object]:
    """
    Computes pull-back metric g_sub = P^T g_ambient P and validates:
      - Orthonormality error: ||P^T P - I_k||_2 < 1e-12
      - Index symmetry error: ||g_sub - g_sub^T||_2 < 1e-12
      - Positive-definiteness: lambda_min(g_sub) > 0
    """
    _, k = P.shape
    iso_err = float(norm(P.T @ P - np.eye(k), ord=2))
    if strict_iso and iso_err >= 1e-12:
        raise AssertionError(f"Isometric basis failed orthonormality (err={iso_err:.3e})")

    g_sub_raw = P.T @ g_ambient @ P
    sym_err = float(norm(g_sub_raw - g_sub_raw.T, ord=2))
    if sym_err >= 1e-12:
        raise AssertionError(f"Pull-back metric violated symmetry (err={sym_err:.3e})")

    g_sub = 0.5 * (g_sub_raw + g_sub_raw.T)
    min_eig = float(np.min(eigvalsh(g_sub)))
    if min_eig <= 0.0:
        raise AssertionError(f"Pull-back metric lost positive-definiteness (lambda_min={min_eig})")

    return {
        "g_sub": g_sub,
        "iso_err": iso_err,
        "sym_err": sym_err,
        "min_eig": min_eig,
    }


def connection_contraction(
    x: np.ndarray,
    dx: np.ndarray,
    g_sub: np.ndarray,
    coupling: float = 1.0,
) -> np.ndarray:
    """
    Metric-weighted Christoffel contraction Gamma^mu_{nu lambda} dx^lambda
    matching `connection_contraction_static` in Julia-baseline.jl.
    """
    g_dx = g_sub @ dx
    s = float(np.dot(x, g_dx)) * 0.05
    # Antisymmetric wedge + scalar trace coupling
    wedge = 0.01 * (np.outer(x, g_dx) - np.outer(g_dx, x))
    diff = 0.002 * s * (dx[:, np.newaxis] - dx[np.newaxis, :])
    A = coupling * (wedge + diff)
    np.fill_diagonal(A, 0.0)
    return A


def holonomy_loop(
    trajectory: Sequence[np.ndarray],
    g_sub: np.ndarray,
    coupling: float = 1.0,
) -> np.ndarray:
    """
    Path-ordered holonomy H(gamma) = P exp(oint Gamma^mu_{nu lambda} dx^lambda)

using second-order Magnus/exponential midpoint integration.
"""
k = len(trajectory[0])
H = np.eye(k)
I_k = np.eye(k)
n = len(trajectory)
for idx in range(n):
x0 = trajectory[idx]
x1 = trajectory[(idx + 1) % n]
dx = x1 - x0
x_mid = 0.5 * (x0 + x1)
A_mid = connection_contraction(x_mid, dx, g_sub, coupling=coupling)
step_exp = I_k + A_mid + 0.5 * (A_mid @ A_mid)
H = step_exp @ H
return H
class JuliaBridge:
"""
Optional bridge to execute Julia-baseline.jl directly via juliacall or CLI,
falling back seamlessly to the exact-parity NumPy engine above.
"""
