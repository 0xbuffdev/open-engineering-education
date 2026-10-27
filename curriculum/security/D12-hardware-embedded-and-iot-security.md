# D12 — Hardware, Embedded & IoT Security

**Track:** Security · **Prerequisite:** D2, S5 · **Elective** · **Time:** 5 weeks, 75 hours · **Project:** elective
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Assess embedded and IoT systems at the hardware/firmware boundary: debug interfaces, flash, boot chains, radio protocols, and update mechanisms. Work only on devices you own or are explicitly authorized to test, and avoid safety-critical or radio-regulatory violations.

## Outcomes

You can:

- identify hardware interfaces (UART, JTAG, SPI, I2C);
- explain secure boot, root of trust, and firmware update;
- extract and inspect firmware safely;
- analyze filesystem images and binaries;
- assess debug access, credential storage, and network services;
- test BLE/MQTT/HTTP surfaces on an authorized device;
- recognize hardware/firmware supply-chain risk;
- document findings without damaging the device;
- respect radio and safety regulations;
- state physical-access assumptions.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| *Practical IoT Hacking* (Chantzis et al.) | Ch. **1–10** | Hardware, firmware, radio, network |
| *The Hardware Hacking Handbook* (Woudenberg & O'Flynn) | Ch. **1–9** | Electrical basics, interfaces, glitching |
| [OWASP IoT Top 10](https://owasp.org/www-project-internet-of-things/) | Current edition | Risk taxonomy |
| [OWASP Firmware Security Testing Methodology](https://github.com/scriptingxss/owasp-fstm) | Full | Firmware method |
| [binwalk docs](https://github.com/ReFirmLabs/binwalk) | Extraction | Firmware analysis |
| [Ghidra docs](https://ghidra-sre.org/) | Selected | Binary analysis |
| [Bluetooth Core spec](https://www.bluetooth.com/specifications/specs/) | Overview | BLE fundamentals |
| [MQTT 3.1.1/5.0 spec](https://mqtt.org/specifications/) | Selected | Messaging security |

## Modules

### 1. Hardware fundamentals and safety

- voltage, current, ground, logic levels;
- multimeter/oscilloscope basics;
- UART, JTAG, SWD, SPI, I2C;
- test pads and headers;
- ESD and physical safety;
- authorization and device ownership;
- radio regulations.

### 2. Firmware acquisition

- vendor update files;
- flash dump with authorized access;
- SPI flash reading;
- bootloader/console;
- extraction with binwalk;
- filesystem types (squashfs, ubifs, ext);
- encryption/packing;
- integrity and provenance.

### 3. Firmware analysis

- filesystem inspection;
- hardcoded credentials/secrets;
- init scripts and services;
- update signature verification;
- secure boot and root of trust;
- key storage;
- vulnerable binaries and libraries;
- SBOM/dependency age.

### 4. Network and radio

- exposed services;
- MQTT/HTTP/CoAP/TLS;
- BLE pairing and GATT;
- Wi-Fi provisioning;
- cloud API boundaries;
- replay and downgrade;
- traffic capture on your own device;
- isolation.

### 5. Assessment and reporting

- threat model with physical access;
- attack surface inventory;
- safe validation;
- severity and safety impact;
- disclosure to vendor;
- remediation (signed updates, debug lock, secure storage);
- residual risk;
- device restoration.

## Labs

### Lab 1 — Interface identification

On a device you own (or a documented training board), identify UART/JTAG/SPI pads and logic levels without connecting power incorrectly. Document the pinout and safety checks.

### Lab 2 — Firmware extraction

Extract a vendor firmware image or use a provided training image. Verify hash, identify filesystem, and list services. Explain what you could not decrypt or verify.

### Lab 3 — Firmware review

Search for hardcoded secrets, debug services, outdated libraries, and update-signature checks. Use synthetic/benign data. Produce three validated findings or explain why the firmware is hardened.

### Lab 4 — Network/radio test

On your own device, capture MQTT or BLE traffic and test authentication/replay in a safe lab. Do not jam, disrupt, or attack nearby devices. Document the boundary and stop conditions.

### Lab 5 — Report and restore

Write an assessment report with physical-access assumptions, findings, severity, remediation, and disclosure. Restore the device to its original state and verify it.

## Exercises

1. Identify UART pins and baud rate safely.
2. Explain secure boot's chain of trust.
3. Compare signed and unsigned firmware updates.
4. Explain a flash-dump threat.
5. Identify a hardcoded credential risk.
6. Map an OWASP IoT risk to a control.
7. Explain BLE pairing vs encryption.
8. Describe a replay attack on MQTT.
9. State physical-access assumptions.
10. Explain radio/safety limits.

## Project increment (optional)

Assess one device or firmware image you own: document the recovery path, extract and inspect the firmware, identify one weakness, and propose a fix or compensating control. Never test a third-party or production device. This is an elective extension to P11/C4, not a new ladder project.

## Exit check

- [ ] identify interfaces safely on an owned device;
- [ ] extract and inspect a training firmware image;
- [ ] validate one firmware finding;
- [ ] test one network/radio boundary without disruption;
- [ ] write remediation and disclosure;
- [ ] restore the device and state residual risk.

## Common failure modes

- Connecting power/ground incorrectly.
- Testing devices you do not own.
- Jamming or disrupting radio spectrum.
- Publishing vendor secrets or private firmware.
- Assuming physical access is out of scope.
- Confusing debug access with a vulnerability by itself.
- Ignoring update-signing and secure boot.
- Not restoring the device.

## Evidence to commit

- `labs/security/D12/` with pinout, firmware extraction, review, network/radio test, report
- `notes/security/D12/summary.md`
- authorization/ownership and device-restoration record

## Optional depth

- *Practical Reverse Engineering* (Dang et al.).
- *The Art of Hardware Hacking* / related hardware texts.
- ChipWhisperer glitching and side-channel tutorials (authorized hardware).
- Android/embedded secure boot documentation.
- FCC equipment authorization and local radio rules.
