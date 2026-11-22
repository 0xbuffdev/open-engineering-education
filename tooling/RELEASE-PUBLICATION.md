# Publishing the first official OEE Toolkit and curriculum release

**Current state (2026-11-22):** the Toolkit 0.1.0 wheel/sdist has passed
independent clean-install tests on Linux, macOS and Windows, but is
**not published**. A trusted OEE curriculum CalVer archive and the
steward's official Ed25519 key have **not** been approved or published.
These are distinct release decisions.

This runbook is for the OEE steward. It uses the existing deterministic
source archive, detached-signature, install and Toolkit export
implementations. It creates no alternate parser, release identity or
automatic Git/HEAD fallback.

## 1. Verified first Toolkit package candidate

- **Source SHA:** `f2afed3e36f6ae0495e2b44a8d9337661defeda1`.
- **Package/version:** `oee-toolkit 0.1.0` (independent of OEE specification
  `v0.2.0` and the separately versioned curriculum CalVer).
- **Wheel:** `oee_toolkit-0.1.0-py3-none-any.whl`, SHA-256
  `eb20281dea91d16a03d79535d65a7b8b271894a5d7a5988cc2d356c88993ecf6`.
- **Source archive:** `oee_toolkit-0.1.0.tar.gz`, SHA-256
  `8eb21f512b4a0e27615b18261b10cd59495f11049a6d141be9e4ae02505d6501`.
- [Exact-final-commit three-platform package smoke](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44959716559) passed.
- [Retained ZIP artifact](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44959716559/artifacts/14729286140) contains the wheel and source archive.

The wheel and source archive were independently downloaded, their file
hashes matched the runner logs, their license/NOTICE entries were
inspected and neither contained educational curriculum source. The ZIP
itself has a **different** SHA-256, so approve each distribution file's
digest, not only the ZIP hash.

Do not upload to PyPI or create a public GitHub Release until you
independently authorize this exact distribution, name and licensing.
The initially recommended distribution path is an OEE-owned GitHub
Release with both files; a registry release can follow separately.

## 2. Prepare one source-pinned, unsigned complete curriculum archive

The next human-facing **candidate** release ID is `2026.11.1`. It is
not final until checked against previous allocation and approved by the
steward. Never reuse an ID if it has already been assigned or withdrawn.

Use [Unsigned OEE curriculum release candidate](../.github/workflows/curriculum-official-candidate.yml)
on the repository's **main** branch with these exact workflow inputs:

| Input | Candidate value |
| --- | --- |
| `release_id` | `2026.11.1` |
| `source_sha` | `f2afed3e36f6ae0495e2b44a8d9337661defeda1` |

The workflow checks that the SHA is a real ancestor of `main`, builds
the complete allowlisted archive from that **exact commit**, inspects
the source closure, independently rebuilds the same CalVer archive on
Linux, macOS and Windows, and compares all bytes and source identities.
It retains an **unsigned**, unpublished artifact for 30 days. It
neither handles production private keys nor creates a GitHub Release.

Inspect the three passing platform jobs and the byte-comparison job.
Record the workflow run URL and approved values of `archiveSha256`,
`manifestSha256`, `fileCount` and `sourceCommit` from `audit.json`.
Check that the academic source remains explicitly `draft` where authored;
a structural check is not a human educational approval.

To download the candidate using GitHub CLI (after replacing
`RUN_ID` with the successful workflow's numeric run ID):

~~~sh
REPO="0xbuffdev/open-engineering-education"
SOURCE_SHA="f2afed3e36f6ae0495e2b44a8d9337661defeda1"
RELEASE_ID="2026.11.1"
RUN_ID="<successful-run-id>"
OUT="$HOME/oee-official-release"
mkdir -p "$OUT"
gh run download "$RUN_ID" --repo "$REPO" \
  --name "oee-curriculum-$RELEASE_ID-unsigned-$SOURCE_SHA" \
  --dir "$OUT"
cat "$OUT/audit.json"
sha256sum "$OUT/curriculum.tar"
~~~

Review source provenance and the candidate audit independently. The
`manifest.sha256` file shipped **inside the same unsigned artifact**
confirms byte consistency, not steward authenticity. Compare its digest
with the independently reviewed workflow log and approved release
decision before signing. Do not automatically trust the downloaded ZIP.

## 3. Establish steward key trust once, offline

**Only the steward performs this step.** Choose a trusted local machine,
an encrypted volume, a protected backup and an offline signing location.
The current signer accepts an **unencrypted PEM private key**, so never
leave that file on a shared/untrusted disk or store it in a source
repository, connected chat, cloud workflow artifact or CI secret.

For a brand-new key only (do not overwrite any existing key):

~~~sh
umask 077
KEY_DIR="/path/to/protected-encrypted-volume/oee-keys"
PRIVATE_KEY="$KEY_DIR/oee-steward-ed25519-private.pem"
PUBLIC_KEY="$KEY_DIR/oee-steward-ed25519-public.pem"
mkdir -p "$KEY_DIR"
chmod 700 "$KEY_DIR"
test ! -e "$PRIVATE_KEY" && test ! -e "$PUBLIC_KEY" || {
  echo "Key files already exist; refusing to overwrite" >&2
  exit 1
}
openssl genpkey -algorithm ED25519 -out "$PRIVATE_KEY"
openssl pkey -in "$PRIVATE_KEY" -pubout -out "$PUBLIC_KEY"
chmod 600 "$PRIVATE_KEY"
openssl pkey -pubin -in "$PUBLIC_KEY" -outform DER | sha256sum
~~~

Record the SHA-256 fingerprint of the **DER-encoded public key** as
the trust reference. The public PEM and its fingerprint are safe to
publish after independent steward review; the private key is not.

Before approving the key, record who controls it, where recovery
backups are stored, which release classes it may sign, and the
revocation/rotation procedure. If compromised, mark the signer
revoked, notify consumers through the authoritative public OEE
channel, use a separately approved replacement key for future
releases, and review previously published attestations. Do not
silently replace a pinned release or delete historical evidence.

## 4. Sign only the independently reviewed archive

Use a local OEE checkout containing the tested publisher script and
a Python environment with `cryptography>=44,<50`. Copy the downloaded
unsigned candidate to that machine. After comparing its digest with
the approved source review, set the **actual** manifest digest:

~~~sh
# The source root is the full checkout containing scripts/.
cd /path/to/open-engineering-education

OUT="$HOME/oee-official-release"
MANIFEST_SHA256="<reviewed-64-character-manifest-sha256>"

python scripts/build-curriculum-release-archive.py sign \
  --archive "$OUT/curriculum.tar" \
  --expected-manifest-sha256 "$MANIFEST_SHA256" \
  --private-key "$PRIVATE_KEY" \
  --attestation "$OUT/oee-curriculum-2026.11.1.attestation.json" \
  --signature "$OUT/oee-curriculum-2026.11.1.sig"

python scripts/build-curriculum-release-archive.py verify \
  --archive "$OUT/curriculum.tar" \
  --expected-manifest-sha256 "$MANIFEST_SHA256" \
  --attestation "$OUT/oee-curriculum-2026.11.1.attestation.json" \
  --signature "$OUT/oee-curriculum-2026.11.1.sig" \
  --trusted-public-key "$PUBLIC_KEY"
~~~

The signer refuses existing output sidecars. That is deliberate:
never overwrite a signature, archive or allocation with different
bytes. Keep the signed archive and its attestation together.

For an additional installed-consumer test, create a **new** controlled
directory and run `install` with the same archive, digest, attestation,
signature and trusted public key, passing `--store` to that directory.
Then check an installed `oee-toolkit export SEF1` using an explicitly
reviewed `oee-curriculum.lock.json`. No network or Git source should be
needed by the installed consumer.

## 5. Publish only after signing and artifact approval

These are **separate OEE-owned GitHub Releases** to avoid collisions
with existing OEE specification tags.

| Artifact class | Proposed tag | Required assets |
| --- | --- | --- |
| Toolkit Python software | `toolkit-v0.1.0` | Exact audited wheel and sdist, digests, package notes |
| Immutable curriculum | `curriculum-2026.11.1` | Signed `curriculum.tar`, detached `.attestation.json`, raw `.sig`, trusted public PEM, full SHA-256 records, release notes |

Create the releases in **draft** first and inspect assets and checksums.
Only the GitHub account with publishing permission should make them
public. On a machine authenticated to the official repository:

~~~sh
# The wheel/sdist must match the approved digests above.
gh release create toolkit-v0.1.0 \
  /path/to/oee_toolkit-0.1.0-py3-none-any.whl \
  /path/to/oee_toolkit-0.1.0.tar.gz \
  --repo 0xbuffdev/open-engineering-education \
  --target f2afed3e36f6ae0495e2b44a8d9337661defeda1 \
  --title "OEE Toolkit 0.1.0" --draft \
  --notes "First independently tested Toolkit distribution. Academic review remains separate."

gh release create curriculum-2026.11.1 \
  "$OUT/curriculum.tar" \
  "$OUT/oee-curriculum-2026.11.1.attestation.json" \
  "$OUT/oee-curriculum-2026.11.1.sig" \
  "$PUBLIC_KEY" \
  --repo 0xbuffdev/open-engineering-education \
  --target f2afed3e36f6ae0495e2b44a8d9337661defeda1 \
  --title "OEE Curriculum 2026.11.1" --draft \
  --notes "Immutable signed OEE curriculum snapshot; course readiness remains as authored."
~~~

Do not publish drafts until the approved manifest digest, signature,
source commit, public-key fingerprint and file hashes have been
recorded in an authoritative release decision and an independent
download/verify/install succeeds. After that review, the steward may
publish by editing the draft releases in GitHub's release UI.

## 6. Complete dependent Workspace and Content activation

After the real Toolkit and signed curriculum archive are public:

1. Pin the official toolkit distribution and trusted curriculum digest,
   distribute the approved public-key trust instructions, and record
   exact install paths for Linux, macOS and Windows.
2. Update [OEE Workspace](https://github.com/0xbuffdev/oee-workspace)
   `README.md` and `CONTRIBUTING.md` with real installation, signature,
   release lock and local-course steps. Run the independent three-OS
   Workspace acceptance again on the **exact merged docs commit**.
3. Publish the new Workspace release from that passing commit; do not
   assert that draft courses are verified or learners have passed.
4. Finish the already planned Content and 0xNAND release-v2 academic
   consumer integration without adding a second curriculum parser.
5. Resume reviewed lesson-level resource mapping once the stable
   released course digest and source access are available.

Neither Toolkit package publication nor the curriculum archive
retroactively validates learner outcomes. Resource maps remain optional
and must not force paid books or overwrite existing learner work.
