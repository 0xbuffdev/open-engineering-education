# Publishing the first official OEE Toolkit and curriculum release

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

## 5. Published artifacts and original draft-publishing commands

Toolkit software and curriculum source have separate GitHub Release tags. The OEE specification has its own version:

| Artifact class | Proposed tag | Required assets |
| --- | --- | --- |
| Toolkit Python software | `toolkit-v0.1.0` | Exact audited wheel and sdist, digests, package notes |
| Immutable curriculum | `curriculum-2026.11.1` | Signed `curriculum.tar`, detached `.attestation.json`, raw `.sig`, trusted public PEM, full SHA-256 records, release notes |

Both releases were created as drafts, checked and then published. The commands below show the original draft creation procedure. They will fail for already allocated tags and must not be used to replace existing assets:

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

The [release decision record](RELEASE-DECISION.md) now contains the approved source, file digests, signing-key fingerprint and verification runs. For future releases, check all assets by downloading them again and verifying the signature before changing a draft to public.

## 6. Workspace and Content follow-up

The signed OEE releases are public. Consumer work follows in this order:

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

The signed archive preserves the academic source as authored. Learner outcomes still require assessment, and optional resource mappings cannot force paid purchases or overwrite learner work.
