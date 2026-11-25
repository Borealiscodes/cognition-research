# Originality, Statistical Recombination, and Provenance Laundering: A Statutory and Forensic Analysis of Automated Ingestion Pipelines

**Author:** Borealis S. Hedling  
**Affiliation:** Independent Systems & Cognitive Geometry Research, Dublin, Ireland (`ORCID: 0009-0004-7968-5707`)  
**Tooling Companion:** [`Berne-Provenance-Toolkit`](https://github.com)  
**Canonical Lineage Anchor:** *Epistemic Coevolution, Statutory Friction, and Sovereign Edge Governance* (`DOI: 10.5281/zenodo.24149283`)  
**Cryptographic Attestation:** `Ed25519` (`SHA256:QUOn/esk9dfLFyc/AwFHMIlK5zbI5JOpZTI5vh3y7Dg`)  
**Governance Posture:** Educational • Forensic • Descriptive-Only • Sealed-Layer Neutral (`Author Sovereignty Charter v1.2`)  
**Date:** 14 November 2026  

---

## Abstract

Contemporary web scrapers, multi-hop repository aggregators, and Model Context Protocol (`MCP`) servers routinely conflate syntactic token transformation with original authorship. When automated ingestion pipelines chunk, summarize, or paraphrase human-authored documentation and source code while stripping upstream metadata, they commit a dual failure: legally, they confuse uncreative statistical recombination with protected derivative authorship; technically, they sever cryptographic chains of custody. Grounded in international treaty law (the **Berne Convention**, the **WIPO Copyright Treaty**, and the **TRIPS Agreement**), European Union originality jurisprudence (*Infopaq*), and **Ireland's Copyright and Related Rights Act 2000**, this paper analyzes the structural flaws in how automated pipelines define "original work." We formalize a four-class forensic defect taxonomy (`BERNE-6BIS-PATERNITY`, `BERNE-6BIS-INTEGRITY`, `PROVENANCE-HOP-DRIFT`, and `MCP-SCHEMA-UNBOUND`) and demonstrate how lightweight `SHA-256` custody manifests and typed JSON Schemas restore verifiable author sovereignty and autonomy.

---

## 1. Introduction: The Fallacy of Syntactic Originality

In software engineering and academic publishing, an "original work" is defined by deliberate human judgment—the selection, arrangement, mathematical formulation, and expressive framing authored by a person. By contrast, high-velocity automated ingestion pipelines treat text and source code as fungible token streams.

When an aggregator or `MCP` server ingests a repository, passes its Markdown files through a summarization prompt, strips copyright headers, and emits flat text strings, downstream consumers frequently treat the output as a self-contained, unencumbered artifact. This practice rests on three flawed assumptions:
1. **The Paraphrase Fallacy:** The belief that altering word order or compressing sentences via a statistical language model generates a fresh, unencumbered work that erases upstream human authorship.
2. **The Permissive-License Fallacy:** The belief that open-source licenses (`MIT`, `Apache-2.0`, `CC-BY-4.0`) waive attribution requirements or permit silent textual distortion.
3. **The Middle-Hop Fallacy:** The belief that citing an intermediate scraper, mirror fork, or vector database satisfies provenance obligations when the canonical origin (`DOI` or origin repository) is known.

---

## 2. What "Original Work" Actually Means Under International & EU Law

Across international copyright frameworks, originality is anchored in **human intellectual creation**, not mechanical or probabilistic transformation:

* **Free and Creative Choices (CJEU *Infopaq* Standard):** Under European Union jurisprudence (*Infopaq International A/S v Danske Dagblades Forening*, Case C-5/08), originality requires that the work constitute its *"author's own intellectual creation,"* reflected through free and creative choices that stamp the work with the creator's personal touch. Purely mechanical routines, automated scraping, and unedited statistical token predictions lack human creative agency.
* **Automatic Protection Without Formalities (Berne Art. 5(2)):** Copyright attaches automatically upon fixation in a tangible or digital medium. Authors are under no obligation to register works or restrict access behind paywalls to preserve their paternity or integrity rights.
* **Transformations Remain Bound to Upstream Lineage (Berne Art. 2(3) & Art. 6bis):** Even where a human author creates a genuine translation, adaptation, or collection, protection is strictly *without prejudice to the copyright in the original work*. Automated pipelines that summarize or restructure upstream text without human creative authorship neither acquire independent copyright nor extinguish the upstream author's moral rights.

---

## 3. Treaty & Statutory Corpus

The table below compiles the primary international treaties, European directives, and national statutory provisions governing originality, moral rights, and attribution integrity:

| Instrument / Provision | Jurisdiction & Year | Core Legal Rule & Engineering Relevance |
| :--- | :--- | :--- |
| **Berne Convention, Art. 2(1) & 2(3)** | International Treaty (1886 / Paris Act 1971) | Protects literary, scientific, and artistic works (including technical papers and code). Adaptations and transformations remain explicitly subordinate to the rights of the original author. |
| **Berne Convention, Art. 5(2)** | International Treaty (1886 / Paris Act 1971) | **No Formalities Rule:** Enjoyment and exercise of copyright shall not be subject to any registration or procedural formality. |
| **Berne Convention, Art. 6bis(1)** | International Treaty (1886 / Paris Act 1971) | **Inalienable Moral Rights:** Independently of economic rights, the author retains the right to claim authorship (**paternity**) and to object to any distortion, mutilation, or modification (**integrity**) prejudicial to honor or reputation. |
| **WIPO Copyright Treaty (WCT), Art. 4 & Art. 12** | International Treaty (1996) | Confirms computer programs are protected as literary works under Berne Art. 2 (Art. 4) and prohibits the unauthorized removal or alteration of electronic **Rights Management Information** (`RMI`) identifying the author and terms of use (Art. 12). |
| **TRIPS Agreement, Art. 9 & Art. 10** | WTO / International (1994) | Incorporates Berne Articles 1–21 into international trade law and mandates protection for source/object code and original compilations of data. |
| **EU InfoSoc Directive (2001/29/EC), Art. 7** | European Union (2001) | Protects electronic rights-management information against removal or alteration when downstream actors distribute or communicate works to the public. |
| **EU Digital Single Market Directive (2019/790), Art. 4 & Art. 53** | European Union (2019) | Governs Text and Data Mining (`TDM`) exceptions, requiring lawful access and respect for machine-readable rights reservations (`W3C ODRL` / `tdmrep`). |
| **EU AI Act (Regulation (EU) 2024/1689), Art. 53(1)(c)–(d)** | European Union (2024) | Requires providers of general-purpose AI models to maintain policies respecting EU copyright law (including opt-out reservations) and publish sufficiently detailed summaries of training content. |
| **Irish Copyright and Related Rights Act (CRRA) 2000, §§ 107, 109, 113** | Republic of Ireland (2000) | Codifies statutory moral rights in Irish law: **Paternity Right (§ 107)** to be identified as author; **Integrity Right (§ 109)** against derogatory treatment; and **False Attribution (§ 113)** prohibiting crediting altered or synthetic text to a creator. |

---

## 4. Forensic Failure Modes in MCP & Aggregator Pipelines

When ingestion systems ignore the treaty corpus above, four recurring forensic defects emerge:

1. **`BERNE-6BIS-PATERNITY` (Attribution Stripping):** Markdown chunkers and web scrapers remove copyright headers, `ORCID` identifiers, and provenance footers to reduce token counts, severing the link between creator and work.
2. **`BERNE-6BIS-INTEGRITY` (Silent Textual Mutation):** An intermediate pipeline summarizes or rewrites a passage using an LLM while leaving the original author's name attached and omitting a `"modified": true` flag, risking false attribution under CRRA 2000 § 113.
3. **`PROVENANCE-HOP-DRIFT` (Middle-Hop Laundering):** Multi-hop aggregators re-host scraped repositories without canonical `DOI` anchors, causing downstream `MCP` servers to cite intermediate scrapers rather than the primary source.
4. **`MCP-SCHEMA-UNBOUND` (Unstructured Token Dumping):** `MCP` tool handlers return bare strings (`{"text": "..."}`) without machine-readable `author_name`, `author_orcid`, `source_uri`, `license_spdx`, or `sha256` fields—violating the electronic Rights Management Information principles of WCT Article 12.

---

## 5. Remediation: Cryptographic Custody & Author Autonomy

Restoring alignment between automated tooling and copyright law requires pairing **Author Sovereignty** (tamper-evident custody) with **Author Autonomy** (active human control over framing and attribution):

* **Deterministic `SHA-256` Custody Ledgers (`generate_manifest.py`):** Authors anchor canonical files in a `JSONL` manifest binding normalized UTF-8 `SHA-256` digests to persistent `ORCID` and `DOI` identifiers.
* **Typed `MCP` Provenance Envelopes (`mcp-provenance.schema.json`):** `MCP` servers validate tool responses against a `JSON Schema (Draft 2020-12)` requiring explicit `author_name`, `author_orcid`, `source_uri`, `license_spdx`, `sha256`, and `modified` boolean flags.
* **Offline Forensic Auditing (`mcp_provenance_auditor.py`):** Creators and auditors verify downstream payloads locally using rolling $k$-shingle overlap and `SHA-256` comparison without external cloud dependencies.

---

## 6. Conclusion

Statistical recombination is not human authorship, and permissive open-source licensing is not an invitation to strip credit or silently distort meaning. By grounding software architecture in the Berne Convention, the WIPO Copyright Treaty, and verifiable SHA-256 provenance envelopes, Berne-Provenance-Toolkit demonstrates that open collaboration and strict creator integrity reinforce one another.

References (APA 7th Edition)

* Berne Convention for the Protection of Literary and Artistic Works, September 9, 1886, as revised at Paris on July 24, 1971, and amended on September 28, 1979, 1161 U.N.T.S. 3. wipo.int
* Copyright and Related Rights Act 2000, No. 28 of 2000 (Ir.). irishstatutebook.ie
* Directive 2001/29/EC of the European Parliament and of the Council of 22 May 2001 on the harmonisation of certain aspects of copyright and related rights in the information society, Official Journal of the European Communities, L 167, 10–19. europa.eu
* Directive (EU) 2019/790 of the European Parliament and of the Council of 17 April 2019 on copyright and related rights in the Digital Single Market, Official Journal of the European Union, L 130, 92–125. europa.eu
* Hedling, B. S. (2026a). Epistemic coevolution, statutory friction, and sovereign edge governance. Zenodo. doi.org
* Hedling, B. S. (2026b). Berne-Provenance-Toolkit: An operational forensic CLI tool and author-rights curriculum for auditing MCP servers, scrapers, and multi-hop aggregators. GitHub. github.com
* Infopaq International A/S v. Danske Dagblades Forening, Case C-5/08, ECLI:EU:C:2009:465 (Court of Justice of the European Union, July 16, 2009). europa.eu
* Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), Official Journal of the European Union, L 2024/1689. europa.eu
* World Intellectual Property Organization. (1996, December 20). WIPO Copyright Treaty (WCT), 2186 U.N.T.S. 121. wipo.int
* World Trade Organization. (1994, April 15). Agreement on Trade-Related Aspects of Intellectual Property Rights (TRIPS), Marrakesh Agreement Establishing the World Trade Organization, Annex 1C, 1869 U.N.T.S. 299. wto.org

🧾 Provenance Footer — Originality & Provenance Preprint (v1.0)

* Artifact-Class / Name: Statutory & Forensic Preprint (ORIGINALITY_AND_PROVENANCE_PREPRINT_v1.0)
* Target-Repository: Borealiscodes/Berne-Provenance-Toolkit
* Maintainer / Location: Borealis S. Hedling (Dublin, Ireland) | Timestamp: 14 November 2026 — 01:28 GMT
* Non-Activation Clause: Descriptive academic and forensic preprint only. Does not constitute formal legal advice; maintains strict Sealed-Layer Neutral boundaries.
* Seal: [ B E R N E • O R I G I N A L I T Y • P R E P R I N T • 0 1 ]
