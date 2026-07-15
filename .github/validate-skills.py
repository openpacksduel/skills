from __future__ import annotations

import re
import sys
from pathlib import Path

NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate(skill_name: str) -> list[str]:
    errors: list[str] = []
    root = Path(skill_name)
    skill_file = root / "SKILL.md"
    agent_file = root / "agents" / "openai.yaml"

    if not skill_file.is_file():
        return [f"{skill_name}: missing SKILL.md"]
    if not agent_file.is_file():
        errors.append(f"{skill_name}: missing agents/openai.yaml")

    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"^---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n", text)
    if not match:
        errors.append(f"{skill_name}: invalid frontmatter")
        return errors

    declared_name, description = match.groups()
    if declared_name != skill_name:
        errors.append(f"{skill_name}: declared name is {declared_name!r}")
    if len(declared_name) > 64 or not NAME.fullmatch(declared_name):
        errors.append(f"{skill_name}: name violates Agent Skills naming rules")
    if len(description.strip()) < 40:
        errors.append(f"{skill_name}: description is not specific enough")
    if "TODO" in text:
        errors.append(f"{skill_name}: unresolved TODO")

    return errors


def main() -> int:
    skill_names = sys.argv[1:] or sorted(
        path.parent.name for path in Path.cwd().glob("*/SKILL.md")
    )
    if not skill_names:
        print("No skills found", file=sys.stderr)
        return 1

    errors = [error for skill in skill_names for error in validate(skill)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(skill_names)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
