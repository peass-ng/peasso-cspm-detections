"""List AWS source pages and headings added since the pinned work-plan revision."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from pathlib import Path


BASE = "fd9bf8863bf7a36de10b8695d366a53a9063c81c"
PREFIX = "src/pentesting-cloud/aws-security/"
HEADING = re.compile(r"^(#{2,5})\s+(.+?)\s*$")


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True, errors="replace")


def headings(source: str) -> list[tuple[int, str]]:
    result = []
    for line_number, line in enumerate(source.splitlines(), 1):
        match = HEADING.match(line)
        if match:
            result.append((line_number, match.group(2)))
    return result


def decision(path: str, title: str) -> str:
    """Carry forward a small set of reviewed decisions, leaving the rest open."""
    if path.endswith("aws-iam-privesc/README.md"):
        if "UpdateAccessKey" in title:
            return "Parcial: regla validada para clave ajena activada; falta uso posterior."
        if "UploadSigningCertificate" in title:
            return "Parcial: regla validada para certificado de usuario ajeno."
    if path.endswith("aws-ec2-privesc/README.md") and "ModifyInstanceMetadataOptions" in title:
        return "Parcial: IMDSv1 opcional y límite de saltos probados en instancia desechable."
    if path.endswith("aws-lambda-privesc/README.md"):
        if title == "Expose a pre-existing `AuthType=NONE` Function URL":
            return "Parcial: URL sin IAM y grant URL público; falta comprobar invocación anónima efectiva."
        if title.startswith("`lambda:GetFunction") or title.startswith("`lambda:GetLayerVersion"):
            return "Lectura sensible; requiere contexto del artefacto y uso posterior."
    if path.endswith("aws-s3-privesc/README.md"):
        if title == "`s3:PutBucketPolicy`":
            return "Parcial: regla validada para GetObject público incondicional."
        if title == "`s3:PutBucketCORS`":
            return "Probada: CORS solo no concede acceso; sin regla independiente."
        if (title.startswith("JSON ") or title.startswith("IF THE S3 BUCKET")
                or title.startswith("Make sure to modify") or title.startswith("An ACL should")):
            return "Ejemplo o nota, no técnica autónoma."
    if path.endswith("aws-sagemaker-persistence/README.md") and title in {
            "Example AWS CLI Commands:", "Types of Studio Application Lifecycle Configurations", "Critical Info:"}:
        return "Encabezado explicativo, revisar técnicas bajo él."
    if "/aws-services/" in path and title in {"Privilege escalation", "Privesc"}:
        return "Navegación, no técnica autónoma."
    return "Pendiente de clasificar/probar"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hacktricks-repo", type=Path, required=True)
    parser.add_argument("--base", default=BASE)
    parser.add_argument("--current", default="HEAD")
    parser.add_argument("--output", type=Path, default=Path("AWS_SOURCE_DELTA.md"))
    args = parser.parse_args()
    repo = args.hacktricks_repo.resolve()
    base = git(repo, "rev-parse", args.base).strip()
    current = git(repo, "rev-parse", args.current).strip()
    changes = git(repo, "diff", "--name-status", base, current, "--", PREFIX).splitlines()
    modified: list[tuple[str, list[tuple[int, str]]]] = []
    added: list[str] = []
    removed: list[str] = []
    for row in changes:
        status, path = row.split("\t", 1)
        if not path.endswith(".md"):
            continue
        if status == "A":
            added.append(path)
        elif status == "D":
            removed.append(path)
        elif status == "M":
            before = git(repo, "show", f"{base}:{path}")
            after = git(repo, "show", f"{current}:{path}")
            former = {text for _, text in headings(before)}
            modified.append((path, [(line, text) for line, text in headings(after) if text not in former]))
    new_count = sum(len(items) for _, items in modified)
    changed_without_headings = [path for path, items in modified if not items]
    base_url = f"https://github.com/HackTricks-wiki/hacktricks-cloud/blob/{current}/"
    output = [
        "# Diferencia de fuentes AWS para el plan de trabajo", "",
        f"Fuente fijada en el plan: `{base}`. Fuente local actual de HackTricks: `{current}`.", "",
        f"Páginas Markdown cambiadas: {len(modified)} modificadas, {len(added)} añadidas, {len(removed)} retiradas. "
        f"Las páginas modificadas contienen {new_count} encabezados nuevos en "
        f"{sum(bool(items) for _, items in modified)} páginas; {len(changed_without_headings)} "
        "otras páginas modificadas requieren revisar el cuerpo.", "",
        "Estos son **encabezados candidatos**, no ataques distintos ni detecciones validadas. "
        "Los cambios de nombre, la navegación, las técnicas duplicadas y los pasos bajo encabezados existentes requieren revisión manual. "
        "Una página sin encabezados nuevos puede contener una técnica nueva en el cuerpo.", "",
        "## Encabezados nuevos en páginas modificadas", "",
        "| ID | Página | Encabezado nuevo | Decisión |", "|---|---|---|---|",
    ]
    for path, items in modified:
        occurrences: dict[str, int] = {}
        for line, title in items:
            occurrences[title] = occurrences.get(title, 0) + 1
            key = hashlib.sha256(f"{path}\0{title}\0{occurrences[title]}".encode()).hexdigest()[:16]
            safe_title = title.replace("|", "\\|")
            output.append(f"| `aws-delta-{key}` | [{path[len(PREFIX):]}]({base_url}{path}#L{line}) "
                          f"| {safe_title} | {decision(path, title)} |")
    output += ["", "## Páginas nuevas", ""]
    for path in added:
        output.append(f"- [{path[len(PREFIX):]}]({base_url}{path}) — revisar todas las técnicas.")
    output += ["", "## Páginas modificadas sin encabezados nuevos", ""]
    for path in changed_without_headings:
        output.append(f"- [{path[len(PREFIX):]}]({base_url}{path}) — revisar cambios en el cuerpo.")
    output += ["", "## Páginas retiradas", ""]
    for path in removed:
        output.append(f"- `{path[len(PREFIX):]}` — reconciliar con página sucesora o baja de técnica.")
    args.output.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(f"modified={len(modified)} added={len(added)} removed={len(removed)} "
          f"new_headings={new_count} body_review={len(changed_without_headings)}")


if __name__ == "__main__":
    main()
