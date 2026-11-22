# OEE release publication record and maintainer runbook

**Release status (2026-11-22):** [OEE Toolkit `0.1.0`](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0) and [signed curriculum `2026.11.1`](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1) are public. This document records how the first release was prepared, signed and verified. **Do not rerun the publication commands below for these tags.** They are retained for auditing the original release; new versions need new reviewed IDs, manifests and release decisions.

This runbook is for OEE release maintainers. It uses the current archive builder, detached Ed25519 signature, installer and Toolkit exporter. Each archive is built from an explicit commit. The consumer never searches Git or follows a moving branch.

## 1. Toolkit package source and distribution

- **Source SHA:** `f2afed3e36f6ae0495e2b44a8d9337661defeda1`.
- **Package/version:** `oee-toolkit 0.1.0` (independent of OEE specification
  `v0.2.0` and the separately versioned curriculum CalVer).
- **Wheel:** `oee_toolkit-0.1.0-py3-none-any.whl`, SHA-256
  `eb20281dea91d16a03d79535d65a7b8b271894a5d7a5988cc2d356c88993ecf6`.
- **Source archive:** `oee_toolkit-0.1.0.tar.gz`, SHA-256
  `8eb21f512b4a0e27615b18261b10cd59495f11049a6d141be9e4ae02505d6501`.
- [Exact-final-commit three-platform package smoke](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44959716559) passed.
- [Retained ZIP artifact](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44959716559/artifacts/14729286140) contains the wheel and source archive.

The wheel and source archive were checked against the runner's SHA-256 records and inspected for the expected license and NOTICE files. Neither package includes educational curriculum source. The enclosing GitHub Actions ZIP has its own hash; the per-file hashes are the distribution identities.

These exact files were published in the [Toolkit GitHub Release](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0). PyPI publication, if introduced later, needs a separate distribution decision.

## 2. Source-pinned unsigned curriculum archive

The first published curriculum release ID is `2026.11.1`. The successful [three-platform candidate run](https://github.com/0xbuffdev/open-engineering-education/actions/runs/44997272152) used the exact source commit below. Future release IDs must be new; never reuse an allocated or withdrawn ID.

Use [Unsigned OEE curriculum release candidate](../.github/workflows/curriculum-official-candidate.yml)
on the repository's **main** branch with these exact workflow inputs:

| Input | Candidate value |
| --- | --- |
| `release_id` | `2026.11.1` |
| `source_sha` | `f2afed3e36f6ae0495e2b44a8d9337661defeda1` |

The workflow checks that the source commit exists in `main` history. It then builds the complete allowlisted archive on Linux, macOS and Windows and compares the resulting bytes. The archived output is unsigned; the workflow has no production private key or publishing permissions.

The comparison passed on all three platforms. The approved manifest SHA-256 is `57441494eb69c2ff9cb3f6029c8adc3c6a56f8c6ecabc43196c9b686e5959a6c`, and the archive SHA-256 is `931b30209a2727717af331f4fd46bfc8e637c94c4d1d95d08d6ffeee753c78d2`. The archive contains 76 courses across 94 source and notice files. Course status remains `draft` where authored.

The following command downloads the historical unsigned candidate. Use the actual run ID (`44997272152`) in place of `RUN_ID` when reproducing the audit:

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

## 3. Steward key trust and custody

The steward created the production Ed25519 signing key on a local machine. The private key remains under steward control. The signer reads an unencrypted PEM, so it must be stored on protected, encrypted media and backed up securely. Never place the private key in the repository, CI, a chat or a public release asset.

The commands below document first-time key generation. **Do not run them for the existing `2026.11.1` key** or overwrite any current key:

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

The independently approved DER public-key SHA-256 fingerprint for this release is `0cbd8335bf39fab19b17a7bfaa33502d121d007fca4bddd5df0f43a9c814e2ef`. The public PEM and fingerprint can be shared; the private key must stay private.

Before approving the key, record who controls it, where recovery
backups are stored, which release classes it may sign, and the
revocation/rotation procedure. If compromised, mark the signer
revoked, notify consumers through the authoritative public OEE
channel, use a separately approved replacement key for future
releases, and review previously published attestations. Do not
silently replace a pinned release or delete historical evidence.

## 4. Local signing and verification

The steward signed the verified archive locally using the OEE release script and `cryptography>=44,<50`. The following publisher commands document the same steps. They expect an unsigned candidate and the approved digest; **do not sign or overwrite the already published `2026.11.1` release again**:

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

## 5. Published artifacts and future release decisions

The specification, Toolkit distribution and curriculum archive have independent versions. The first official artifacts are permanently identified by their public tags:

| Artifact | Published tag | Source and verification |
| --- | --- | --- |
| Toolkit Python wheel and sdist | [toolkit-v0.1.0](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0) | Reviewed source, exact package hashes and three-platform clean-install results |
| Signed curriculum TAR and attestation | [curriculum-2026.11.1](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1) | Manifest/archive digests, approved public-key fingerprint and three-platform canonical archive checks |

The [release decision](RELEASE-DECISION.md) retains the original hashes, signing-key fingerprint and verification runs. Published tags and release assets remain immutable. The original draft-creation commands are available in the tagged Git history; they are omitted from this current runbook to avoid accidentally recreating the same release.

For a **new** release, choose a new version and source commit, independently review license notices and source closure, test the package and archive across supported platforms, approve the public key and manifest digest separately, and verify the exact draft artifacts before publication. A downloaded checksum or passing CI run cannot establish steward trust on its own. Key rotation and revocation remain explicit steward decisions.

## 6. Consumer status

[OEE Workspace v0.1.0](https://github.com/0xbuffdev/oee-workspace/releases/tag/v0.1.0) installs and verifies the signed curriculum through the published Toolkit. Its [official](https://github.com/0xbuffdev/oee-workspace/actions/runs/45005744426) and [disposable](https://github.com/0xbuffdev/oee-workspace/actions/runs/45005744423) smoke tests passed on Ubuntu, macOS and Windows before publication.

Content/0xNAND integration requires separate consumer approval. Optional lesson-level resource maps need review against the actual released course source before activation. A signature proves source identity; it cannot promote academic course status, certify learners or authorize changes to learner files.
