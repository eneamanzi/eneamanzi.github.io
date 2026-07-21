#!/usr/bin/env python3
"""Scaffolds new _projects/*.md pages from assets/json/resume.json's "projects"
array (itself generated from the Curriculum-Vitae repo's data/50-projects.json,
the single source of truth).

Runs automatically in CI whenever resume.json changes (see
.github/workflows/scaffold-projects.yml) - never run by hand.

Matching logic: a CV project is considered "already covered" if any existing
_projects/*.md file (outside _projects/examples/) has a frontmatter `cv_id:`
matching the project's stable `id` (assigned once in data/50-projects.json,
carried through resume.json, and written into the page when it's first
scaffolded). This id is never recomputed from `name`/`title`, so either one can
be freely reworded later without the check breaking. Existing pages are NEVER
modified or deleted, only new ones are added for projects with no matching id.
"""

import json
import os
import re
import sys

from pydantic import BaseModel, ConfigDict, Field

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
PROJECTS_DIR = os.path.join(REPO_ROOT, "_projects")
RESUME_JSON = os.path.join(REPO_ROOT, "assets", "json", "resume.json")

CV_ID_RE = re.compile(r"^cv_id:\s*(.+?)\s*$", re.MULTILINE)


class Frontmatter(BaseModel):
    """Validated before a page is written - catches a malformed/missing field
    in resume.json's projects entry before a broken page ever gets committed."""

    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    importance: int = Field(gt=0)
    category: str = Field(min_length=1)
    cv_id: str = Field(min_length=1)
    course: str
    highlights_md: str = Field(min_length=1)


def strip_md(s):
    """frontmatter `description:` is rendered as plain text (no markdownify) by
    the theme, so **bold**/*italic* markers must not reach it verbatim."""
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s)
    s = re.sub(r"\*(.*?)\*", r"\1", s)
    return s


def existing_cv_ids():
    ids = set()
    for fname in os.listdir(PROJECTS_DIR):
        path = os.path.join(PROJECTS_DIR, fname)
        if not os.path.isfile(path) or not fname.endswith(".md"):
            continue
        with open(path, encoding="utf-8") as f:
            content = f.read()
        match = CV_ID_RE.search(content)
        if match:
            ids.add(match.group(1).strip().strip('"').strip("'"))
    return ids


def scaffold(proj):
    cv_id = proj["id"]
    importance = proj["importance"]
    name = proj["name"]
    course = proj.get("course", "")
    # resume.json's "summary" is "{course}\n\n{description}" (folded together for
    # the CV page's rendering) - strip the course prefix back off here since we
    # show it separately in the scaffolded page.
    summary = proj["summary"]
    if course and summary.startswith(course):
        description = summary[len(course):].lstrip("\n")
    else:
        description = summary
    description = strip_md(description)
    highlights = proj.get("highlights", [])
    category = proj.get("category", "Academic")

    highlights_md = "\n".join(f"- {h}" for h in highlights)

    fm = Frontmatter(
        title=name,
        description=description,
        importance=importance,
        category=category,
        cv_id=cv_id,
        course=course,
        highlights_md=highlights_md,
    )

    content = f"""---
layout: page
title: {fm.title}
description: {fm.description}
img:
importance: {fm.importance}
category: {fm.category}
permalink: /projects/{fm.cv_id}/
cv_id: {fm.cv_id}
toc:
  sidebar: left
---

<!-- Scaffolded from the CV's data (single source of truth) - expand with the
     full write-up below the Summary section. -->

## Summary (from CV)

{f"*{fm.course}*" if fm.course else ""}

{fm.highlights_md}
"""
    return content


def main():
    if not os.path.exists(RESUME_JSON):
        print(f"{RESUME_JSON} not found, nothing to do.")
        return

    with open(RESUME_JSON, encoding="utf-8") as f:
        resume = json.load(f)

    projects = resume.get("projects", [])
    existing_ids = existing_cv_ids()

    created = []
    for proj in projects:
        if proj["id"] in existing_ids:
            continue
        content = scaffold(proj)
        out_path = os.path.join(PROJECTS_DIR, f"{proj['id']}.md")
        if os.path.exists(out_path):
            print(f"SKIP {out_path} exists but has no matching cv_id: {proj['id']} - check manually")
            continue
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(out_path)
        print(f"Created {out_path}")

    if not created:
        print("Nothing to scaffold - every CV project already has a matching page.")


if __name__ == "__main__":
    main()
