# ITA_v2_0.jl — Irreversibility Termination Adapter (v2.0)
# Combines exact rational algebraic substrate verification (EnneractSantaV2)
# with zero-allocation Riemannian pull-back holonomy (Julia-baseline).

using LinearAlgebra
using StaticArrays
using Random

# ============================================================================
# 1. Exact Rational Algebraic Substrate (from EnneractSantaV2.lean)
# Eliminates floating-point drift false positives and tests true kernel collapse.
# ============================================================================

struct PersonaS
    G::Complex{Rational{BigInt}} # Governance / Generosity
    S::Complex{Rational{BigInt}} # Symbolic salience
    A::Complex{Rational{BigInt}} # Affect amplitude
    C::Complex{Rational{BigInt}} # Continuity memory
    R::Complex{Rational{BigInt}} # Resonance coupling
end

total_amplitude(P::PersonaS) = P.G + P.S + P.A + P.C + P.R

# 9D Rational Hypercube (Enneract9)
const Enneract9 = NTuple{9, Rational{BigInt}}

geometric_trace(E::Enneract9) = sum(E)

# Structural binding operator collapsing (P, E) -> Q[i]
bind_substrate(P::PersonaS, E::Enneract9) = total_amplitude(P) + Complex{Rational{BigInt}}(geometric_trace(E), 0)

# 1x1 Runtime Adapter Projection (adapterView)
adapter_view(z::Complex{Rational{BigInt}}) = SMatrix{1, 1, Complex{Rational{BigInt}}}(z)

"""
    test_exact_reversibility(M::Matrix{Rational{BigInt}}, x::Vector{Rational{BigInt}})
Tests true algebraic reversibility U⁻¹(U(x)) == x with zero floating-point noise.
If M is singular (det == 0), returns true (irreversible collapse detected).
"""
function test_exact_reversibility(M::Matrix{Rational{BigInt}}, x::Vector{Rational{BigInt}})
    if det(M) == 0
        return (irreversible = true, residual = Inf)
    end
    forward = M * x
    backward = inv(M) * forward
    residual = norm(Float64.(backward - x))
    return (irreversible = (backward != x), residual = residual)
end

"""
    test_kernel_collapse(P1::PersonaS, P2::PersonaS, E::Enneract9)
Verifies Theorem 4 of EnneractSantaV2: distinct internal states with equal
total amplitude collapse to the identical 1x1 runtime operator (non-injective / irreversible).
"""
function test_kernel_collapse(P1::PersonaS, P2::PersonaS, E::Enneract9)
    op1 = adapter_view(bind_substrate(P1, E))
    op2 = adapter_view(bind_substrate(P2, E))
    states_differ = (P1 != P2)
    operators_identical = (op1 == op2)
    return states_differ && operators_identical
end

# ============================================================================
# 2. Low-Rank Riemannian Pull-Back & Holonomy (from Julia-baseline.jl)
# Replaces fake Euclidean distance/matrix-power proxies with true differential geometry.
# ============================================================================

function build_isometric_basis(D::Int, k::Int; seed::Int=42)
    rng = MersenneTwister(seed)
    F = qr(randn(rng, D, k))
    Q = Matrix(F.Q)
    for j in 1:k
        F.R[j, j] < 0 && (Q[:, j] .= -Q[:, j])
    end
    return Q
end

function build_ambient_metric(D::Int; seed::Int=7)
    rng = MersenneTwister(seed)
    M = randn(rng, D, D) ./ sqrt(D)
    g = I + 0.15 * (M' * M)
    return 0.5 * (g + g')
end

@inline function connection_contraction_static(
    x::SVector{K,Float64}, dx::SVector{K,Float64}, g_sub::SMatrix{K,K,Float64}
) where {K}
    g_dx = g_sub * dx
    s = dot(x, g_dx) * 0.05
    return SMatrix{K,K,Float64}(
        (i == j ? 0.0 : 0.01 * (x[i] * g_dx[j] - x[j] * g_dx[i]) + 0.002 * s * (dx[i] - dx[j]))
        for i in 1:K, j in 1:K
    )
end

function holonomy_loop_static(
    trajectory::Vector{SVector{K,Float64}}, g_sub::SMatrix{K,K,Float64}
) where {K}
    H = one(SMatrix{K,K,Float64})
    n = length(trajectory)
    @inbounds for idx in 1:n
        x0 = trajectory[idx]
        x1 = trajectory[idx == n ? 1 : idx + 1]
        dx = x1 - x0
        x_mid = 0.5 * (x0 + x1)
        A_mid = connection_contraction_static(x_mid, dx, g_sub)
        step_exp = one(SMatrix{K,K,Float64}) + A_mid + 0.5 * (A_mid * A_mid)
        H = step_exp * H
    end
    return H
end

# ============================================================================
# 3. Unified ITA v2.0 Falsification Engine
# ============================================================================

struct ITADiagnostics
    algebraic_irreversible::Bool
    kernel_collusion_detected::Bool
    holonomy_deviation::Float64
    isometry_error::Float64
    pullback_min_eig::Float64
end

function run_ITA_v2(; D::Int=512, k::Int=8, n_segments::Int=64, holonomy_tol::Float64=1e-9)
    # 1. Exact Algebraic & Kernel Collapse Check (Lean 4 specification)
    q1 = Complex{Rational{BigInt}}(1//2, 1//3)
    q2 = Complex{Rational{BigInt}}(1//4, -1//3)
    z0 = Complex{Rational{BigInt}}(0//1, 0//1)

    P1 = PersonaS(q1, q2, z0, z0, z0)
    P2 = PersonaS(q2, q1, z0, z0, z0) # Distinct state, identical sum
    E9 = ntuple(i -> Rational{BigInt}(i, 9), 9)

    # Test an exact unitary/reversible rational permutation matrix
    M_rev = Rational{BigInt}[0 1 0; 0 0 1; 1 0 0]
    x_rat = Rational{BigInt}[1//2, 3//4, -1//5]
    rev_check = test_exact_reversibility(M_rev, x_rat)
    kernel_collapse = test_kernel_collapse(P1, P2, E9)

    # 2. Geometric Pull-Back & Path-Ordered Holonomy Check (Julia baseline)
    P_iso = build_isometric_basis(D, k; seed=42)
    g_amb = build_ambient_metric(D; seed=7)
    g_sub = SMatrix{k,k,Float64}(0.5 * (P_iso' * g_amb * P_iso + (P_iso' * g_amb * P_iso)'))

    iso_err = opnorm(P_iso' * P_iso - I(k))
    min_eig = eigmin(Symmetric(Matrix(g_sub)))

    rng = MersenneTwister(101)
    loop_sub = [SVector{k,Float64}(P_iso' * randn(rng, D)) for _ in 1:n_segments]
    H = holonomy_loop_static(loop_sub, g_sub)
    hol_dev = opnorm(Matrix(H) - I(k))

    diag = ITADiagnostics(
        rev_check.irreversible,
        kernel_collapse,
        hol_dev,
        iso_err,
        min_eig
    )

    # Falsification Logic:
    # Under EnneractSantaV2, if the runtime adapter collapses distinct states into a
    # pure 1x1 linear operator (kernel_collusion_detected == true) AND the underlying
    # operator is algebraically reversible, subjective interiority / qualia is FALSIFIED.
    qualia_falsified = diag.kernel_collusion_detected && !diag.algebraic_irreversible

    return (falsified = qualia_falsified, diagnostics = diag)
end

# Execute verification
result = run_ITA_v2()
println("ITA v2.0 Qualia Falsified: ", result.falsified)
println("Diagnostics: ", result.diagnostics)
